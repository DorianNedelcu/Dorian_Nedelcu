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
#	PAGE_TITLE = "Articles"  ;  st.title(PAGE_TITLE)
	st.title(":chart_with_upwards_trend: :green[Published Articles]")
	
	# --- LIST OF BOOKS   ---
	st.write("#")
	st.subheader(":red[150 x articles published between 2023-2002]")   
	st.write("---")
	st.subheader(":gray[24 x ISI published articles indexed in the Web of Science]")

	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		1.1. Article  Title: :green[Effect of Zeolite Mineral on the Formulation of a Wood-plastic
		Composite] Author(s): UZIEL MEJIA-GONZALEZ, DORIAN NEDELCU2, JAVIER CRUZ SALGADO, 
		MISAELA FRANCISCO-MARQUEZ, Source: :blue[MATERIALE PLASTICE]  Volume: 60  Issue: 3 Pages: 11-18
		Published: SEP :red[2023], Web of Science Accession Number: WOS:001083326000002
	"""   )
	col2.link_button("View", "https://revmaterialeplastice.ro/pdf/2%20UZIEL%203%2023.pdf")

	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		1.2. Article  Title: :green[A structural health monitoring Python code to detect 
		small changes in frequencies] Author(s): Nedelcu, D, Gillich, GR, 
		:blue[MECHANICAL SYSTEMS AND SIGNAL PROCESSING] , Volume: ‏ 1
		Article Number: 107087,  Published: ‏ JAN 15 :red[2021], 
		DOI: 10.1016/j.ymssp.2020.107087, ISSN: 0888-3270,
		Web of Science Accession Number: WOS:000572359600008
	"""   )
	col2.link_button("View", "https://www.sciencedirect.com/science/article/abs/pii/S0888327020304738")

	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		1.3. Article  Title: :green[Study Regarding the Influence of the Printing Orientation Angle
		on the Mechanical Behavior of Parts Manufactured by Material Jetting], Author(s): 
		Cojocaru, V., Frunzaverde, D., Nedelcu, D., Miclosina, CO., Marginean, G.,
		 Source: :blue[MATERIALE PLASTICE] Volume 58 Issue 3 Page 198-209 Published: Sep. :red[2021] 
		Web of Science Accession Number: WOS:000705010100007
	"""   )
	col2.link_button("View", "https://revmaterialeplastice.ro/pdf/19%20COJOCARU%20V%203%2021.pdf")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		1.4. Article  Title: :green[Redesign of Layout Runner in Rubber Injection Molding for Filling of 
	a Multi-cavity Mold] Author(s): Sanchez-Castillo, L., Nedelcu, D.,Francisco-Marquez,
	Source: :blue[MATERIALE PLASTICE] Volume 58 Issue 3 Page 121-128 Published: Sep. :red[2021] 
	Web of Science Accession Number: WOS:000756838700003
	"""   )
	col2.link_button("View", "https://revmaterialeplastice.ro/pdf/12%20LESLIE%20SANCHEZ%203%2021.pdf")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		1.5. Article  Title: :green[Numerical Investigation of Nozzle Jet Flow in a Pelton Microturbine],  
		Author(s): Nedelcu, D., Cojocaru, V., Avasiloaie, RC., Source: :blue[MACHINES] Volume 9 Issue 8 
		Published: Aug. :red[2021] Web of Science Accession Number: WOS:000689390300001
	"""   )
	col2.link_button("View", "https://www.mdpi.com/2075-1702/9/8/158")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		1.6. Article  Title: :green[Analysis and Optimization of UAV Frame Design for Manufacturing
		from Thermoplastic Materials on FDM 3D Printer] Author(s): Palinkas, I., Pekez, J.,  
		Desnica, E., Rajic, A., Nedelcu, D., :blue[MATERIALE PLASTICE] , Volume: ‏58, Published: DEC :red[2021], 
		DOI10.37358/MP.21.4.5549, ISSN: 0025-5289, Web of Science Accession Number: WOS:WOS:000756908700002
	"""   )
	col2.link_button("View", "https://revmaterialeplastice.ro/pdf/25%20PALINKAS%204%2021.pdf")

	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		1.7. Article  Title: :green[A Multibody Inertial Propulsion Drive 
		with Symmetrically Placed Balls Rotating on Eccentric Trajectories],
		Author(s): Gerocs, A.,  Gillich, G.R., Nedelcu, D., Korka, Z.I.,
		:blue[SYMMETRY - BASEL], Volume: ‏12, Issue: ‏ 9,  Article Number: 1422, 
		Published: ‏ SEP :red[2020], Web of Science Accession Number: 
		WOS:000587588000001 
	"""   )
	col2.link_button("View", "https://www.mdpi.com/2073-8994/12/9/1422")

	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		1.8. Article  Title: :green[The Kinematic and Dynamic Study of an Inertial 
		Propulsion System Based on Rotating Masses], Gerocs, A., Korka, 
		Z.I., Biro, I., Nedelcu, D., :blue[ACTA POLYTECHNICA HUNGARICA], 
		Volume: ‏ 17, Issue: ‏ 6, Pages: ‏ 225-237, Published: :red[‏2020], 
		Web of Science Accession Number: WOS:000550576000013
	"""   )
	col2.link_button("View", "http://acta.uni-obuda.hu/Gerocs_Korka_Biro_Nedelcu_103.pdf")

	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		1.9. Article  Title: :green[3D Printing Technology with Plastic Materials 
		for Hip Implant Master Patterns Manufacturing] Author(s): 
		Rajic, A., Desnica, E., Palinkas, I., Nedelcu, D., 
		Vulicevic, Source: :blue[MATERIALE PLASTICE] Volume: 56  Issue: 4 Pages: 882-890
		Published: DEC :red[2019], Web of Science Accession Number: WOS:000509920700029
	"""   )
	col2.link_button("View", "https://revmaterialeplastice.ro/pdf/29%20RAJIC%204%2019.pdf")


	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		1.10. Article  Title: :green[Using of Polymers for Rapid Prototyping of an 
		Axial Microturbine Runner and Wicked Gates] Author(s): Nedelcu, D.,
		Cojocaru, V., Micu, LM., Florea, D., Hluscu, M, Source: :blue[MATERIALE 
		PLASTICE]  Volume: 56  Issue: 2  Pages: 454-459  Published: 
		JUN :red[2019], Web of Science Accession Number: WOS:000476641000033
	"""   )
	col2.link_button("View", "https://revmaterialeplastice.ro/pdf/NEDELCU%20D.pdf%204%2015.pdf")

	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		1.11. Article  Title: :green[The Effect of the Friction Coefficient and 
		the Pendulum Radius on the Behavior of Structures Isolated with 
		Simple Friction Pendulums] Author(s): Gillich, GR., Nedelcu, D., Malin,
		TC., Iancu, V., Hamat, CO., Gillich, N, Source: :blue[ROMANIAN JOURNAL 
		OF ACOUSTICS AND VIBRATION]  Volume: 15  Issue: 2  Pages: 130-135
		Published: :red[2018]  Web of Science Accession Number: WOS:000457418600008
	"""   )
	col2.link_button("View", "https://www.researchgate.net/publication/330512050_The_Effect_of_the_Friction_Coefficient_and_the_Pendulum_Radius_on_the_Behavior_of_Structures_Isolated_with_Simple_Friction_Pendulums")

	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		1.12. Article  Title: :green[A comparative Study Between the Costs of 
		Polymer Based Rapid Prototyping and Steel Based Manufacture] Author(s): 
		Nedelcu, D.,Bara, A., Pellac, A., Bogdan, SL, Source: :blue[MATERIALE PLASTICE]
		Volume: 54  Issue: 3  Pages: 443-446  Published: SEP :red[2017] 
		Web of Science Accession Number: WOS:000426412300008
	"""   )
	col2.link_button("View", "https://revmaterialeplastice.ro/pdf/8%20NEDELCU%20A%203%2017.pdf")

	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		1.13. Article  Title: :green[The Study of Contact Problems for Small 
		Rolling Bearings Manufactured of Plastic Material] Author(s): 
		Nedelcu, D., Manescu, T., Ursoniu, C., Avram, SR., Mimis, CM, 
		Source: :blue[MATERIALE PLASTICE]  Volume: 53  Issue: 4 Pages: 594-598
		Published: DEC :red[2016] Web of Science Accession Number: WOS:000395047100005
	"""   )
	col2.link_button("View", "https://revmaterialeplastice.ro/pdf/NEDELCU%20D%204%2016.pdf")

	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		1.14. Article  Title: :green[Considerations Regarding the Use of Polymers 
		for the Rapid Prototyping of the Hydraulic Turbine Runners 
		Designed for Experimental Research on the Model] Author(s): Nedelcu, D., C
		ojocaru, V., Ghican, A., Peris-Bendu, F,. Avasiloaie, R., Source: :blue[MATERIALE 
		PLASTICE]  Volume: 52  Issue: 4 Pages: 475-479 Published: DEC :red[2015] 
		Web of Science Accession Number: WOS:000368971900011
	"""   )
	col2.link_button("View", "https://revmaterialeplastice.ro/pdf/NEDELCU%20D.pdf%204%2015.pdf")

	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		1.15. Article  Title: :green[Failure analysis of a Ti-6Al-4V ultrasonic horn used 
		in cavitation erosion tests] Author(s): Nedelcu, D., Cojocaru, V., Nedeloni, M., 
		Peris-Bendu, F., Ghican, A., Source: :blue[MECHANIKA] Issue: 4 Pages: 272-276 DOI: 
		10.5755/j01.mech.21.3.10023 Published: :red[2015] Web of Science Accession Number: 
		WOS:000361845600003
	"""   )
	col2.link_button("View", "https://mechanika.ktu.lt/index.php/Mech/article/view/10023")

	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		1.16. Article  Title: :green[Numerical simulation and additive manufacturing 
		technology in design of knee implant patterns] Author(s): Rajic, A., Desnica, E.,
		Stojadinovic, S., Nedelcu, D., Source: :blue[JOURNAL OF OPTOELECTRONICS AND 
		ADVANCED MATERIALS]  Volume: 16 Issue: 9-10 Pages: 1180-1190 Published: SEP-OCT :red[2014]
		Web of Science Accession Number: WOS:000343844900030
	"""   )
	col2.link_button("View", "https://joam.inoe.ro/articles/numerical-simulation-and-additive-manufacturing-technology-in-design-of-knee-implant-patterns/fulltext")

	col1, col2 = st.columns([0.8,0.2])
	col1.write( """
		1.17. Article  Title: :green[Linear stress analysis on the cabin's framework of a mobile equipment] 
		Author(s): Manescu, TS., Nedelcu, D., Source: :blue[METALURGIA INTERNATIONAL]  Volume: 15  
		Issue: 3  Pages: 25-30  Published: MAR :red[2010]  Web of Science Accession Number: WOS:000274149300005
	"""   	)
	with col2:
		FCT_Down( current_dir / 'DOCS' / 'Art_MetInt_2010.pdf', "Article Download" )

	
	col1, col2 = st.columns([0.8,0.2])
	col1.write( """
		1.18. Article  Title: :green[SIMULATION OF THE KAPLAN ROTOR HUB CASTING AND COMPARISON WITH THE 
		EXPERIMENTAL RESULTS] Author(s): Marta, C., Suciu, L., Nedelcu, D., Source: :blue[METALURGIA INTERNATIONAL]
		Volume: 14  Issue: 10  Pages: 33-38  Published: :red[2009]  Web of Science Accession Number: WOS:000266190300006
	"""   	)
	with col2:
		FCT_Down( current_dir / 'DOCS' / 'Art_MetInt_2009.pdf', "Article Download" )

	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		1.19. Article  Title: :green[Considerations about using polymers in adaptive guardrails construction] 
		Author(s): Nedelcu, D., Gillich, GR., Cziple, F., Ciuca, I., Padurean, Source: :blue[MATERIALE PLASTICE]
		Volume: 45  Issue: 1  Pages: 47-52  Published: MAR :red[2008]  Web of Science Accession Number: 
		WOS:000255295400010
	"""   	)
	col2.link_button("View", "https://revmaterialeplastice.ro/pdf/NEDELCU%20D..pdf")
	
	col1, col2 = st.columns([0.8,0.2])
	col1.write( """
		1.20. Article  Title: :green[About cavitation erosion resistance of the austenitic stainless steel 
		heat treated] Author(s): Padurean, L., Trusculescu, M., Arpad, F., Nedelcu, D., Padurean, E., 
		Source: :blue[METALURGIA INTERNATIONAL]  Volume: 13  Issue: 9  Pages: 23-26  Published: :red[2008]  
		Web of Science Accession Number: WOS:000258493500005
	"""   	)
	with col2:
		FCT_Down( current_dir / 'DOCS' / 'Art_MetInt3_2008.pdf', "Article Download" )

	
	col1, col2 = st.columns([0.8,0.2])
	col1.write( """
		1.21. Article  Title: :green[Cavitation erosion resistance of the austenitic stainless steel 
		from welding reconditioned hydraulic turbines blades zones] Author(s): D. Padurean, D. Nedelcu,
		E. Padurean, Fay, A., Marin, T., Source: :blue[METALURGIA INTERNATIONAL]  Volume: 13  Issue: 6
		Pages: 26-31  Published: :red[2008]  Web of Science Accession Number: WOS:000256691800006
	"""   	)
	with col2:
		FCT_Down( current_dir / 'DOCS' / 'Art_MetInt2_2008.pdf', "Article Download" )

	col1, col2 = st.columns([0.8,0.2])
	col1.write( """
		1.22. Article  Title: :green[Researches upon cavitation erosion resistance of martensitic 
		stainless steel used for moulding Kaplan and Francis turbines runner blades] Author(s): 
		I. Padurean., D. Nedelcu, E. Padurean, A. Fay, T. Marin, Source: :blue[METALURGIA INTERNATIONAL]
		Volume: 13  Issue: 5  Pages: 34-40  Published: :red[2008]   Accession Number: WOS:000256691600006
	"""   	)
	with col2:
		FCT_Down( current_dir / 'DOCS' / 'Art_MetInt1_2008.pdf', "Article Download" )
	
	col1, col2 = st.columns([0.8,0.2])
	col1.write( """
		1.23. Article  Title: :green[About cavitation erosion resistance of the martensitic stainless 
		steel from zones reconditioned by welding] Author(s): Padurean, I., Trusculescu, M.,
		Arpad, F., Nedelcu, D., Padurean, E., Source: :blue[METALURGIA INTERNATIONAL]
		Volume: 13  Issue: 10  Pages: 60-66  Published: :red[2008]  Accession Number: WOS:000258493600012
	"""   	)
	with col2:
		FCT_Down( current_dir / 'DOCS' / 'Art_MetInt4_2008.pdf', "Article Download" )

	
	col1, col2 = st.columns([0.9,0.2])
	col1.write( """
		1.24. Article  Title: :green[Numerical study of the local stress for a circular fillet corner]
		Author(s): Dorian, N. Source: :blue[METALURGIA INTERNATIONAL]  Volume: 12  Issue: 3  
		Pages: 30-36  Published: :red[2007]  Accession Number: WOS:000255786000004
	"""   	)
	with col2:
		FCT_Down( current_dir / 'DOCS' / 'Art_MetInt_2007.pdf', "Article Download" )

	

	# ==================================================================================

	st.write("---")
	st.subheader(":gray[11 x Proceedings Paper published articles indexed in the Web of Science]")  

	col1, col2 = st.columns([0.9,0.1])
	col1.write( """	
		2.1. Proceedings Paper  Title: :green[The Reverse Engineering technique performed on a Francis 
		Runner Geometry through Photogrammetry] Author(s): Bogdan, SL., Nedelcu, D.,Padurean, I.,
		Source: INTERNATIONAL CONFERENCE ON APPLIED SCIENCES  Book Series: 
		IOP Conference Series-Materials Science and Engineering, Volume: 477  Article Number: 012021, 
		DOI:10.1088/1757-899X/477/1/012021  Published: :red[2019]  Web of Science Accession Number: WOS:000461184100021
	"""   )
	col2.link_button("View", "https://iopscience.iop.org/article/10.1088/1757-899X/477/1/012021/pdf")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """	
		2.2. Proceedings Paper  Title: :green[Innovative natural rubber bearing 
		for earthquake isolation] Author(s): Iancu, V., Nedelcu, D. Source: 
		:blue[INTERNATIONAL CONFERENCE ON APPLIED SCIENCES]  Book Series: 
		IOP Conference Series-Materials Science and Engineering
		Volume: 477  Article Number: 012022 DOI: 10.1088/1757-899X/477/1/012022
		Published: :red[2019], Web of Science Accession Number: WOS:000461184100022
	"""   )
	col2.link_button("View", "https://iopscience.iop.org/article/10.1088/1757-899X/477/1/012022/pdf")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		2.3. Proceedings Paper Title: :green[The calculation of the Kaplan Turbine 
		Hill Chart using the HydroHillChart software] Author(s): Nedelcu, D., 
		Padurean, I., Bostan, A. Source: :blue[INTERNATIONAL CONFERENCE ON APPLIED 
		SCIENCES]  Book Series: IOP Conference Series-Materials Science and 
		Engineering, Volume: 477, Article Number: 012023, 
		DOI: 10.1088/1757-899X/477/1/012023, Published: :red[2019], 
		Web of Science Accession Number: WOS:000461184100023
	"""   )
	col2.link_button("View", "https://iopscience.iop.org/article/10.1088/1757-899X/477/1/012023/pdf")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		2.4. Proceedings Paper Title: :green[Comparative analysis of stress state 
		and fatigue behaviour of two types of welded joints used for 
		a HEM-beams structure] Author(s): Ene, T., Nedelcu, D., Cojocaru, V., 
		Vela, DG, Source: :blue[8TH INTERNATIONAL CONFERENCE ON ADVANCED CONCEPTS 
		IN MECHANICAL ENGINEERING]  Book Series: IOP Conference Series-Materials 
		Science and Engineering  Volume: 444  Article Number: 062008 
		DOI: 10.1088/1757-899X/444/6/062008  Published: :red[2018], 
		Web of Science Accession Number: WOS:000467443600095
	"""   )
	col2.link_button("View", "https://iopscience.iop.org/article/10.1088/1757-899X/444/6/062008/pdf")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		2.5. Proceedings Paper  Title: :green[Static, dynamic and fatigue analysis 
		of a railway bridge with pedestrian area] Author(s): Ene, T., Cojocaru, V., 
		Nedelcu, D, Source: :blue[8TH INTERNATIONAL CONFERENCE ON ADVANCED CONCEPTS 
		IN MECHANICAL ENGINEERING]  Book Series: IOP Conference Series-Materials 
		Science and Engineering  Volume: 444  Article Number: 062009 
		DOI: 10.1088/1757-899X/444/6/062009  Published: :red[2018]  Web of Science 
		Accession Number: WOS:000467443600096
	"""   )
	col2.link_button("View", "https://www.researchgate.net/publication/329303468_Static_dynamic_and_fatigue_analysis_of_a_railway_bridge_with_pedestrian_area")
	

	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		2.6. Proceedings Paper Title: :green[Cavitation Erosion Research on the X3CrNi13-4 
		Stainless Steel] Author(s): Nedelcu, D., Nedeloni, MD., Lupinca, CI., Source: 
		:blue[METALLOGRAPHY XV  Book Series: Materials Science Forum]  Volume: 782
		Pages: 263-+  DOI: 10.4028/www.scientific.net/MSF.782.263
		Published: :red[2014]  Web of Science Accession Number: WOS:000338978600047
	"""   )
	col2.link_button("View", "https://www.researchgate.net/publication/272067662_Cavitation_Erosion_Research_on_the_X3CrNi13-4_Stainless_Steel")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		2.7. Proceedings Paper Title: :green[Gray Cast Iron Behaviour in Cavitation Erosion]
		Author(s): Lupinca, CI., Nedeloni, MD., Nedelcu, D.,Edited by: Longauerova M., 
		Zubko P., Source: :blue[METALLOGRAPHY XV Book Series: Materials Science Forum], Volume: 782
		Pages: 269-+ Published: :red[2014] DOI: 10.4028/ www.scientific.net/MSF.782.269
		Web of Science Accession Number: WOS:000338978600048
	"""   )
	col2.link_button("View", "https://www.scientific.net/MSF.782.269")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		2.8. Proceedings Paper Title: :green[Hydrodynamics automatic optimization of runner 
		blades for reaction hydraulic turbines], Author(s): Balint, D., Campian, V., Nedelcu, D.,
		Megheles, O.,Edited by: Wu Y; Wang Z; Liu S; Yuan S; Luo X; Wang F Source: 
		:blue[26TH IAHR SYMPOSIUM ON HYDRAULIC MACHINERY AND SYSTEMS, PTS 1-7 
		Book Series]: IOP Conference Series-Earth and Environmental Science 
		Volume: 15  Article Number: 032014  DOI: 10.1088/1755-1315/15/3/032014 
		Published: :red[2013]  Web of Science Accession Number: WOS:000324782300044
	"""   	)
	col2.link_button("View", "https://iopscience.iop.org/article/10.1088/1755-1315/15/3/032014/pdf")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		2.9. Proceedings Paper Title: :green[Failure Analysis of a Kaplan Turbine Runner Blade by 
		Metallographic and Numerical Methods] Author(s): Frunzaverde, D., Campian, V., Nedelcu, D., 
		Gillich, GR., Marginean, G., Source: :blue[CONTINUUM MECHANICS, FLUIDS, HEAT  Book Series: 
		WSEAS Mechanical Engineering Series]  Pages: 60-+  Published: :red[2010]  
		Web of Science Accession Number: WOS:000276890300007
	"""   	)
	col2.link_button("View", "https://www.academia.edu/15057817/Failure_analysis_of_a_Kaplan_turbine_runner_blade_by_metallographic_and_numerical_methods")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		2.10. Proceedings Paper Title: :green[Stress concentration factors for pin lever of runner 
		blade mechanism from Kaplan turbines] Author(s): Pittner, AM., Campian, CV., Nedelcu, D.,
		Frunzaverde, D., Cojocaru, V., Source: :blue[LATEST TRENDS ON ENGINEERING MECHANICS, 
		TRUCTURES, ENGINEERING GEOLOGY Book Series: Mathematics and Computers in Science and Engineering] 
		Pages: 181-+  Published: red[2010]  Web of Science Accession Number: WOS:000288686900034
	"""   	)
	col2.link_button("View", "https://www.academia.edu/68587575/Stress_concentration_factors_for_pin_lever_of_runner_blade_mechanism_from_Kaplan_turbines?uc-sb-sw=11922614")
		
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		2.11. Proceedings Paper Title: :green[DYNAMIC ANALYSIS OF THE DOUBLE HARMONIC TRANSMISSION (DHT)]
		Author(s): Ianici, D., Nedelcu, D., Ianici, S., Coman, L., Source: :blue[SIXTH INTERNATIONAL 
		SYMPOSIUM ABOUT FORMING AND DESIGN IN MECHANICAL ENGINEERING] Pages: 155-158 Published: :red[2010]
		Web of Science Accession Number: WOS:000397473500026
	"""   	)
	col2.link_button("View", "https://www.researchgate.net/profile/Sava-Ianici/publication/291136956_Dynamic_analysis_of_the_Double_Harmonic_Transmission/links/569e37d308ae00e5c99199f4/Dynamic-analysis-of-the-Double-Harmonic-Transmission.pdf")
			
	st.write("---")
	st.subheader(":gray[115 x Published articles between 2023-2002 included in Conferences,Journals & Databases]")  
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.1. Article  Title: :green[USING STREAMLIT AND BASIC4ANDROID (B4A) TO CREATE THE SAME APPLICATION – B4A VERSION]
		Author(s): D Nedelcu, T Latinovic, L Sikman, Mladen TODIC, Aleksandar MAJSTOROVIC, Source: :blue[ACTA TECHNICA CORVINIENSIS – Bulletin of Engineering], 
		e–ISSN: 2067 – 3809, Tome XVII, Published: OCT :red[2024]
	"""   )
	col2.link_button("View", "https://acta.fih.upt.ro/pdf/2024-4/ACTA-2024-4-15.pdf")

	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.2. Article  Title: :green[USING STREAMLIT AND BASIC4ANDROID (B4A) TO CREATE THE SAME APPLICATION – STREAMLIT VERSION]
		Author(s): D Nedelcu, T Latinovic, L Sikman, Mladen TODIC, Aleksandar MAJSTOROVIC, Source: :blue[ANNALS of Faculty Engineering Hunedoara – INTERNATIONAL JOURNAL OF ENGINEERING], 
		Tome XXII, Fascicule 4,Published: NOV :red[2024]
	"""   )
	col2.link_button("View", "https://acta.fih.upt.ro/pdf/2024-4/ACTA-2024-4-15.pdf")

	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.3. Article  Title: :green[PyDigitizer–A Python module for digitizing 2D curves]
		Author(s): D Nedelcu, T Latinovic, L Sikman, Source: :blue[Journal of Physics: Conference Series]
		Volume: 2540  Issue: 1 Pages: 012015 Published: IUL :red[2023]
	"""   )
	col2.link_button("View", "https://iopscience.iop.org/article/10.1088/1742-6596/2540/1/012015/pdf")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.4. Article  Title: :green[Numerical investigation of the stress state in the runner
		hub of a Kaplan turbine] Author(s): V. Cojocaru, C-O Miclosina*, C. V. Campian, 
		D. Frunzaverde, D. Nedelcu Source: :blue[IOP Conference Series: Materials Science and Engineering]
		Volume: 1262,  Issue: 1, Pages: 012046, Published: OCT :red[2022]
	"""   )
	col2.link_button("View", "https://iopscience.iop.org/article/10.1088/1757-899X/1262/1/012046/pdf")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.5. Article  Title: :green[Study on the Behavior of the Isolated Structures with Friction Pendulums
		and a Counterweight], Author(s): Tatian-Cristian Malin, Gilbert-Rainer Gillich, Dorian Nedelcu
		Source: :blue[Acoustics and Vibration of Mechanical Structures–AVMS-2021]: Proceedings of the 16th 
		AVMS, Timişoara, Romania, May 28-29, 2021, Pages: 364-371 Published: :red[2022]
	"""   )
	col2.link_button("View", "https://link.springer.com/chapter/10.1007/978-3-030-96787-1_39")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.6. Article  Title: :green[STRENGTH CALCULATIONS PERFORMED ON THE SPIRAL CASING OF A FRANCIS 
		TURBINE OPERATING IN SECONDARY CONTROL REGIME], Author(s): E. Birtarescu, VC. Campian, D. Nedelcu,
		Source: :blue[U.P.B. Sci. Bulletin], Series D, Vol. 83, Iss. 2, ISSN 1454-2358
		Published: :red[2021]
	"""   )
	col2.link_button("View", "https://www.scientificbulletin.upb.ro/rev_docs_arhiva/full826_198598.pdf")

	col1, col2 = st.columns([0.8,0.2])
	col1.write( """
		3.7. Article Title: :green[A MOTION STUDY OF THE QUADRILATERAL PLANE MECHANISM WITH SOLIDWORKS], , Authors: 
		D. Nedelcu, C. Hatiegan, N. Gillich, MM. Pop, Source: :blue[The 9th International Conference on Computational 
		Mechanics and Virtual Engineering COMEC 2021], Brașov, ROMANIA, 21-23 October, :red[2021]
	"""   )
	with col2:
		FCT_Down( current_dir / 'DOCS' / 'Art_COMEC 2021.pdf', "Article Download" )	

	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.8. Article  Title: :green[Displacement and velocity estimation of the earthquake response signals 
		measured with accelerometers], Author(s): D Nedelcu, T C Malin, G R Gillich, C I Barbinta, V Iancu,
		Source: :blue[IOP Conf. Series: Materials Science and Engineering], 997, 012051 IOP Publishing
		doi:10.1088/1757-899X/997/1/012051 Published: :red[2020]
	"""   )
	col2.link_button("View", "https://iopscience.iop.org/article/10.1088/1757-899X/997/1/012051/pdf")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.9. Article  Title: :green[Development of an inertial propulsion drive by using Motion
		Simulation], Author(s): A. Gerocs, ZI. Korka, D. Nedelcu, G R Gillich, Source: 
		:blue[IOP Conf. Series: Materials Science and Engineering], 997, 012043 IOP Publishing
		doi:10.1088/1757-899X/997/1/012043  Published: :red[2020]
	"""   )
	col2.link_button("View", "https://iopscience.iop.org/article/10.1088/1757-899X/997/1/012043/pdf")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.10. Article  Title: :green[Deriving patterns for the vibration-based damage detection in
		side frames of bogies], Author(s): CI. Barbinta, G R Gillich, D. Nedelcu, T. Manescu, Source: 
		:blue[IOP Conf. Series: Materials Science and Engineering], 997, 012035 IOP Publishing
		doi:10.1088/1757-899X/997/1/012035  Published: :red[2020]
	"""   )
	col2.link_button("View", "https://iopscience.iop.org/article/10.1088/1757-899X/997/1/012035/pdf")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.11. Article  Title: :green[A new predictive model to estimate the frequencies for beams with 
		branched cracks], Author(s): C. Tufisi, GR. Gillich, CI. Barbinta, D. Nedelcu, CO. Hamat,
		Source: :blue[IOP Conf. Series: Materials Science and Engineering], 997, 012063 IOP Publishing
		doi:10.1088/1757-899X/997/1/012063  Published: :red[2020]
	"""   )
	col2.link_button("View", "https://iopscience.iop.org/article/10.1088/1757-899X/997/1/012063/pdf")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.12. Article  Title: :green[A Python application to generate digital signals], Author(s): 
		TC. Malin, GR. Gillich, D. Nedelcu, Source: :blue[STUDIA UNIVERSITATIS BABEȘ-BOLYAI], 
		Engineering 65(1) 2020, doi:10.24193/subbeng.2020.1.10  Published: :red[2020]
	"""   )
	col2.link_button("View", "https://www.academia.edu/44609795/A_Python_application_to_generate_digital_signals")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.13. Article  Title: :green[A Python application to calculate the mode shapes of rectangular plates], 
		Author(s): D. Nedelcu, CI. Barbinta, GR. Gillich, ZI. Korka, C. Hatiegan,
		Source: :blue[Vibroengineering PROCEDIA], Vol.33, pp. 66-71
		doi.org:10.2/vp2020.217191595  Published: :red[2020]
	"""   )
	col2.link_button("View", "https://www.extrica.com/article/21719")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.14. Proceedings Paper  Title: :green[Exact solution for the severity of transverse cracks in prismatic beams]
		Authors: Tufisi, C., Gillich, GR., Hamat, CO., Biro, I., Gillich, N., Nedelcu, D., Source: :blue[INTERNATIONAL 
		CONFERENCE ON APPLIED SCIENCES (ICAS)  Book Series: Journal of Physics Conference Series] Volume: 1426 
		Article Number: 012023 DOI: 10.1088/1742-6596/1426/1/012023 Published: :red[2020] Location: 
		Engn Fac Hunedoara, Hunedoara, ROMANIA, Date: MAY 09-11, 2019 
	"""   )
	col2.link_button("View", "https://iopscience.iop.org/article/10.1088/1742-6596/1426/1/012023/pdf")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.15. Proceedings Paper  Title: :green[About the calculus of the relative frequency shifts for a 
		beam with multiple cracks] Authors: Gillich, GR., Nedelcu, D., Hamat, CO., Wahab, MA., 
		Barbinta, CI., Source: :blue[INTERNATIONAL CONFERENCE ON APPLIED SCIENCES (ICAS)  Book Series: 
		Journal of Physics Conference Series] Volume: 1426 Article Number: 012024 DOI: 
		10.1088/1742-6596/1426/1/012024 Published: :red[2020] Location: 
	Engn Fac Hunedoara, Hunedoara, ROMANIA, Date: MAY 09-11, 2019 
	"""   )
	col2.link_button("View", "https://iopscience.iop.org/article/10.1088/1742-6596/1426/1/012024/pdf")
		
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.16. Proceedings Paper  Title: :green[The kinematic and kinetostatic study of the shaker mechanism 
		with SolidWorks Motion] Authors: Nedelcu, D., Gillich, GR., Bloju, A., Padurean, I., Source: 
		:blue[INTERNATIONAL CONFERENCE ON APPLIED SCIENCES (ICAS)  Book Series: Journal of Physics 
		Conference Series], Volume: 1426, Article Number: 012025, DOI: 10.1088/1742-6596/1426/1/012025, 
		Published: :red[2020] Location: Engn Fac Hunedoara, Hunedoara, ROMANIA, Date: MAY 09-11, 2019
	"""   )
	col2.link_button("View", "https://www.academia.edu/88259202/The_kinematic_and_kinetostatic_study_of_the_shaker_mechanism_with_SolidWorks_Motion")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.17. Proceedings Paper  Title: :green[A comparative study between photogrammetry and laser 
		technology applied on model turbine blades] Authors: Nedelcu, D., Gillich, GR., Gerocs, A., 
		Padurean, I., Source: :blue[INTERNATIONAL CONFERENCE ON APPLIED SCIENCES (ICAS)  
		Book Series: Journal of Physics Conference Series], Volume: 1426 Article Number: 012026
		DOI: 10.1088/1742-6596/1426/1/012026, Published: :red[2020] Location: Engn Fac Hunedoara, 
		Hunedoara, ROMANIA, Date: MAY 09-11, 2019 
	"""   )
	col2.link_button("View", "https://iopscience.iop.org/article/10.1088/1742-6596/1426/1/012026/pdf")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.18. Proceedings Paper  Title: :green[A new mathematical model for cracked beams with uncertain 
		boundary conditions] Authors: Gillich, GR., Nedelcu, D., Wahab, MA., Pop, MV., Hamat, CO., 
		Source: :blue[PROCEEDINGS OF INTERNATIONAL CONFERENCE ON NOISE AND VIBRATION ENGINEERING 
		(ISMA2020) / INTERNATIONAL CONFERENCE ON UNCERTAINTY IN STRUCTURAL DYNAMICS (USD2020)],
		Pages: 3871-3883 , Published: :red[2020] Location: Leuven, BELGIUM, Date: SEP 07-09, 2020 
	"""   )
	col2.link_button("View", "https://past.isma-isaac.be/downloads/isma2020/proceedings/Contribution_157_proceeding_3.pdf")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.19. Article Title: :green[Assessing multiple cracks in beams by a method based on the damage location coefficients]
		 Authors: Gillich, G.-R., Aman, A.T., Nedelcu, D., Hamat, C.O., Manescu, T. Source: :blue[Vibroengineering Procedia 
		23(3):49-54, DOI:10.21595/vp.2019.20661, Published: :red[2019]
	"""   )
	col2.link_button("View", "https://web.archive.org/web/20200306225844id_/https://www.jvejournals.com/article/20661/pdf")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.20. Article Title: :green[A comparative study about some application packages used in Photogrammetry],
		Authors: D. Nedelcu1, G-R Gillich, C. Malin-Tatian, Source: :blue[IOP Conference Series: Materials 
		Science and Engineering 564 (1), 012054, doi:10.1088/1757-899X/564/1/012054, Published: :red[2019]
	"""   )
	col2.link_button("View", "https://iopscience.iop.org/article/10.1088/1757-899X/564/1/012054/pdf")

	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.21. Article Title: :green[A versatile algorithm for estimating natural frequencies with high accuracy]
		Authors: Gilbert-Rainer Gillich, Dorian Nedelcu, Constantin-Ioan Barbinta, Nicoleta Gillich, 
		DOI doi.org/10.21595/vp.2019.20946, Source: :blue[Vibroengineering PROCEDIA] 27, 37-42, 
		Published: :red[2019]
	"""   )
	col2.link_button("View", "https://www.extrica.com/article/20946/pdf")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.22. Article Title: :green[Sensitivity analysis for frequency-based prediction of cracks in open 
		cross-section beams], Authors: Barbinta, Constantin-Ioan, Tufisi, Cristian, Hamat, Codruta Oana,
		Nedelcu, Dorian, Gillich, Gilbert-Rainer, Source: :blue[Vibroengineering Procedia], 2019, Vol 27, p7, 
		ISSN 2345-0533, DOI 10.21595/vp.2019.20969, Published: :red[2019]
	"""   )
	col2.link_button("View", "https://www.extrica.com/article/20969")

	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.23. Article Title: :green[The study of the punching cards mechanism with SolidWorks Motion],  
		Authors: Dorian Nedelcu, Gilbert-Rainer Gillich, Istvan Biro, Zoltan-Iosif, Korka, Attila Gerocs,
		Source: :blue[Analele Universitatii'Eftimie Murgu'], 26 (1), ANUL XXVI, no.1, 2019, ISSN 1453 - 7397,
		Published: :red[2019]
	"""   )
	col2.link_button("View", "http://anale-ing.uem.ro/2019/23.pdf")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.24. Article Title: :green[Earthquake registration databases], Authors: Tatian-Cristian Mălin, 
		Gilbert-Rainer Gillich, Dorian Nedelcu, Source: :blue[Analele Universitatii'Eftimie Murgu'],
		ANUL XXVI, no. 1, 2019, ISSN 1453 - 7397, Published: :red[2019]
	"""   )
	col2.link_button("View", "https://www.academia.edu/80785518/Earthquake_registration_databases")

	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.25. Article Title: :green[Efficient algorithm for frequency estimation used in structural 
		damage detection], Authors: Gilbert-Rainer Gillich, Dorian Nedelcu, Cristian-Tatian Malin, 
		Istvan Biro, M. Abdel Wahab, Source: :blue[	Proceedings of the 13th International Conference on 
		Damage Assessment of Structures], DAMAS 2019, 9-10 July 2019, Porto, Portugal, Published: :red[2019]
	"""   )
	col2.link_button("View", "https://www.researchgate.net/publication/334261324_Efficient_Algorithm_for_Frequency_Estimation_Used_in_Structural_Damage_Detection")

	col1, col2 = st.columns([0.8,0.2])
	col1.write( """
		3.26. Article Title: :green[ACCURACY OF FREQUENCY EVALUATION PERFORMED WITH THE PySINC SOFTWARE],
		Authors: Gilbert-Rainer Gillich	Dorian Nedelcu, Nicoleta Gillich, Source: :blue[The 8th International 
		Conference on Computational Mechanics and Virtual Engineering COMEC 2019], ICMS 2019 & COMEC 2019	
		2019-11-21...2020-01-22, Brasov, Published: :red[2019]
	"""   )
	with col2:
		FCT_Down( current_dir / 'DOCS' / 'Art_COMEC 2019a.pdf', "Article Download" )

	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.27. Article Title: :green[AN ALGORITHM TO FIND THE TWO SPECTRAL LINES ON THE MAIN LOBE OF A DFT],
		Authors: Gilbert-Rainer Gillich,	Dorian Nedelcu, Andrea Amalia Minda, David Lupu, Source: :blue[	The 8th 
		International Conference on Computational Mechanics and Virtual Engineering COMEC 2019],
		ICMS 2019 & COMEC 2019	2019-11-21...2019-11-22, Brasov, Published: :red[2019]
	"""   )
	col2.link_button("View", "https://www.researchgate.net/publication/337704894_AN_ALGORITHM_TO_FIND_THE_TWO_SPECTRAL_LINES_ON_THE_MAIN_LOBE_OF_A_DFT")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.28. Article Title: :green[DIGITIZATION OF EARTHQUAKE SIGNALS STORED AS IMAGES], Authors: Tatian-Cristian Malin, 
		Gilbert-Rainer Gillich, Dorian Nedelcu, Vasile Iancu, Source: :blue[The 8th International Conference on Computational 
		Mechanics and Virtual Engineering COMEC 2019] ICMS 2019 & COMEC 2019, 2019-11-21...2019-11-22, Brasov, Published: :red[2019]
	"""   )
	col2.link_button("View", "https://www.researchgate.net/publication/337705114_DIGITIZATION_OF_EARTHQUAKE_SIGNALS_STORED_AS_IMAGES")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.29. Article Title: :green[APPRAISING THE ACCURACY OF A NOVEL MODEL FOR L-SHAPED CRACKS], Authors: Cristian Tufisi,
		Dorian Nedelcu, Gilbert-Rainer Gillich, Source: :blue[The 8th International Conference on Computational Mechanics 
		and Virtual Engineering COMEC 2019], ICMS 2019 & COMEC 2019	2019-11-21...2019-11-22, Brasov, Published: :red[2019]
	"""   )
	col2.link_button("View", "https://www.researchgate.net/publication/337705115_APPRAISING_THE_ACCURACY_OF_A_NOVEL_MODEL_FOR_L-_SHAPED_CRACKS")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.30. Article Title: :green[Comparison of the performance of friction pendulums with uniform and variable radii], 
		Authors: CT. Malin, D.Nedelcu, GR. Gillich, A. Petrica, I. Padurean Source: :blue[VIBROENGINEERING PROCEDIA],
		APRIL 2019, VOLUME 23 Published: :red[2019]
	
	"""   )
	col2.link_button("View", "https://web.archive.org/web/20200306225434id_/https://www.jvejournals.com/article/20667/pdf")
	
	col1, col2 = st.columns([0.8,0.2])
	col1.write( """
		3.31. Article Title: :green[SELF-MANAGEMENT OF MACHINES IN SMART FACTORIES VIA ADVANCED ALGORITHMS], Authors: Gillich, 
		Edwald-Viktor; Nedelcu, Doian; Popescu, Cristinel, Source: :blue[Annals of 'Constantin Brancusi' University of Targu-Jiu. 
		Engineering Series], Seria Inginerie, 2019, Issue 1, p65, ISSN 1842-4856, Published: :red[2019]
	"""   )
	with col2:
		FCT_Down( current_dir / 'DOCS' / 'Art_Tg_Jiu_2019.pdf', "Article Download" )	

	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.32. Article Title: :green[The reverse engineering of a blade runner geometry through photogrammetry], 
		Authors: D.Nedelcu, SL. Bogdan,  I. Padurean Source: :blue[IOP Conf. Series: Materials Science and Engineering],
		393 (2018) 012126,  doi:10.1088/1757-899X/393/1/012126  Published: :red[2018]
	
	"""   )
	col2.link_button("View", "https://iopscience.iop.org/article/10.1088/1757-899X/393/1/012126/pdf")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.33. Article Title: :green[Determining the geometric parameters of a blade runner that has a geometry 
		obtained through the photogrammetry technique], Authors: SL. Bogdan, D.Nedelcu, I. Padurean 
		Source: :blue[IOP Conf. Series: Materials Science and Engineering], 393 (2018) 012127,  
		doi:10.1088/1757-899X/393/1/012127  Published: :red[2018]
	"""   )
	col2.link_button("View", "https://iopscience.iop.org/article/10.1088/1757-899X/393/1/012127/pdf")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.34. Article Title: :green[General aspects of speed  increaser gearboxes], Authors: A. Bara, 
		D.Nedelcu, C. Hatiegan, AC. Bejenariu, L.Nedeloni Source: :blue[IOP Conf. Series: Materials 
		Science and Engineering], 294, (2018), 012032  doi:10.1088/1757-899X/294/1/012032   
		Published: :red[2017]
	"""   )
	col2.link_button("View", "https://iopscience.iop.org/article/10.1088/1757-899X/294/1/012032/pdf")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.35. Article Title: :green[Optimizing the Geometry of a LHy-M Hybrid Locomotive’s Chassis 
		by Resistance Calculations], Authors: A. Bara, D.Nedelcu, Corneliu Dica,  Source: 
		:blue[ANALELE UNIVERSITĂŢII “EFTIMIE MURGU” REŞIŢA], ANUL XXV, no. 2, 2018, ISSN 1453 - 7397   
		Published: :red[2018]
	"""   )
	col2.link_button("View", "http://anale-ing.uem.ro/2018/3.pdf")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.36. Article Title: :green[Thermal Calculation of the Reduction Gear 2XAB/StCu110So as 
		Part of Hybrid Locomotive’s LHy-M Mechanical Transmission], Authors: Aurel Băra, Dorian 
		Nedelcu, Corneliu Dica, Source: :blue[ANALELE UNIVERSITĂŢII “EFTIMIE MURGU” REŞIŢA], 
		ANUL XXV, no. 2, 2018, ISSN 1453 - 7397, Published: :red[2018]
	"""   )
	col2.link_button("View", "http://anale-ing.uem.ro/2018/4.pdf")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.37. Article Title: :green[THE REVERSE ENGINEERING OF A PELTON BUCKET BY PHOTOGRAMMETRY], 
		Authors: Sorin-Laurenţiu BOGDAN, Dorian NEDELCU, Ioan PĂDUREAN, Source: :blue[Proceedings 
		of 2018 International Conference on Hydraulics and Pneumatics - HERVEX], ISSN 1454 - 8003,
		November 7-9, Băile Govora, Romania, Published: :red[2018]
	"""   )
	col2.link_button("View", "https://fluidas.ro/hervex/proceedings2018/24-31.pdf")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.38. Article Title: :green[STUDY ON THE EFFECT OF A SIMPLE FRICTION PENDULUM RADIUS ON THE 
		RESPONSE OF ISOLATED STRUCTURES], Authors: Dorian Nedelcu, Gilbert-Rainer Gillich, Vasile 
		Iancu, Cristian-Tatian Mălin, Source: :blue[The 42th International Conference on “Mechanics 
		of Solids, Acoustics and Vibrations” – ICMSAV 2018], Brașov, ROMANIA, 25- 26 October, 
		Published: :red[2018]
	"""   )
	col2.link_button("View", "http://aspeckt.unitbv.ro/jspui/bitstream/123456789/2310/1/35%20Nedelcu%20paper%20COMAT%202018%20Brasov.pdf")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.39. Article Title: :green[EFFECT OF THE ORIENTATION OF AN OBLIQUE CRACK BRANCHES ON THE 
		BEAM EIGENFREQUENCIES], Authors: Cristian Tufisi, Gilbert-Rainer Gillich, Dorian Nedelcu, 
		Source: :blue[The 42th International Conference on “Mechanics of Solids, Acoustics and 
		Vibrations” – ICMSAV 2018], Brașov, ROMANIA, 25- 26 October, Published: :red[2018]
	"""   )
	col2.link_button("View", "http://aspeckt.unitbv.ro/jspui/bitstream/123456789/2294/1/19%20TUFISI%20paper%20COMAT%202018%20Brasov.pdf")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.40. Article Title: :green[Numerical study on complex shaped cracks in cantilever beams 
		concerning frequency and stiffness changes], Authors: Cristian Tufisi, Gilbert-Rainer Gillich, 
		Dorian Nedelcu, Codruta-Oana Hamat, Source: :blue[33rd International Conference on VIBROENGINEERING], 
		24-26th September, 2018 in Zittau, Germany, Published: :red[2018]
	"""   )
	col2.link_button("View", "https://www.extrica.com/article/20123")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.41. Article Title: :green[Study on the effect of the friction coefficient on the
		response of structures isolated with friction pendulums], Authors: Dorian Nedelcu, 
		Vasile Iancu, Gilbert-Rainer Gillich, Sorin Laurentiu Bogdan, Source: :blue[33rd 
		International Conference on VIBROENGINEERING], 24-26th September, 2018 in Zittau, 
		Germany, Published: :red[2018]
	"""   )
	col2.link_button("View", "https://www.extrica.com/article/20152/pdf")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.42. Article Title: :green[A procedure for an accurate estimation of the natural 
		frequencies of structures], Authors: Gilbert-Rainer Gillich, Ion Cornel Mituletu,
		Dorian Nedelcu, Codruta Oana Hamat, Source: :blue[33rd 	International Conference 
		on VIBROENGINEERING], 24-26th September, 2018 in Zittau, Germany, Published: :red[2018]
	"""   )
	col2.link_button("View", "https://www.extrica.com/article/20153")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.43. Article Title: :green[The Structural Analysis of the Classic Constructive Solution of a 
		Bridge Deck with a Railroad – Part I], Authors: T. Ene, D.Nedelcu, Source: :blue[
		ANALELE UNIVERSITĂŢII “EFTIMIE MURGU” REŞIŢA], ANUL XXIV, no. 1, 2017, ISSN 1453 - 7397,
		Published: :red[2017]
	"""   )
	col2.link_button("View", "http://anale-ing.uem.ro/2017/12.pdf")
	
	col1, col2 = st.columns([0.8,0.2])
	col1.write( """
		3.44. Article Title: :green[The improvement of the classic constructive solution of a bridge 
		deck with a railroad – Part II], Authors: T. Ene, D.Nedelcu, Source: :blue[
		ANALELE UNIVERSITĂŢII “EFTIMIE MURGU” REŞIŢA], ANUL XXIV, no. 1, 2017, ISSN 1453 - 7397,
		Published: :red[2017]
	"""   )
	with col2:
		FCT_Down( current_dir / 'DOCS' / 'Art_SysStruc 2017.pdf', "Article Download" )
	
	col1, col2 = st.columns([0.8,0.2])
	col1.write( """
		3.45. Article Title: :green[Sustainable development and CAD], Authors: A. Rajic, D.Nedelcu, 
		Source: :blue[ANALELE UNIVERSITĂŢII “EFTIMIE MURGU” REŞIŢA], ANUL XXIV, no. 1, 2017, 
		ISSN 1453 - 7397, Published: :red[2017]
	"""   )
	with col2:
		FCT_Down( current_dir / 'DOCS' / 'Art_Zrejnanin 2017.pdf', "Article Download" )
	
	col1, col2 = st.columns([0.8,0.2])
	col1.write( """
		3.46. Article Title: :green[Analysis and Processing of Index Tests Results at 
		Double-Adjust Hydraulic Turbines with a Computer-Aided Design Software], 
		Authors: A.Cuzmos, D.Nedelcu, CV. Campian, F. Cristian, AM. Budai Source: 
		:blue[Applied Mechanics and Materials], Vol. 823, (2016), pp 396-401,
		doi:10.4028/www.scientific.net/AMM.823.396 Published: :red[2016]
	"""   )
	with col2:
		FCT_Down( current_dir / 'DOCS' / 'Art_ICOME 2016.pdf', "Article Download" )

	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.47. Article Title: :green[DESFĂŞURAREA VIROLELOR UNEI CAMERE SPIRALE UTILIZÂND 
		MODULUL SHEET METAL DIN SOLIDWORKS], Authors: D.Nedelcu, V. Iancu Source: :blue[
		A XVI-a Conferinţă internaţională – multidisciplinară,  'Profesorul Dorin Pavel - 
		fondatorul hidroenergeticii româneşti'], Sebes, Published: :red[2016]
	"""   )
	col2.link_button("View", "https://stiintasiinginerie.ro/wp-content/uploads/2016/07/29-50-DESF%C4%82%C5%9EURAREA-VIROLELOR-UNEI-CAMERE-SPIRALE.pdf")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.48. Article Title: :green[RECONSTITUIREA GEOMETRIEI COMPONENTELOR MECANICE PRIN 
		FOTOGRAMETRIE PARTEA I], Authors: D.Nedelcu, :blue[
		A XVI-a Conferinţă internaţională – multidisciplinară,  'Profesorul Dorin Pavel - 
		fondatorul hidroenergeticii româneşti'], Sebes, Published: :red[2016]
	"""   )
	col2.link_button("View", "https://stiintasiinginerie.ro/wp-content/uploads/2016/07/29-71-RECONSTITUIREA-GEOMETRIEI-COMPONENTELOR-I.pdf")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.49. Article Title: :green[RECONSTITUIREA GEOMETRIEI COMPONENTELOR MECANICE PRIN 
		FOTOGRAMETRIE PARTEA II], Authors: D.Nedelcu, Source: :blue[
		A XVI-a Conferinţă internaţională – multidisciplinară,  'Profesorul Dorin Pavel - 
		fondatorul hidroenergeticii româneşti'], Sebes, Published: :red[2016]
	"""   )
	col2.link_button("View", "https://stiintasiinginerie.ro/wp-content/uploads/2016/07/29-72-RECONSTITUIREA-GEOMETRIEI-COMPONENTELOR-II.pdf")
	
	col1, col2 = st.columns([0.8,0.2])
	col1.write( """
		3.50. Article Title: :green[The 3D reconstruction and dimensional control of the reference part], 
		Authors: D.Nedelcu, BS. Laurentiu, A. Rajic Source: :blue[
		The 5th Scientific Conference "Entrepreneurship, Engineering and Management", PIM5], 
		Technical College of Applied Sciences in Zrenjanin, pp 49-56, Published: :red[2016]
	"""   )
	with col2:
		FCT_Down( current_dir / 'DOCS' / 'Art_Zrejnanin 2016.pdf', "Article Download" )

	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.51. Article Title: :green[The Calculation of the Pelton and Francis Turbine Hill 
		Chart Using the HydroHillChart Software], Authors: D.Nedelcu, A. Ghican, Source: :blue[
		'HIDRAULICA-Magazine of Hydraulics, Pneumatics, Tribology, Ecology, Sensorics, Mechatronics'], 
		No. 4/2015, ISSN 1453 – 7303, Published: :red[2015]
	"""   )
	col2.link_button("View", "https://hidraulica.fluidas.ro/2015/nr4/7-16.pdf")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.52. Article Title: :green[The Hill Chart Calculation for Francis Runner Models
		using the HydroHillChart - Francis Module Software ], Authors: D.Nedelcu, 
		A. Bostan, F. Peris-Bendu Source: :blue[ANALELE UNIVERSITĂŢII “EFTIMIE MURGU” 
		REŞIŢA'], ANUL XXII, no. 1, 2015,ISSN 1453 - 7397, Published: :red[2015]
	"""   )
	col2.link_button("View", "http://anale-ing.uem.ro/2015/13.pdf")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.53. Article Title: :green[The Hill Chart Calculation for Pelton Runner Models
		using the HydroHillChart - Pelton Module Software], Authors: A. Bostan,D.Nedelcu, 
		 F. Peris-Bendu Source: :blue[ANALELE UNIVERSITĂŢII “EFTIMIE MURGU” 
		REŞIŢA'], ANUL XXII, no. 1, 2015,ISSN 1453 - 7397, Published: :red[2015]
	"""   )
	col2.link_button("View", "http://anale-ing.uem.ro/2015/14.pdf")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.54. Article Title: :green[HydroHillChart – Francis module. Software used to
		Calculate the Hill Chart of the Francis Hydraulic Turbines], Authors: 
		D.Nedelcu, A. Bostan, F. Peris-Bendu Source: :blue[ANALELE UNIVERSITĂŢII 
		“EFTIMIE MURGU” REŞIŢA'], ANUL XXII, no. 1, 2015,ISSN 1453 - 7397, 
		Published: :red[2015]
	"""   )
	col2.link_button("View", "http://anale-ing.uem.ro/2015/31.pdf")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.55. Article Title: :green[HydroHillChart – Pelton module. Software used to
		Calculate the Hill Chart of the Pelton Hydraulic Turbines], Authors: 
		D.Nedelcu, A. Bostan, F. Peris-Bendu Source: :blue[ANALELE UNIVERSITĂŢII 
		“EFTIMIE MURGU” REŞIŢA'], ANUL XXII, no. 1, 2015,ISSN 1453 - 7397, 
		Published: :red[2015]
	"""   )
	col2.link_button("View", "http://anale-ing.uem.ro/2015/32.pdf")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.56. Article Title: :green[CONSIDERAŢII PRIVIND CONCEPŢIA MODELULUI DE VANĂ 
		FLUTURE DESTINAT EFECTUĂRII CERCETĂRILOR EXPERIMENTALE], Authors: F. Peris-Bendu, 
		A. Bostan, D.Nedelcu,Source: :blue[A XV-a Conferinţă internaţională – multidisciplinară,  
		'Profesorul Dorin Pavel - fondatorul hidroenergeticii româneşti'], Sebes, 
		Published: :red[2015]
	"""   )
	col2.link_button("View", "https://stiintasiinginerie.ro/wp-content/uploads/2015/06/27-52.pdf")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.57. Article Title: :green[CONSIDERAŢII PRIVIND CERCETĂRILE EXPERIMENTALE 
		REALIZATE PE UN MODEL DE VANĂ FLUTURE], Authors: F. Peris-Bendu, A. Bostan,
		D.Nedelcu,Source: :blue[A XV-a Conferinţă internaţională – multidisciplinară,  
		'Profesorul Dorin Pavel - fondatorul hidroenergeticii româneşti'], Sebes, 
		Published: :red[2015]
	"""   )
	col2.link_button("View", "https://stiintasiinginerie.ro/wp-content/uploads/2015/06/27-51.pdf")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.58. Article Title: :green[Theoretical and Experimental Research Performed on
		the Tesla Turbine - Part I], Authors: D.Nedelcu, P. Guran, A. Cantaragiu
		Source: :blue[ANALELE UNIVERSITĂŢII “EFTIMIE MURGU” REŞIŢA'], ANUL XXII, no. 2, 
		2015,ISSN 1453 - 7397, Published: :red[2015]
	"""   )
	col2.link_button("View", "http://anale-ing.uem.ro/2015/225.pdf")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.59. Article Title: :green[Theoretical and Experimental Research Performed on
		the Tesla Turbine – Part II], Authors: D.Nedelcu, EV. Gillich, V. Iancu, F. Muntean
		Source: :blue[ANALELE UNIVERSITĂŢII “EFTIMIE MURGU” REŞIŢA'], ANUL XXII, no. 2, 
		2015,ISSN 1453 - 7397, Published: :red[2015]
	"""   )
	col2.link_button("View", "http://anale-ing.uem.ro/2015/226.pdf")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.60. Article Title: :green[APPLICATIONS OF THE ADDITIVE MANUFACTURING TECHNOLOGY 
		TO MANUFACTURE THE HIP IMPLANTS], Authors: A. Rajic, S. STOJADINOVIC, D.Nedelcu, 
		E. DESNICA, L. a LAZIC VULICEVIC, Source: :blue[ANNALS of Faculty Engineering Hunedoara  
		– International Journal of EngineeringTome XII [2014] – Fascicule 2 [May] 
		ISSN: 1584‐2665 [print]; ISSN: 1584‐2673 [online], Published: :red[2014]
	"""   )
	col2.link_button("View", "https://annals.fih.upt.ro/pdf-full/2014/ANNALS-2014-2-14.pdf")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.61. Article Title: :green[CONSIDERAŢII PRIVIND OPTIMIZAREA FORMEI DISCULUI LA O 
		VANĂ FLUTURE PENTRU REDUCEREA COEFICIENTULUI DE REZISTENŢĂ HIDRAULICĂ], Authors: 
		F. Peris-Bendu, D.Nedelcu, V. Campian, Source: :blue[A XIV-a Conferinţă internaţională 
		– multidisciplinară, 'Profesorul Dorin Pavel - fondatorul hidroenergeticii româneşti'], 
		Sebes, Published: :red[2014]
	"""   )
	col2.link_button("View", "https://stiintasiinginerie.ro/wp-content/uploads/2014/07/25-58.pdf")
	
	col1, col2 = st.columns([0.8,0.2])
	col1.write( """
		3.62. Article Title: :green[APLICAREA INGINERIEI INVERSE PENTRU RECONSTRUCŢIA GEOMETRIEI 
		UNUI DRAGON], Authors: D.Nedelcu, Source: :blue[A XIV-a Conferinţă internaţională 
		– multidisciplinară, 'Profesorul Dorin Pavel - fondatorul hidroenergeticii româneşti'], 
		Volumul 26, Sebes, Published: :red[2014]
	"""   )
	with col2:
		FCT_Down( current_dir / 'DOCS' / 'Art_Sebes_2014.pdf', "Article Download" )
	
	col1, col2 = st.columns([0.8,0.2])
	col1.write( """
		3.63. Article Title: :green[RESEARCH REGARDING THE CAVITATION EROSION RESISTANCE OF THE
		STAINLESS STEEL WITH 13% Cr AND 4% Ni USED TO MANUFACTURE THE COMPONENTS OF KAPLAN, FRANCIS 
		AND PELTON HYDRAULIC TURBINES], Authors: NEDELONI MARIAN-DUMITRU, NEDELCU DORIAN, CÂMPIAN 
		VIOREL CONSTANTIN, CHIRUS DANIEL, AVASILOAIE RAOUL-CRISTIAN, DĂNUł FLOREA, Source: :blue[
		Constanta Maritime University Annals], Year XIV, Vol.19, Published: :red[2013]
	"""   )
	with col2:
		FCT_Down( current_dir / 'DOCS' / 'Art_Constanta1_2013.pdf', "Article Download" )
	
	col1, col2 = st.columns([0.8,0.2])
	col1.write( """
		3.64. Article Title: :green[NUMERICAL SIMULATION OF THE SHORT FLEXIBLE WHEEL 
		OF THE DOUBLE HARMONIC GEAR TRANSMISSION], Authors: IANICI DRAGHIŢA, NEDELCU 
		DORIAN, IANICI SAVA, Source: :blue[Constanta Maritime University Annals], 
		Year XIV, Vol.20, Published: :red[2013]
	"""   )
	with col2:
		FCT_Down( current_dir / 'DOCS' / 'Art_Constanta2_2013.pdf', "Article Download" )
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.65. Article Title: :green[APLICAREA INGINERIEI INVERSE PENTRU RECONSTRUCŢIA 
		GEOMETRIEI UNUI ROTOR], Authors: Dorian NEDELCU, Raoul AVASILOAIE, Dănuţ FLOREA, 
		Source: :blue[A XIII-a Conferinţă internaţională – multidisciplinară, 'Profesorul 
		Dorin Pavel - fondatorul hidroenergeticii româneşti'], Sebes, Published: :red[2013]
	"""   )
	col2.link_button("View", "https://stiintasiinginerie.ro/wp-content/uploads/2013/12/23-57-APLICAREA-INGINERIEI-INVERSE-PENTRU-RECONSTRUC%C5%A2IA-GEOMETRIEI-UNUI-ROTOR.pdf")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.66. Article Title: :green[STUDIUL NUMERIC AL CONCENTRATORULUI DE TENSIUNE PENTRU
		O BARĂ CU CRESTĂTURI ÎN „V” SUPUSĂ SOLICITĂRII DE ÎNTINDERE], Authors: Dorian NEDELCU, 
		Dănuţ FLOREA, Raoul AVASILOAIE Source: :blue[A XIII-a Conferinţă internaţională – multidisciplinară, 'Profesorul 
		Dorin Pavel - fondatorul hidroenergeticii româneşti'], Sebes, Published: :red[2013]
	"""   )
	col2.link_button("View", "http://stiintasiinginerie.ro/wp-content/uploads/2013/12/23-73-STUDIUL-NUMERIC-AL-CONCENTRATORULUI-DE-TENSIUNE-PENTRU-O-BAR%C4%82-CU-CREST%C4%82TURI-%C3%8EN-%E2%80%9EV%E2%80%9D-SUPUS%C4%82-SOLICIT%C4%82RII-DE-%C3%8ENTINDERE.pdf")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.67. Article Title: :green[CONSIDERAŢII PRIVIND SOLUŢII MODERNE ÎN
		PROIECTAREA VANELOR FLUTURE CU DISC BIPLAN], Authors: Florin PERIŞ-BENDU, 
		Dorian NEDELCU, Constantin Viorel CÂMPIAN Source: :blue[A XIII-a Conferinţă 
		internaţională – multidisciplinară, 'Profesorul Dorin Pavel - fondatorul 
		hidroenergeticii româneşti'], Sebes, Published: :red[2013]
	"""   )
	col2.link_button("View", "http://stiintasiinginerie.ro/wp-content/uploads/2013/12/59-CONSIDERA%C5%A2II-PRIVIND-SOLU%C5%A2II-MODERNE-%C3%8EN-PROIECTAREA-VANELOR-FLUTURE-CU-DISC-BIPLAN.pdf")
	
	col1, col2 = st.columns([0.8,0.2])
	col1.write( """
		3.68. Article Title: :green[Considerations Regarding the Stresses and the
		Deformations of the Butterfly Valve Body], Authors: Florin Peris-Bendu, 
		Adelina Bostan, Viorel Câmpian, Dorian NedelcuSource: :blue[ANALELE 
		UNIVERSITĂŢII “EFTIMIE MURGU” REŞIŢA'], ANUL XX, no. 1, 2013, ISSN 1453 - 7397, 
		Published: :red[2013]
	"""   )
	with col2:
		FCT_Down( current_dir / 'DOCS' / 'Art_SysStruc_2013.pdf', "Article Download" )
	
	col1, col2 = st.columns([0.8,0.2])
	col1.write( """
		3.69. Article Title: :green[THE PELTON RUNNER DESIGN METHODOLOGY], Authors: 
		Hopota Adrian, Nedelcu Dorian, Avasiloaie Raoul Source: :blue[
		THINK-HYDRO Conference], Resita, Published: :red[2013]
	"""   )
	with col2:
		FCT_Down( current_dir / 'DOCS' / 'Art_ThinkHydro1 2013.pdf', "Article Download" )
	
	col1, col2 = st.columns([0.8,0.2])
	col1.write( """
		3.70. Article Title: :green[MICROHYDROPOWER WITH PERMANENT MAGNET
		GENERATOR AND IMMERSED RUNNER], Authors: Nedelcu Dorian, Hopota 
		Adrian, Florea Dănuţ Source: :blue[	THINK-HYDRO Conference], 
		Resita, Published: :red[2013]
	"""   )
	with col2:
		FCT_Down( current_dir / 'DOCS' / 'Art_ThinkHydro2 2013.pdf', "Article Download" )
	
	col1, col2 = st.columns([0.8,0.2])
	col1.write( """
		3.71. Article Title: :green[APPLICATIONS OF THE ADDITIVE MANUFACTURING
		TECHNOLOGY TO MANUFACTURE THE HIP IMPLANTS], Authors: Aleksandar Rajic, 
		Slobodan Stojadinovic, Dorian Nedelcu, Eleonora Desnica, Ljubica Lazic 
		Vulicevic Source: :blue[III International Conference Industrial Engineering 
		And Environmental Protection 2013 (IIZS 2013)], October 30th, 2013, 
		Zrenjanin, Serbia  Published: :red[2013]
	"""   )
	with col2:
		FCT_Down( current_dir / 'DOCS' / 'Art_Zrejnaninn 2013.pdf', "Article Download" )
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.72. Article Title: :green[The Reverse Engineering of a Spring Support using
		the Noomeo Optinum 3D Scanner and the Rapidform XOR3 Software], Authors: 
		Dorian Nedelcu, Aleksandar Rajic, DănuŃ Florea, Raoul Avasiloaie  Source: 
		:blue[ANALELE UNIVERSITĂŢII “EFTIMIE MURGU” REŞIŢA'], ANUL XX, no. 1, 2013, 
		ISSN 1453 - 7397, Published: :red[2013]
	"""   )
	col2.link_button("View", "http://anale-ing.uem.ro/2013/24.pdf")

	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.73. Article Title: :green[Applications of the Rapid Prototyping Technology to
		Manufacture the Pelton Runners], Authors: Dorian Nedelcu, Raoul Avasiloaie, 
		Dănut Florea, Aleksandar Rajic, Source: :blue[ANALELE UNIVERSITĂŢII “EFTIMIE 
		MURGU” REŞIŢA'], ANUL XX, no. 1, 2013, ISSN 1453 - 7397, Published: :red[2013]
	"""   )
	col2.link_button("View", "http://anale-ing.uem.ro/2013/23.pdf")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.74. Article Title: :green[Determine the Correlation between Wicked Gates
		Angles and Servomotors Strokes for Asymmetric Hydrofoil], Authors: Daniel Daia, 
		Dorian Nedelcu , Source: :blue[ANALELE UNIVERSITĂŢII “EFTIMIE 
		MURGU” REŞIŢA'], ANUL XX, no. 1, 2013, ISSN 1453 - 7397 , Published: :red[2013]
	"""   )
	col2.link_button("View", "http://anale-ing.uem.ro/2013/11.pdf")
	
	col1, col2 = st.columns([0.8,0.2])
	col1.write( """
		3.75. Article Title: :green[Variants of sonotrode for a vibratory apparatus for 
		test cavitation erosion by the indirect method], Authors: Nedeloni M.D., 
		Nedelcu D.  Source: :blue[Constanta Maritime University Annals],Vol.17, 
		Year XIII, ISSN 1582-3601, Published: :red[2012]
	"""   )
	with col2:
		FCT_Down( current_dir / 'DOCS' / 'Art_Constanta1_2012.pdf', "Article Download" )

	col1, col2 = st.columns([0.8,0.2])
	col1.write( """
		3.76. Article Title: :green[Calibration of a sonotrode from a stand component for test 
		cavitation erosion through direct method], Authors: Nedeloni M.D., Nedelcu D., Ion I., 
		Ciubotariu R.  Source: :blue[Constanta Maritime University Annals],Vol.17, Year XIII, 
		ISSN 1582-3601, Published: :red[2012]
	"""   )
	with col2:
		FCT_Down( current_dir / 'DOCS' / 'Art_Constanta2_2012.pdf', "Article Download" )

	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.77. Article Title: :green[Cavitation Erosion Tests Performed by Indirect Vibratory Method 
		on Stainless Steel Welded Samples with Hardened Surface], Authors: Nedeloni M.D., Cojocaru V., 
		Ciubotariu R.,Nedelcu D., Source: :blue[	ANALELE UNIVERSITĂŢII “EFTIMIE MURGU”],	ANUL XIX, 
		no. 1, ISSN 1453-7397, Published: :red[2012]
	"""   )
	col2.link_button("View", "http://anale-ing.uem.ro/2012/25.pdf")

	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.78. Article Title: :green[Research through Direct and Indirect Cavitation Method for a 
		Aluminum Specimen], Authors: Nedeloni M.D., Nedelcu D., Source: :blue[	ANALELE 
		UNIVERSITĂŢII “EFTIMIE MURGU”],	ANUL XIX, no. 1, ISSN 1453-7397, Published: :red[2012]
	"""   )
	col2.link_button("View", "http://anale-ing.uem.ro/2012/24.pdf")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.79. Article Title: :green[PROTOTIPAREA RAPIDĂ A UNUI ROTOR PELTON], Authors: 
		Dorian NEDELCU, Florentin Mirel POP, Vasile COJOCARU,Adrian HOPOTA, Source: 
		:blue[A XIII-a Conferinţă internaţională – multidisciplinară, 'Profesorul 
		Dorin Pavel - fondatorul hidroenergeticii româneşti'], Published: :red[2012]
	"""   )
	col2.link_button("View", "http://stiintasiinginerie.ro/wp-content/uploads/2013/12/43-PROTOTIPAREA-RAPID%C4%82-A-UNUI-ROTOR-PELTON.pdf")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.80. Article Title: :green[RECONSTITUIREA GEOMETRIEI UNUI IMPLANT DE GENUNCHI], 
		Authors: Dorian NEDELCU, Vasile COJOCARU, Source: :blue[A XIII-a Conferinţă 
		internaţională – multidisciplinară, 'Profesorul Dorin Pavel - fondatorul 
		hidroenergeticii româneşti'], Published: :red[2012]
	"""   )
	col2.link_button("View", "http://stiintasiinginerie.ro/wp-content/uploads/2013/12/102-RECONSTITUIREA-GEOMETRIEI-UNUI.pdf")

	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.81. Article Title: :green[Hydrodynamics automatic optimization of runner blades for
		reaction hydraulic turbines ], Authors: D Balint, V Câmpian, D Nedelcu,O. Megheles , 
		Source: :blue[26th IAHR Symposium on Hydraulic Machinery and Systems - IOP Conf. 
		Series: Earth and Environmental Science 15 (2012) 032014], doi:10.1088/1755-1315/15/3/032014
		Published: :red[2012]
	"""   )
	col2.link_button("View", "https://iopscience.iop.org/article/10.1088/1755-1315/15/3/032014/pdf")
	
	col1, col2 = st.columns([0.8,0.2])
	col1.write( """
		3.82. Article Title: :green[Aplicarea tehnologiilor de prototipare rapidă şi reconstituire 
		geometrie în turnarea pieselor], Authors: Dorian Nedelcu, Lupinca Cinca Ionel,Source: :blue[
		A 21-a CONFERINTA NATIONALA DE TURNATORIE], June 2012, IASI, ROMÂNIA Published: :red[2012]
	"""   )
	with col2:
		FCT_Down( current_dir / 'DOCS' / 'Art_Iasi_2012.pdf', "Article Download" )
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.83. Article Title: :green[FINITE ELEMENT ANALYSIS AND DYNAMIC ANALYSIS OF THE
		OUTER BEARING BUSH FROM THE BLADE ADJUSTMENT MECHANISM OF KAPLAN TURBINES], 
		Authors: Dorian NEDELCU, Vasile COJOCARU, Source: :blue[The 4th International Conference
		'Computational Mechanics and Virtual Engineering' COMEC 2011], 20-22 OCTOBER 2011, 
		Brasov, RomaniaPublished: :red[2011]
	"""   )
	col2.link_button("View", "http://aspeckt.unitbv.ro/jspui/bitstream/123456789/1396/1/281-286,%20C.Jianu_C.V.Campian_V.Cojocaru_D.Nedelcu.pdf")
	
	col1, col2 = st.columns([0.8,0.2])
	col1.write( """
		3.84. Article Title: :green[A Numerical Study of the Local Stress for a Fillet with 
		Tensile Force Applied on a Rectangular Plate], Authors: Dorian Nedelcu, Marian-Dumitru 
		Nedeloni, Draghiţa Ianici, Daniel Daia, Florentin Mirel Pop, Raoul Cristian Avasiloaie, 
		Source: :blue[ANALELE UNIVERSITĂŢII “EFTIMIE MURGU” REŞIŢA], ANUL XVIII, no. 1, 2011, 
		ISSN 1453 - 7397 Published: :red[2011]
	"""   )
	with col2:
		FCT_Down( current_dir / 'DOCS' / 'Art_Anale_2011.pdf', "Article Download" )

	col1, col2 = st.columns([0.8,0.2])
	col1.write( """
		3.85. Article Title: :green[Numerical Investigations of Flow on the Kaplan Turbine 
		Runner Blade Anticavitation Lip with Modified Cross Section], Authors: Vasile Cojocaru, 
		Daniel Balint, Viorel Constantin Campian, Dorian Nedelcu and Camelia Jianu, 
		Source: :blue[Proceedings of the 2nd International Conference on Fluid Mechanics
		and Heat and Mass Transfer 2011 (FLUIDSHEAT '11)], Corfu Island, Greece, July 14-16, 
		ISBN: 978-1-61804-020-6 Published: :red[2011]
	"""   )
	with col2:
		FCT_Down( current_dir / 'DOCS' / 'Art_Corfu_2011.pdf', "Article Download" )
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.86. Article Title: :green[The Kinematic and Dynamic Analysis of the Crank Mechanism 
		with SolidWorks Motion], Authors: Dorian Nedelcu, MARIAN-DUMITRU NEDELONI, DANIEL DAIA, 
		Source: :blue[Recent Advances in Signal Processing, Computational Geometry and Systems Theory] 
		Florence, Italy, August 23-25, ISBN: 978-1-61804-027-5, pg. 245-250, Published: :red[2011]
	"""   )
	col2.link_button("View", "http://www.wseas.us/e-library/conferences/2011/Florence/GAVTASC/GAVTASC-42.pdf")

	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.87. Article Title: :green[Calculul fortei aerodinamice si distributiei de presiuni pentru 
		un cos vertical], Authors: Dorian Nedelcu, Draghita Ianici, Marian-Dumitru Nedeloni, Daniel Daia, 
		Florentin Mirel Pop, Raoul Cristian Avasiloaie Source: :blue[Conferinta Nationala multidisciplinara-
		cu participare internationala „Profesorul Dorin PAVEL-Fondatorul hidroenergeticii romanesti”] 
		Published: :red[2011]
	"""   )
	col2.link_button("View", "http://stiintasiinginerie.ro/wp-content/uploads/2014/01/37-CALCULUL-FOR%C5%A2EI-AERODINAMICE-%C5%9EI-DISTRIBU%C5%A2IEI.pdf")
	

	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.88. Article Title: :green[Metallographic and Numerical Methods Investigations about 
		Failure of a Kaplan Turbine Runner Blade], Authors: Doina Frunzăverde, Viorel Câmpian, 
		Dorian Nedelcu, Gilbert-Rainer Gillich, Gabriela Mărginean, Source: :blue[WSEAS TRANSACTIONS
		on FLUID MECHANICS] ISSN: 1790-5087], Issue 1, Volume 5, Published: :red[2010]
	"""   )
	col2.link_button("View", "http://www.wseas.us/e-library/transactions/fluid/2010/89-546.pdf")

	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.89. Article Title: :green[Numerical behavior reproduction of a truss structure and beam, 
		subjected to concentrated load], Authors: Nedelcu Dorian, Ianici Draghita, Nedeloni Marian, 
		Daia Daniel, Source: :blue[Analele Universității “Eftimie Murgu” Reşiţa] ISSN 1453 – 7397	
		Anul XVII, no. 1, Published: :red[2010]
	"""   )
	col2.link_button("View", "http://anale-ing.uem.ro/2010/A_36.pdf")
	
	col1, col2 = st.columns([0.8,0.2])
	col1.write( """
		3.90. Article Title: :green[Determination of Double Flexible Toothed Wheel Length 
		function of Elasticity Module], Authors: D.G. Vela, D. Nedelcu, I. Vela, Source: 
		:blue[Analele Universității “Eftimie Murgu” Reşiţa Fascicula de Inginerie], no. 1 ,
		ISSN 1453 -7394,Published: :red[2010]
	"""   )
	with col2:
		FCT_Down( current_dir / 'DOCS' / 'Art_Anale_2010.pdf', "Article Download" )
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.91. Article Title: :green[The Geometry Optimisation of a Triple Branch Pipe 
		using Finite Element Method], Authors: Nedelcu Dorian Cojocaru Vasile, 
		Călin-Octavian Micloşină, Source: :blue[Analele Universității “Eftimie Murgu” 
		Reşiţa], ISSN 1453-7394, Published: :red[2008]
	"""   )
	col2.link_button("View", "http://anale-ing.uem.ro/2008/2008_a41.pdf")
	
	col1, col2 = st.columns([0.8,0.2])
	col1.write( """
		3.92. Article Title: :green[The Parametrical Design of the Parts from the same 
		Tehnological Family], Authors: Cojocaru Vasile Nedelcu Dorian, Călin-Octavian 
		Micloşină, Source: :blue[Analele Universității “Eftimie Murgu” 
		Reşiţa], ISSN 1453-7394, Published: :red[2008]
	"""   )
	with col2:
		FCT_Down( current_dir / 'DOCS' / 'Art_Anale2_2008.pdf', "Article Download" )

	col1, col2 = st.columns([0.8,0.2])
	col1.write( """
		3.93. Article Title: :green[Mobile Robot Command], Authors: Călin-Octavian 
		Micloşină, Codruta-Oana Hamat, Nedelcu Dorian, Cojocaru Vasile, Source: 
		:blue[Analele Universității “Eftimie Murgu” 
		Reşiţa], ISSN 1453-7394, Published: :red[2008]
	"""   )
	with col2:
		FCT_Down( current_dir / 'DOCS' / 'Art_Anale1_2008.pdf', "Article Download" )

	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.94. Article Title: :green[Index tests performed on a Francis turbine 
		from HPP Ruieni], Authors: Cuzmoş Adrian, Dumbravă Cosmin, Câmpian 
		Constantin Viorel, Nedelcu Dorian, Source: :blue[Analele Universității 
		“Eftimie Murgu” Reşiţa], ISSN 1453-7394, Published: :red[2008]
	"""   )
	col2.link_button("View", "http://anale-ing.uem.ro/2008/2008_a17.pdf")
	
	col1, col2 = st.columns([0.8,0.2])
	col1.write( """
		3.95. Article Title: :green[Hydrodynamic Design and Numerical Analysis 
		of a New Francis Turbine with High Specific Speed], Authors: Bobar Maria,
		Zsembinszki Stefan, Muntean Sebastian, Nedelcu Dorian, Source: :blue[Scientific 
		Bulletin of the "Politehnica" University of Timisoara, Transactions on Mechanics], 
		ISSN  1224-6077, Published: :red[2008]
	"""   )
	with col2:
		FCT_Down( current_dir / 'DOCS' / 'Art_SciBul4_2008.pdf', "Article Download" )
	
	col1, col2 = st.columns([0.8,0.2])
	col1.write( """
		3.96. Article Title: :green[Research upon Cavitation Erosion Resistance of Heat 
		Treated Martensitic Stainless Steels], Authors: Padurean Ioan Trusculescu Marin, 
		Nedelcu Dorian, Megheles Octavian, Popoviciu Mircea Octavian, Hota Ioan, Source: 
		:blue[Scientific Bulletin of the "Politehnica" University of Timisoara, Transactions 
		on Mechanics], ISSN  1224-6077, Published: :red[2008]
	"""   )
	with col2:
		FCT_Down( current_dir / 'DOCS' / 'Art_SciBul1_2008.pdf', "Article Download" )

	col1, col2 = st.columns([0.8,0.2])
	col1.write( """
		3.97. Article Title: :green[About Influences of the Structural State in Cavitation 
		Erosion Resistance of Thermally Treated Austenitic Stainless Steels], Authors: Padurean 
		Ioan Trusculescu Marin, Nedelcu Dorian, Megheles Octavian, Popoviciu Mircea Octavian, 
		Hota Ioan, Source: 	:blue[Scientific Bulletin of the "Politehnica" University of Timisoara, 
		Transactions on Mechanics], ISSN  1224-6077, Published: :red[2008]
	"""   )
	with col2:
		FCT_Down( current_dir / 'DOCS' / 'Art_HME1_2008.pdf', "Article Download" )

	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.98. Article Title: :green[Influence of the Heat Treatment to the Cavitation Erosion 
		Resistance of Austenitic Stainless Steel], Authors: Pădurean Ioan Nedelcu Dorian, 
		Fay Arpad, Micloşină Călin, Source: 	:blue[Scientific Bulletin of the "Politehnica" 
		University of Timisoara, Transactions on Mechanics],  Tom 53 (67), Fasc. 4, ISSN 1224-6077 
		Published: :red[2008]
	"""   )
	col2.link_button("View", "https://www.researchgate.net/publication/271646341_Influence_of_the_Heat_Treatment_to_the_Cavitation_Erosion_Resistance_of_Austenitic_Stainless_Steel")

#	col1, col2 = st.columns([0.8,0.2])
#	col1.write( """
#		3.97 Article Title: :green['2-Finger' Parallel Gripper and Experimental Determination 
#		of Prehension Force], Authors: Micloşină Călin-Octavian Nedelcu Dorian, Pădurean Ioan, 
#		Source: :blue[Scientific Bulletin of the "Politehnica" University of Timisoara, 
#		Transactions on Mechanics],  Tom 53 (67), Fasc. 4, ISSN 1224-6077, Published: :red[2008]
#	"""   )
#	#	col2.link_button("View", "http://anale-ing.uem.ro/2008/2008_a17.pdf")
#
	col1, col2 = st.columns([0.8,0.2])
	col1.write( """
		3.99. Article Title: :green[Efficiency Measurements on Unit No.1 in Remeti Hydro Power 
		Plant], Authors: Campian Constantin Viorel Nedelcu Dorian, Grando Ioan, Cuzmos Adrian, 
		Dumbrava Cosmin, Source: :blue[Scientific Bulletin of the "Politehnica" University of Timisoara, 
		Transactions on Mechanics],  Tom 53 (67), Fasc. 4, ISSN 1224-6077, Published: :red[2008]
	"""   )
	with col2:
		FCT_Down( current_dir / 'DOCS' / 'Art_SciBul3_2008.pdf', "Article Download" )
	
	col1, col2 = st.columns([0.8,0.2])
	col1.write( """
		3.100. Article Title: :green[About the Convergence of the Finite Elements Analysis], 
		Authors: Nedelcu Dorian Micloşină Călin-Octavian, Pădurean Ioan, Source: :blue[Scientific 
		Bulletin of the "Politehnica" University of Timisoara, Transactions on Mechanics],  
		Tom 53 (67), Fasc. 4, ISSN 1224-6077, Published: :red[2008]
	"""   )
	with col2:
		FCT_Down( current_dir / 'DOCS' / 'Art_SciBul5_2008.pdf', "Article Download" )
	
	col1, col2 = st.columns([0.8,0.2])
	col1.write( """
		3.101. Article Title: :green[Stress and Deformations on Pelton Turbine Blade Calculated 
		by Finite Element Method], Authors: Nedelcu Dorian, Constantin Viorel Campian, Ioan Padurean, 
		Source: :blue[Scientific Bulletin of the "Politehnica" University of Timisoara, 
		Transactions on Mechanics],  Tom 53 (67), Fasc. 4, ISSN 1224-6077, Published: :red[2008]
	"""   )
	with col2:
		FCT_Down( current_dir / 'DOCS' / 'Art_SciBul2_2008.pdf', "Article Download" )
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.102. Article Title: :green[Service life estimation for runner’s blade of an axial turbine], 
		Authors: Nedelcu Dorian Câmpian C. Viorel, Padurean Ioan, 
		Source: :blue[Revista Academie Roumaine, Revue Roumaine des Sciences Techniques, Serie 
		de Mecanique Applique], Tom 53, No. 1, ISSN 0035-4074, Published: :red[2008]
	"""   )
	col2.link_button("View", "https://academiaromana.ro/sectii2002/RomanianJournalTS/rev2008-1/RJTS-AM_2008_1_a02_p9-18_Nedelcu.pdf")

	col1, col2 = st.columns([0.8,0.2])
	col1.write( """
		3.103. Article Title: :green[The design of an Kaplan turbine Runner using Autodesk Inventor], 
		Authors: Nedelcu Dorian, Padurean Ioan, Source: :blue[Scientific Bulletin of the "Politehnica" 
		University of Timisoara, Transactions on Mechanics], Published: :red[2007]
	"""   )
	with col2:
		FCT_Down( current_dir / 'DOCS' / 'Art_SciBul6_2007.pdf', "Article Download" )

	col1, col2 = st.columns([0.8,0.2])
	col1.write( """
		3.104. Article Title: :green[Computer aided design of an Draft Tube’s Elbow for hydraulic turbine 
		using Microstation], Authors: Nedelcu Dorian, Padurean Ioan, Source: :blue[Scientific Bulletin of 
		the "Politehnica" University of Timisoara, Transactions on Mechanics], Published: :red[2007]
	"""   )
	with col2:
		FCT_Down( current_dir / 'DOCS' / 'Art_SciBul2_2007.pdf', "Article Download" )
	
	col1, col2 = st.columns([0.8,0.2])
	col1.write( """
		3.105. Article Title: :green[CAD modelling of an axial blade turbine using Autodesk Inventor], 
		Authors: Nedelcu Dorian, Padurean Ioan, Source: :blue[Scientific Bulletin of 
		the "Politehnica" University of Timisoara, Transactions on Mechanics], Published: :red[2007]
	"""   )
	with col2:
		FCT_Down( current_dir / 'DOCS' / 'Art_SciBul4_2007.pdf', "Article Download" )
	
	col1, col2 = st.columns([0.8,0.2])
	col1.write( """
		3.106. Article Title: :green[Stress and deformations  on axial blade turbine calculated 
		by finite elements method],  Authors: Nedelcu Dorian, Padurean Ioan, Source: :blue[Scientific 
		Bulletin of the "Politehnica" University of Timisoara, Transactions on Mechanics], 
		Published: :red[2007]
	"""   )
	with col2:
		FCT_Down( current_dir / 'DOCS' / 'Art_SciBul5_2007.pdf', "Article Download" )
	
	col1, col2 = st.columns([0.8,0.2])
	col1.write( """
		3.107. Article Title: :green[FAILURE ANALYSIS OF A KAPLAN TURBINE RUNNER BLADE],  
		Authors: Viorel C. Câmpian, Doina Frunzăverde, Nedelcu Dorian, Gabriela Mărginean, 
		Source: :blue[IAHR 24th Symposium on Hydraulic Machinery and Systems], 
		OCTOBER 27-31, FOZ DO IGUASSU. Brazil
		Published: :red[2007]
	"""   )
	with col2:
		FCT_Down( current_dir / 'DOCS' / 'Art_Brasil_IAHR_2008.pdf', "Article Download" )
	
	col1, col2 = st.columns([0.8,0.2])
	col1.write( """
		3.108. Article Title: :green[Cosmos Design Star study: The tensile tests of the 
		rectangular plate with stress concentrators],  Authors: Nedelcu Dorian, Padurean Ioan, 
		Source: :blue[Revista Academie Roumaine, Revue Roumaine des Sciences Techniques, 
		Serie de Mecanique Applique], Tom 52, No. 3, September-December, ISSN 0035-4074
		Published: :red[2007]
	"""   )
	with col2:
		FCT_Down( current_dir / 'DOCS' / 'Art_Academie 2007.pdf', "Article Download" )

	col1, col2 = st.columns([0.8,0.2])
	col1.write( """
		3.109. Article Title: :green[Influence of structural state on cavitational erosion 
		of martensitic stainless steel GX4CRNI 13-4 quenching tempering and nitriding],	Authors: 
		Padurean Ioan, Nedelcu Dorian, Source: :blue[Scientific Bulletin of the "Politehnica" 
		University of Timisoara, Transactions on Mechanics],ISSN 1224-6077, Published: :red[2007]
	"""   )
	with col2:
		FCT_Down( current_dir / 'DOCS' / 'Art_SciBul1_2007.pdf', "Article Download" )
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.110. Article Title: :green[Computer Aided Design of an Admission Valve with Autodesk 
		Inventor],  Authors: Nedelcu Dorian, Source: :blue[Analele Universitatii "Eftimie 
		Murgu " Resita], ANUL XIV, no. 1, 2007, ISSN 1453 - 7397, Published: :red[2007]
	"""   )
	col2.link_button("View", "http://anale-ing.uem.ro/2007/2007_a22.pdf")
	
	col1, col2 = st.columns([0.8,0.2])
	col1.write( """
		3.111. Article Title: :green[EXPERIMENTAL RESEARCHES UPON CAVITATION EROSION RESISTANCE 
		OF THE AUSTENITIC STAINLESS STEEL HEAT TREATING BY SOLUTION TREATMENT AND NITRIDING],
		Authors: Ioan PĂDUREAN, Nedelcu Dorian, Source: :blue[SCIENTIFIC BULLETIN OF THE 
		„POLITEHNICA” UNIVERSITY OF TIMISOARA, ROMANIA Transactions  on  MECHANIC], Tom 52 
		(66), ISSN 1224-6077, Fasc.  1, Published: :red[2007]
	"""   )
	with col2:
		FCT_Down( current_dir / 'DOCS' / 'Art_SciBul3_2007.pdf', "Article Download" )
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.112. Article Title: :green[Numerical simulation of the stress and deformation 
		zone on the cabin’s framework of a mobile equipment],  Authors: Nedelcu Dorian, 
		Mănescu Tiberiu Ştefan, Source: :blue[Meridian Ingineresc],  no. 2,  Editura U.T.M., 
		Chişinău, ISSN 1683-853X, Published: :red[2007]
	"""   )
	col2.link_button("View", "http://repository.utm.md/bitstream/handle/5014/4520/MI_2007_2_pg_15_20.pdf?sequence=1&isAllowed=y")
	
	col1, col2 = st.columns([0.9,0.1])
	col1.write( """
		3.113. Article Title: :green[Finite Element Analysis Through COSMOS M/Design STAR],  
		Authors: Nedelcu Dorian, Mănescu Tiberiu Ştefan, C.V.Campian, Source: 
		:blue[FME Transactions, Faculty of Mechanical Engineering, Belgrade], Volume 32, 
		Number 1, pg. 36-42, Published: :red[2004]
	"""   )
	col2.link_button("View", "https://www.mas.bg.ac.rs/_media/istrazivanje/fme/vol32/1/fme_vol_32_no1_manesku.pdf")

	col1, col2 = st.columns([0.8,0.2])
	col1.write( """
		3.114. Article Title: :green[The results from index tests performed on the Kaplan 
		turbines], Authors: Câmpian C. Viorel, Nedelcu Dorian,  Source: :blue[Proceedings 
		of the International Conference: Clasic and Fashion in Fluid Machinery], October, 
		18-20, Belgrade, Yugoslavia-Serbia, pp 35-44, 10 pg, Published: :red[2002]
	"""   )
	with col2:
		FCT_Down( current_dir / 'DOCS' / 'Art_BELGRAD1_2002.pdf', "Article Download" )

	col1, col2 = st.columns([0.8,0.2])
	col1.write( """
		3.115. Article Title: :green[ Determine The Correlation Between Wicket Gates 
		Angles and Servomotors Strokes], Authors: Nedelcu Dorian, Câmpian C. Viorel, 
		Source: :blue[Proceedings 
		of the International Conference: Clasic and Fashion in Fluid Machinery], October, 
		18-20, Belgrade, Yugoslavia-Serbia, pp 35-44, 10 pg, Published: :red[2002]
	"""   )
	with col2:
		FCT_Down( current_dir / 'DOCS' / 'Art_BELGRAD2_2002.pdf', "Article Download" )
	