import streamlit as st
from PIL import Image



def FAQ_page():
    

    st.markdown("""
    <style>
    @font-face {
        font-family: 'Segoe UI';
        src: url('https://fonts.cdnfonts.com/s/16059/Segoe%20UI%20Regular.woff') format('woff');
    }

    body {
        font-family: 'Segoe UI', sans-serif;
    }

    h1, h2, h3, h4, h5, h6 {
        font-family: 'Segoe UI', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)


    st.markdown("<h3 style='text-align: center; color: #20B2AA;'>FAQ</h1>", unsafe_allow_html=True)
    
    
    questions  = [
        "Can the gesture of taking a photo with one hand be recognized?",
        "Can the system successfully recognize gestures when multiple people are in the camera frame?",
        "Is it necessary to hold a phone in hands for the gesture to be recognized?",
        "Can the distance for taking photos be adjusted?",
        "Does freezing the screen mean the same as pausing playback?",
        "Can the system recognize gestures if I take photos vertically?",
        "What are the suitable scenarios for using this system?",
        "Can the system only recognize one gesture?"
    ]
    
    answers = [
        """
        - **Current Implementation**: No, the current implementation checks for both hands' landmarks to determine if the user is holding a phone.
        - **Enhancement**: To recognize a one-handed gesture, we could consider to modify the code to check for landmarks from a single hand. Adjust the ```is_holding_phone_gesture``` function to detect specific finger positions from one hand only.
        """,
        """
        No, the current system may mistakenly recognize hands from two different people as belonging to one person.
        To recognize gestures of multiple people, we can improve the system's ability to correctly identify and track hands from different individuals. 
        **Here's some possible solutions:**
        1. ***Hand Tracking with IDs***:  
            Implement a hand tracking mechanism that assigns unique IDs to each detected hand. ``MediaPipe's hand tracking module`` already provides this functionality to some extent. The ```tracked_hands``` deque maintains a history of tracked hand positions, which can help in distinguishing between multiple hands over time.
        2. ***Bounding Box Analysis***:  
            Analyze the bounding boxes of detected hands to ensure that the hands being considered for gesture recognition belong to the same individual. The positions and distances of bounding boxes are used to ensure hands are within a reasonable range, reducing the likelihood of misidentification.
        3. ***Face Detection***:  
            Use a face detection model (e.g., ``Haar Cascades``, ``Dlib``, or ``MediaPipe Face Detection``) to detect faces in the frame.
            Associate hands with the nearest face based on distance metrics.
                    
        """,
        """
        - **Current Implementation**: The system detects the gesture by checking the relative positions of both hands and it's fingers, not the actual presence of a phone.
        - **Enhancement**: To specifically recognize a phone, you could incorporate object detection using a model like ``YOLO`` or ``SSD`` to detect a phone and combine it with hand landmark detection.
        """,
        """
        - **Current Implementation**: Recognition depends on the *relative positions* of the hands. The distance between the user station and the LED display affects recognition results. Too far or too close can cause an effect.
        - **Enhancement**: To adjust the distance, we could calibrate the system to recognize gestures at different scales or distances. Administrator of the system could adjust the ``distance_thumb_tips`` to meet the specific needs. 
        """,
        """
        Freezing the screen sends a "*freeze*" command, which stop the LED screen from updating. However, the source video will continue to play as usual. Due to the LED display system's ``API`` doesn't support a pause funtion, so there will be a jump after the playback resumes.          
        """,
        """
        The system checks the relative positions of the thumb and index fingers of both hands. Theortically, it should be able to recognized regardless of the orienation. However, it is difficult to satisfy the calculation rules of this system when the user holds the phone vertically to take a picture. **So please use the system with a horizontal style of holding the phone.**
        """,
        """
        The system can be used in some specific use case and considerations, highlighting that it is recommended for controlled environments like pop-up shops, museums, exhibitions and shows. The system could be adapted for other interactive environments by integrating additonal gestures and controls.
        """,
        """
        - **Current Implementation**: Yes, it currently recognizes the "*holding phone*" gesture to freeze and unfreeze the screen.
        - **Enhancement**: To recognize multiple gestures, we could expand the ``fingersUp`` function to detect additional hand gestures. Implement a gesture classification system that maps different gestures to specific actions.
        """
    ]

   
    #setting 
    st.markdown("""
        <style>
        a {
            color: #008B8B; /* 你可以根据需要更改颜色 */
            text-decoration: none; /* 去掉下划线 */
            font-size: 18px; /* 字体大小 */
        }
        a:hover {
            color: #20B2AA; /* 鼠标悬停时的颜色 */
            text-decoration: underline; /* 加下划线 */
        }
        
        </style>
        """, unsafe_allow_html=True)

    

    for i, question in enumerate(questions):
        st.markdown(f"[{question}](#{i+1})")
        st.markdown('')

  
    st.divider()

    st.markdown("""
    <style>
    h2 {
        font-size: 28px;
        font-weight: bold;
        margin-top: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

    for i, (question, answer) in enumerate(zip(questions, answers)):
        st.markdown(f"<a name='{i+1}'></a>", unsafe_allow_html=True)
        st.markdown(f"### {question}")
        st.markdown(answer)
        st.markdown('')
        st.markdown('')
    
   

    
