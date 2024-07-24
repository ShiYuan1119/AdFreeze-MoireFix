import streamlit as st
from PIL import Image
import os
import torch

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
        justify-content: center;
        align-items: center;
        height: 100vh;
        text-align: center;
        
    }
    .image {
        margin: 20px 0;
    }
    .title {
        font-size: 3em;
        color: #4682B4;
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
        <div class="image">
            <img src="https://www.researchgate.net/publication/362871842/figure/fig1/AS:11431281084350163@1663153181104/MediaPipe-Hands-21-landmarks-13.ppm" salt="Example Image" width="300">
        </div>
        <div class="title">AdFreeze & MoiréFix</div>
        <div class="subtitle">Welcome to AdFreeze & MoiréFix! 👋</div>
        <div class="description">
            Easily freeze LED screens with a gesture and remove moiré patterns from your photos. Your Solution for Perfect LED Screen Photography.
        </div>
    </div>
    ''', unsafe_allow_html=True)

# Navigation
st.sidebar.title("Navigation")
st.sidebar.markdown("[Home](#)")
st.sidebar.markdown("[Freeze Screen](#freeze-screen)")
st.sidebar.markdown("[MoiréFix](#moirefix)")
st.sidebar.markdown("[Contact Us](#contact-us)")



# Page footer
st.markdown("---")
st.markdown("© 2024 AdFreeze & MoiréFix. All rights reserved.")

