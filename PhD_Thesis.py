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

def app():
	# --- GENERAL VARIABLES ---
#	PAGE_TITLE = "PhD Thesis"  ;  st.title(PAGE_TITLE)
	st.title(":ice_cube:  :green[PhD Thesis Supervised]")

	# --- PhD Thesis ---
	st.write("#")
	st.subheader(":red[10 x [PhD theses supervised by Dorian Nedelcu](https://eng.ubbcluj.ro/?page_id=2945)]")


	# --- THESIS ---

	# ================================================================
	st.write("---")
	col1, col2 = st.columns(2,gap="small")
	with col1:
		st.write(":one: Contributions to the constructive-functional improvement of double harmonic gearboxes") 
		st.write( """
			- PhD student: Ianici (Rujici) Draghiţa 
			- Year of registration : 2009
			- Dissertation defended in 02.11.2012
			- The PhD title awarded according Ministerial Order no. 3250 MD/20.02.2013
		"""		)

	with col2:
		image_Rujici = current_dir / "Images" / "Thesis_Rujici.jpg"
		st.image(Image.open(image_Rujici), width=200)
#		
		Teza_Rujici_file = current_dir / 'DOCS' / 'Teza Rujici ID.pdf'
		FCT_Down( Teza_Rujici_file, "Thesis Download" )

	# ================================================================ XXXX
	st.write("---")
	col1, col2 = st.columns(2,gap="small")
	with col1:
		st.write(":two: Cavitational erosion research on materials used in the manufacture of hydraulic turbine components") 
		st.write( """
			- PhD student: Nedeloni Marian-Dumitru 
			- Year of registration : 2009
			- Dissertation defended in 18.12.2012
			- The PhD title awarded according Ministerial Order no. 3250 MD/20.02.2013
		"""		)
	with col2:
		image_Nedeloni = current_dir / "Images" / "Thesis_Nedeloni.jpg"
		st.image(Image.open(image_Nedeloni), width=200)
		
		Teza_Nedeloni_file = current_dir / 'DOCS' / 'Teza Nedeloni.pdf'
		FCT_Down( Teza_Nedeloni_file, "Thesis Download" )

	# ================================================================
	st.write("---")
	col1, col2 = st.columns(2,gap="small")
	with col1:
		st.write(":three: Theoretical and experimental contributions to the study and design of the spiral chamber, stator and wicked gate of hydraulic turbines") 
		st.write( """
			- PhD student: Daia Daniel  
			- Year of registration : 2009
			- Dissertation defended in 27.03.2013
			- The PhD title awarded according Ministerial Order no. 3930 MD/20.06.2013
		"""		)
	with col2:
		image_Daia = current_dir / "Images" / "Thesis_Daia.jpg"
		st.image(Image.open(image_Daia), width=200)
		
		Teza_Daia_file = current_dir / 'DOCS' / 'Teza DAIA.pdf'
		FCT_Down( Teza_Daia_file, "Thesis Download" )
	# ================================================================
	st.write("---")
	col1, col2 = st.columns(2,gap="small")
	with col1:
		st.write(":four: Theoretical and experimental investigations on an axial-tubular microturbine equipped with an immersed generator with permanent magnets") 
		st.write( """
			- PhD student: Florea Dănuţ 
			- Year of registration : 2010
			- Dissertation defended in 29.11.2013
			- The PhD title awarded according Ministerial Order no. 20/21.01.2014
		"""		)
	with col2:
		image_Florea = current_dir / "Images" / "Thesis_Florea.jpg"
		st.image(Image.open(image_Florea), width=200)

		Teza_Florea_file = current_dir / 'DOCS' / 'Teza Florea Danut.pdf'
		FCT_Down( Teza_Florea_file, "Thesis Download" )
	# ================================================================
	st.write("---")
	col1, col2 = st.columns(2,gap="small")
	with col1:
		st.write(":five: Theoretical and experimental contributions on high and low head flow microturbines") 
		st.write( """
			- PhD student: Avasiloaie Raoul-Cristian 
			- Year of registration : 2010
			- Dissertation defended in 29.11.2013
			- The PhD title awarded according Ministerial Order no. 20/21.01.2014
		"""		)
	with col2:
		image_Avasiloae = current_dir / "Images" / "Thesis_Avasiloae.jpg"
		st.image(Image.open(image_Avasiloae), width=200)

		Teza_Avasiloaie_file = current_dir / 'DOCS' / 'Teza Avasiloaie Raoul.pdf'
		FCT_Down( Teza_Avasiloaie_file, "Thesis Download" )
	# ================================================================ XXXX
	st.write("---")
	col1, col2 = st.columns(2,gap="small")
	with col1:
		st.write(":six: Research on the construction and operation of harmonic transmissions having wave generator with shape memory alloy elements") 
		st.write( """
			- PhD student: Bizău Viorel Ionuţ 
			- Year of registration : 2011
			- Dissertation defended in 30.09.2014
			- The PhD title awarded according Ministerial Order no. 694/10.12.2014
		"""		)
	with col2:
		image_Bizau = current_dir / "Images" / "Thesis_Bizau.jpg"
		st.image(Image.open(image_Bizau), width=200)

		Teza_Bizau_file = current_dir / 'DOCS' / 'Teza Bizau.pdf'
		FCT_Down( Teza_Bizau_file, "Thesis Download" )
		
	# ================================================================ XXXX
	st.write("---")
	col1, col2 = st.columns(2,gap="small")
	with col1:
		st.write(":seven: Research on the optimization of the biplane disc shape of butterfly valves considering hydraulic losses") 
		st.write( """
			- PhD student: Periş Bendu Florin 
			- Year of registration : 2012
			- Dissertation defended in 24.09.2015
			- The PhD title awarded according Ministerial Order no. 5954/07.12.2015
		"""		)
	with col2:
		image_Peris = current_dir / "Images" / "Thesis_Peris.jpg"
		st.image(Image.open(image_Peris), width=200)
		
		Teza_Peris_file = current_dir / 'DOCS' / 'Teza Peris.pdf'
		FCT_Down( Teza_Peris_file, "Thesis Download" )
		
	# ================================================================ 
	st.write("---")
	col1, col2 = st.columns(2,gap="small")
	with col1:
		st.write(":eight: Contributions to the improvement of experimental measurement methods and results processing in the hydraulic turbine model test stand") 
		st.write( """
			- PhD student: Ghican Adelina 
			- Year of registration : 2012
			- Dissertation defended in 24.09.2015
			- The PhD title awarded according Ministerial Order no. 5954/07.12.2015
		"""		)
	with col2:
		image_Ghican = current_dir / "Images" / "Thesis_Ghican.jpg"
		st.image(Image.open(image_Ghican), width=200)

		Teza_Ghican_file = current_dir / 'DOCS' / 'Teza Ghican Adeline.pdf'
		FCT_Down( Teza_Ghican_file, "Thesis Download" )
	# ================================================================ XXXX
	st.write("---")
	col1, col2 = st.columns(2,gap="small")
	with col1:
		st.write(":nine: Research on the behaviour of preloaded gears of speed multipliers") 
		st.write( """
			- PhD student: Băra Aurel  
			- Year of registration : 2013
			- Dissertation defended in 13.07.2018
			- The PhD title awarded according Ministerial Order no. 5474/14.11.2018
		"""		)
	with col2:
		image_Bara = current_dir / "Images" / "Thesis_Bara.jpg"
		st.image(Image.open(image_Bara), width=200)

#		st.write("https://rei.gov.ro/teza-doctorat-document/804065e78bebc94466-Teza-Bara-Aurel.pdf")
		Teza_Bara_file = current_dir / 'DOCS' / 'Teza Bara.pdf'
		FCT_Down( Teza_Bara_file, "Thesis Download" )
	# ================================================================ XXXX
	st.write("---")
	col1, col2 = st.columns(2,gap="small")
	with col1:
		st.write(":one::zero: Application of reverse engineering to the reconstruction of the geometry of profiled components of hydraulic turbines") 
		st.write( """
			- PhD student: Bogdan Sorin-Laurenţiu   
			- Year of registration : 2015
			- Dissertation defended in 22.07.2019
			- The PhD title awarded according Ministerial Order no. 5308/20.11.2019
		"""		)
	with col2:
		image_Bogdan = current_dir / "Images" / "Thesis_Bogdan.jpg"
		st.image(Image.open(image_Bogdan), width=200)
		#	st.write("https://rei.gov.ro/teza-doctorat-document/8210085e78bef1797f2-tz_Teza-doctorat_Bogdan.pdf")

		Teza_Bogdan_file = current_dir / 'DOCS' / 'Teza Bogdan.pdf'
		FCT_Down( Teza_Bogdan_file, "Thesis Download" )
		
	st.write("---")

	# ================================================================