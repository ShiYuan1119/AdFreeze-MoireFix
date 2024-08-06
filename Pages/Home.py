import streamlit as st


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
    <style>
    .centered {
        text-align: center;
        padding: 20px;
    }
    .title {
        font-size: 2em;
        margin-bottom: 20px;
    }
    .image img {
        max-width: 100%;
        height: auto;
    }
    .subtitle {
        font-size: 1.5em;
        margin-top: 20px;
    }
    .description {
        font-size: 1em;
        margin-top: 20px;
        padding: 0 10%;
    }
    @media (max-width: 768px) {
        .title {
            font-size: 1.7em;
        }
        .subtitle {
            font-size: 1.3em;
        }
        .description {
            font-size: 1.1em;
            padding: 0 5%;
        }
    }
    </style>
    <div class="centered">
        <div class="title">AdFreeze & MoiréFix</div>
        <div class="image">
            <img src="https://www.researchgate.net/publication/362871842/figure/fig1/AS:11431281084350163@1663153181104/MediaPipe-Hands-21-landmarks-13.ppm" alt="Example Image" width="300">
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