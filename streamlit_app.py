import streamlit as st
import math

st.title("_Menghitung_ Volume tabung :rocket:")

r = st.number_input("masukan jari-jari(cm)",0)
t = st.number_input("masukan tinggi(cm)",0)

if st.button("Hitung Volume", type="primary"):
  v = math.pi*(r**2)*t
  st.success(f'Volume tabung adalah {f:.2f}')
