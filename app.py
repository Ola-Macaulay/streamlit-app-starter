import pandas as pd
import streamlit as st


import get_data as data

st.set_page_config(page_title="WebScrapping - PY101", page_icon="🛒", layout="wide")
st.image("https://unpackai.github.io/unpackai_logo.svg")
st.title("WebScrapping of Lego Prices around the world 🌏")
st.write("*by <Solo>*")
# st.write("---")

st.markdown("This is a list of number within the range of 6")
st.write([1,2,3,4,5])
# st.image("data:image/jpeg;base64,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")


def launch_baloons_and_snow():
  st.baloons()
  st.snow()
st.button("Launch baloons", on_click=st.baloons())

st.button("Make it snow", on_click=st.snow())

fruit=st.radio("Fruit type", ["Apples", "Pears", "Lemons"])
number_of_fruits=st.slider(f"Number of {fruit}, 1, 35")

st.write("There are", number_of_fruits, fruit)
                           
st.write(number_of_fruits/2)