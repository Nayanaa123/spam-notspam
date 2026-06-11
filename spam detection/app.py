import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import os
from datetime import datetime
import textwrap

# Page settings
st.set_page_config(
    page_title="Handwritten Text Generator",
    page_icon="✍️",
    layout="wide"
)

# UI style
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #eef4ff, #f8fbff);
}
.title {
    text-align:center;
    font-size:42px;
    font-weight:bold;
    color:#1e3a8a;
}
.sub {
    text-align:center;
    color:#475569;
    font-size:18px;
    margin-bottom:20px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="title">✍️ Handwritten Text Generator</p>', unsafe_allow_html=True)
st.markdown('<p class="sub">Convert typed text into handwritten-style notes</p>', unsafe_allow_html=True)

# Input box
user_text = st.text_area(
    "Enter your text:",
    height=220,
    placeholder="Type something here..."
)

if st.button("Generate Handwriting"):

    if user_text.strip() == "":
        st.warning("Please enter some text.")
    else:

        # create white page
        img = Image.new("RGB", (1000, 700), color="white")
        draw = ImageDraw.Draw(img)

        # font
        font_path = "fonts/SEGOESC.TTF"
        font = ImageFont.truetype(font_path, 42)

        # wrap lines
        wrapped_text = textwrap.fill(user_text, width=32)

        # blue pen ink
        draw.multiline_text(
            (60, 60),
            wrapped_text,
            fill=(0, 32, 96),
            font=font,
            spacing=18
        )

        # save image
        os.makedirs("generated", exist_ok=True)

        filename = f"generated/handwriting_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        img.save(filename)

        st.success("Handwriting generated successfully ✅")

        st.image(filename, caption="Generated Handwriting", use_container_width=True)