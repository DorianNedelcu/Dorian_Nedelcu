#! /usr/bin/env python
#coding=utf-8

import streamlit as st
st.set_page_config(
	page_title="Dorian NEDELCU",  )
# set_page_config() can only be called once per app page, 
# and must be called as the first Streamlit command in your script.

from pathlib import Path
#from streamlit_option_menu import option_menu
import streamlit_option_menu
from PIL import Image
import CV, Academic, PhD_Thesis, Books, Articles, Research, Programming, YouTube, Contact

# ---  PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
#st.write(current_dir)
profile_image = current_dir / "Images" / "Dorian Nedelcu.jpg"
# CV_file = current_dir / "DOCS" / "Dorian Nedelcu.jpg"


class MultiApp:

	def __init__(self):
		self.apps = []

	def add_app(self, title, func):

		self.apps.append({
			"title": title,
			"function": func
		})

	def run():
		# app = st.sidebar(
		with st.sidebar:		
			app = option_menu(
				menu_title='Dorian NEDELCU ',
				options=['CV','Academic','PhD Thesis','Books', 'Articles', 'Research', 'Programming', 'YouTube', 'Contact'],
#				icons=[":wave:",":wave:",":wave:",":wave:",":wave:",":wave:",":wave:",":wave:",":wave:"],
#				menu_icon='chat-text-fill',
				default_index=0,
				styles={
					"container": {"padding": "5!important","background-color":'black'},
		"icon": {"color": "white", "font-size": "23px"}, 
		"nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
		"nav-link-selected": {"background-color": "#02ab21"},}
			)
		if app == "CV":
			CV.app()
		if app == "Academic":
			Academic.app()	
		if app == "PhD Thesis":
			PhD_Thesis.app()   
		if app == "Books":
			Books.app()  
		if app == "Articles":
			Articles.app()  
		if app == "Research":
			Research.app()  		
		if app == "Programming":
			Programming.app() 
		if app == "YouTube":
			YouTube.app()  
		if app == "Contact":
			Contact.app()  
	run()			
		 


