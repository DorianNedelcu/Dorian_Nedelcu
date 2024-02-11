#! /usr/bin/env python
#coding=utf-8

import streamlit as st
from PIL import Image
from pathlib import Path
import CV, Academic, PhD_Thesis, Books, Articles
import Research, Programming, YouTube, Contact

st.set_page_config(
	page_title="Dorian NEDELCU",
	page_icon="🧊",
	initial_sidebar_state="expanded" )
	# layout="wide",

# ---  PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
img_Black = current_dir / "Images" / "Black.avif"
st.markdown(f"""
            <style>
            .stApp {{background-image: img_Black); 
                     background-attachment: fixed;
                     background-size: cover}}
			</style>
			""", unsafe_allow_html=True)

st.header(":large_blue_square: Dorian NEDELCU Activity :arrow_down:")

st.sidebar.title(":classical_building: Dorian Nedelcu")
st.sidebar.write("---")
st.sidebar.write(":point_down: :red[Select an option below!] ")

sidebar = { "backgroundColor": "#fffd80", "contrast": 1.2 }

if st.sidebar.button(':gear: Digital CV ', use_container_width=True):
	CV.app()
if st.sidebar.button(':chart: Academic Info', use_container_width=True):
	Academic.app()
if st.sidebar.button(':ice_cube:  PhD Thesis Supervised', use_container_width=True):
	PhD_Thesis.app()
if st.sidebar.button(':books: Published Books', use_container_width=True):
	Books.app()
if st.sidebar.button(':chart_with_upwards_trend: Published Articles', use_container_width=True):
	Articles.app()
if st.sidebar.button(':anger: Research Projects', use_container_width=True):
	Research.app()
if st.sidebar.button(':hammer_and_pick: Programming', use_container_width=True):
	Programming.app()
if st.sidebar.button(':o: YouTube Videos', use_container_width=True):
	YouTube.app()
if st.sidebar.button(':email: Contact', use_container_width=True):
	Contact.app()

	
	

		 


