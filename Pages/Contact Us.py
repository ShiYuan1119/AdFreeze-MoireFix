import streamlit as st
import os

# Contact Us
st.set_page_config(
    page_title="AdFreeze & MoiréFix",
    page_icon="🪄",
)


st.header("Contact Us")
st.markdown("If you have any questions or feedback, please reach out to us.")
st.text_input("Your Name")
st.text_input("Your Email")
st.text_area("Your Message")
st.button('Submit')
