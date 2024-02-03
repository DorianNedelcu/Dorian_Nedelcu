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
#	PAGE_TITLE = "YouTube Videos"  ;  st.title(PAGE_TITLE)
	st.title(":anger: :green[Research Projects]")
	st.write("#")
	
	
	# --- RESEARCH PROJECTS     ---
	st.write("---")
	st.subheader(":red[ACADEMIC RESEARCH PROJECTS]")
	st.write( """
		:ice_cube:  Project manager: :green['Center for Numerical Simulation & Digital / Rapid Prototyping'] 
				within the program “Romania-Republic of Serbia IPA CBC Program, Priority Axis 3, 
				Measure 3.3, carried out for a period of 12 months :red[December 2010-December 2011] 
	"""    	)

	col1, col2, col3, col4, col5 = st.columns([0.25,0.25,0.25,0.25,0.25])
	with col1:
		FCT_Down( current_dir / 'DOCS' / 'BROSURA_CSNP.pdf', "Description" )
	with col2:
		FCT_Down( current_dir / 'DOCS' / 'PLIANT_CSNP.pdf', "Flyer" )
	with col3:
		FCT_Down( current_dir / 'DOCS' / 'Articol 1 T&T.pdf', "Article 1" )
	with col4:
		FCT_Down( current_dir / 'DOCS' / 'Articol 2 T&T.pdf', "Article 2" )
	with col5:
		st.write("Video [link](https://www.youtube.com/watch?v=Ykj9vP9k85A)")
	
	left_co,cent_co,last_co = st.columns([0.06,0.8,0.14])
	with cent_co:
		image_VS = current_dir / "Images" / "CSNP.jpg"
		st.image(Image.open(image_VS), width=600)
	
	st.write( """
		:ice_cube: Project manager: :green['Virtual knowledge space - The path to integration'] within the program 
				'Phare CBC 2006 / 018.448, budget line: B 22.0202, priority 2, People-to People Action, 
				Measure 2.1, Common Fund for Small Projects', carried out for a period of 9 months 
				starting with 23.09.:red[2008].
	"""  )

	left_co,cent_co,last_co = st.columns([0.06,0.8,0.14])
	with cent_co:
		image_VS = current_dir / "Images" / "VirtualSpace.jpg"
		st.image(Image.open(image_VS), width=600)

	st.write( """
		:ice_cube: Lecturer course: :red[2008] :green['Computer Aided Design'], within the Phare project: Establishment of a 
				enter for Vocational Guidance and Reconversion (CORP), contract Phare / 2005 / 
				017-553.04.02.01.01.509.
	"""    	)
	st.write( """
		:ice_cube:  Assistant project manager: :green['University Center for Professional Development'], PHARE 2000 - 
				'Economic and Social Cohesion - Human Resources Development in the context of industrial restructuring', 
				budget line RO-0007.02.01, :red[2003].
		"""    	)
	left_co,cent_co,last_co = st.columns([0.06,0.8,0.14])
	with cent_co:
		image_VS = current_dir / "Images" / "CUPP.jpg"
		st.image(Image.open(image_VS), width=600)
	
	


	st.write( """		
		:ice_cube:  Project team member: :green['Technology Transfer Center'], ANDR Program for Regional and Cohesion Policies 
				RO 807.01 Industrial Restructuring and Human Resources Development Second open tender, :red[2000-2001].
	"""    	)

	# ----------------------
	st.write("#")
	st.write("---")
	st.subheader(""":red[12 x Research project leader and collaborator between 1997-1983 at the Research and Development Directorate Design Institute ]""")
	
	st.markdown( """ 
		1.:blue[D. Nedelcu], Research project leader, :green[ Mathematical modelling of hydrodynamic phenomena with 
		application to computer-aided design of hydraulic turbines], Project A2, :red[1994 – 1997].
	"""   )
	st.markdown( """ 
		2.:blue[D. Nedelcu], Research project leader, :green[ Increasing electricity production and available 
		power at Pingarati CHE by increasing installed flow and upgrading existing hydropower plants], 
		Research project no. 95820-16-01- 230, :red[1995].
	"""   )
	st.markdown( """ 
		3.:blue[D. Nedelcu], Research project leader, :green[ Determination of the technical condition of 
		hydro-aggregates at the Pingarati CHE], Research project no. Ac 14.94.193, :red[1994].
	"""   )
	st.markdown( """ 
		4.:blue[D. Nedelcu], Research project collaborator, :green[ Research on experimental models for 
		the improvement and assimilation of "S" type pump turbines], Research project no. Ac. 94825-61-200, 
		:red[1996-1999].
	"""   )
	st.markdown( """ 
		5.:blue[D. Nedelcu], Research project collaborator, :green[ Research to improve design solutions 
		for Francis turbines], Research project no. Ac. 14.94.186, :red[1992-1995].
	"""   )
	st.markdown( """ 
		6.:blue[D. Nedelcu], Research project leader, :green[ Theoretical and experimental research on 
		turbines and diagonal turbine-pumps], Research project no. Ac 14.94.244, :red[1988-1990].
	"""   )
	st.markdown( """ 
		7.:blue[D. Nedelcu], Research project leader, :green[Research on experimental models for the 
		assimilation of turbines and turbine-pumps type Deriaz], Research project no. Ac 14.94.192, :red[1985-1987].
	"""   )
	st.markdown( """ 
		8.:blue[D. Nedelcu], Research project collaborator, :green[Hydro units equipped with Kaplan turbines. 
		Hydraulic models for 10-20 m head], Research project no. Ac. 14.94.138, :red[1985-1987].
	"""   )
	st.markdown( """ 
		9.:blue[D. Nedelcu], Research project leader, :green[Pelton microturbine for turbofan degassing-cooling], 
		Research project no. 2812/1985, :red[1985].
	"""   )
	st.markdown( """ 
		10.:blue[D. Nedelcu], Research project collaborator, :green[Aerodynamic research for the determination of 
		forces and moments necessary for the dimensioning of wicked gates], Research project no. Ac. 14.94.188, 
		:red[1983-1985].
	"""   )
	st.markdown( """ 
		11.:blue[D. Nedelcu], Research project leader, :green[Design/execution of Pelton turbine prototype - turbofan 
		10.000 m3/h for ships], Research project no. 2762/1984, :red[1984].
	"""   )
	st.markdown( """ 
		12.:blue[D. Nedelcu], Research project collaborator, :green[Hardware and software interfaces for an 
		automatic experimental data acquisition system of SAPETH hydraulic turbine models], Research project 
		no. 6292, :red[1983].
	"""   )
	

	# ----------------------
	st.write("#")
	st.write("---")
	st.subheader(":red[131 x Contractual research work at the Hydraulics Research Centre and Thermal Processes of the University 'Eftimie Murgu'Reșița and the Research and Development Directorate Design Institute]")


	st.markdown( """ 
		1. C.V. Câmpian, D. Frunzăverde,:blue[D. Nedelcu],V. Cojocaru,I. Bejan, :green[Endurance calculations and fatigue 
		estimates for spiral chamber, spherical valve and the pressure regulator of the CHE Raul Mare Retezat], Research 
		paper U-16-400-496-R, Contract Hydraulics Research Centre and Thermal Processes of the University "Eftimie Murgu" 
		Reșița, June, :red[2016].
	"""   )
	st.markdown( """ 
		2. :blue[D. Nedelcu],I. Hota,:green[Elaboration of the design for the execution of spatial shoes for the verification 
		of the HA3 PDF1 rotor blade geometry, in situ rotor blade scanning and data processing], Research paper 
		U-16-400-492-R, Contract Hydraulics Research Centre and Thermal Processes of the University "Eftimie Murgu" Reșița,
		Contract 30/22.02.2016, 16 pg. & 6 x A3 & 1 CD, March, :red[2016].
	"""   )
	st.markdown( """ 
		3. C.V. Câmpian,:blue[D. Nedelcu],I.O. Bejan, C. Dumbrava,V. Cojocaru :green[TENSOMETRIC TESTS, STRENGTH AND 
		FATIGUE CALCULATIONS CARRIED OUT ON THE SPIRAL CHAMBER IN CHE VIDRARU], Research paper U-15-400-472, 
		Contract Hydraulics Research Centre and Thermal Processes of the University "Eftimie Murgu" Reșița,
		Contract 152/13.07.2015, 20 pg., November, :red[2015].
	"""   )
	st.markdown( """ 
		4. C.V. Câmpian,:blue[D. Nedelcu],C. Dumbrava :green[Reconstruction of the runner blade geometry of the upgraded 
		turbine at Portile de Fier I CHE], Research paper U-15-400-383-a, Contract Hydraulics Research Centre and Thermal 
		Processes of the University "Eftimie Murgu" Reșița,57 pg. & 9 x A3 & 1 CD, July, :red[2015].
	"""   )
	st.markdown( """ 
		5. C.V. Câmpian,:blue[D. Nedelcu],C. Dumbrava :green[Francis rotor geometry reconstruction and execution 
		drawing for HA CHE Cumpâna - Curtea de Argeș 5 MW], Research paper U-15-400-382, Contract 
		Hydraulics Research Centre and Thermal Processes of the University "Eftimie Murgu" Reșița, Contract 
		UCMR Reşiţa 705/DC0030/20.04.2015, 16 pg. & 6 x A3 & 1 CD, June, :red[2015].
	"""   )
	st.markdown( """ 
		6. C.V. Câmpian,D. Frunzăverde, :blue[D. Nedelcu],:green[Grandfors HPEE Refurbishment Unit 2. Technical Offer 
		Hydraulic Turbine. Energetic and Cavitations' Characteristics], Research paper U-14-400-374, Contract 
		Hydraulics Research Centre and Thermal Processes of the University "Eftimie Murgu" Reșița, Contract 
		7182/15.10.2014, November, :red[2014].
	"""   )
	st.markdown( """ 
		7. C.O. Micloşină, C.V. Câmpian,D. Frunzăverde, :blue[D. Nedelcu], A.Cuzmoş :green[STUDY BY FINITE ELEMENT 
		CALCULATIONS OF THE STRESSES OCCURRING IN THE ADJUSTMENT MECHANISM OF THE BLADES OF THE UPGRADED TURBINE 
		IN THE IRON GATES I], Research paper U-12-400-349, Contract Hydraulics Research Centre and Thermal 
		Processes of the University "Eftimie Murgu" Reșița, Contract 22/20.03.2012, April, :red[2012].
	"""   )
	st.markdown( """ 
		8. C.V. Câmpian,D. Balint, :blue[D. Nedelcu],C. Miclosina :green[THE STUDY OF THE FLOW THROUGH THE UPGRADED 
		AND NON-UPGRADED TURBINES OF THE IRON GATES THROUGH NUMERICAL SIMULATIONS TO DETERMINE THE HYDRAULIC FORCES 
		AND APPLICATION POINTS FOR VARIOUS OPERATING REGIMES], Research paper U-12-400-348, Contract Hydraulics 
		Research Centre and Thermal Processes of the University "Eftimie Murgu" Reșița, Contract 21/20.03.2012, 
		April, :red[2012].
	"""   )
	st.markdown( """ 
		9. C.V. Câmpian,:blue[D. Nedelcu],:green[ANALYSIS OF DATA FROM MODEL TESTS ON EXISTING, UPGRADED ROMANIAN AND SERBIAN 
		TURBINES IN THE IRON GATES I SYSTEM POWER PLANTS IN ORDER TO GENERATE THE NECESSARY OPERATING CHARACTERISTICS AND 
		TABLES FOR CURRENT OPERATION PHASE: CALCULATION OF THE DIFFERENCES BETWEEN THE VALUES CALCULATED BY CCHAPT 
		(REPORT NO. U-11-400-332) AND THOSE GIVEN BY THE SERBIAN PARTNER. COMPARISON OF THE IDLING CURVES], Research paper 
		U-12-400-347, Contract Hydraulics Research Centre and Thermal Processes of the University "Eftimie Murgu" Reșița, 
		Contract 23 din 20.03.2012, March, :red[2012].
	"""   )
	st.markdown( """ 
		10. C.V. Câmpian,:blue[D. Nedelcu],:green[SUMMARY OF STRENGTH AND FATIGUE CALCULATIONS ON THE CRANK HANDLE AND 
		BUSHINGS OF THE TURBINE RUNNER BLADE ADJUSTMENT MECHANISM AT THE IRON GATES I], Research paper U-11-400-341, 
		Contract Hydraulics Research Centre and Thermal Processes of the University "Eftimie Murgu" Reșița, Contract 
		3/08.12.1997-CCHAPT/UEMR; 9893/22.12.1997/SH PdF ad. 15/2011, December, :red[2011].
	"""   )
	st.markdown( """ 
		11. C.V. Câmpian,D. Frunzăverde, Gh. Liuba, :blue[D. Nedelcu],C.O. Hamat, C. Dumbravă, A. Cuzmoş, C. Copocean
		:green[DETERMINATION OF THE OPERATING PARAMETERS AND TECHNICAL CONDITION OF THE HYDRO-AGGREGATE HA2 - CHE 
		ZAVIDENI, BEFORE AND AFTER THE CAPITAL REPAIR WORKS, BY INDEX TESTS], Research paper U-11-400-338, Contract 
		Hydraulics Research Centre and Thermal Processes of the University "Eftimie Murgu" Reșița, Contract 
		. 40-113.03 / 2009 ad. 2/2011, 74 pg., December, :red[2011].
	"""   )
	st.markdown( """ 
		12. C.V. Câmpian,:blue[D. Nedelcu],:green[ANALYSIS OF THE FINAL LABORATORY REPORT NEUTRAL LMH-EPFL OF OCTOBER 
		2010 / APRIL 2011, PROCESSING CHARACTERISTICS OF AND GENERATION OF P-Q-ETA TABLES FOR HYDRO-AGGREGATES 
		FROM PDF I SYSTEM], Research paper U-11-400-332, Contract Hydraulics Research Centre and Thermal Processes 
		of the University "Eftimie Murgu" Reșița, Contract 3/08.12.1997-CCHAPT/UEMR; 9893/22.12.1997/SH PdF 
		ad. 15/2011, 15 pg., October, :red[2011].
	"""   )
	st.markdown( """ 
		13. :blue[D. Nedelcu],:green[STRENGTH CALCULATIONS FOR BANKI TURBINE 1.2 MW], Research paper U-10-400-316, 
		Contract  Hydraul 32/2009 ad. 2/2010, 69 pg., December, :red[2010].
	"""   )
	st.markdown( """ 
		14. :blue[D. Nedelcu],:green[RESISTANCE CALCULATIONS FOR THE ADJUSTING RING OF THE WICKED GATES], Research paper 
		U-10-400-301, Contract  Hydraulics Research Centre and Thermal Processes of the University "Eftimie Murgu" 
		Reșița, Contract 32/2009 ad. 8/11.2010, 10 pg., April, :red[2010].
	"""   )
	st.markdown( """ 
		15. :blue[D. Nedelcu],:green[STRENGTH CALCULATIONS AND OPTIMIZATION OF THE STRUCTURE OF THE RASTOLITA SPIRAL CHAMBER], 
		Research paper U-10-400-300, Contract  Hydraulics Research Centre and Thermal Processes of the University "Eftimie 
		Murgu" Reșița, Contract 32/2009 ad. 8/11.2010, 10 pg., April, :red[2010].
	"""   )
	st.markdown( """ 
		16. :blue[D. Nedelcu],:green[RESISTANCE CALCULATIONS KILAVUZLU SPIRAL CHAMBER 4 X 15.9 MVA ], Research paper 
		U-10-400-299, Contract  Hydraulics Research Centre and Thermal Processes of the University "Eftimie Murgu" Reșița, 
		Contract 32/2009 ad. 8/11.2010, 21 pg., April, :red[2010].
	"""   )
	st.markdown( """ 
		17. C.V. Câmpian, D. Frunzăverde, :blue[D. Nedelcu],C. Dumbravă,:green[CALCULATION OF THE COMPOUND MECHANICAL STRESSES 
		OCCURRING ON THE EXISTING TURBINE ROTOR CRANK FROM THE IRON GATES I], Research paper U-10-400-293, Contract 
		Hydraulics Research Centre and Thermal Processes of the University "Eftimie Murgu" Reșița, Contract
		3/08.12.1997-CCHAPT/UEMR; 9893/22.12.1997/SH PdF Ad. 14/2010, 15 pg., March, :red[2010].
	"""   )
	st.markdown( """ 
		18. C.V. Câmpian, D. Frunzăverde, :blue[D. Nedelcu],A.M. Pittner,V. Cojocaru,  A.Cuzmoş, L. Gruionu :green[LIFE CALCULATIONS FOR 
		THE TURBINE RUNNER BLADE CRANK AT THE IRON GATES I], Research paper U-09-400-289, Contract Hydraulics Research 
		Centre and Thermal Processes of the University "Eftimie Murgu" Reșița, 164 pg. & 1 CD, November, :red[2009].
	"""   )
	st.markdown( """ 
		19. C.V. Câmpian, :blue[D. Nedelcu],M. Popovici :green[POINT OF VIEW ON 'Proposal to modify the crank handle 
		of turbine No 5 of the Iron Gates I CHP'], Research paper U-09-400-279, Contract Hydraulics Research Centre 
		and Thermal Processes of the University "Eftimie Murgu" Reșița, Contract 3/08.12.1997-CCHAPT/UEMR; 
		9893/22.12.1997/SH PdF Ad. 13/2008, 6 pg., June, :red[2009].
	"""   )
	st.markdown( """ 
		20. C.V. Câmpian, :blue[D. Nedelcu],V. Cojocaru, :green[IMPROVEMENT OF THE REPAIR TECHNOLOGY FOR THE ANTI-CAVITATION 
		RIBS OF TURBINE ROTOR BLADES IN CHE IRON GATES I Phase III CORRELATION BETWEEN TURBINE OPERATING REGIME AND 
		CAVITATIONAL EROSION INTENSITY], Research paper U-09-400-265, Contract Hydraulics Research Centre and Thermal 
		Processes of the University "Eftimie Murgu" Reșița, Contract 122/12.12.2008, 13 pg. & 4 x DVD , February, 
		:red[2009].
	"""   )
	
	st.markdown( """ 
		21. C.V. Câmpian, :blue[D. Nedelcu],M. Popoviciu, M. Bărglăzan, I. Bordeiaşu, C. Isbăşoiu  :green[Solution analysis 
		presented in ANDRITZ HYDRO TECHNICAL REPORT Z/08-152 REV 2 'TECHNICAL SOLUTIONS TO SOLVE THE PROBLEMS OF 
		CAVITATIONAL EROTATION AND CRACKS IN THE ANTICAVITATIONAL EDGE OF THE RUNNER BLADES OF THE TURBINE OF CHE PdF I'], 
		Research paper U-09-400-264, Contract Hydraulics Research Centre and Thermal Processes of the 
		University "Eftimie Murgu" Reșița, Contract 3/08.XII.1997-CCHAPT/UEMR; 9893/22.XII.1997/SH PdF ADIŢIONAL 
		NR. 13/2009, 19 pg., March, :red[2009].
	"""   )
	st.markdown( """ 
		22. C.V. Câmpian, :blue[D. Nedelcu],A.M. PITTNER,C. ISBĂŞOIU, E. ALĂMOREANU  :green[CALCULATION OF THE COMPOUND 
		MECHANICAL STRESSES OCCURRING ON THE TURBINE RUNNER CRANK FROM THE IRON GATES I. LINEAR STATIC ANALYSIS], 
		Research paper U-08-400-262, Contract Hydraulics Research Centre and Thermal Processes of the 
		University "Eftimie Murgu" Reșița, Contract 3/08.12.1997-CCHAPT/UEMR; 9893/22.12.1997/SH PdF Ad. 12/2008
		, 74 pg., December, :red[2008].
	"""   )
	st.markdown( """ 
		23. C.V. Câmpian, :blue[D. Nedelcu], :green[PROCESSING OPERATING CHARACTERISTICS OF HYDRO-AGGREGATES FROM THE
		Iron Gates I], Research paper U-08-400-258, Contract Hydraulics Research Centre and Thermal Processes of the 
		University "Eftimie Murgu" Reșița, Contract RU 273/17.12.2007, AD. 2/2007, 328 pg., December, :red[2008].
	"""   )
	st.markdown( """ 
		24. C.V. Câmpian, :blue[D. Nedelcu], D. Frunzaverde, C. Dumbravă, A. Cuzmoş,  A. Ladislau, C. Hamat, :green[EXPERIMENTAL 
		RESEARCH ON INCREASING THE PERFORMANCE OF 57.5 - 128.5 FRANCIS FVM TURBINES AT CHE BRĂDIȘOR], Research paper U-08-400-256, 
		Contract Hydraulics Research Centre and Thermal Processes of the University "Eftimie Murgu" Reșița, 191 pg., December, :red[2008].
	"""   )
	st.markdown( """ 
		25. C.V. Câmpian, G. Liuba, :blue[D. Nedelcu], A. Cuzmoş, C. Dumbravă, A. Ladislau, :green[STUDY ON THE BEHAVIOUR OF 
		HYDRO-AGGREGATES FROM RAUL ALB TO LOAD THROWS], Research paper U-08-400-255, Contract Hydraulics Research Centre 
		and Thermal Processes of the University "Eftimie Murgu" Reșița, Contract  44/14.10.2008, November, :red[2008].
	"""   )
	st.markdown( """ 
		26. C.V. Câmpian, :blue[D. Nedelcu], C. Hamat, A. Cuzmoş, C. Dumbravă, :green[DETERMINATION OF THE OPERATING 
		PARAMETERS AND TECHNICAL CONDITION OF THE HA2 - CHE RM. VÂLCEA BEFORE CAPITAL REPAIR WORKS, BY INDEX TESTS 
		CSPV CODE 71314300-5], Research paper U-08-400-254, Contract Hydraulics Research Centre and Thermal Processes 
		of the University "Eftimie Murgu" Reșița, Contract 104-113.03/29.10.2008, 61 pg., November, :red[2008].
	"""   )
	st.markdown( """ 
		27. C.V. Câmpian, :blue[D. Nedelcu], C. Hamat, A. Cuzmoş, C. Dumbravă, :green[DIAGNOSTIC ANALYSIS OF HA 1 CHE DAESTI 
		AFTER CAPITAL REPAIR], Research paper U-08-400-250, Contract Hydraulics Research Centre and Thermal Processes 
		of the University "Eftimie Murgu" Reșița, 61 pg., November, :red[2008].
	"""   )
	st.markdown( """ 
		28. C.V. Câmpian, C. Isbăşoiu, :blue[D. Nedelcu], E. Alămureanu, A.M. Pittner :green[ANALYSIS OF THE SWISS TECHNICAL 
		EXPERTISE REPORT FOR THE ECC ARBITRATION CASE NO. 14703/FM], Research paper U-08-400-247, Contract Hydraulics 
		Research Centre and Thermal Processes of the University "Eftimie Murgu" Reșița, June, :red[2008].
	"""   )
	st.markdown( """ 
		29. C.V. Câmpian, C. Isbăşoiu, :blue[D. Nedelcu], E. Alămureanu, A.M. Pittner :green[EXPERT REPORT ON 'TECHNICAL 
		EXPERTISE REPORT FOR ICC ARBITRATION CASE NO. 14703/FM'], Research paper U-08-400-246, Contract Hydraulics 
		Research Centre and Thermal Processes of the University "Eftimie Murgu" Reșița, Contract 45/19.11.2007, 
		6 pg., June, :red[2008].
	"""   )
	st.markdown( """ 
		30. C.V. Câmpian, :blue[D. Nedelcu], C. Dumbravă, I. Grando, A. Cuzmoş,:green[EQUIPMENT FOR MONITORING THE OPTIMAL 
		FUNCTIONING OF HA 1, HA2 IN CHE RUIENI USER MANUAL], Research paper U-08-400-243, Contract Hydraulics Research 
		Centre and Thermal Processes of the University "Eftimie Murgu" 	Reșița, Contract 72/19.XI.2007, 49 pg., January, 
		:red[2008].
	"""   )
	st.markdown( """ 
		31. C.V. Câmpian, :blue[D. Nedelcu], A. Cuzmoş, C. Dumbravă, I. Grando, V. Cojocaru :green[DEVELOPMENT AND VALIDATION 
		OF CRITERIA FOR OPTIMISING THE OPERATION OF HYDRO-AGGREGATES IN THE CHE RUIENI RESULTING FROM THE DATA PROVIDED 
		BY THE IMPLEMENTED OPTIMISATION SYSTEM. CORRELATING THEM WITH THE ENERGY PRODUCTION SUPPLY PROGRAMME.], Research 
		paper U-08-400-242, Contract Hydraulics Research Centre and Thermal Processes of the University "Eftimie Murgu" 
		Reșița, Contract  72/19.XI.2007, 104 pg., January, :red[2008].
	"""   )
	st.markdown( """ 
		32. C.V. Câmpian, :blue[D. Nedelcu], A. Cuzmoş, C. Dumbravă :green[Index tests performed on HA4 from Iron Gates II 
		before and after refurbishment], Research paper U-08-400-241, Contract Hydraulics Research Centre and 
		Thermal Processes of the University "Eftimie Murgu" Reșița, Contract 3/08.XII.1997-., 44 pg., March, :red[2008].
	"""   )
	st.markdown( """ 
		33. C.V. Câmpian, :blue[D. Nedelcu], I. Grando, A. Cuzmoş, C. Dumbravă :green[STUDY ON THE DETERMINATION OF THE 
		OPERATING PARAMETERS OF THE HYDROREGATE NO. 1 CHE REMEȚI AND THE TECHNICAL CONDITION BEFORE CAPITAL REPAIR, 
		BY INDEX TESTS C.P.V. CODE 74233500-6], Research paper U-07-400-237, Contract Hydraulics Research Centre and 
		Thermal Processes of the University "Eftimie Murgu" Reșița, 116 pg., December, :red[2007].
	"""   )
	st.markdown( """ 
		34. C.V. Câmpian, :blue[D. Nedelcu], A. Cuzmoş, C. Dumbravă :green[DETERMINATION OF THE OPERATING PARAMETERS AND 
		TECHNICAL CONDITION OF THE HYDRO-REGION HA2 - CHE CĂLIMĂNEȘTI, BEFORE THE CAPITAL REPAIR, BY INDEX TESTS], 
		Research paper U-07-400-235, Contract Hydraulics Research Centre and Thermal Processes of the University "Eftimie 
		Murgu" Reșița, Contract  158-12.02 / 2007, December, :red[2007].
	"""   )
	st.markdown( """ 
		35. C.V. Câmpian, :blue[D. Nedelcu], S. Muntean, A. Cuzmoş, C. Dumbravă :green[MEASUREMENT OF PRESSURE PULSATIONS IN 
		THE SUCTION TUBE CONE, IN STATIONARY AND NON-STATIONARY OPERATING MODES OF THE TURBINE FROM THE RUIENI CHE], 
		Research paper U-07-400-234, Contract Hydraulics Research Centre and Thermal Processes of the University "Eftimie 
		Murgu" Reșița, Contract  58 / 04.10.2007, December, :red[2007].
	"""   )
	st.markdown( """ 
		36. C.V. Câmpian, :blue[D. Nedelcu], A. Cuzmoş, C. Dumbravă, V. Cojocaru :green[COMPARISON OF THE PERFORMANCE OF 
		OLD AND UPGRADED TURBINES AT THE IRON GATES HYDROPOWER PLANT I DETERMINED FROM MODEL MEASUREMENTS MADE IN THE 
		ASTRÖ LABORATORY], Research paper U-07-400-233, Contract Hydraulics Research Centre and Thermal Processes of the University "Eftimie Murgu" 
		Reșița, Contract  10226/16.11.2007 , November, :red[2007].
	"""   )
	st.markdown( """ 
		37. C.V. Câmpian, C. Isbăşoiu, :blue[D. Nedelcu],E. Alămureanu, A.M. Pittner :green[STRENGTH CALCULATIONS WITH CLASSICAL 
		AND MODERN METHODS FOR THE RUNNER BLADES OF THE UPGRADED IRON GATE TURBINE I], Research paper 
		U-07-400-232, Contract Hydraulics Research Centre and Thermal Processes of the University "Eftimie Murgu" 
		Reșița, December, :red[2007].
	"""   )
	st.markdown( """ 
		38. C.V. Câmpian, :blue[D. Nedelcu], S. Muntean, A. Cuzmoş, C. Dumbravă :green[MEASUREMENT OF PRESSURE PULSATIONS 
		IN THE SUCTION TUBE CONE, IN STATIONARY AND NON-STATIONARY OPERATING MODES OF THE CHE MUNTENI], Research paper 
		U-07-400-231, Contract Hydraulics Research Centre and Thermal Processes of the University "Eftimie Murgu" 
		Reșița, Contract 5007 / 27.06.2007, December, :red[2007].
	"""   )
	st.markdown( """ 
		39. C.V. Câmpian, :blue[D. Nedelcu], A. Cuzmoş, C. Dumbravă :green[DETERMINATION OF THE OPERATING PARAMETERS AND 
		TECHNICAL CONDITION OF THE HA1 - CHE IONESTI, PRIOR TO CAPITAL REPAIR, BY INDEX TESTS], Research paper 
		U-07-400-229, Contract Hydraulics Research Centre and Thermal Processes of the University "Eftimie Murgu" 
		Reșița, Contract 60-12.02 / 15.05.2007, September, :red[2007].
	"""   )
	st.markdown( """ 
		40. :blue[D. Nedelcu], C.V. Câmpian,  :green[STRENGTH AND SERVICE LIFE CALCULATIONS FOR TURBINE RUNNER BLADES AT 
		CHE TURNU], Research paper U-07-400-227, Contract Hydraulics Research Centre and Thermal 
		Processes of the University "Eftimie Murgu" Reșița, Contract nr. 9661/07.08.2007, August, :red[2007].
	"""   )
	
	st.markdown( """ 
		41. C.V. Câmpian, :blue[D. Nedelcu], :green[PreDEx software for processing experimental data obtained on the 
		Iron Gates I turbine models], Research paper U-07-400-222-223, Contract Hydraulics Research Centre and Thermal 
		Processes of the University "Eftimie Murgu" Reșița, Contract nr. 3/08.XII.1997, April, :red[2007].
	"""   )
	st.markdown( """ 
		42. C.V. Câmpian, Gh. Liuba, D. Frunzăverde, :blue[D. Nedelcu], O. Megheleş, A. Cuzmoş, C. Dumbravă :green[DIAGNOSTIC 
		ANALYSIS OF HA 1 CHE DAESTI BEFORE CAPITAL REPAIR], Research paper U-07-400-219, Contract Hydraulics Research Centre and Thermal Processes of the 
		University "Eftimie Murgu" Reșița, Contract 5-12.02/26.01.2007, March, :red[2007].
	"""   )
	st.markdown( """ 
		43. C.V. Câmpian, :blue[D. Nedelcu], :green[STRENGTH CALCULATIONS FOR THE QUICK-CLOSING VALVE ACTUATOR ROD 
		AT THE IRON GATE I], Research paper U-07-400-217, Contract Hydraulics Research Centre and Thermal Processes of the 
		University "Eftimie Murgu" Reșița, Contract nr. 3/08.XII.1997-CCHAPT/UEMR ; 9893/22.XII.1997/SH PdF ADIŢIONAL 
		nr. 10/2006, December, :red[2006].
	"""   )
	st.markdown( """ 
		44. C.V. Câmpian, :blue[D. Nedelcu], :green[COMPARISON OF EXISTING AND REFURBISHED RUNNER BLADES AT THE IRON GATES I 
		AND HE DJERDAP I ], Research paper U-06-400-213, Contract Hydraulics Research Centre and Thermal Processes of the 
		University "Eftimie Murgu" Reșița, Contract NR. 3/08.XII.1997-CCHAPT/UEMR ; 9893/22.XII.1997/SH PdF ADIŢIONAL 
		nr. 10/2006December, :red[2006].
	"""   )
	st.markdown( """ 
		45. C.V. Câmpian, :blue[D. Nedelcu], C. HAMAT, A. Cuzmoş, D. Vela, C. Dumbravă, :green[CALCULATION AND VALIDATION 
		OF THE NON-CAVITATING OPERATING RANGES OF HA1, HA2 EQUIPPED WITH TURBINES IN THE CZECH REPUBLIC ], Research 
		paper U-06-400-211, Contract Hydraulics Research Centre and Thermal Processes of the University "Eftimie Murgu" 
		Reșița, CONTRACT nr. 118 / 24.11.2006, December, :red[2006].
	"""   )
	st.markdown( """ 
		46. C.V. Câmpian, :blue[D. Nedelcu], D. Frunzăverde, A. Cuzmoş, C. Dumbravă, :green[STRESS AND LIFETIME CALCULATIONS FOR THE 
		REFURBISHED TURBINE RUNNER BLADES AT THE IRONGATES I - Phase II], Research paper U-06-400-194, Contract Hydraulics 
		Research Centre and Thermal Processes of the University "Eftimie Murgu" Reșița, Contract nr. RU  din 18.11.2005,
		July, :red[2006].
	"""   )
	st.markdown( """ 
		47. Viorel C. Câmpian , :blue[Dorian Nedelcu], Vasile Barbu, Cosmin Dumbravă, Adrian Cuzmoş, Suciu Vasile, 
		:green[Determination of operating parameters and technical condition of HA1 Râureni, after capital repair, 
		by index tests], Research paper U-05-400-186, Decembrie, Contract Hydraulics Research Centre and 
		Thermal Processes of the University "Eftimie Murgu" Reșița (CCHAPT/UEMR), nr. 137-12.02/06.09.2005 SH 
		Râmnicu- Vâlcea, 95 pg, :red[2005].
	"""   )
	st.markdown( """ 
		48. Viorel C. Câmpian , :blue[Dorian Nedelcu], Vasile Barbu, Cosmin Dumbravă, Adrian Cuzmoş, Suciu Vasile, 
		:green[Determination of the operating parameters and technical condition of HA1 Zăvideni after capital repair, 
		by index tests], Research paper U-05-400-185 Decembrie, Contract Hydraulics Research Centre and 
		Thermal Processes of the University "Eftimie Murgu" Reșița,  nr. 137-12.02/06.09.2005 SH Râmnicu- Vâlcea, 85 pg, 
		:red[2005].
	"""   )
	st.markdown( """ 
		49. Viorel C. Câmpian, :blue[Dorian Nedelcu], Vasile Barbu, Cosmin Dumbravă, Adrian Cuzmoş, :green[Study on the realization and 
		implementation of the optimal exploitation functions of hydro-aggregates in the Ruieni CHE. Phase II. Realization 
		and implementation of the optimal exploitation functions of hydro-aggregates in the Ruieni HEC], Research paper 
		U-05-400-188 Noiembrie, Contract Hydraulics Research Centre and Thermal Processes of the University "Eftimie Murgu" 
		Reșița,  nr.  49/ 15.07.05 SH Caransebeş, 28 pg, :red[2005].
	"""   )
	st.markdown( """ 
		50. Viorel C. Câmpian, :blue[Dorian Nedelcu], Adrian Cuzmoş, Cosmin Dumbravă, Valentin Nedelea,  
		:green[Analysis of tests performed on the model of turbines - bulb pumps of hydroelectric power plants 
		in the Slatina - Danube sector], Research paper  U-05-400-182 August, Contract Hydraulics Research Centre 
		and Thermal Processes of the University "Eftimie Murgu" Reșița, Contract nr. 167 / 04.05.2005 SH 
		Slatina, 144 pg, :red[2005].
	"""   )
	st.markdown( """ 
		51. Viorel C. Câmpian, :blue[Dorian Nedelcu], Adrian Cuzmoş, Cosmin Dumbravă, George Tecliş,  :green[Study on the 
		realization and implementation of optimal exploitation functions of hydro-aggregates in Ruieni CHE], 
		Research paper U-05-400-181 August, Contract Hydraulics Research Centre and Thermal Processes 
		of the University "Eftimie Murgu" Reșița, Contract nr. 49/15.07.2005 CCHAPT/UEMR, 42 pg, :red[2005].
	"""   )
	st.markdown( """ 
		52. Viorel C. Câmpian, :blue[Dorian Nedelcu], :green[Analysis of differences between efficiency tables generated from primary 
		data and those calculated by PrelDate software version 2 for Iron Gates I and Iron Gates II HECs], Research paper
		U-05-400-180 June, Contract Hydraulics Research Centre and Thermal Processes 
		of the University "Eftimie Murgu" Reșița, Contract nr. 3/08.XII.1997-CCHAPT/UEMR ; 9893/22.XII.1997/SH PDF 
		adiţional nr. 8, 1 CD + 13 pg, :red[2005].
	"""   )
	st.markdown( """ 
		53. Viorel C. Câmpian, :blue[Dorian Nedelcu], Adrian Cuzmoş, Cosmin Dumbravă, 
		:green[Average turbine and hydro-aggregate efficiencies at Iron Gates I CHP],
		Research paper U-05-400-176 Martie, Contract Hydraulics Research Centre and Thermal Processes 
		of the University "Eftimie Murgu" Reșița, Contract nr. 3/08.XII.1997-CCHAPT/UEMR; 9893/22.XII.1997/SH  
		PdF ADIŢIONAL NR. 9/2005,  8 pg, :red[2005].
	"""   )
	st.markdown( """ 
		54. Viorel C. Câmpian, :blue[Dorian Nedelcu], Ion Vela, Adrian Cuzmoş,  :green[Execution project for Francis 
		turbine model nskw=285], Research paper U-05-400-174 February, Contract nr. 5478/06.X.2004 
		S.C. RECONT S.A. Timişoara,  166 pg, :red[2005].
	"""   )
	st.markdown( """ 
		55. Viorel C. Câmpian, :blue[Dorian Nedelcu], Adrian Cuzmoş, Cosmin Dumbravă, Suciu Vasile, 
		:green[Determination of the turbine flow through the hydraulic circuit of the hydro-aggregates from 
		CHE Gura Lotrului, Turnu and Daesti], Research paper 164 for Beneficiary Sucursala Hidrocentrale 
		Ramnicu Valcea, 84 pg., :red[2004].
	"""   )
	st.markdown( """ 
		56. Viorel C. Câmpian, :blue[Dorian Nedelcu], Adrian Cuzmoş, Doina Frunzaverde, Cosmin Dumbravă, Suciu Vasile, 
		:green[Determination of the operating parameters and technical condition of the hydro-aggregate HA No. 2 
		of CHE Turnu after capital repair, by index tests], Research paper  U-04-400-70 December, 
		Beneficiary Sucursala Hidrocentrale Ramnicu Valcea, 87 pg., :red[2004].
	"""   )
	st.markdown( """ 
		57. Viorel C. Câmpian, :blue[Dorian Nedelcu], Adrian Cuzmoş, Cosmin Dumbravă, Suciu Vasile, :green[Determination of 
		operating parameters and technical condition of HA No 1 Turnu hydro-aggregate prior to capital repair by 
		index tests], Research paper U-04-400-69 December, Contract249-12.02/10.12.2004 ad 1 CCHAPT- SH Râmnicu Valcea, 
		72 pg., :red[2004].
	"""   )
	st.markdown( """ 
		58. Viorel C. Câmpian, :blue[Dorian Nedelcu], Doina Frunzaverde, Adrian Cuzmoş, Cosmin Dumbravă, Suciu Vasile, 
		:green[Determination of the operating parameters and technical condition of the hydro-aggregate no. 2 of CHE 
		Băbeni, prior to capital repair, by index tests],  Research paper U-04-400-68 December, Contract 249 CCHAPT- SH Ramnicu 
		Valcea, 80 pg., :red[2004].
	"""   )
	st.markdown( """ 
		59. Viorel C. Câmpian, :blue[Dorian Nedelcu], Adrian Cuzmoş, Cosmin Dumbravă, Suciu Vasile, 
		:green[Study on the determination of the causes of cavitation in the HA turbines of CHE Tileagd with 
		determination of the actual cavitational characteristics operation], Research paper U-04-400-67 
		December, Contract CCHAPT- SH Cluj-UE Crisuri Oradea Contract nr. 3179, 111 pg.,  :red[2004].
	"""   )
	st.markdown( """ 
		60. Viorel C. Câmpian, :blue[Dorian Nedelcu], Adrian Cuzmoş, Cosmin Dumbravă, Suciu Vasile, :green[Determination of the 
		parameters and technical condition of the CHE Valcea hydro-aggregate no. 1, prior to capital repair], 
		Research paper U-04-400-66 December, Contract CCHAPT- SH Ramnicu Valcea, 112 pg., :red[2004].
	"""   )
	st.markdown( """ 
		61. Viorel C. Câmpian, :blue[Dorian Nedelcu], :green[Software for processing characteristics of hydraulic machines], 
		Research paper  U-04-400-64 Octomber, Contract RU 296/09.XI.2004 CCHAPT-Hidroelectrica 
		SA – SH Portile de Fier, 17 pg., :red[2004].
	"""   )
	st.markdown( """ 
		62. Viorel C. Câmpian, :blue[Dorian Nedelcu], Adrian Cuzmoş, Cosmin Dumbravă, :green[The characteristics and 
		hill charts diagrams of the Iron Gates I and Iron Gates II CHEs], Research paper U-04-400-63 Octomber, 
		Research paper 3/08.XII.1997-CCHAPT/UEMR; 9893/22.XII.1997/SH PdF ad nr. 8/2004CCHAPT- SH Ramnicu Valcea, 
		635 pg., :red[2004].
	"""   )
	st.markdown( """ 
		63. Viorel C. Câmpian, :blue[Dorian Nedelcu], Cosmin Dumbravă, :green[Operating diagram of the upgraded turbine of 
		at Iron Gates II based on laboratory model measurements], Research paper U-04-400-61 Mai, Contract 
		3/08.XII.1997-CCHAPT/UEMR; 9893/22.XII.1997/FE PdF Adiţional nr. 8, 76 pg., :red[2004].
	"""   )
	st.markdown( """ 
		64. Viorel C. Câmpian, :blue[Dorian Nedelcu], Cosmin Dumbravă, Gheorghe Liuba, Adrian Cuzmoş, :green[Optimising operation 
		of the hydro-aggregates at the Ruieni CHE using data and monitoring system. determining optimal P - Q 
		loadings based on optimal ranges in the 300 - 330 m range:green], Research paper U-03-400-58 December, 
		Contract Hydraulics Research Centre and Thermal Processes of the University "Eftimie Murgu" Reșița
		Contract 53 CCHAPT/UEMR, 98 pg., :red[2003].
		"""   )
	st.markdown( """ 
		65. Viorel C. Câmpian, :blue[Dorian Nedelcu], Cosmin Dumbravă, Gheorghe Liuba, Adrian Cuzmoş, :green[Determination of parameters 
		and technical condition of the hydro-aggregate No. 1 of the Zăvideni CHE before capital repair], Research paper
		U-03-400-57 December, Contract CCHAPT- SH Ramnicu Valcea Contract nr. 2, 132 pg., :red[2003].
		"""   )
	st.markdown( """ 
		66. Viorel C. Câmpian, :blue[Dorian Nedelcu], Cosmin Dumbravă, Gheorghe Liuba, Adrian Cuzmoş, :green[Optimising operation 
		of the hydro-aggregates at the Ruieni CHE using data and monitoring system. Determining optimal P - Q loadings 
		based on optimal efficiency in the 300 - 330 m range], Research paper CCHAPT December, 98 pg., :red[2003].
		"""   )
	st.markdown( """ 
		67. Viorel C. Câmpian, :blue[Dorian Nedelcu], Cosmin Dumbravă, Gheorghe Liuba, Adrian Cuzmoş, :green[Determination of the 
		parameters of and technical condition of hydro-aggregate No. 1 of CHE Râureni before capital repair],  
		Research paper U-03-400-56 Noiember, Contract CCHAPT- SH Ramnicu Valcea Contract nr. 2, 113 pg., :red[2003].
		"""   )
	st.markdown( """ 
		68. Viorel C. Câmpian, :blue[Dorian Nedelcu], Cosmin Dumbravă, Gheorghe Liuba, Adrian Cuzmoş, :green[Determination of the 
		parameters and technical condition of the hydroaggregate no. 1 of CHE Govora after capital repair], 
		Research paper U-04-400-54 August, Contract CCHAPT- SH Ramnicu Valcea Contract nr. nr. 2, 99 pg., :red[2003].
		"""   )
	st.markdown( """ 
		69. Viorel C. Câmpian, :blue[Dorian Nedelcu], Adrian Cuzmoş, :green[Three-dimensional mathematical models for the runner blade 
		of the bulb turbine of the Iron Gates II CHE], Research paper  U-04-400-48 Februarie, Contract 765/19.04.1999 
		ADIŢIONAL nr. 7, 58 pg., :red[2003].
	"""   )
	st.markdown( """ 
		70. Viorel C. Câmpian, :blue[Dorian Nedelcu], Adrian Cuzmoş, :green[Repeated index tests on hydroaggregate No. 6 at CHE 
		Iron Gates I after refurbishment], Research paper U-04-400-47 Februarie, 34 pg., :red[2003].
		"""   )
	st.markdown( """ 
		71. Viorel C. Câmpian, :blue[Dorian Nedelcu], Cosmin Dumbravă, Adrian Cuzmoş, :green[Drawing combinatorial curves for 
		the existing runner of the turbines of the Portile de Fier I and HE Djerdap I], Research paper U-02-400-46 
		Noiember, Contract Hydraulics Research Centre and Thermal Processes of the University "Eftimie Murgu" Reșița 
		Contract nr. 3/08.XII.1997-CCHAPT/UEMR ; 9893/22.XII.1997/FE PdF I ADIŢIONAL NR. 6, 35 pg., :red[2002].
		"""   )
	st.markdown( """ 
		72. Viorel C. Câmpian, :blue[Dorian Nedelcu], Cosmin Dumbravă, Adrian Cuzmoş, Gheorghe Liuba, 
		:green[Study on the behaviour of HA CHE Ruieni at load throwing], Research paper U-02-400-45 
		CCHAPT Octomber, Contract nr. 765/19.04.1999 ADIŢIONAL NR. 3, 73 pg., :red[2002].
		"""   )
	st.markdown( """ 
		73. Viorel C. Câmpian, :blue[Dorian Nedelcu], :green[Determination and optimization of the flow through 
		hydro-aggregate cooling system of the Iron Gates HEC I - STEP II: Determination of 
		range of flow rates through Lakos separators as a function of the number of separators, 
		at inlet water temperature t = 21.3 Celsius degree and net head hn = 24.15 m], Research 
		paper U-02-400-44 CCHAPT Octomber, Contract Hydraulics Research Centre and Thermal 
		Processes of the University "Eftimie Murgu" Reșița Contract nr. 3/08.XII.1997-CCHAPT/UEMR; 
		9893/22.XII.1997/FE PdF I ADIŢIONAL NR. 6, 9 pg., :red[2002].
		"""   )
	st.markdown( """ 
		74. Viorel C. Câmpian, :blue[Dorian Nedelcu], Adrian Cuzmos, :green[Index tests carried out on hydro-aggregate 
		no. 6 of the Iron Gates I CHE before and after the refurbishment], Research paper U-02-400-43 
		CCHAPT August, Contract ADIŢIONAL NR. 6, 39 pg., :red[2002].
		"""   )
	st.markdown( """ 
		75. Viorel C. Câmpian, :blue[Dorian Nedelcu], Cosmin Dumbravă, Adrian Cuzmos, :green[Comparison of the efficiencies of 
		the existing and refurbished turbines from CHE Iron Gates I, taking as reference the measurements 
		performed on models in the ASTRO neutral laboratory], Research paper U-02-400-42 CCHAPT August, 
		Contract  ADIŢIONAL NR. 6, 127 pg., :red[2002].
		"""   )
	st.markdown( """ 
		76. Viorel C. Câmpian, :blue[Dorian Nedelcu], :green[Analysis and comparison of neutral laboratory offers 
		selection of the neutral laboratory for testing the models at the Iron Gates II CHE], Research paper 
		U-02-400-41 CCHAPT July, Contract Hydraulics Research Centre and Thermal 
		Processes of the University "Eftimie Murgu" Reșița Contract nr. 3/08.XII.1997-CCHAPT/UEMR ; 
		9893/22.XII.1997/FE PdF I, 9 pg., :red[2002].
		"""   )
	st.markdown( """ 
		77. :blue[Dorian Nedelcu], :green[KA 80Z motherboard deformation analysis and optimization solutions. 
		Displacement analyse of KA 80Z support and optimize solution], Research paper  CTT June, 
		Contract UEMR/CTT–Pro Red & Engineering nr. 99, 25 pg., :red[2002].		
		"""   )
	st.markdown( """ 
		78. Viorel C. Câmpian, :blue[Dorian Nedelcu], :green[Determinarea şi optimizarea debitului tranzitat prin sistemul 
		de răcire al hidroagregatelor de la CHE Porţile de Fier I - ETAPA I: Determinarea domeniului de 
		debite tranzitate prin separarea Lakos, funcţie de numărul de separatoare, la temperatura apei 
		la intrare de t = 11 C şi căderea netă Hn = 26,26 m], Research paper U-02-400-38, CCHAPT May, 
		Contract Hydraulics Research Centre and Thermal Processes of the University "Eftimie Murgu" Reșița 
		Contract nr. 3/08.XII.1997-CCHAPT/UEMR ; 9893/22.XII.1997/SH PdF ad nr. 6, 11 pg., :red[2002].
	"""   )
	st.markdown( """ 
		79. Viorel C. Câmpian, :blue[Dorian Nedelcu], :green[Checking the geometry of the turbine model runner blades 
		from CHE Iron Gates and HE Djerdap manufactured by Turboinstitut Ljubljana], Research paper 
		U-02-400-37 March, Contract Hydraulics Research Centre and Thermal Processes of the University 
		"Eftimie Murgu" Reșița, Contract 3/08.XII.1997-CCHAPT/UEMR ; 9893/22.XII.1997/SH PdF ad nr. 6, 54 
		pg., :red[2002].
		"""   )
	st.markdown( """ 
		80. Viorel C. Câmpian, :blue[Dorian Nedelcu], Gheorghe Liuba, Doina Frunzăverde, O. Megheleş, Cosmin Dumbravă, 
		Adrian Cuzmoş, :green[Determination of the operating parameters of hydro-aggregates in the Turnu HEC and the 
		their technical condition prior to capital repair by index tests], Research paper  U-02-400-36 C.T.T. 
		January, Contract 8/22.XI.2001-CTT/UEMR, 78 pg., :red[2002].
		"""   )
	st.markdown( """ 
		81. Viorel C. Câmpian, :blue[Dorian Nedelcu],  :green[Calculation of the weighted average efficiency of the upgraded turbine 
		of the Iron Gates I CHP taking into account the influence of the anti-cavitation edge], Research paper 
		U-01-400-35 Ianuarie, 14 pg.,  :red[2002].
		"""   )
	st.markdown( """ 
		82. Viorel C. Câmpian, :blue[Dorian Nedelcu], :green[Strength calculation for grate segment from hydroaggregates 
		CHE Iron Gate I], Research paper, December, 11 pg., :red[2001].
		"""   )
	st.markdown( """ 
		83. Viorel C. Câmpian, :blue[Dorian Nedelcu], :green[Work programme for index testing of Romanian turbines 
		refurbished at net head at maximum efficiency in accordance with the Minutes of the Group Meeting 
		of the Joint Romanian-Yugoslav Iron Gates Commission which took place during the period 
		10.09.2001-15.09.2001 in Belgrade],  Research paper  U-01-400-33 Octombrie, 35 pg., :red[2001].
		"""   )
	st.markdown( """ 
		84. Viorel C. Câmpian, :blue[Dorian Nedelcu], :green[Comments on the material 'Determining the differences in 
		efficiency differences between upgraded and existing Romanian hydro-aggregates', prepared by the 
		Yugoslav side dated 07.VIII.2001], Research paper U-01-400-32 Septembrie, Contract 
		Hydraulics Research Centre and Thermal Processes of the University "Eftimie Murgu" Reșița,
		Contract nr. 3/08.XII.1997-CCHAPT/UEMR ; 9893/22.XII.1997/FE PdF I ADIŢIONAL NR. 5, 11 pg., :red[2001].
		"""   )
	st.markdown( """ 
		85. Viorel C. Câmpian, :blue[Dorian Nedelcu], :green[Calculation of the exploitation diagram of the upgraded hydro-aggregate 
		at Iron Gates I CHE based on model measurements in the neutral laboratory Astro by the methodology agreed 
		with the Yugoslav partner; Phase 1: Comparative calculation of the powers and hydro-aggregates in the 
		15.5 - 31 m head range in the 0.5 in 0.5 m and flow rates 100 - 990 m3/s with 10 m3/s step], Research paper
		U-00-400-31 August, Contract Hydraulics Research Centre and Thermal Processes of the University "Eftimie Murgu" 
		Reșița Contract nr. 3/08.XII.1997-CCHAPT/UEMR ; 9893/22.XII.1997/FE PdF I ADIŢIONAL NR. 5, 59 pg., :red[2001].
		"""   )
	st.markdown( """ 
		86. Viorel C. Câmpian, :blue[Dorian Nedelcu], :green[Work programme for index testing of Romanian turbines 
		refurbished at net head at maximum efficiency], Research paper  U-00-400-27 March, Contract 
		Hydraulics Research Centre and Thermal Processes of the University "Eftimie Murgu" 
		Reșița Contract nr. 3/08.XII.1997-CCHAPT/UEMR ; 9893/22.XII.1997/FE PdF I ADIŢIONAL NR. 5/2001, 
		35 pg., :red[2001].
		"""   )
	st.markdown( """ 
		87. Viorel C. Câmpian, :blue[Dorian Nedelcu], :green[Comparison of weighted average efficiency - Iron Gates 
		I RR 1998 + ER 2002 + RR 2002], Contract Hydraulics Research Centre and Thermal Processes of the 
		University "Eftimie Murgu" Reșița, Contract nr. 3/08.XII.1997-CCHAPT/UEMR ; 9893/22.XII.1997/FE 
		PdF I ADIŢIONAL NR. 4, 10 pg., :red[2001].
	"""   )
	st.markdown( """ 
		88. Viorel C. Câmpian, :blue[Dorian Nedelcu], :green[Romanian - Yugoslav index tests for hydropower plant 
		Iron Gates I], Research paper U-00-400-23 November, Contract Hydraulics Research Centre and 
		Thermal Processes of the University "Eftimie Murgu" Reșița, Contract nr. 3/08.XII.1997-CCHAPT/UEMR 
		; 9893/22.XII.1997/FE PdF I ADIŢIONAL NR. 4, 29 pg., :red[2000].
		"""   )
	st.markdown( """ 
		89. Viorel C. Câmpian, :blue[Dorian Nedelcu], :green[Strength calculation for shaft-runner coupling pin],  Research 
		paper, May, Contract Hydraulics Research Centre and  Thermal Processes of the University "Eftimie 
		Murgu" Reșița, Contract nr. 3/08.XII.1997-CCHAPT/UEMR ; 9893/22.XII.1997/FE PdF I ADIŢIONAL NR. 4, 
		20 pg., :red[2000].
		"""   )
	st.markdown( """ 
		90. Viorel C. Câmpian, :blue[Dorian Nedelcu], :green[Hill chart characteristics of old hydro-aggregates from 
		Iron Gates I, for the head range H = 18 - 31 m, with 1 m step, and aggregate power 
		with 1 MW step], Research paper U-00-400-21 Aprilie, Contract Hydraulics Research Centre and  Thermal 
		Processes of the University "Eftimie Murgu" Reșița, Contract nr. 3/08.XII.1997-CCHAPT/UEMR ; 
		9893/22.XII.1997/FE PdF I ADIŢIONAL NR. 4, 43 pg., :red[2000].
		"""   )
	st.markdown( """ 
		91. Viorel C. Câmpian, :blue[Dorian Nedelcu], :green[Conclusions on the final processing of LMZ measurements], Research paper 
		U-00-400-20 Martie, Contract Hydraulics Research Centre and  Thermal Processes of the University "Eftimie 
		Murgu" Reșița, Contract nr. 3/08.XII.1997-CCHAPT/UEMR ; 9893/22.XII.1997/FE PdF I ADIŢIONAL NR. 4, 10 pg., 
		:red[2000].
		"""   )
	st.markdown( """ 
		92. Viorel C. Câmpian, :blue[Dorian Nedelcu], :green[Operating characteristics of the old turbine at Iron Gates I, 
		for heads H = 19 m, 20 m, 21 m, 22 m, 24 m, 25 m, 26 m, 28 m, 29 m, 30 m], Research paper U-00-400-18 March, 
		Contract Hydraulics Research Centre and  Thermal Processes of the University "Eftimie Murgu" Reșița, 
		Contract nr. 3/08.XII.1997-CCHAPT/UEMR ; 9893/22.XII.1997/FE PdF I ADIŢIONAL NR. 4, 16 pg., :red[2000].
		"""   )
	st.markdown( """ 
		93. Viorel C. Câmpian, :blue[Dorian Nedelcu], :green[Operating characteristics of the old turbine at Iron Gates I, 
		for head H = 18 m, 23 m, 27 m, 31 m], Research paper U-00-400-17 March, Contract Hydraulics Research Centre 
		and  Thermal Processes of the University "Eftimie Murgu" Reșița,  Contract nr. 3/08.XII.1997-CCHAPT/UEMR ; 
		9893/22.XII.1997/FE PdF I ADIŢIONAL NR. 4, 28 pg., :red[2000].
	"""   )
	st.markdown( """ 
		94. Viorel C. Câmpian, :blue[Dorian Nedelcu], :green[Comparison of the LMZ model characteristics of the turbines at the Gates CHE 
		I with those calculated by the Romanian and Yugoslav teams], Research paper U-00-400-16 Martie, Contract 
		Hydraulics Research Centre and  Thermal Processes of the University "Eftimie Murgu" Reșița,
		Contract nr. 3/08.XII.1997-CCHAPT/UEMR ; 9893/22.XII.1997/FE PdF I ADIŢIONAL NR. 4, 72 pg., :red[2000].
		"""   )
	st.markdown( """ 
		95. Viorel C. Câmpian, :blue[Dorian Nedelcu], :green[Calculation and plotting of the helical characteristics of the model 
		of the turbines of the Iron Gates I CHP in the second transposition step], Research paper U-00-400-15 February, 
		Contract Hydraulics Research Centre and  Thermal Processes of the University "Eftimie Murgu" Reșița,
		Contract nr. 3/08.XII.1997-CCHAPT/UEMR ; 9893/22.XII.1997/FE PdF I ADIŢIONAL NR. 4, 55 pg., :red[2000].
		"""   )
	st.markdown( """ 
		96. Viorel C. Câmpian, :blue[Dorian Nedelcu], :green[Servomotor characteristics of the wicked gate "S" depending on the opening 
		of the guide vanes "ao" on the old turbines of the Iron Gates CHE I], Research paper U-00-400-14 February, 
		Contract Hydraulics Research Centre and  Thermal Processes of the University "Eftimie Murgu" Reșița, Contract
		nr. 3/08.XII.1997-CCHAPT/UEMR ; 9893/22.XII.1997/FE PdF I ADIŢIONAL NR. 4, 9 pg., :red[2000].
		"""   )
	st.markdown( """ 
		97. Viorel C. Câmpian, :blue[Dorian Nedelcu], :green[Determination of the mechanical efficiency of the old turbines at CHE Iron 
		Gates I], Research paper U-00-400-13 February, Contract Hydraulics Research Centre and  Thermal Processes of the 
		University "Eftimie Murgu" Reșița, Contract nr. 3/08.XII.1997-CCHAPT/UEMR; 9893/22.XII.1997/FE PdF I ADIŢIONAL 
		NR. 4, 11 pg., :red[2000].
		"""   )
	st.markdown( """ 
		98. Viorel C. Câmpian, :blue[Dorian Nedelcu],  :green[Calculation and drawing of helical characteristics of the LMZ turbine model 
		turbine of the Iron Gates I hydropower plant], Research paper U-99-400-12 December, Contract Hydraulics Research 
		Centre and  Thermal Processes of the University "Eftimie Murgu" Reșița,  Contract nr. 3/08.XII.1997-CCHAPT/UEMR; 
		9893/22.XII.1997/FE PdF I ADIŢIONAL NR. 3, 71 pg.,  :red[1999].
		"""   )
	st.markdown( """ 
		99. Viorel C. Câmpian, :blue[Dorian Nedelcu], :green[Tests on the hydraulic turbine model of the Iron Gates I CHE. Select the neutral
		laboratory. Warranty test programme], Research paper  U-98-400-03 January, Contract Hydraulics Research Centre and 
		Thermal Processes of the University "Eftimie Murgu" Reșița, Contract nr. 3/08.XII.1997-CCHAPT/UEMR; 9893/22.XII.1997/FE 
		PdF I ADIŢIONAL NR. 1, 54 pg., :red[1998].
		"""   )
	st.markdown( """ 
		100. Viorel C. Câmpian, :blue[Dorian Nedelcu],  :green[Analysis of laboratories specialising in turbine measurements to determine 
		energy-cavitational characteristics and verification of guarantees. Criteria for assessment and selection of laboratories], 
		 Research paper U-97-400-02 Decembrie, Contract Hydraulics Research Centre and  Thermal Processes of the University 
		"Eftimie Murgu" Reșița, Contract nr.3/08.XII.1997-CCHAPT/UEMR; 9893/22.XII.1997/FE PdF, 71 pg.,  :red[1997].
		"""   )
	st.markdown( """ 
		101. Viorel C. Câmpian, :blue[Dorian Nedelcu], I. Ruja, O. Crivacucea, I. Grando, :green[Investigating industry interest in the 
		vest region for research and development], Research paper U–97-400-01 November, Contract nr. UEMR, 15 pg., :red[1997].
		"""   )
	st.markdown( """ 
		102. :blue[Dorian Nedelcu], :green[Hydrodynamics of bulb pump turbines. Study and design methods], D.C.P.D. - U.C.M.Reşiţa, :red[1996].
		"""   )
	st.markdown( """ 
		103. :blue[Dorian Nedelcu], :green[Mathematical modelling of the stresses and strains state of which runner and guide vanes are subjected 
		for bulb turbines], D.C.P.D. - U.C.M.Reşiţa, :red[1996].
		"""   )
	st.markdown( """ 
		104. :blue[Dorian Nedelcu], :green[Mathematical modelling of water flow through the bulb turbine with application to turbines offered for C.H.E. 
		Turnu Măgurele - Nicopole], D.C.P.D. - U.C.M.Reşiţa, :red[1996].
		"""   )
	st.markdown( """ 
		105. I. Hota, :blue[Dorian Nedelcu],  :green[Mathematical methods for hydrodynamic study and design of axial turbines. Turbine hydrodynamics 
		bulb. Study and design methods], D.C.P.D. - U.C.M.Reşiţa,  :red[1996].
		"""   )
	st.markdown( """ 
		106. :blue[Dorian Nedelcu], :green[Mathematical modelling of the stresses and strains state of to which the runner and guide vanes are subjected
		for Kaplan turbines], D.C.P.D. - U.C.M.Reşiţa, :red[1995].
		"""   )
	st.markdown( """ 
		107. :blue[Dorian Nedelcu], :green[Mathematical modelling of water flow through the Kaplan turbine, with application to the turbines at Iron Gates 
		I], D.C.P.D. - U.C.M.Reşiţa, :red[1994].
		"""   )
	st.markdown( """ 
		108. :blue[Dorian Nedelcu],  :green[Hydrodynamics of Kaplan turbines. Study and design methods], D.C.P.D. - U.C.M.Reşiţa,  :green[1994].
		"""   )
	st.markdown( """ 
		109. :blue[Dorian Nedelcu], C. Secosan, I. Hota,  :green[Determination of the technical condition of hydro-aggregates at CHE Pângărați. 
		Mathematical modelling of hydroaggregate], D.C.P.D. - U.C.M.Reşiţa, :red[1994].
		"""   )
	st.markdown( """ 
		110. C.V.Campian, :blue[Dorian Nedelcu], C. Secosan, I. Hota, :green[Mathematical modelling in hydrodynamics], D.C.P.D. - U.C.M.Reşiţa, :red[1993].
		"""   )
	st.markdown( """ 
		111. :blue[Dorian Nedelcu], :green[Calibration of tube and nozzle Venturi], Scientific Research and Technological Engineering Centre for Hydropower 
		Equipment Resita, :red[1988].
		"""   )
	st.markdown( """ 
		112. :blue[Dorian Nedelcu], :green[P.E. Diagonal turbine-pump - Stage I], Scientific Research and Technological Engineering Centre for Hydropower 
		Equipment Resita, :red[1988].
		"""   )
	st.markdown( """ 
		113. :blue[Dorian Nedelcu], :green[P.E. rotor variant D45], Scientific Research and Technological Engineering Centre for Hydropower 
		Equipment Resita,  :red[1988].
		"""   )
	st.markdown( """ 
		114. :blue[Dorian Nedelcu], :green[P.E. parts of hydraulic components], Scientific Research and Technological Engineering Centre 
		for Hydropower Equipment Resita, :red[1988].
		"""   )
	st.markdown( """ 
		115. :blue[Dorian Nedelcu], :green[Concluding study on contract 2812/1985], Scientific Research and Technological Engineering Centre for 
		Hydropower Equipment Resita, :red[1987].
		"""   )
	st.markdown( """ 
		116. :blue[Dorian Nedelcu], :green[Experiments D45/2], Scientific Research and Technological Engineering Centre for Hydropower Equipment Resita, 
		:red[1987].
		"""   )
	st.markdown( """ 
		117. :blue[Dorian Nedelcu], :green[Experiments D45 - Stage II], Scientific Research and Technological Engineering Centre for Hydropower 
		Equipment Resita, :red[1986].
		"""   )
	st.markdown( """ 
		118. :blue[Dorian Nedelcu], :green[Experiments D45 - Stage I], Scientific Research and Technological Engineering Centre for Hydropower 
		Equipment Resita, :red[1986].
		"""   )
	st.markdown( """ 
		119. :blue[Dorian Nedelcu], :green[P.E. runner D 45/2 and wicked gate], Scientific Research and Technological Engineering Centre for Hydropower 
		Equipment Resita, :red[1986].
		"""   )
	st.markdown( """ 
		120. :blue[Dorian Nedelcu], :green[Improved prototype documentation], Scientific Research and Technological Engineering Centre for Hydropower Equipment Resita, :red[1986].
		"""   )
	st.markdown( """ 
		121. :blue[Dorian Nedelcu], :green[Complex research work on turbofan assembly and improved turbine], Scientific Research and Technological Engineering Centre for Hydropower 
		Equipment Resita, :red[1986].
		"""   )
	st.markdown( """ 
		122. :blue[Dorian Nedelcu], :green[Complex research work (design, execution, experiments) on the TVA 450 NAE turbofan assembly], Scientific Research and Technological 
		Engineering Centre for Hydropower Equipment Resita, :red[1986].
		"""   )
	st.markdown( """ 
		123. :blue[Dorian Nedelcu], :green[Development of adaptation documentation for the prototype], Scientific Research and Technological Engineering Centre for Hydropower 
		Equipment Resita, :red[1986].
		"""   )
	st.markdown( """ 
		124. :blue[Dorian Nedelcu], :green[Deriaz pump turbine documentation], Scientific Research and Technological Engineering Centre for Hydropower Equipment Resita, :red[1985]
		"""   )
	st.markdown( """ 
		125. :blue[Dorian Nedelcu], :green[Final prototype experiments], Scientific Research and Technological Engineering Centre for Hydropower Equipment Resita, :red[1985].
		"""   )
	st.markdown( """ 
		126. :blue[Dorian Nedelcu], :green[Pre-final experiments of prototype turbine PO 0.005-70 with nozzle], Scientific Research and Technological Engineering Centre for 
		Hydropower Equipment Resita, :red[1985].
		"""   )
	st.markdown( """ 
		127. :blue[Dorian Nedelcu], :green[P.E. rotor and enlarged casing with view for turbine PO 0.005-70 with nozzle based on experimental results], Scientific Research 
		and Technological Engineering Centre for Hydropower Equipment Resita, :red[1985].
		"""   )
	st.markdown( """ 
		128. :blue[Dorian Nedelcu], :green[Complex research works (design, execution, variant experiments) prototype turbine PO 0.005-70 with nozzle], Scientific Research 
		and Technological Engineering Centre for Hydropower Equipment Resita, :red[1985].
		"""   )
	st.markdown( """ 
		129. :blue[Dorian Nedelcu], :green[Stand and experiments for prototype turbine PO 0.005-70 with nozzle], Scientific Research and Technological Engineering 
		Centre for Hydropower Equipment Resita, :red[1984].
		"""   )
	st.markdown( """ 
		130. :blue[Dorian Nedelcu], :green[Closed circuit preselection stand. Mechanical part], Scientific Research and Technological Engineering Centre for Hydropower 
		Equipment Resita, :red[1984.
		"""   )
	st.markdown( """ 
		131. :blue[Dorian Nedelcu], :green[Prototype design of PO 0.005-70 turbine with nozzle], Scientific Research and Technological Engineering Centre for Hydropower 
		Equipment Resita, :red[1984].
		"""   )















