import streamlit as st

def resources_page():
    st.markdown(
        '<h1 style="text-align: center;">Resources</h1>', unsafe_allow_html=True)
    st.markdown(
         '<div style="text-align: justify;"><p style="text-indent: 2em;">Here, you will find a comprehensive collection of materials that provide in-depth information and guidance on the technologies and methodologies employed in this system. These resources include academic papers, official manuals, and other reference materials to help you better understand and utilize the system.</p></div>', unsafe_allow_html=True)
    st.divider()
    st.markdown(
       """
        ### Academic Papers
        - [MediaPipe: A Framework for Building Perception Pipelines](https://arxiv.org/abs/1906.08172)
        - [Towards Efficient and Scale-Robust Ultra-High-Definition Image Demoireing](https://arxiv.org/abs/2207.09935)
    """)
    st.divider()
    st.markdown(
        """
        ### Official Manuals
        - [Crystal LED VERONA 2404](https://www.sony.jp/products/catalog/Crystal_LED_VERONA_2404.pdf)
        - [HELIOS - Megapixel](https://megapixelvr.com/helios/)
        - [OpenCV - Open Computer Vision Library](https://opencv.org/)
        - [Home - MediaPipe](https://chuoling.github.io/mediapipe/)
        - [MediaPipe Solution guide](https://ai.google.dev/edge/mediapipe/solutions/guide)
        - [Requests: HTTP for Humans](https://requests.readthedocs.io/en/master/)
        - [Streamlit - A fastest way to build and share data apps](https://streamlit.io/)
""")
    
    st.divider()
    st.markdown(
        """
        ### Reference Materials
        - [Logicool C922N Pro Stream Webcam](https://www.logicool.co.jp/ja-jp/products/webcams/c922n-pro-stream-webcam.960-001262.html)
        - [HELIOS LED Processing Platform User Guide](https://megapixelvr.com/wp-content/uploads/2023/09/megapixel-helios-processing-system-user-guide.pdf)
        - [MediaPipe on GitHub](https://github.com/google-ai-edge/mediapipe)
        - [OpenCV release](https://opencv.org/releases/)
""")