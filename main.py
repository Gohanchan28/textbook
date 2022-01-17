# -*- coding: utf-8 -*-
import fpdf
import graphviz as graphviz
import streamlit as st
import os
import base64
import pandas as pd
import sqlite3 
import hashlib
import numpy as np
from fpdf import FPDF
import base64
from PIL import Image
import requests

def main():
    st.write("""
     Test!
    """)

add_selectbox = st.sidebar.selectbox(
    "Choose the chapter",
    (
        "Chapter１ 時制", 
        "Chapter２ 助動詞", 
        "Chapter３ 動名詞",
        "小学生作文"
    )
)

#cute but...just once, maybe! ;)
#st.balloons()

image = Image.open('interext_chapter1.png')
st.image(image, caption='Am I still dreaming?')

st.write("Chapter 1: 時制")


# text components
st.caption('文法の基礎')
st.markdown('**品詞**')

# user input
title = st.text_input('Write down what you heard here!')
st.write('Your answer', title)

# user input as a form
with st.form(key='my_form'):

    audio_file = open('test.mp3', 'rb')
    # audio_file = open('test.ogg', 'rb')
    audio_bytes = audio_file.read()

    st.audio(audio_bytes, format='audio/mp3')
    # st.audio(audio_bytes, format='audio/ogg')

    text_input = st.text_input(label='What did you hear?')
    submit_button = st.form_submit_button(label='Submit')

with st.expander("Read the script"):
    st.write("""
        I should have known that you would be here.
    """)
    'Hello world!'

    #File download 
    with open('basic_grammer.pdf') as file:
        file.write(response.content)
    #file = basic_grammer.pdf
        filename = 'basic_grammer'
        st.download_button("basic_grammer.pdf", file)

    clicked = st.button('Just click! Nothing will happen I promise!')


col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")

report_text = st.text_input("Report Text")

export_as_pdf = st.button("Export Report")

def create_download_link(val, filename):
    b64 = base64.b16decode(val) #val looks
    return f'<a href="data:application/octet-streaml;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'

if export_as_pdf:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(40, 10, report_text)

    html = create_download_link(pdf.output(dest="S"), filename)

    st.markdown(html, unsafe_allow_html=True)

st.graphviz_chart('''
    digraph {
        run -> intr
        intr -> runbl
        runbl -> run
        run -> kernel
        kernel -> zombie
        kernel -> sleep
        kernel -> runmem
        sleep -> swap
        swap -> runswap
        runswap -> new
        runswap -> runmem
        new -> runmem
        sleep -> runmem
    }
''')