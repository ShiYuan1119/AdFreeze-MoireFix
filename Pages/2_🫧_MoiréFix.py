import streamlit as st
import torch
import sys
import os
import torchvision.transforms as transforms
import torch.nn.functional as F
from PIL import Image
from io import BytesIO
import math
import time

# Set the page config
st.set_page_config(layout="wide", page_title="AdFreeze & MoiréFix", page_icon="🪄")

# Add the models folder to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'models')))
from models.nets import my_model

# Set the device to GPU if available
os.environ["CUDA_VISIBLE_DEVICES"] = "1"
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

@st.cache_resource
def load_model():
    model = my_model(
        en_feature_num=48,
        en_inter_num=32,
        de_feature_num=64,
        de_inter_num=32,
        sam_number=1,
    ).to(device)

    load_path = "./models/mix.pth"
    model_state_dict = torch.load(load_path, map_location=device)
    model.load_state_dict(model_state_dict)
    model.eval()
    return model

model1 = load_model()

def img_pad(x, w_pad, h_pad, w_odd_pad, h_odd_pad):
    x1 = F.pad(x[:, 0:1, ...], (w_pad, w_odd_pad, h_pad, h_odd_pad), value=0.3827)
    x2 = F.pad(x[:, 1:2, ...], (w_pad, w_odd_pad, h_pad, h_odd_pad), value=0.4141)
    x3 = F.pad(x[:, 2:3, ...], (w_pad, w_odd_pad, h_pad, h_odd_pad), value=0.3912)
    return torch.cat([x1, x2, x3], dim=1)

def preprocess_image(img):
    t_list = [transforms.ToTensor()]
    composed_transform = transforms.Compose(t_list)
    return composed_transform(img)

def image_to_bytes(img):
    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    return img_byte_arr

@st.cache_resource
def process_image_bytes(image_bytes):
    img = Image.open(BytesIO(image_bytes))
    in_img = preprocess_image(img).to(device).unsqueeze(0)
    b, c, h, w = in_img.size()
    w_pad = (math.ceil(w / 32) * 32 - w) // 2
    w_odd_pad = w_pad
    h_pad = (math.ceil(h / 32) * 32 - h) // 2
    h_odd_pad = h_pad

    if w % 2 == 1:
        w_odd_pad += 1
    if h % 2 == 1:
        h_odd_pad += 1

    in_img = img_pad(in_img, w_pad=w_pad, h_pad=h_pad, w_odd_pad=w_odd_pad, h_odd_pad=h_odd_pad)

    progress_container = st.empty()
    info_container = st.empty()

    progress = progress_container.progress(0)
    info_container.info("Starting model processing...", icon = "⏳")

    with torch.no_grad():
        out_1, out_2, out_3 = model1(in_img)
        progress.progress(50)
        info_container.info("Model processing done...", icon = "✅")
        if h_pad != 0:
            out_1 = out_1[:, :, h_pad:-h_odd_pad, :]
        if w_pad != 0:
            out_1 = out_1[:, :, :, w_pad:-w_odd_pad]
    
    progress.progress(75)
    info_container.info("Building output image...", icon = "⏳")

    out_1 = out_1.squeeze(0)
    out_1 = Image.fromarray(torch.clamp(out_1 * 255, min=0, max=255).byte().permute(1, 2, 0).cpu().numpy())

    fixed_image_bytes = BytesIO()
    out_1.save(fixed_image_bytes, format='PNG')
    fixed_image_bytes.seek(0)

    progress.progress(100)
    time.sleep(0.5)
    progress_container.empty()
    info_container.empty()
    st.success("Image processing successfully done! The fixed image is ready to download.")
    
    return fixed_image_bytes

st.markdown(
        "<h3 style='text-align: center; color: black;font-size: 50px'>Clean Your Moire Images!</h1>",
        unsafe_allow_html=True)
#st.title("")
st.write(
    "🐧Try uploading an image to watch the moire patterns magically removed. \n"
    "Fixed images can be downloaded from the sidebar. \n"
    "⏳Note: It may cost more than 40s per 4K image(e.g., iPhone:4032x3024).\n"
    "Check out the [paper](https://arxiv.org/abs/2207.09935) which describes more details about the model and the training process."
)
st.sidebar.write("## Upload and download :gear:")

col1, col2 = st.columns(2)

def fix_image(image_path):
    image = Image.open(image_path)
    col1.write("Original Image :camera:")
    col1.image(image)
    
    start_time = time.time()
    
    image_bytes = image_to_bytes(image)
    fixed_image_bytes = process_image_bytes(image_bytes)
    
    fixed_image = Image.open(fixed_image_bytes)
    col2.write("Fixed Image :wrench:")
    col2.image(fixed_image)
    
    end_time = time.time()
    processing_time = end_time - start_time

    st.markdown("""
        <style>
        .stDownloadButton button {
            background-color: #4CAF50; /* green background*/
            color: white; /* white text */
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 12px; /* circle shape */
        }
        .stDownloadButton button:hover {
            background-color: #45a049; /* green background when hovered */
        }
        </style>
    """, unsafe_allow_html=True)
   
    st.sidebar.download_button(
        label="Download fixed image",
        data=fixed_image_bytes,
        file_name="fixed.png",
        mime="image/png"
    )

    st.sidebar.success(f"Processing time: {processing_time:.2f} seconds")

my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if my_upload is None:
    col1.write("Original Image :camera:")
    col1.image("./penguin.jpg")
    col2.write("Fixed Image :wrench:")
    col2.image("./penguin_fixed.png")
else:
    fix_image(my_upload)
