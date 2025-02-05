#! /usr/bin/env python
#coding=utf-8
from pathlib import Path
import streamlit as st
from PIL import Image

def FCT_Down( Fisier_PDF, LABEL ):
	with open(Fisier_PDF,"rb") as pdf_file:
		PDFbyte = pdf_file.read()
	st.download_button(
		label=LABEL, data=PDFbyte, 
		file_name=Fisier_PDF.name, 
		mime="application/octet-stream",   	)
	return

# ---  PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()

def app():
	# --- GENERAL VARIABLES ---
#	PAGE_TITLE = "Programming" ; st.title(PAGE_TITLE)
	st.title(":hammer_and_pick:  :green[Programming]") 
	
	# --- PROGRAMMING ---
	st.write("#")
	st.subheader(":large_orange_square: :red[Python]") 


	image_Python = current_dir / "Images" / "Python Introduction.jpg"
	st.image(Image.open(image_Python), width=700)
	col1, col2 = st.columns(2,gap="small")
	with col1:
		st.write("University VITEZ - Python Presentation") 
	with col2:
		Python_file = current_dir / 'DOCS' / 'Python Introduction.pdf'
		FCT_Down( Python_file, "Download presentation" )
	st.write("---")
	st.subheader(":gray[1. PyDigitizer]") 
	col1, col2 = st.columns(2,gap="small")
	with col1:
		st.write(" - A Python module for digitizing 2D curves")
		st.write(" :ice_cube: [Acces files](https://data.mendeley.com/datasets/jnwyr7jzrd/1)")
		st.write(" - Contributors: Dorian Nedelcu & Tihomir Latinovic")
		st.write(" - DOI:10.17632/jnwyr7jzrd.1") 
		st.write( """
			- The digitizing process consists of extracting a curve numerical coordinates from an explicit 
			image. The paper describes the PyDigitizer module for digitizing 2D curves from images, 
			created with the help of free and Open Source resources, using Python as a programming 
			language and wx.Python as a graphical user interface toolkit. 
		"""	 )
		st.write(" - Licence: CC0 1.0:  You can copy, modify, distribute and perform the work, even for commercial purposes, all without asking permission.") 
	with col2:
		image_Simulation = current_dir / "Images" / "PyDigitizer.jpg"
		st.image(Image.open(image_Simulation), width=300)
		image_Simulation = current_dir / "Images" / "PyDigitizer2.jpg"
		st.image(Image.open(image_Simulation), width=300)
		
		col3, col4 = st.columns(2,gap="small")
		with col3:
			st.write("View video [link](https://www.youtube.com/watch?v=WifxfTgQKcY)")
		with col4:
			PDF_file = current_dir / 'DOCS' / 'PyDigitizer.pdf'
			FCT_Down( PDF_file, "Download article" )

	st.write("---")
	st.subheader(":gray[2. PyChart]") 
	col1, col2 = st.columns(2,gap="small")
	with col1:
		st.write(" - A Python module for analysis and visual view of 2D/3D Charts")
		st.write(":ice_cube: [Acces files](https://data.mendeley.com/datasets/35jrmwd4fw/1)")
		st.write(" - Contributors: Dorian Nedelcu & Tihomir Latinovic")
		st.write(" - DOI:10.17632/35jrmwd4fw.1") 
		st.write(" - Licence: LGPL:  The GNU Lesser General Public License allows others to use and integrate software into their own software without being required to release the source code of their own components.") 
	with col2:
		image_Simulation = current_dir / "Images" / "PyChart1.jpg"
		st.image(Image.open(image_Simulation), width=300)
		image_Simulation = current_dir / "Images" / "PyChart2.jpg"
		st.image(Image.open(image_Simulation), width=300)
		
		col3, col4 = st.columns(2,gap="small")
		with col3:
			st.write("View [link](https://data.mendeley.com/datasets/35jrmwd4fw/1/files/72619d3c-1740-4e95-97bd-e994210d727c)")
		with col4:
			PDF_file = current_dir / 'DOCS' / 'PyChart.pdf'
			FCT_Down( PDF_file, "Download article" )
		
	st.write( """
		The PyChart module (aimed at analysis and visual view of 2D/3D Charts) was created 
		with the help of free and Open Source resources, using Python as a programming language 
		and wx.Python as a graphical user interface toolkit. The chart data is imported from 
		a Excel/ CSV file with a template structure and is drawn in the PyChart module as XY 
		or XYZ curves similar with Excel scatter with smooth lines and markers style. 
		The module is provided with zooming instruments (fit, pan, zoom in, zoom out), 
		cubic spline curves interpolation, chart intersection with constant X, Y or Z values, 
		visual follow of the 2D chart points to view coordinates, export of data in 
		Windows Clipboard, Excel or Microsoft Word format and saving the chart as a image file. 
	"""	 )
	
	st.write("---")
	st.subheader(":gray[3. PyPlate]") 
	col1, col2 = st.columns(2,gap="small")
	with col1:
		st.write(" - The PyPLATE software draws the mode shapes of a rectangular plate for various vibration modes.")
		st.write(":ice_cube: [Acces files](https://data.mendeley.com/datasets/4d78cwxkg2/1)")
		st.write(" - Contributors: Dorian Nedelcu & Gilbert-Rainer Gillich")
		st.write(" - DOI:10.17632/4d78cwxkg2.1") 
		st.write( """
			- Licence: CC BY 4.0:  You can share, copy and modify this dataset 
			so long as you give appropriate credit, provide a link to the CC BY 
			license, and indicate if changes were made, but you may not do so 
			in a way that suggests the rights holder has endorsed you or your 
			use of the dataset. Note that further permission may be required 
			for any content within the dataset that is identified as belonging 
			to a third party.")  
		"""	 )
	with col2:
		image_Simulation = current_dir / "Images" / "PyPlate1.jpg"
		st.image(Image.open(image_Simulation), width=300)
		image_Simulation = current_dir / "Images" / "PyPlate2.jpg"
		st.image(Image.open(image_Simulation), width=300)
	
	st.write("---")
	st.subheader(":gray[4. PyLoc]") 
	image_Simulation = current_dir / "Images" / "PyLoc.jpg"
	st.image(Image.open(image_Simulation), width=700)
	st.write(" - A Python application to localize cracks in beams with uncertain boundary conditions.)")
	st.write(" :ice_cube: [Acces files](https://data.mendeley.com/datasets/gzw84k3x4s/1)")
	st.write(" - Contributors: Dorian Nedelcu & Gilbert-Rainer Gillich")
	st.write(" - DOI:10.17632/gzw84k3x4s.1") 
	st.write( """
		- Licence: CC BY 4.0:  You can share, copy and modify this dataset 
		so long as you give appropriate credit, provide a link to the CC BY 
		license, and indicate if changes were made, but you may not do so 
		in a way that suggests the rights holder has endorsed you or your 
		use of the dataset. Note that further permission may be required 
		for any content within the dataset that is identified as belonging 
		to a third party.")  
	"""	 )
	
	st.write("---")
	st.subheader(":gray[5. PyFest]") 
	image_Simulation = current_dir / "Images" / "PyFest.jpg"
	st.image(Image.open(image_Simulation), width=700)
	col3, col4 = st.columns([0.7,0.3])
	with col3:
		st.write(" - A Python application for accurate frequency estimation.")
		st.write(" :ice_cube: [Acces files](https://data.mendeley.com/datasets/zxfxd59554/3)")
	with col4:
		PDF_file = current_dir / 'DOCS' / 'PyFest.pdf'
		FCT_Down( PDF_file, "Download article" )

	st.write(" - Contributors: Gilbert-Rainer Gillich & Dorian Nedelcu")
	st.write(" - DOI:10.17632/zxfxd59554.3") 
	st.write( """
		- The app can be used to estimate the frequencies of short-time signals with high accuracy. 
		Along with the application, examples with generated signal (single-ton, multi-tone, noisy, damped etc.) 
		and measured signals are delivered for testing purposes. The frequencies of the harmonic components 
		are evaluated one-by-one with high accuracy. Because the actions performed do not imply 
		previous expertise, the results are not influenced by human intervention.

	"""	 )
	st.write( """
		- Licence: CC BY 4.0:  You can share, copy and modify this dataset 
		so long as you give appropriate credit, provide a link to the CC BY 
		license, and indicate if changes were made, but you may not do so 
		in a way that suggests the rights holder has endorsed you or your 
		use of the dataset. Note that further permission may be required 
		for any content within the dataset that is identified as belonging 
		to a third party.")  
	"""	 )

	st.write("---")
	st.subheader(":gray[6. VOICE COMMANDS OF A 2D GRAPH]") 
	image_Simulation = current_dir / "Images" / "Sisom.jpg"
	st.image(Image.open(image_Simulation), width=700)
	col3, col4 = st.columns([0.7,0.3])
	with col3:
		st.write(" - Contributors: Dorian Nedelcu")
	with col4:
		PDF_file = current_dir / 'DOCS' / 'Art_Sisom.pdf'
		FCT_Down( PDF_file, "Download article" )
	st.write( """
		- The paper focuses on the voice commands of a 2D graph, using 
		Microsoft Speech SDK as a speech recognition tool and Python as a
		programming language. The main functions of the graph are activated 
		through voice commands, but also in Windows style: menus and toolbar.
	"""	 )

	# ====================================================================
	st.write("---")
	st.subheader(":large_orange_square: :red[Visual Basic]") 
	col3, col4 = st.columns([0.7,0.3])
	with col3:
		st.write(" - Software for Computing of the Hydraulic Turbines Characteristics")
	with col4:
		PDF_file1 = current_dir / 'DOCS' / 'Art_Software MH_2004.pdf'
		FCT_Down( PDF_file1, "Download article" )
		PDF_file2 = current_dir / 'DOCS' / 'Art_HMH_2004.pdf'
		FCT_Down( PDF_file2, "Download article" )
		PDF_file3 = current_dir / 'DOCS' / 'Art_IAHR_2007..pdf'
		FCT_Down( PDF_file3, "Download article" )
	col5, col6 = st.columns([0.7,0.3])
	with col5:
		st.write(" - Software for the for the mechanical device design")
	with col6:
		PDF_file1 = current_dir / 'DOCS' / 'Art_Dispozitive_2004.pdf'
		FCT_Down( PDF_file1, "Download article" )

	# ====================================================================
	st.write("---")
	col1, col2 = st.columns(2,gap="small")
	with col1:
		st.subheader(":large_orange_square: :red[Basic4Android (B4A)]") 
		st.write(" -  :green[Unfold Sheets Parts]")
		st.write(""" -  This application is accessible on Android smartphones 
				and has been developed in B4A to unfold the sheet metal parts. """)
		st.info(":aqua[This application does not share data over the internet, the code  runs entirely on the user's smartphone, does not contain any viruses and not store data to any external server.]", icon="🔥")
		st.write( "Step to install on smartphone:")
		st.write( """
				- Download the ':green[Unfold Sheets Parts.apk]' file on PC or Laptop;
				- Copy the file on smartphone;
				- On smartphone tap the apk file name;
				- Select 'Package Installer' option to install.
				""")
		FCT_Down( current_dir / 'DOCS' / 'Unfold_Sheet_Parts.apk', ":green[Unfold Sheets Parts.apk] :red[ Download]" )
		FCT_Down( current_dir / 'DOCS' / 'UnfoldSheetsParts-Project.zip', ":green[UnfoldSheetsParts-Project.zip] :red[ Download]" )
	with col2:
		profile_picture = Image.open(current_dir / "Images" / "Unfold_Sheets_Parts.jpg")
		st.image(profile_picture, width=350)
		

	# ====================================================================
	st.write("---")
	col1, col2 = st.columns(2,gap="small")
	with col1:
		st.subheader(":large_orange_square: :red[Streamlit]") 
		st.write(" - :green[Unfold Sheets Part]")	
		
		st.write("This application has been developed in Streamlit & Python & Matplotlib to unfold the sheet metal parts. It is the same application developed in Basic4Android.")
		st.info(":aqua[The application is accesible through Internet, does not contain any viruses and not store data to any external server.]", icon="🔥")			
		st.link_button(":red[ Go To Test Web page]", "https://unfoldsheetsparts.streamlit.app/")
	with col2:
		profile_picture = Image.open(current_dir / "Images" / "Unfold_Streamlit.jpg")
		st.image(profile_picture, width=350)
			
	# ====================================================================
	st.write("---")
	st.subheader(":large_orange_square: :red[Three.js]") 
	st.write(" - Computer Aidedd Design Applications (for student use).")
	
	st.write(" :ice_cube: [Go TO Web Page](http://vechi.uem.ro/fileadmin/3_ACADEMICA/1_FACULTATI/1_FIM/cadre/NedelcuD/Aplicatii/_index.html)")
	st.info(":aqua[Use only Firefox or Chrome browsers to display 3D models correctly !]", icon="🔥")




