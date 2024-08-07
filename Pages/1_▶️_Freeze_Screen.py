import streamlit as st
import cv2
import mediapipe as mp
import numpy as np
from PIL import Image
import requests
from threading import Thread

# HandDetector class definition
class HandDetector:
    def __init__(self, mode=False, max_hands=2, detection_confidence=0.5, minTrackingConfidence=0.5):
        self.mode = mode
        self.max_hands = max_hands
        self.modelComplex = False
        self.detection_confidence = detection_confidence
        self.minTrackingConfidence = minTrackingConfidence

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.max_hands,
            min_detection_confidence=self.detection_confidence,
            min_tracking_confidence=self.minTrackingConfidence
        )

        self.mpDraw = mp.solutions.drawing_utils
        self.tipIds = [4, 8, 12, 16, 20]
        self.lmList = []
        self.bboxInfo = []

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mp_hands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw=True):
        xList = []
        yList = []
        bbox = []
        self.lmList = []
        if self.results.multi_hand_landmarks:
            if len(self.results.multi_hand_landmarks) > handNo:
                myHand = self.results.multi_hand_landmarks[handNo]
                for id, lm in enumerate(myHand.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    xList.append(cx)
                    yList.append(cy)
                    self.lmList.append([id, cx, cy])
                    if draw:
                        cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
                xmin, xmax = min(xList), max(xList)
                ymin, ymax = min(yList), max(yList)
                boxW = xmax - xmin
                boxH = ymax - ymin
                bbox = xmin, ymin, boxW, boxH

                cx, cy = bbox[0] + bbox[2] // 2, bbox[1] + bbox[3] // 2
                self.bboxInfo = {"id": id, "bbox": bbox, "center": (cx, cy)}

                if draw:
                    cv2.rectangle(img, (bbox[0] - 20, bbox[1] - 20), 
                                  (bbox[0] + bbox[2] + 20, bbox[1] + bbox[3] + 20), 
                                  (0, 255, 0), 2)

        return self.lmList, self.bboxInfo

    def fingersUp(self):
        fingers = []
        if self.lmList:
            if self.lmList[self.tipIds[0]][1] > self.lmList[self.tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
            for id in range(1, 5):
                if self.lmList[self.tipIds[id]][2] < self.lmList[self.tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
        return fingers

def send_freeze_request():
    url = "https://43.31.79.29/api/v1/public"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "dev": {
            "display": {
                "freeze": True
            }
        }
    }
    try:
        response = requests.patch(url, json=data, headers=headers, verify=False)
        if response.status_code == 200:
            print("Freeze request successful")
        else:
            print(f"Failed to send freeze request: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Exception occurred while sending request: {e}")

def send_freezeoff_request():
    url = "https://43.3.151.238/api/v1/public"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "dev": {
            "display": {
                "freeze": False
            }
        }
    }
    try:
        response = requests.patch(url, json=data, headers=headers, verify=False)
        if response.status_code == 200:
            print("Freeze off request successful")
        else:
            print(f"Failed to send freeze off request: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Exception occurred while sending request: {e}")

def is_holding_phone_gesture(lmList1, lmList2):
    if len(lmList1) == 0 or len(lmList2) == 0:
        return False
    
    # 両手の親指と人差し指の指先の座標を取得
    thumb_tip_1 = lmList1[4]
    index_tip_1 = lmList1[8]
    thumb_tip_2 = lmList2[4]
    index_tip_2 = lmList2[8]
    
    # 親指と人差し指の指先間のユークリッド距離を計算
    distance_thumb_tips = np.linalg.norm(np.array(thumb_tip_1[1:]) - np.array(thumb_tip_2[1:]))
    distance_index_tips = np.linalg.norm(np.array(index_tip_1[1:]) - np.array(index_tip_2[1:]))
    
    # 距離が指定範囲内にある場合、スマホを構えているジェスチャーと判断
    if 30 < distance_thumb_tips < 100 and 30 < distance_index_tips < 100:
        return True
    return False

def main():
    st.set_page_config(
    layout="wide",
    page_title="AdFreeze & MoiréFix",
    page_icon="🪄",
)
    
    col1, col2 = st.columns([2, 2])
    
    col1.markdown("# Freeze LED Display with Hand Gesture")
    col2.image("./freeze_demo.gif", use_column_width=True)

   
    
   
    st.markdown(" You can choose to enable or disable the freeze feature. When the 'holding phone' gesture is detected,the display will be frozen. You can also turn off the freeze feature by choosing 'Disable' option.")
    st.markdown("---")
    st.sidebar.write("## Enable freeze feature🏄‍♀️")
    enable_freeze = st.sidebar.radio("", ["Disable", "Enable"])


    st.sidebar.image("./gesture.jpg", width=200 )
    st.sidebar.write('### *Show the [holding phone] gesture to freeze the display.*')

    cap = None
    detector = None
    stframe = None    
    
    if enable_freeze == "Enable":
        cap = cv2.VideoCapture(1)
        detector = HandDetector()
        stframe = st.empty()

    if cap is not None and detector is not None:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                st.error("Failed to capture image from camera.")
                break

            frame = detector.findHands(frame)
            lmList1, bbox1 = detector.findPosition(frame, handNo=0)
            lmList2, bbox2 = detector.findPosition(frame, handNo=1)

            if lmList1 and lmList2:
                if is_holding_phone_gesture(lmList1, lmList2):
                    x_1, y_1 = bbox1["bbox"][0], bbox1["bbox"][1]
                    cv2.putText(frame, "Holding Phone Detected", (x_1, y_1), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
                    # Thread(target=send_freeze_request).start()
                else:
                    x_1, y_1 = bbox1["bbox"][0], bbox1["bbox"][1]
                    cv2.putText(frame, "Freeze Off", (x_1, y_1), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
                    # Thread(target=send_freezeoff_request).start()

            # Display the resulting frame
            stframe.image(frame, channels="BGR")

        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()