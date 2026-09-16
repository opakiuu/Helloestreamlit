#2026/9/15
import streamlit as st
import cv2
import numpy as np

st.title("Sabrina app")

# User inputs
x = st.number_input("X position", min_value=0, value=1700)
y = st.number_input("Y position", min_value=0, value=1100)

if st.button("Generate"):

    art = cv2.imread("art.jpg")
    background = cv2.imread("background.jpg")

    art = cv2.resize(art, (400, 400))

    mask = np.any(art < 250, axis=2)

    h, w = art.shape[:2]

    roi = background[y:y+h, x:x+w]

    roi[mask] = art[mask]

    # OpenCV BGR → RGB for Streamlit
    result = cv2.cvtColor(background, cv2.COLOR_BGR2RGB)

    st.image(result, caption="Result")