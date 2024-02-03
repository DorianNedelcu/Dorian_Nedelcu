#! /usr/bin/env python
#coding=utf-8
from pathlib import Path
import streamlit as st
import smtplib
from email.mime.text import MIMEText


# ---  PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()

def app():
	# --- GENERAL VARIABLES ---
#	PAGE_TITLE = "Contact"  ;  st.title(PAGE_TITLE)
	st.title(":email: :green[CONTACT]")
	

	# --- EMAILS ---
	st.write("#")
	st.subheader(":red[Emails]") 
	st.title(" :e-mail:" )
	st.write(":large_yellow_square: dorian.nedelcu@ubbcluj.ro")
	st.write(":large_yellow_square: ne_dor@yahoo.com")
	st.write(":large_yellow_square: nedor1957@gmail.com")
