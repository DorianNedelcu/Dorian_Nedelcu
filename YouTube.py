#! /usr/bin/env python
#coding=utf-8
from pathlib import Path
import streamlit as st
from PIL import Image

# ---  PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()


def FCT_Down( Fisier_PDF, LABEL ):
	with open(Fisier_PDF,"rb") as pdf_file:
		PDFbyte = pdf_file.read()
	st.download_button(
		label=LABEL, data=PDFbyte, 
		file_name=Fisier_PDF.name, 
		mime="application/octet-stream",   	)
	return

def AUTOCAD( TITLU, LINK, PUBLISHED, DURATION, LANGUAGE, IMG_PATH, WIDTH ):
	st.write("---")
	col1, col2 = st.columns(2,gap="small")
	col1.subheader(TITLU)  	# ":gray[2.10 AutoCAD Tutorial 4.10 - Unfolding of a hexagonal prism]"
	
	col1.write(PUBLISHED)	# "Published Oct 4, 2015"
	col1.write(DURATION)	# "Duration 6:44 minutes"
	col1.write(LANGUAGE)	# "Language: Romanian"
	col2.image(Image.open(IMG_PATH), width=WIDTH) # current_dir / "Images" / "AutoCad_4_10.jpg"
	col2.write(LINK)  		# "View video [link](https://youtu.be/JP4X6El9sOA)"




def app():
	# --- GENERAL VARIABLES ---
#	PAGE_TITLE = "YouTube Videos"  ;  st.title(PAGE_TITLE)
	st.title(":green[YouTube Videos]")
	
	st.write("#")
	st.subheader(":red[1. Hydro Hill Chart Python Apps - 6 videos]")  
	# st.write("9 books published, of which 6 as unique author: ") 

	# ================================================================
	st.write("---")
	col1, col2 = st.columns(2,gap="small")
	with col1:
		st.subheader(":gray[1.1 HydroHillChart – Kaplan module]") 
		st.write( """
			The Hydro Hill Chart - Kaplan module Python application 
			is used to calculate the Hill Chart of the Kaplan 
			hydraulic turbine models, by processing the data 
			measured on the test rig.
		"""   		)
		st.write("Published Sep 29, 2015") 
		st.write("Duration 5:27 minutes") 
	with col2:
		image_Simulation = current_dir / "Images" / "YT_Kaplan.jpg"
		st.image(Image.open(image_Simulation), width=300)

		st.write("View video [link](https://www.youtube.com/watch?v=hl2BWxMLoqU)")
		PDF_file = current_dir / 'DOCS' / 'HHC-Kaplan module.pdf'
		FCT_Down( PDF_file, "Download article" )
		

	# ================================================================
	st.write("---")
	col1, col2 = st.columns(2,gap="small")
	with col1:
		st.subheader(":gray[1.2. HydroHillChart – Francis module - ao scenario]") 
		st.write( """
			For a Francis turbine model, measurements can be performed 
			by using the following parameters ao=const., wicked gate 
			opening, or n11=const., unitary speed. Therefore, when 
			reading the input data, the Francis module should be 
			notified by the user about the measuring scenarios that 
			were used (ao = const. or n11 = const), by specifying 
			the option when a new database is created. Although the 
			input data fields are identical, for all measurement 
			scenarios, graphic representations and calculation 
			algorithms differ for the two scenarios.
		"""   		)
		st.write("Published Sep 29, 2015") 
		st.write("Duration 4:38 minutes") 
	with col2:
		image_Simulation = current_dir / "Images" / "YT_Francis_ao.jpg"
		st.image(Image.open(image_Simulation), width=300)
	
		st.write("View video [link](https://www.youtube.com/watch?v=-7810z2RSyM)")
		
		PDF_file1 = current_dir / 'DOCS' / 'HHC-Francis module.pdf'
		FCT_Down( PDF_file1, "Download article 1") 
		PDF_file2 = current_dir / 'DOCS' / 'HHC-Pelton and Francis module.pdf'
		FCT_Down( PDF_file2, "Download article 2") 
		
		
	# ================================================================
	st.write("---")
	col1, col2 = st.columns(2,gap="small")
	with col1:
		st.subheader(":gray[1.3. HydroHillChart – Francis module - n11 scenario]") 
		st.write( """
			For a Francis turbine model, measurements can be performed 
			by using the following parameters ao=const., wicked gate opening, 
			or n11=const., unitary speed. Therefore, when reading the input 
			data, the Francis module should be notified by the user about 
			the measuring scenarios that were used (ao = const. or n11 = const), 
			by specifying the option when a new database is created. 
			Although the input data fields are identical, for all measurement 
			scenarios, graphic representations and calculation algorithms 
			differ for the two scenarios.
		"""   		)
		st.write("Published Sep 29, 2015") 
		st.write("Duration 3:28 minutes") 
	with col2:
		image_Simulation = current_dir / "Images" / "YT_Francis_n11.jpg"
		st.image(Image.open(image_Simulation), width=300)
	
		st.write("View video [link](https://youtu.be/1XS1JW7nGDQ)")
		PDF_file1 = current_dir / 'DOCS' / 'HHC-Francis Calculation.pdf'
		FCT_Down( PDF_file1, "Download article 1") 
		

	# ================================================================
	st.write("---")
	col1, col2 = st.columns(2,gap="small")
	with col1:
		st.subheader(":gray[1.4. Hydro Hill Chart - Francis module - Library option]") 
		st.write( """
			The Hydro Hill Chart - Francis module is used to calculate the 
			Hill Chart of Francis hydraulic turbine models, by processing 
			the data that was measured on the test rig. This video shows 
			the Library option, a database for multiple runners hill charts.
		"""   		)
		st.write("Published Apr 20, 2016") 
		st.write("Duration 9:44 minutes") 
	with col2:
		image_Simulation = current_dir / "Images" / "YT_Francis_Library.jpg"
		st.image(Image.open(image_Simulation), width=300)
	
		st.write("View video [link](https://youtu.be/Z3-JlsskxTE)")
	
	# ================================================================
	st.write("---")
	col1, col2 = st.columns(2,gap="small")
	with col1:
		st.subheader(":gray[1.5. HydroHillChart – Pelton module]") 
		st.write( """
			For Pelton turbines, the energetic characteristic 
			expresses the dependence from the following sizes: 
			unitary speed n11, unitary flow Q11, efficiency, 
			injector needle opening S. The methods used for 
			determining these features, based on experimental 
			data acquired for different models of hydraulic 
			turbines, are laborious and sometimes subjective. 
			The creation of a specialized application has the 
			purpose of objectifying the process used to determine 
			these features. The software, called HydroHillChart, 
			was created using the Python programming language 
			and associated libraries.
		"""   		)
		st.write("Published Sep 29, 2015") 
		st.write("Duration 4:29 minutes") 
	with col2:
		image_Simulation = current_dir / "Images" / "YT_Pelton.jpg"
		st.image(Image.open(image_Simulation), width=300)
	
		st.write("View video [link](https://youtu.be/bXtsjMqbENI)")
		
		PDF_file1 = current_dir / 'DOCS' / 'HHC-Pelton module.pdf'
		FCT_Down( PDF_file1, "Download article 1") 
		
		PDF_file2 = current_dir / 'DOCS' / 'HHC-Pelton Calculation.pdf'
		FCT_Down( PDF_file2, "Download article 2" )
		
		
	# ================================================================
	st.write("---")
	col1, col2 = st.columns(2,gap="small")
	with col1:
		st.subheader(":gray[1.6. HydroHillChart – DEX module]") 
		st.write( """
			The Hydro Hill Chart - DEX module application is used to calculate 
			the  operation diagram for the industrial turbine prototype.
		"""   		)
		st.write("Published Sep 29, 2015") 
		st.write("Duration 1:55 minutes") 
	with col2:
		image_Simulation = current_dir / "Images" / "YT_DEX.jpg"
		st.image(Image.open(image_Simulation), width=300)
	
		st.write("View video [link](https://youtu.be/knw5E6-eIpc)")
		PDF_file = current_dir / 'DOCS' / 'HHC-DEX module.pdf'
		FCT_Down( PDF_file, "Download article" )
		
		
	# ================================================================
	st.write("#")
	st.subheader(":red[2. AutoCAD Tutorials]")
  
	st.write("---")
	st.subheader(":gray[19 x AutoCAD Tutorials based on the following book:]")
	col1, col2= st.columns([0.7,0.3])
	with col1:
		st.write( """
			- Authors: Dorian NEDELCU & Vasile COJOCARU
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

	AUTOCAD( ":gray[2.1 AutoCAD Tutorial 4.1 - Unfolding a cylinder ]" , 
		"View video [link](https://www.youtube.com/watch?v=a-raTwA7aMw)" , "Published Oct 4, 2015" , 
		"Duration 9:28 minutes" , "Language: Romanian" , 
		current_dir / "Images" / "AutoCad_4_1.jpg" , 300  )	
	
	AUTOCAD( ":gray[2.2 AutoCAD Tutorial 4.2 - Unfolding of a trunk of con ] " , 
		"View video [link](https://www.youtube.com/watch?v=sAvHP1eZw_I)" , "Published Oct 4, 2015" , 
		"Duration 8:07 minutes" , "Language: Romanian" , 
		current_dir / "Images" / "AutoCad_4_2.jpg" , 300  )	
	
	AUTOCAD( ":gray[2.3 AutoCAD Tutorial 4.3 - Unfolding of a cylinder intersected by two planes - Version 1]" , 
		"View video [link](https://youtu.be/oCQIdFMCc98)" , "Published Oct 4, 2015" , 
		"Duration 7:31 minutes" , "Language: Romanian" , 
		current_dir / "Images" / "AutoCad_4_3.jpg" , 300  )	

	AUTOCAD( ":gray[2.4 AutoCAD Tutorial 4.4 - Unfolding of a cylinder intersected by two planes  - Version 2]" , 
		"View video [link](https://youtu.be/eNBls-20Kf0)" , "Published Oct 4, 2015" , 
		"Duration 11:05 minutes" , "Language: Romanian" , 
		current_dir / "Images" / "AutoCad_4_4.jpg" , 300  )	

	AUTOCAD( ":gray[2.5 AutoCAD Tutorial 4.5 - Unfolding the intersection of 2 cylinders]" , 
		"View video [link](https://youtu.be/F9oYBv2UH2I)" , "Published Oct 4, 2015" , 
		"Duration 12:06 minutes" , "Language: Romanian" , 
		current_dir / "Images" / "AutoCad_4_5.jpg" , 300  )	
	
	AUTOCAD( ":gray[2.6 AutoCAD Tutorial 4.6 - Unfolding the intersection of 3 cylinders]" , 
		"View video [link](https://youtu.be/ZogKnjtbtxk)" , "Published Oct 4, 2015" , 
		"Duration 10:08 minutes" , "Language: Romanian" , 
		current_dir / "Images" / "AutoCad_4_6.jpg" , 300  )	
	
	AUTOCAD( ":gray[2.7 AutoCAD Tutorial 4.7 - Unfolding the elements of a cylindrical elbow]" , 
		"View video [link](https://youtu.be/7aqhzV_GdUU)" , "Published Oct 4, 2015" , 
		"Duration 13:13 minutes" , "Language: Romanian" , 
		current_dir / "Images" / "AutoCad_4_7.jpg" , 300  )

	AUTOCAD( ":gray[2.8 AutoCAD Tutorial 4.8 - 2D graph plotting with parametric curves]" , 
		"View video [link](https://youtu.be/Wa6aDyNeLv4)" , "Published Oct 4, 2015" , 
		"Duration 18:35 minutes" , "Language: Romanian" , 
		current_dir / "Images" / "AutoCad_4_8.jpg" , 300  )
	
	AUTOCAD( ":gray[2.9 AutoCAD Tutorial 4.9 - Generating a 3D flange]" , 
		"View video [link](https://youtu.be/gyZiasIDzqU)" , "Published Oct 4, 2015" , 
		"Duration 11:46 minutes" , "Language: Romanian" , 
		current_dir / "Images" / "AutoCad_4_9.jpg" , 300  )
	
	AUTOCAD( ":gray[2.10 AutoCAD Tutorial 4.10 - Unfolding of a hexagonal prism]" , 
		"View video [link](https://youtu.be/JP4X6El9sOA)" , "Published Oct 4, 2015" , 
		"Duration 6:44 minutes" , "Language: Romanian" , 
		current_dir / "Images" / "AutoCad_4_10.jpg" , 300  )
	
	AUTOCAD( ":gray[2.11 AutoCAD Tutorial 3.1 - Generate 3D geometry]" , 
		"View video [link](https://youtu.be/kDYUoro8oq0)" , "Published Oct 4, 2015" , 
		"Duration 16:59 minutes" , "Language: Romanian" , 
		current_dir / "Images" / "AutoCad_4_11.jpg" , 300  )
	
	AUTOCAD( ":gray[2.12 AutoCAD Tutorial 3.2 - Generate 3D geometry]" , 
		"View video [link](https://youtu.be/Kr76P4CBN5Y)" , "Published Oct 4, 2015" , 
		"Duration 17:30 minutes" , "Language: Romanian" , 
		current_dir / "Images" / "AutoCad_4_12.jpg" , 300  )
	
	AUTOCAD( ":gray[2.13 AutoCAD Tutorial 3.3 - Generate 3D geometry]" , 
		"View video [link](https://youtu.be/pA1Lz9ohdh8)" , "Published Oct 4, 2015" , 
		"Duration 22:22 minutes", "Language: Romanian" , 
		current_dir / "Images" / "AutoCad_4_13.jpg", 300  )

	AUTOCAD( ":gray[2.14 AutoCAD Tutorial 3.4 - Generate 3D geometry]" , 
		"View video [link](https://youtu.be/JD3t8zT0m-4)" , "Published Oct 4, 2015" , 
		"Duration 15:52 minutes", "Language: Romanian" , 
		current_dir / "Images" / "AutoCad_4_14.jpg", 300  )
	
	AUTOCAD( ":gray[2.15 AutoCAD Tutorial 3.5 - Generate 3D geometry]" , 
		"View video [link](https://youtu.be/ocyM5HHBceY)" , "Published Oct 4, 2015" , 
		"Duration 18:00 minutes", "Language: Romanian" , 
		current_dir / "Images" / "AutoCad_4_15.jpg", 300  )

	AUTOCAD( ":gray[2.16 AutoCAD Tutorial 3.6 - Generate 3D geometry]" , 
		"View video [link](https://youtu.be/Jv2FW_sRldE)" , "Published Oct 4, 2015" , 
		"Duration 19:30 minutes", "Language: Romanian" , 
		current_dir / "Images" / "AutoCad_4_16.jpg", 300  )
	
	AUTOCAD( ":gray[2.17 AutoCAD Tutorial 3.7 - Generate 3D geometry]" , 
		"View video [link](https://youtu.be/TMFhFXXMS7I)" , "Published Oct 4, 2015" , 
		"Duration 13:07 minutes", "Language: Romanian" , 
		current_dir / "Images" / "AutoCad_4_17.jpg", 300  )
	
	AUTOCAD( ":gray[2.18 AutoCAD Tutorial 3.8 - Generate 3D geometry]" , 
		"View video [link](https://youtu.be/jn8UQv0n71U)" , "Published Oct 4, 2015" , 
		"Duration 12:51 minutes", "Language: Romanian" , 
		current_dir / "Images" / "AutoCad_4_18.jpg", 300  )
	
	AUTOCAD( ":gray[2.19 AutoCAD Tutorial 3.9 - Generate 3D geometry]" , 
		"View video [link](https://youtu.be/cHwVAarbt5E)" , "Published Oct 4, 2015" , 
		"Duration 13:08 minutes", "Language: Romanian" , 
		current_dir / "Images" / "AutoCad_4_19.jpg", 300  )
	