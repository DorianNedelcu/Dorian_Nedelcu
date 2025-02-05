#! /usr/bin/env python
#coding=utf-8
from pathlib import Path
import streamlit as st
from PIL import Image

# ---  PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()

def app():

	# --- GENERAL VARIABLES ---
#	PAGE_TITLE = "Digital CV - Dorian NEDELCU"  ;  st.title(PAGE_TITLE)
	PAGE_ICON = ":flag-ro:"
	NAME = "Dorian NEDELCU"
	DESCRIPTION = """ Former Full Professor at Babes-Bolyai University Cluj Napoca, 
		Faculty of Engineering, Resita, Romania,  currently retired at the age limit.
		"""
	
	st.title(":gear: :green[Digital CV - Dorian NEDELCU]") 
	st.write("---")

	st.link_button(":gray[Dorian NEDELCU - International Member of The Bosnian-Herzegovinian American Academy of Arts and Sciences (BHAAAS) - started from July 2024]", 
				"https://www.bhaaas.org/")
	image_BHAAAS1 = current_dir / "Images" / "BHAAAS1.jpg"
	st.image(Image.open(image_BHAAAS1), width=700)
	st.link_button(":gray[Search BHAAAS members]", "https://www.bhaaas.org/en/dashboard/members")
	image_BHAAAS2 = current_dir / "Images" / "BHAAAS2.jpg"
	st.image(Image.open(image_BHAAAS2), width=700)

	st.write("---")

	# --- COLUMNS SECTION ---	
	col1, col2 = st.columns(2,gap="small")
	with col1:
		st.subheader(":gray[:red[Former] Full Professor at Babes-Bolyai University Cluj Napoca, Faculty of Engineering, Resita, Romania,  currently retired at the age limit...]")
		st.title(" :wave:" )
	with col2:
		profile_picture = Image.open(current_dir / "Images" / "Dorian Nedelcu.jpg")
		st.image(profile_picture, width=300)
		
	st.write("---")
	
	# --- EDUCATION---
#	st.write("#")
	st.subheader(":red[EDUCATION]")
	st.write( """
	- :green[October 1978...1983]  Mechanical Engineering Faculty of Polytechnic, 
			University Timisoara, Romania, Hydraulic Machines specialization, 
			Diploma of Mechanical Engineer with the specialization 
			“Hydraulic and pneumatic machines”.
	- :green[1989...1996] PhD in Mechanical Engineering with the thesis 
			:red[*'Mathematical modelling of hydrodynamic phenomena with application 
			to computer-aided design of axial turbines and radial-axial pumps'*], 
			PhD Leader Acad. Prof. Docent DHC Dr. Ing. [Ioan ANTON](https://ro.wikipedia.org/wiki/Ioan_Anton)
			,Faculty of Politechnic, University Timisoara. 
	- :green[2002] Postgraduate course in pedagogy, 
			Department for Teaching Staff Training, West University of Timisoara.
		""" )

	# --- WORK EXPERIENCE  ---
	st.write("#")
	st.subheader(":red[WORK EXPERIENCE]")
	st.markdown( """
	 - :green[1983...1991] 
			:o: Scientific Researcher,
			:o: Head of the Computer Aided Design Collective Laboratory,
			Scientific research and design in the field of Hydraulic Machines
			:ice_cube: The Research and Development Design Directorate Institut 
	- :green[1991...1999] 
		:o: Principal Scientific Researcher Grade I, Scientific research and design 
		in the field of Hydraulic Machines, :ice_cube: Resita Machine Building Plant, 
	 - :green[1999...2001] Programmer Analyst, Programming, systems maintenance, 
		network administrator, :ice_cube: Resita Forestry Directorate
	 - Lecturer (:green[01.X.2001]), Associate Professor (:green[01.X.2002]), 
		Full Professor (:green[01.X.2008]), :ice_cube: "Eftimie Murgu" University 
		of Resita, Romania 
	 - :green[2009-2019 ] [10 PhD theses supervised](https://eng.ubbcluj.ro/?page_id=2945) in the field of "Mechanical 
		Engineering", :ice_cube: "Eftimie Murgu" University of Resita, Romania.
	- :green[Starting with 2020] "Eftimie Murgu" University of Resita merged with Babes-Bolyai 
		University of Cluj-Napoca, Romania.
	- :green[September 2022] - Retirement from academic activity at the age limit, according article no. 1 
	from the regulations and teaching policy of Babeș-Bolyai University Cluj-Napoca, Romania:
	*Methodology for the continuation of the teachers activitiy and after reaching retirement 
	age. Approved by HS No 16 547/25.09.2018. Amended and supplemented by HS No 10/15.02.2021.*
	[link](https://www.ubbcluj.ro/ro/staff/files/resurse-umane/continuarea_activitatii/Anexa_la_HS_nr_10_completarea_Metodologie_privind_continuarea_activitatii_did_dupa_pensionare.pdf)
	"""  )

	# --- RESEARCH INTERESTS   ---
	st.write("#")
	st.subheader(":red[RESEARCH INTERESTS]") 
	st.write( """
	- Computer Aided Design in Mechanical Engineering.
	- Rapid Prototyping & Reverse Engineering.
	- Strength calculations in Mechanical Engineering by the Finite Element Method.
	- Numerical simulations in the field of fluids.
	- Calculation of mechanisms.
	- Hydraulic Machines Design.
	"""
	)

