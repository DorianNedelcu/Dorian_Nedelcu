#! /usr/bin/env python
#coding=utf-8
from pathlib import Path
import streamlit as st
from PIL import Image
#from streamlit_lottie import st_lottie

# ---  PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()

def app():
#	PAGE_TITLE = "ACADEMIC"  ;  st.title(PAGE_TITLE)
	st.title(":chart:   :green[ACADEMIC]") 
#	st.write("#")
	# --- AUTHOR IDENTIFIER ---

	st.subheader(":red[AUTHOR IDENTIFIER]") 
	st.write(":ice_cube: Web of Science – ResearcherID: A-3786-2015")
	st.write("---")
	st.write(":ice_cube: ResearchGate: [link](https://www.researchgate.net/profile/Dorian-Nedelcu)")
	image_Microstation = current_dir / "Images" / "ResearchGate.jpg"
	st.image(Image.open(image_Microstation), width=600)
	st.write("---")
	st.write(":ice_cube: Scopus Author ID: 24366917300: [link](https://www.scopus.com/authid/detail.uri?authorId=24366917300)")
	image_Microstation = current_dir / "Images" / "Scopus.jpg"
	st.image(Image.open(image_Microstation), width=600)
	st.write("---")
	st.write(":ice_cube: Orcid: [link](https://orcid.org/0000-0002-4927-1042)")
	image_Microstation = current_dir / "Images" / "ORCID.jpg"
	st.image(Image.open(image_Microstation), width=600)
	st.write("---")
	st.write(":ice_cube: Google Scholar: [link](https://scholar.google.ro/citations?user=emwk1kgAAAAJ&hl=ro)")
	image_Microstation = current_dir / "Images" / "GoogleScholar.jpg"
	st.image(Image.open(image_Microstation), width=600)
	
#	with col2:
#		vid_name = current_dir / "Videos" / "academic-education-8467490-6670203.mp4"
#		video_file = open(vid_name , 'rb')
#		video_bytes = video_file.read()
#		st.video(video_bytes,  format="video/mp4", start_time=0)
#		st.write("  [link](https://cdnl.iconscout.com/lottie/premium/thumb/academic-education-8467490-6670203.mp4)")
	
	

#	# --- COURSES TAUGHT ---
	st.write("#")
	st.subheader(":red[COURSES TAUGHT]")
	st.write("'Eftimie Murgu' University of Resita, Romania &  Babes-Bolyai University of Cluj-Napoca")
	st.write("Extract from courses taught during 2018-2022") 
	st.write( """
		- Static & Dynamic Analysis using the Finite Element Method (Course, Master)
		- Technical Drawing & Computer Graphics (Course & Laboratory, Master)
		- Rapid Prototyping & Reverse Engineering (Course & Laboratory, Master)
		- Fluid Mechanics & Hydraulic Machines (Course, License)
	"""
	)
	
	# --- SKILLS ---
	st.write("#")
	st.subheader(":red[SKILLS]")
	st.write( """
	- Computer Aided Design (SolidWorks, Autodesk Inventor, AutoCAD, Microstation).
	- Rapid Prototyping & Reverse Engineering (Geomagic Design X, Agisoft Metashape, 3DF ZEPHYR).
	- Strength calculations (SolidWorks Simulation).
	- Fluid simulation (SolidWorks Flow Simulation).
	- Calculation of mechanisms (SolidWorks Motion).
	- Programming languages:  PYTHON,  VIZUAL BASIC, VIZUAL FoxPRO, Microsoft Excel, Microsoft Access, 
		FORTRAN, BASIC, dBASE, PASCAL, FoxPRO, HTML, Basic4Android (B4A), Matplotlib, Streamlit, Three.js.	
	"""
	)

	# --- VISITING PROFESSOR  ---
	st.write("#")
	st.subheader(":red[VISITING PROFESSOR]")
	st.write( """
		- :green[2020...2021], :red[Visiting professor] at the Master's program of Industrial 
				Engineering offered by the Postgraduate Studies and Research 
				Section from the Professional Interdisciplinary Unit of Engineering 
				and Management and Social Sciences (UPIICSA) from the National 
				Polytechnic Institute (IPN), Mexico. Taught in English language 
				the course "SolidWorks" during the semesters: B20 (from September 
				2020 to January 2021) and A21 (from February 2021 to June 2021)  
				for a total of 68 hours.
		- :green[2021],:red[Carrying out the double direction of thesis] of the student Leslie Stefany 
				Sanchez Castillo with registration B190588 of the Master in Industrial 
				Engineering of the Postgraduate Research Section of the UPIIC5A-IPN. 
				The thesis topic is: "Waste reduction through optimization of preforms 
				in the compression vulcanizing process in a company of the automotive industry".
		- :green[2021...2022],  :red[Visiting professor] at the master's program of Industrial Engineering 
				offered by the Postgraduate Studies and Research Section from the Professional 
				Interdisciplinary Unit of Engineering and Management and Social Sciences (UPIICSA) 
				from the National Polytechnic Institute (IPN), Mexico. Taught in English language 
				the course "SolidWorks" from September 2021 to January 2022 and  from February 
				2022 to June 2022 for a total of 68 hours..
		- :green[2022],:red[Carrying out the double direction of thesis] of the student Uziel Mejia Gonzalez 
				with registration of the Master in Industrial Engineering of the Postgraduate 
				Research Section of the UPIIC5A-IPN. The thesis topic is: "Design of a wood plastic 
				composite, for simulation of a bin plastic for the handling and transfer of products ".
		"""
		)
	profile_picture1 = Image.open(current_dir / "Images" / "VisitingProfessor.jpg")
	st.image(profile_picture1, width=500)





