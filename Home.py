import streamlit as st
from PIL import Image
import os
from Pages import freeze_screen, moire_fix

# Set page title and icon

st.set_page_config(
    page_title="AdFreeze & MoiréFix",
    page_icon="🪄",
)

# Add custom CSS
st.markdown("""
    <style>
    .centered {
        display: flex;
        flex-direction: column;
        justify-content: justifiy;
        align-items: center;
        height: 100vh;
        text-align: center;
        
    }
    .image {
        margin: 20px 0;
    }
    .title {
        font-size: 3em;
        color: #4072B3;
    }
            
    .subtitle {
        font-size: 2em;
        margin-top: 20px;
    }
    .description {
        font-size: 1.5em;
        margin-top: 10px;
        color: #6c757d;
    }
    </style>
    """, unsafe_allow_html=True)

# Centered content
st.markdown('''
    <div class="centered">
        <div class="title">AdFreeze & MoiréFix</div>
        <div class="image">
            <img src="https://www.researchgate.net/publication/362871842/figure/fig1/AS:11431281084350163@1663153181104/MediaPipe-Hands-21-landmarks-13.ppm" salt="Example Image" width="300">
        </div>
        <div class="subtitle">Welcome to AdFreeze & MoiréFix! 👋</div>
        <div class="description">
            Easily freeze LED screens with a gesture and remove moiré patterns from your photos. Your Solution for Perfect LED Screen Photography.
        </div>
    </div>
    ''', unsafe_allow_html=True)



# Navigation
st.sidebar.title("Navigation")
st.sidebar.markdown("[Introduction](#introduction)")
st.sidebar.markdown("[Freeze Screen](#freeze-screen)")
st.sidebar.markdown("[MoiréFix](#moirefix)")

st.markdown("---")
st.title("Introduction")
st.write("AdFreeze & MoiréFix is a solution for perfect LED screen photography. It provides a simple and user-friendly interface for freezing LED screens with a gesture and removing moiré patterns from your photos. It is designed to work with any smartphone or tablet with a camera and LED screen. The solution is easy to use and can be used for both landscape and portrait photography. The solution is powered by MediaPipe, a machine learning framework that provides solutions for computer vision tasks. The solution is open-source and can be modified and customized to suit your needs.")

st.markdown("---")
st.title("Freeze Screen")
st.write("To freeze the LED screen, you can use the freeze gesture. The freeze gesture is a simple and intuitive way to freeze the LED screen. You can use your thumb to point to the LED screen and then move your fingers towards the camera. This will freeze the LED screen and prevent any further motion. The LED screen will remain frozen until you release your fingers from the screen. The freeze gesture is designed to be easy to use and requires no training. The solution is powered by MediaPipe, a machine learning framework that provides solutions for computer vision tasks. The solution is open-source and can be modified and customized to suit your needs.")

st.markdown("---")
st.title("MoiréFix")
st.write("Moiré is a type of interference that occurs when two or more light sources in the same plane produce a pattern that appears to be a single image. Moiré can be caused by a variety of factors, including the lens used to focus the light, the distance between the light sources, and the angle between the light sources. MoiréFix is a solution for removing moiré patterns from your photos. The solution is designed to work with any smartphone or tablet with a camera and LED screen. The solution is easy to use and can be used for both landscape and portrait photography. The solution is powered by MediaPipe, a machine learning framework that provides solutions for computer vision tasks. The solution is open-source and can be modified and customized to suit your needs.")


st.sidebar.title("More")
st.sidebar.markdown(
    "🪲[Report a bug ](https://github.com/ShiYuan1119/AdFreeze-MoireFix/issues/new?assignees=&labels=bug&projects=&template=bug_report.md&title=)")
st.sidebar.markdown(
    "💡[Features request](https://github.com/ShiYuan1119/AdFreeze-MoireFix/issues/new?assignees=&labels=enhancement&projects=&template=feature_request.md&title=%5BFEATURE%5D)")
st.sidebar.markdown(
    "👩‍💻[Need HELP](https://github.com/ShiYuan1119/AdFreeze-MoireFix/issues/new?assignees=&labels=help+wanted&projects=&template=need-help.md&title=%5BHELP%5D)")



# Page footer
st.markdown("---")
st.markdown("© 2024 AdFreeze & MoiréFix. All rights reserved.")

st.write('This is user verison')