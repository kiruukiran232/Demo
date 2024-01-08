import streamlit as st
st.set_page_config(page_title='My_Pets')
st.header("Types of Pets")

col1, col2 = st.columns(2)
with col1:
  st.subheader("Pilla Pichuka")
  st.image("./IMG-20230405-WA0002.jpg", caption="Pilla Pichuka", width=300,use_column_width=True)
  st.write("This pilla pichuka is very rare piece in the world")
with col2:
  st.subheader("Donkollu Pattevodu")
  st.image("./Screenshot_20221127-143419_Call.jpg", caption="Donkollu Pattevodu", width=300,use_column_width=True)
  st.write("This Donkollu pattevodu always catch Hens")
