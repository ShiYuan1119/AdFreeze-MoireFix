import streamlit as st
import numpy as np
import hydralit_components as hc
from Pages.SubPages.Guide import Guide_page
from Pages.SubPages.HW_SW import HW_SW
from Pages.SubPages.Resources import resources_page
from Pages.SubPages.FAQ import FAQ_page





# NavBar

GUIDE = 'Guide'
DETALIS = 'Hardware/Software'
RESOURCE = 'Resources'
FAQ = 'FAQ'

tabs = [
    GUIDE,
    DETALIS,
    RESOURCE,
    FAQ,
]

option_data = [
    {'icon': "🏠", 'label': GUIDE},
    {'icon': "🧩", 'label': DETALIS},
    {'icon': "📑", 'label': RESOURCE},
    {'icon': "❔", 'label': FAQ},
]

over_theme = {'txc_inactive': 'black', 'menu_background': '#D6E5FA', 'txc_active': 'white', 'option_active': '#749BC2'}
font_fmt = {'font-class': 'h3', 'font-size': '50%'}

st.markdown("""
    <style>
    .navbar-container {
        display: flex;
        overflow-x: auto;
        white-space: nowrap;
    }
    .navbar-item {
        flex: none;
        margin-right: 15px;
    }
    .hc_option_bar {
        display: flex;
        overflow-x: auto;
        white-space: nowrap;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="navbar-container">', unsafe_allow_html=True)

chosen_tab = hc.option_bar(
    option_definition=option_data,
    title='',
    key='PrimaryOptionx',
    override_theme=over_theme,
    horizontal_orientation=True,
)

st.success("Welcome to AdFreeze & MoiréFix! "
           "In this interface, you will learn how to freeze and freeze off LED screen using gestures. "
           "Please note that there are certain limitations regarding gestures and distance between the device and the screen."
           "Hoping you have an enjoyable experience 😊")

if chosen_tab == GUIDE:
    Guide_page()
elif chosen_tab == DETALIS:
    HW_SW()
elif chosen_tab == RESOURCE:
    resources_page()
elif chosen_tab == FAQ:
    FAQ_page()
    
