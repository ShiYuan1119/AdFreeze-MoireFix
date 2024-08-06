import streamlit as st

def HW_SW():
    st.markdown('')
    st.markdown(
        "<h3 style='text-align: center; color: #2a3a4a; font-size: 40px;'>Hardware and Software Used in This System</h1>",
        unsafe_allow_html=True
    )
    st.markdown('')
    st.markdown("<h3 style='text-align: center; color: black;'>Hardware Overview</h1>", unsafe_allow_html=True)
    st.markdown(
    """
    ### Camera
    - **Function:** Captures video feed for gesture recognition.
    - **Description:** Logitech C922n Streaming Web camera mounted on the LED display panel to capture hand gestures in real-time. It provides high-definition 1080p video at 30fps or 720p at 60fps.
   
    ### PC
    - **Function:** Runs the gesture recognition algorithm.
    - **Description:** A laptop will be used to run the administrator version of the system, and it will be connected to a web camera via USB. The specific scene for gesture recognition can be viewed in real-time on the laptop.

    ### VERONA
    - **Function:** Crystal LED display cabinet(2x2).
    - **Description:** The Sony Crystal LED VERONA is a high-definition display solution designed for professional use. It offers unparalleled image quality with true-to-life colors, deep blacks, and high brightness. The display is built for reliability and longevity, making it ideal for various applications, including broadcasting, control rooms, and high-end digital signage. VERONA panels are modular, allowing for flexible installation and scalability to fit different sizes and configurations.

    ### Helios
    - **Function:** LED display controller.
    - **Description:** The Helios LED Processing Platform by Megapixel VR is a state-of-the-art solution designed for high-performance and large-format displays. In this system, it will be used to control the LED display panels. It provides api for developers to control the display panels and can be integrated with other systems for advanced features.
         """)

    st.divider()

    st.markdown("<h3 style='text-align: center; color: black;'>Software Overview</h1>", unsafe_allow_html=True)

    st.markdown(
    """

    ### OpenCV
    - **Function:**  Primarily used for image capture and display, as well as some image processing and drawing operations, such as converting images from BGR to RGB, drawing hand keypoints, displaying text, and more.
    - **Description:** OpenCV (Open Source Computer Vision Library) is an open-source library of programming functions mainly aimed at real-time computer vision. It is used in this system for capturing and processing video and images.
    
    ### Mediapipe
    - **Function:**  Used for hand tracking and gesture recognition.
    - **Description:** Mediapipe is a cross-platform framework for building multimodal (e.g., voice, face, hand) applications. It provides a set of libraries for building applications that can recognize and manipulate various types of data, including hand gestures. In this system, it will be used for hand tracking and gesture recognition.
    
    ### Python
    - **Function:**  Primary programming language used for the system.
    - **Description:** Python is a high-level programming language that is widely used for various applications, including data analysis, machine learning, and web development. It is used in this system for implementing the gesture recognition algorithm.
    
    ### Request
    - **Function:**  Used for sending HTTP requests to the controller.
    - **Description:** Request is a Python library that allows you to send HTTP/1.1 requests. It is used in this system to send HTTP requests to the controller to control the LED display panels.
    
    ### ESDNet
    - **Function:**  Used for removing moiré patterns from 4K images. 
    - **Description:** ESDNet is a deep learning-based approach introduces a semantic-aligned scale-aware module (SAM) to handle scale variations in moiré patterns efficiently. ESDNet uses an encoder-decoder architecture with SAM to achieve high performance while being lightweight. 
    
    ### Streamlit
    - **Function:**  Used for creating the user interface.
    - **Description:** Streamlit is an open-source Python library that makes it easy to create beautiful and shareable web apps. It is used in this system for creating the admin/user interface.

    """)