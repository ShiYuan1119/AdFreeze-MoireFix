import streamlit as st
from PIL import Image


def Guide_page():
    st.markdown('')
    st.markdown(
        "<h3 style='text-align: center; color: black; font-size: 40px;'>How to Use the Gesture-Based Screen Freeze System</h1>",
        unsafe_allow_html=True)
    
    st.markdown('')
    st.subheader(':blue[Step 1] Positioning')
    col1, col2 = st.columns([2,1], gap = 'medium')

    with col1:
        st.markdown(
            "<h3 style = 'text-align: justify; font-size: 20px;'>Stand within 1 meter of the LED screen. Ensure that the camera can capture your hand clearly.</h3>"
            ,unsafe_allow_html=True)
   
        st.info("💡Make sure that no other person's hands should appear in the frame except for the users.")
   
    with col2:
        image = Image.open('./specified_distance.png')
        st.image(image, use_column_width=True)
    st.markdown('')
    st.subheader(':blue[Step 2] Preparing for Gesture Recognition')
    col3, col4 = st.columns([2,1], gap = 'medium')

    with col3:
        st.markdown(
            "<h3 style = 'text-align: justify; font-size: 20px;'>Hold your phone horizontally as if you are about to take a photo. </h3>"
            ,unsafe_allow_html=True)
        st.info(" 💡Make sure to hold the phone with both hands, and with your index fingers and thumbs visible for easier recognition.")

    with col4:
        image = Image.open('./gesture.jpg')
        st.image(image, use_column_width=True)
    st.markdown('')
    st.subheader(':blue[Step 3] Gesture Recognition and Screen Freeze')
    st.markdown(
        "<h3 style = 'text-align: justify; font-size: 20px;'>When you are ready, the camera will detect the gesture of you are holding the phone to take a photo. The system will immediately freeze the currently playing screen. </h3>"
        ,unsafe_allow_html=True)
    st.info(" ▶️ Now you can take photos of the screen enjoyably while the screen is frozen.")

    st.markdown('')
    st.subheader(':blue[Step 4] Taking the Photo')
    st.markdown(    
        "<h3 style = 'text-align: justify; font-size: 20px;'>After the screen is frozen, you can take a photo of the screen as you normally would. </h3>"
        ,unsafe_allow_html=True)
    st.info(" 💡To freeze the screen successfully, make sure to keep your hand gesture still and not move it during the photo taking process.")

    st.markdown('')
    st.subheader(':blue[Step 5] Freeze Off')
    st.markdown(
        "<h3 style = 'text-align: justify; font-size: 20px;'>After you have taken your photo, change your gesture or simply put down your hands. The screen will automatically freeze off and resume displaying the ongoing content. </h3>"
        ,unsafe_allow_html=True)
    st.info(" 💡Please note that even if you have put down your hands, as long as you maintain the **holding phone** gesture, it will still be recognized as a freeze screen command. ")

    st.markdown('')
    st.subheader(':blue[Step 6] Using MoiréFix to Remove Moire Effects')
    st.markdown(
        "<h3 style = 'text-align: justify; font-size: 20px;'>After taking your photos, you can access the MoiréFix interface from the side bar on the left. Upload your image for moiré pattern removal.  </h3>"
        ,unsafe_allow_html=True)


    st.markdown('')
    st.markdown("<h3 style='color:#FFC93C;'>Important Tips</h3>", unsafe_allow_html=True)



    html_message = """
    <div style="border: 2px solid #abcae8; padding: 10px; border-radius: 10px; background-color: #ffeed5;">
        <p>Ensure you are the only person within the camera's field of view.
        <p>Make sure your hands are clearly visible and positioned as described for accurate gesture recognition.</p>
        <p>The screen will freeze as soon as the system detects the "taking a photo" gesture and will unfreeze once the gesture changes or is no longer recognized.</p>
    </div>
    """

    st.markdown(html_message, unsafe_allow_html=True)