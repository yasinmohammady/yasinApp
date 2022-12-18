import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

img1 = Image.open("images/img1.png")
img2 = Image.open("images/img2.png")
img3 = Image.open("images/img3.png")
img4 = Image.open("images/img4.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Sven :wave:")
    st.title("A Data Analyst From Germany")
    st.write(
        "I am passionate about finding ways to use Python and VBA to be more efficient and effective in business settings."
    )

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            On my YouTube channel I am creating tutorials for people who:
            - are looking for a way to leverage the power of Python in their day-to-day work.
            - are struggling with repetitive tasks in Excel and are looking for a way to use Python and VBA.
            - want to learn Data Analysis & Data Science to perform meaningful and impactful analyses.
            - are working with Excel and found themselves thinking - "there has to be a better way."

            If this sounds interesting to you, consider subscribing and turning on the notifications, so you don’t miss any content.
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- Graphics ----
# import pandas as pd 
# import numpy as np 
# import matplotlib.pyplot as plt 
# import streamlit as st
# SampleData = pd.read_excel('Numunelerin yük taşıma kapasitesi.xlsx', sheet_name = 'Sayfa1') 
# cols = SampleData.columns.values.tolist()
#plt.figure(figsize=(8, 3))


#Yük Grafiği
# plt.bar(SampleData['Numune ismi'], SampleData['Yük (kN)'], color="red")
# plt.title('', fontsize=12)
# plt.xlabel('Numune ismi', fontsize=8)
# plt.ylabel('Yük (kN)', fontsize=8)
with st.container():
    st.write("---")
    st.header("Grafikler")
    st.write("##")
    image_column, text_column = st.columns((2, 1))
    with image_column:
        st.image(img1)
    with text_column:
        st.subheader("Yük Grafiği")
        st.write(
            """
            """
        )
st.write("##")
# #Yerdeğiştirme Grafiği
# plt.bar(SampleData['Numune ismi'], SampleData['Yerdeğiştirme (mm)'], color="blue")
# plt.title('', fontsize=12)
# plt.xlabel('Numune ismi', fontsize=8)
# plt.ylabel('Yerdeğiştirme (mm)', fontsize=8)
with st.container():
    image_column, text_column = st.columns((2, 1))
    with image_column:
        st.image(img2)
    with text_column:
        st.subheader("Yerdeğiştirme Grafiği")
        st.write(
            """
            """
        )
st.write("##")
# #Enerji Tüketimi (kNmm) Grafiği
# plt.bar(SampleData['Numune ismi'], SampleData['Enerji Tüketimi (kNmm)'], color="black")
# plt.title('', fontsize=12)
# plt.xlabel('Numune ismi', fontsize=8)
# plt.ylabel('Enerji Tüketimi (kNmm)', fontsize=8)
with st.container():
    image_column, text_column = st.columns((2, 1))
    with image_column:
        st.image(img3)
    with text_column:
        st.subheader("Enerji Tüketimi (kNmm) Grafiği")
        st.write(
            """
            """
        )
st.write("##")
# #Rijitlik (kN/mm) Grafiği
# plt.bar(SampleData['Numune ismi'], SampleData['Rijitlik (kN/mm)'], color="pink")
# plt.title('', fontsize=12)
# plt.xlabel('Numune ismi', fontsize=8)
# plt.ylabel('Rijitlik (kN/mm)', fontsize=8)
with st.container():
    image_column, text_column = st.columns((2, 1))
    with image_column:
        st.image(img4)
    with text_column:
        st.subheader("Rijitlik (kN/mm) Grafiği")
        st.write(
            """
            """
        )
