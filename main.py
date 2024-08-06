import streamlit as st
from PIL import Image
import os
import numpy as np
import hydralit_components as hc
# Set page title and icon

st.set_page_config(
    page_title="AdFreeze & MoiréFix",
    layout="wide",
    page_icon="🪄",
)

st.markdown('''
    <style>
   
    @media (max-width: 768px) {
        .title {
            font-size: 1.5em;
        }
        .subtitle {
            font-size: 1.2em;
        }
        .description {
            font-size: 0.9em;
            padding: 0 5%;
        }
    }
            ''', unsafe_allow_html=True)

Home_page = st.Page(page = "Pages/Home.py", title = "HOME", icon = "🌏")
Freeze_Screen_page = st.Page(page = "Pages/Freeze_Screen.py", title = "Freeze Screen", icon = "🧊")
MoiréFix_page = st.Page(page = "Pages/MoiréFix.py", title = "MoiréFix", icon = "🧩")
Contact_page = st.Page(page = "Pages/Contact Us.py", title = "Contact Us", icon = "💬")
pg = st.navigation([Home_page, Freeze_Screen_page, MoiréFix_page, Contact_page])
pg.run()




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



