#! /usr/bin/env python
#coding=utf-8
from pathlib import Path
import streamlit as st
from PIL import Image

# ---  PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
img_Black = current_dir / "Images" / "Black.avif"


def FCT_Down( Fisier_PDF, LABEL ):
	with open(Fisier_PDF,"rb") as pdf_file:
		PDFbyte = pdf_file.read()
	st.download_button(
		label=LABEL, data=PDFbyte, 
		file_name=Fisier_PDF.name, 
		mime="application/octet-stream",   	)
	return


def app():
	# --- GENERAL VARIABLES ---
#	PAGE_TITLE = "Books"  ;  st.title(PAGE_TITLE)
	st.title(":books:  :green[Published Books]") 
	st.subheader(":gray[10 books, of which 6 as unique author:]") 

	# --- LIST OF BOOKS   ---

	# ================================================================
	st.write("---")
	image_Monography1 = current_dir / "Images" / "Python_Monography_1.jpg"
	st.image(Image.open(image_Monography1), width=700)
	image_Monography2 = current_dir / "Images" / "Python_Monography_2.jpg"
	st.image(Image.open(image_Monography2), width=700)

	col1, col2 = st.columns(2,gap="small")
	with col1:
		st.write( """
			- :one: Authors: Dorian NEDELCU & Tihomir Latinovic
			- Title: Programming engineering application in Python, wxPython and Streamlit
			- Publishing: Presa Universitara Clujeana, Cluj-Napoca, Romania
			- ISBN: 978-606-37-2500-5
			- Year of publication: 2025
			- No. of pages: 201
			- Language: English.
		""" 		)

	with col2:
		col2.link_button("Download PDF file of the book", "http://www.editura.ubbcluj.ro/www/ro/books/search.php")

		st.write( """:information_source: Write 'Python' word in Search field to find the PDF file""")
		st.write( """   """) ; st.write( """   """)
		st.write( """   """) ; st.write( """   """)

		Monography_Code_file = current_dir / 'DOCS' / 'Monography_files.zip'
		FCT_Down( Monography_Code_file, "Download the code of the scripts - 425 MB" )

	st.write( """:green[The book "Programming Engineering Application in Python, wxPython and Streamlit" by Dorian Nedelcu and Tihomir Latinovic 
		   is designed for both beginners and those with some programming experience. It covers various applications of Python, including 
		   numerical integration, databases, image operations, and more. The content is accessible, making it suitable for students, teachers 
		   and self-learners. Each application comes with the complete code as well as detailed explanations and visual results.]""" )

		# ================================================================
	st.write("---")
	col1, col2 = st.columns(2,gap="small")
	with col1:
		st.write( """
			- :two: Author: Dorian NEDELCU
			- Title: RESISTANCE CALCULUS APPLICATIONS WITH SOLIDWORKS SIMULATION
			- Publishing: Eftimie Murgu, Reşiţa
			- ISBN: 978-606-631-071-0
			- Year of publication: 2018
			- No. of pages: 233
			- Language: Romanian.
		"""   	)
	with col2:
		image_Simulation = current_dir / "Images" / "Book_Simulation.jpg"
		st.image(Image.open(image_Simulation), width=150)

		SW_Sim_file = current_dir / 'DOCS' / 'Book_SW_Simulation.pdf'
		FCT_Down( SW_Sim_file, "Download book" )


		# ================================================================
	st.write("---")
	col1, col2 = st.columns(2,gap="small")
	with col1:
		st.write( """
			- :three: Author: Dorian NEDELCU
			- Title: CAD AND NUMERICAL SIMULATION WITH SOLIDWORKS
			- Publishing: Eurostampa, Timişoara
			- ISBN: 978-606-569-276-3
			- Year of publication: 2011
			- No. of pages: 380
			- Language: Romanian & English.
		"""   	)
	with col2:
		image_SW = current_dir / "Images" / "Book_SW.jpg"
		st.image(Image.open(image_SW), width=150)

		SW_file = current_dir / 'DOCS' / 'Book_SolidWorks.pdf'
		FCT_Down( SW_file, "Download book" )

		# ================================================================
	st.write("---")
	col1, col2 = st.columns(2,gap="small")
	with col1:
		st.write( """
			- :four: Authors: Dorian NEDELCU & Vasile COJOCARU
			- Title: AUTOCAD GRAPHIC DESIGN
			- Publishing: Eftimie Murgu, Reşiţa
			- ISBN: 978-973-1906-84-36
			- Year of publication: 2010
			- No. of pages: 510
			- Language: Romanian.
		"""   	)
	with col2:
		image_Autocad = current_dir / "Images" / "Book_Autocad.jpg"
		st.image(Image.open(image_Autocad), width=150)

		Autocad_file = current_dir / 'DOCS' / 'Book_AutoCAD.pdf'
		FCT_Down( Autocad_file, "Download book" )

		# ================================================================
	st.write("---")
	col1, col2 = st.columns(2,gap="small")
	with col1:
		st.write( """
			- :five: Authors: Tiberiu Stefan MĂNESCU & Dorian NEDELCU
			- Title: STRUCTURAL ANALYSIS BY FINITE ELEMENT METHOD
			- Publishing: Orizonturi Universitare, Timişoara
			- ISBN: 973-638-217-6
			- Year of publication: 2005
			- No. of pages: 232
			- Language: Romanian.
		"""   	)
	with col2:
		image_FEM = current_dir / "Images" / "Book_FEM.jpg"
		st.image(Image.open(image_FEM), width=150)

		FEM_file = current_dir / 'DOCS' / 'Book_FEM.pdf'
		FCT_Down( FEM_file, "Download book" )

		# ================================================================
	st.write("---")
	col1, col2 = st.columns(2,gap="small")
	with col1:
		st.write( """
			- :six: Author: Dorian NEDELCU 
			- Title: PARMETRICAL MODELLING WITH AUTODESK INVENTOR
			- Publishing: Orizonturi Universitare, Timişoara
			- ISBN: 973-638-116-1
			- Year of publication: 2004
			- No. of pages: 430
			- Language: Romanian.
		"""   	)
	with col2:
		image_Inventor = current_dir / "Images" / "Book_Inventor.jpg"
		st.image(Image.open(image_Inventor), width=150)

		INVENTOR_file = current_dir / 'DOCS' / 'Book_Inventor.pdf'
		FCT_Down( INVENTOR_file, "Download book" )
	
	# ================================================================
	st.write("---")
	col1, col2 = st.columns(2,gap="small")
	with col1:
		st.write( """
			- :seven: Author: Dorian NEDELCU 
			- Title: 2D/3D COMPUTER AIDED DESIGN APPLICATIONS
			- Publishing: Orizonturi Universitare, Timişoara
			- ISBN: 973-638-037-8
			- Year of publication: 2003
			- No. of pages: 203
			- Language: Romanian.
		"""   	)
	with col2:
		image_Proiectare = current_dir / "Images" / "Book_PTAC.jpg"
		st.image(Image.open(image_Proiectare), width=150)
		
		PTAC_file = current_dir / 'DOCS' / 'Book_PTAC.pdf'
		FCT_Down( PTAC_file, "Download book" )
	
	# ================================================================
	st.write("---")
	col1, col2 = st.columns(2,gap="small")
	with col1:
		st.write( """
			- :eight: Author: Dorian NEDELCU 
			- Title: MICROSOFT EXCEL. THEORETICAL CONCEPTS AND APPLICATIONS
			- Publishing: Orizonturi Universitare, Timişoara
			- ISBN: 973-638-008-4
			- Year of publication: 2003
			- No. of pages: 200
			- Language: Romanian.
		"""   	)
	with col2:
		image_Excel = current_dir / "Images" / "Book_Excel.jpg"
		st.image(Image.open(image_Excel), width=150)
	
		Excel_file = current_dir / 'DOCS' / 'Book_Excel.pdf'
		FCT_Down( Excel_file, "Download book" )
	
	# ================================================================
	st.write("---")
	col1, col2 = st.columns(2,gap="small")
	with col1:
		st.write( """
			- :nine: Author: Dorian NEDELCU 
			- Title: COMPUTER PROGRAMMING IN TURBOPASCAL
			- Publishing: Eurostampa, Timişoara
			- ISBN: 973-687-013-8
			- Year of publication: 2002
			- No. of pages: 228
			- Language: Romanian.
		"""   	)
	with col2:
		image_Pascal = current_dir / "Images" / "Book_Pascal.jpg"
		st.image(Image.open(image_Pascal), width=150)

		Pascal_file = current_dir / 'DOCS' / 'Book_Pascal.pdf'
		FCT_Down( Pascal_file, "Download book" )

	# ================================================================
	st.write("---")
	col1, col2 = st.columns([0.7,0.3])
	with col1:
		st.write( """
			- :one::zero: Author: Dorian NEDELCU 
			- Title: COMPUTER AIDED DESIGN BY MICROSTATION
			- Publishing: Eurostampa, Timişoara
			- ISBN: 973-8244-03-X
			- Year of publication: 2001
			- No. of pages: 364
			- Language: Romanian.
		""" 		)

	with col2:
		image_Microstation = current_dir / "Images" / "Book_Microstation.jpg"
		st.image(Image.open(image_Microstation), width=150)

		Microstation_file = current_dir / 'DOCS' / 'Book_Microstation.pdf'
		FCT_Down( Microstation_file, "Download book" )

	st.write("---")
	
