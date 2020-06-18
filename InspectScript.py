# -*- coding: utf-8 -*-

import gom
import logging
import os
import datetime
import glob
import time


def SetLogger(filepath):	
	logfolder = os.path.join(filepath,"Logs")
	if not os.path.exists(logfolder):
		os.mkdir(logfolder)
	
	logging.basicConfig(level=logging.DEBUG,filename=os.path.join(logfolder,"{} - Logs.txt".format(datetime.date.today().strftime("%b-%d-%y"))),
					filemode='a', format='%(asctime)s - %(levelname)s - %(message)s',
					datefmt='%d-%b-%y %H:%M:%S')

def Legal():
	DIALOG=gom.script.sys.create_user_defined_dialog (content='<dialog>' \
' <title>Choose STL Location</title>' \
' <style></style>' \
' <control id="OkCancel"/>' \
' <position></position>' \
' <embedding>always_toplevel</embedding>' \
' <sizemode>fixed</sizemode>' \
' <size width="523" height="736"/>' \
' <content columns="2" rows="3">' \
'  <widget column="0" row="0" type="display::text" columnspan="2" rowspan="1">' \
'   <name>text</name>' \
'   <tooltip></tooltip>' \
'   <text>&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">' \
'&lt;html>&lt;head>&lt;meta name="qrichtext" content="1" />&lt;style type="text/css">' \
'p, li { white-space: pre-wrap; }' \
'&lt;/style>&lt;/head>&lt;body style="    ">' \
'&lt;p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;span style=" font-size:8pt;">1.       Each party’s proprietary information shall remain the property of that party except as expressly provided otherwise by the other provisions of this Quote. &lt;/span>&lt;/p>' \
'&lt;p style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;span style=" font-size:8pt;">  &lt;/span>&lt;/p>' \
'&lt;p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;span style=" font-size:8pt;">&amp;quot;Proprietary Information&amp;quot; means all written and oral communications and all tangible and &lt;/span>&lt;/p>' \
'&lt;p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;span style=" font-size:8pt;">intangible products and materials related to the sale. Proprietary Information may include, but is not limited to: products, manufacturing techniques, pricing, cost of manufacture, trade secrets, research and development and engineering designs, concepts, technologies, processes, methods and capabilities, intellectual property, program code, and any other work instructions, including those developed to perform inspections or related Purchaser activity using the GOM or ATOS systems, and any other information that Seller may designate as being Proprietary Information. In addition, any supplementary files which are related to the aforementioned items shall also be considered “Proprietary Information.” &lt;/span>&lt;/p>' \
'&lt;p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;span style=" font-size:8pt;">  &lt;/span>&lt;/p>' \
'&lt;p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;span style=" font-size:8pt;">2.      &lt;/span>&lt;span style=" font-size:8pt; color:#000000;">Intellectual Property developed or acquired by either party before or during the scope of Purchaser’s order is considered Background Intellectual Property. Seller’s Intellectual property shall include program code, supplementary files, and other work instructions developed to perform inspections or related Buyer activity using the GOM or ATOS systems.&lt;/span>&lt;span style=" font-size:8pt;"> &lt;/span>&lt;/p>' \
'&lt;p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;span style=" font-size:8pt;">  &lt;/span>&lt;/p>' \
'&lt;p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;span style=" font-size:8pt; color:#000000;">3.      All Seller’s property, Sellers Background Intellectual Property shall be deemed Seller’s Proprietary information&lt;/span>&lt;span style=" font-size:8pt;"> &lt;/span>&lt;/p>' \
'&lt;p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;span style=" font-size:8pt; color:#000000;"> &lt;/span>&lt;span style=" font-size:8pt;"> &lt;/span>&lt;/p>' \
'&lt;p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;span style=" font-size:8pt; color:#000000;">4.      Purchaser shall not disclose Seller’s Proprietary Information to any third part&lt;/span>&lt;span style=" font-size:8pt; color:#ff0000;">y &lt;/span>&lt;span style=" font-size:8pt; color:#000000;">o&lt;/span>&lt;span style=" font-size:8pt; color:#ff0000;">r &lt;/span>&lt;span style=" font-size:8pt; color:#000000;">use Seller’s&lt;/span>&lt;span style=" font-size:8pt;"> &lt;/span>&lt;/p>' \
'&lt;p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;span style=" font-size:8pt; color:#000000;">Proprietary information for the benefit of any third party without Seller’s consent. Purchaser shall protect Seller’s Proprietary Information against unauthorized use or disclose using at least those measures that it takes to protect its own Proprietary Information of a similar nature, but no less that reasonable care. &lt;/span>&lt;/p>' \
'&lt;p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;span style=" font-size:8pt; color:#000000;"> &lt;/span>&lt;span style=" font-size:8pt;"> &lt;/span>&lt;/p>' \
'&lt;p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;span style=" font-size:8pt; color:#000000;">In the event Buyer is required by applicable law or regulation to disclose Seller’s Proprietary Information, Buyer shall provide Seller with prompt notice thereof and a reasonable opportunity to comment or undertake protective measures prior to such disclosure. Buyer may only disclose the information that is required by such law or regulation to be disclosed without liability under this agreement.&lt;/span>&lt;span style=" font-size:8pt;"> &lt;/span>&lt;/p>' \
'&lt;p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;span style=" font-size:8pt;">  &lt;/span>&lt;/p>' \
'&lt;p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;span style=" font-size:8pt;">5.      Purchaser shall be liable to Seller for any unauthorized use of disclosure by Buyer’s personnel or any third party to which Purchaser discloses Seller’s Proprietary Information. &lt;/span>&lt;/p>' \
'&lt;p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;span style=" font-size:8pt;">Due to the unique nature of the Proprietary Information, Buyer understands that Seller will suffer irreparable harm in the event of any breach of these terms and that monetary damages will be inadequate to compensate for any such breach. Buyer therefore agrees that Seller will, in addition to any such remedies available to it at law or in equity, be entitled to injunctive relief to enforce the terms of this Agreement. The failure of Buyer to comply with the terms of this Agreement will obligate Buyer to pay all expenses, including a reasonable attorney\'s fee, incurred by Seller because of that failure. &lt;/span>&lt;/p>&lt;/body>&lt;/html></text>' \
'   <wordwrap>true</wordwrap>' \
'  </widget>' \
'  <widget column="0" row="1" type="input::checkbox" columnspan="1" rowspan="1">' \
'   <name>cb</name>' \
'   <tooltip></tooltip>' \
'   <value>false</value>' \
'   <title>I Accept</title>' \
'  </widget>' \
'  <widget column="1" row="1" type="spacer::horizontal" columnspan="1" rowspan="1">' \
'   <name>spacer</name>' \
'   <tooltip></tooltip>' \
'   <minimum_size>0</minimum_size>' \
'   <maximum_size>-1</maximum_size>' \
'  </widget>' \
'  <widget column="0" row="2" type="input::file" columnspan="2" rowspan="1">' \
'   <name>file</name>' \
'   <tooltip></tooltip>' \
'   <type>directory</type>' \
'   <title>Choose File</title>' \
'   <default></default>' \
'   <limited>false</limited>' \
'   <file_types/>' \
'   <file_types_default></file_types_default>' \
'  </widget>' \
' </content>' \
'</dialog>')
	
	#
	# Event handler function called if anything happens inside of the dialog
	#
	def dialog_event_handler (widget):
		if DIALOG.cb.value == False:
			DIALOG.file.enabled = False
		else:
			DIALOG.file.enabled = True
		
		
		pass
	
	DIALOG.handler = dialog_event_handler
	
	RESULT=gom.script.sys.show_user_defined_dialog (dialog=DIALOG)
	
	
	filepath = RESULT.file
	
	return filepath

def main(filepath):
	
	ProgramInfo = os.path.join(os.getcwd(),"ProgramInfo")
	#ProgramInfo = r"Y:\AAC - Advanced Airfoil Components\19177-01 (2515 Fired Core)\Turn-Key Elements\EncryptMe"
	os.chdir(ProgramInfo)
	
	logging.info("-----------------------------------------------------New Run Started---------------------------------------------------------------------------")
	
		
	logging.info("Select Path : %s",filepath)
	
	
	datafolder = os.path.join(filepath,"Data")	
	if not os.path.exists(datafolder):
		os.mkdir(datafolder)
	
	logging.info("Data Folder Created")
	
	#gom.script.sys.create_project ()
	
	logging.info("Program Created")
	
	try:
	
		for file in os.listdir(ProgramInfo):
			if file.endswith(".gelements"):
				gom.script.sys.import_project (
				file=os.path.join(ProgramInfo,file), 
				import_mode='replace_elements')
				logging.info("%s Imported",file[:-10])
			
		CAD_ALIGNMENT=gom.script.alignment.create_prealignment (
			actual_element=gom.app.project.actual_elements['actual_master'], 
			computation_mode='enhanced', 
			compute_additional_bestfit=True, 
			name_expression='Prealignment', 
			nominal_element=gom.app.project.nominal_elements['all_cad_groups'], 
			parent_alignment=gom.app.project.alignments['Original alignment'])
			
		
		
		CAD_ALIGNMENT=gom.script.alignment.create_rps (
			general_constraint={'adjust_translate_x': True}, 
			max_search_distance=5.00000000e+01, 
			minimum_quota=0.00000000e+00, 
			name_expression='RPS', 
			parent_alignment=gom.app.project.alignments['Prealignment'], 
			rps_rules=[{'blocked': False, 'comparison': gom.app.project.inspection['A1'], 'constrain_category': 'tolerance_xyz', 'constraint': 'none', 'is_required': True, 'lower_limit': 0.00000000e+00, 'upper_limit': 0.00000000e+00, 'use_x': True, 'use_y': False, 'use_z': False}, {'blocked': False, 'comparison': gom.app.project.inspection['A2'], 'constrain_category': 'tolerance_xyz', 'constraint': 'none', 'is_required': True, 'lower_limit': 0.00000000e+00, 'upper_limit': 0.00000000e+00, 'use_x': True, 'use_y': False, 'use_z': False}, {'blocked': False, 'comparison': gom.app.project.inspection['A3'], 'constrain_category': 'tolerance_xyz', 'constraint': 'none', 'is_required': True, 'lower_limit': 0.00000000e+00, 'upper_limit': 0.00000000e+00, 'use_x': True, 'use_y': True, 'use_z': False}, {'blocked': False, 'comparison': gom.app.project.inspection['B1'], 'constrain_category': 'tolerance_xyz', 'constraint': 'none', 'is_required': True, 'lower_limit': 0.00000000e+00, 'upper_limit': 0.00000000e+00, 'use_x': False, 'use_y': True, 'use_z': False}, {'blocked': False, 'comparison': gom.app.project.inspection['B2'], 'constrain_category': 'tolerance_xyz', 'constraint': 'none', 'is_required': True, 'lower_limit': 0.00000000e+00, 'upper_limit': 0.00000000e+00, 'use_x': False, 'use_y': True, 'use_z': False}, {'blocked': False, 'comparison': gom.app.project.inspection['C6'], 'constrain_category': 'tolerance_xyz', 'constraint': 'none', 'is_required': True, 'lower_limit': 0.00000000e+00, 'upper_limit': 0.00000000e+00, 'use_x': False, 'use_y': False, 'use_z': True}])
		
		gom.script.sys.recalculate_project (with_reports=False)
		
		logging.info("Alignment Created")
		
	except Exception as c:
		
		logging.critical(c)
		gom.script.sys.exit_program()
	
	

	
	
	
	
	DIALOG=gom.script.sys.create_user_defined_dialog (content='<dialog>' \
	' <title>2515 Fired Core </title>' \
	' <style></style>' \
	' <control id="OkCancel"/>' \
	' <position></position>' \
	' <embedding></embedding>' \
	' <sizemode></sizemode>' \
	' <size width="213" height="246"/>' \
	' <content rows="6" columns="2">' \
	'  <widget column="0" type="label" columnspan="2" rowspan="1" row="0">' \
	'   <name>filenametxt</name>' \
	'   <tooltip></tooltip>' \
	'   <text>filename</text>' \
	'   <word_wrap>false</word_wrap>' \
	'  </widget>' \
	'  <widget column="0" type="label" columnspan="2" rowspan="1" row="1">' \
	'   <name>eaparttxt</name>' \
	'   <tooltip></tooltip>' \
	'   <text>ea step</text>' \
	'   <word_wrap>false</word_wrap>' \
	'  </widget>' \
	'  <widget column="0" type="display::progressbar" columnspan="2" rowspan="1" row="2">' \
	'   <name>eaprogressbar</name>' \
	'   <tooltip></tooltip>' \
	'   <value>0</value>' \
	'   <minimum>0</minimum>' \
	'   <maximum>100</maximum>' \
	'   <parts>1</parts>' \
	'   <step>0</step>' \
	'   <text>percentage</text>' \
	'   <mode>system</mode>' \
	'  </widget>' \
	'  <widget column="0" type="label" columnspan="2" rowspan="1" row="3">' \
	'   <name>stlcounttxt</name>' \
	'   <tooltip></tooltip>' \
	'   <text>STL Count:</text>' \
	'   <word_wrap>false</word_wrap>' \
	'  </widget>' \
	'  <widget column="0" type="label" columnspan="2" rowspan="1" row="4">' \
	'   <name>reportcounttxt</name>' \
	'   <tooltip></tooltip>' \
	'   <text>Report Count:</text>' \
	'   <word_wrap>false</word_wrap>' \
	'  </widget>' \
	'  <widget column="0" type="label" columnspan="1" rowspan="1" row="5">' \
	'   <name>totaltxt</name>' \
	'   <tooltip></tooltip>' \
	'   <text>Total Progress:</text>' \
	'   <word_wrap>false</word_wrap>' \
	'  </widget>' \
	'  <widget column="1" type="display::progressbar" columnspan="1" rowspan="1" row="5">' \
	'   <name>totalprogressbar</name>' \
	'   <tooltip></tooltip>' \
	'   <value>0</value>' \
	'   <minimum>0</minimum>' \
	'   <maximum>100</maximum>' \
	'   <parts>1</parts>' \
	'   <step>0</step>' \
	'   <text>percentage</text>' \
	'   <mode>manual</mode>' \
	'  </widget>' \
	' </content>' \
	'</dialog>')
	
	#
	# Event handler function called if anything happens inside of the dialog
	#
	def dialog_event_handler (widget):        
		
		def generate_snapshots():
							
			gom.script.sys.recalculate_project (with_reports=False)
			gom.script.cad.show_element_exclusively (elements=[gom.app.project.inspection['#2.dN'], gom.app.project.inspection['#5.dN'], gom.app.project.inspection['#6.dN'], gom.app.project.inspection['#1.dN'], gom.app.project.inspection['#7.dN'], gom.app.project.inspection['#8.dN'], gom.app.project.inspection['#3.dN'], gom.app.project.inspection['#4.dN'], gom.app.project.inspection['Surface comparison 1']])
			gom.script.view.set_yp (
				up_axis='X+', 
				use_animation=False, 
				widget='3d_view')
			gom.script.view.adjust_view_to_element_by_front_view (
				element=gom.app.project.inspection['Surface comparison 1'], 
				use_animation=False)
	
			
			gom.script.report.create_report_page (
				animated_page=False, 
				imitate_fit_mode='create', 
				master_name='Style_a3', 
				template_name='3D', 
				template_orientation='landscape', 
				title='')
			gom.script.cad.show_element_exclusively (elements=[gom.app.project.inspection['#15.dN'], gom.app.project.inspection['#14.dN'], gom.app.project.inspection['#12.dN'], gom.app.project.inspection['#9.dN'], gom.app.project.inspection['#10.dN'], gom.app.project.inspection['#13.dN'], gom.app.project.inspection['#16.dN'], gom.app.project.inspection['#11.dN'], gom.app.project.inspection['Surface comparison 1']])
			gom.script.view.set_ym (
				up_axis='X+', 
				use_animation=False, 
				widget='3d_view')
			gom.script.view.adjust_view_to_element_by_front_view (
				element=gom.app.project.inspection['Surface comparison 1'], 
				use_animation=False)
			gom.script.report.create_report_page (
				animated_page=False, 
				imitate_fit_mode='create', 
				master_name='Style_a3', 
				template_name='3D', 
				template_orientation='landscape', 
				title='')
				
		
			
		def delete_snapshots():
			for report in gom.app.project.reports:
				gom.script.cad.delete_element (
					elements=[report], 
					with_measuring_principle=True)
					
		snapshots = False
		
		try:
		
			for file in os.listdir(filepath):
				
				if file.endswith(".stl"):
					
					stlCounter = len(glob.glob1(filepath,"*.stl"))
					csvCounter = len(glob.glob1(os.path.join(filepath,"Data"),"*.csv"))
					DIALOG.stlcounttxt.text = "STL Count: {}".format(stlCounter)
					DIALOG.reportcounttxt.text = "Report Count: {}".format(csvCounter)
					incr = 100/stlCounter
					
					
					filename = file[:-4]
					DIALOG.filenametxt.text = filename
					
					DIALOG.eaparttxt.text = "Importing STL"
					gom.script.sys.import_stl (
						bgr_coding=True, 
						files=[os.path.join(filepath,file)], 
						geometry_based_refining=False, 
						import_mode='replace_elements', 
						length_unit='inch', 
						stl_color_bit_set=False, 
						target_type='mesh')
						
					logging.info("%s.stl Imported", filename)
					
					
					
					generate_snapshots()
					
					DIALOG.eaparttxt.text = "Recalculating Project"
					gom.script.sys.recalculate_project (with_reports=True)
					
					DIALOG.eaparttxt.text = "Exporting Data"
					gom.script.sys.delay_script (time=1)
					
					gom.script.table.export_table_contents (
						cell_separator=',', 
						codec='iso 8859-1', 
						decimal_separator='.', 
						elements=[gom.app.project.inspection['A1.dN'], gom.app.project.inspection['B1.dN'], gom.app.project.inspection['A2.dN'], gom.app.project.inspection['B2.dN'], gom.app.project.inspection['A3.dN'], gom.app.project.inspection['C6.dN'], gom.app.project.inspection['#16.dN'], gom.app.project.inspection['#13.dN'], gom.app.project.inspection['#11.dN'], gom.app.project.inspection['#15.dN'], gom.app.project.inspection['#12.dN'], gom.app.project.inspection['#14.dN'], gom.app.project.inspection['#4.dN'], gom.app.project.inspection['#1.dN'], gom.app.project.inspection['#2.dN'], gom.app.project.inspection['#3.dN'], gom.app.project.inspection['#5.dN'], gom.app.project.inspection['#6.dN'], gom.app.project.inspection['#7.dN'], gom.app.project.inspection['#8.dN'], gom.app.project.inspection['#9.dN'], gom.app.project.inspection['#10.dN']], 
						file='{}.csv'.format(os.path.join(datafolder,filename)), 
						header_export=True, 
						line_feed='\n', 
						sort_column=0, 
						sort_order='ascending', 
						template_name='Overview', 
						text_quoting='', 
						write_one_line_per_element=False)
					
					gom.script.report.export_pdf (
						export_all_reports=True, 
						file='{}.pdf'.format(os.path.join(datafolder,filename)), 
						jpeg_quality_in_percent=100)
						
					delete_snapshots()
					
					
					logging.info("%s.stl Data Exported", filename)
					
					DIALOG.totalprogressbar.value += incr
			gom.script.sys.close_user_defined_dialog (dialog=DIALOG)
			
		except Exception as d:
			logging.critical("----------------------------------------------------------------------------------------------------------------------------------------------")
			logging.critical(d)
			logging.critical("----------------------------------------------------------------------------------------------------------------------------------------------")
			gom.script.sys.close_user_defined_dialog (dialog=DIALOG)
			
		
		pass
	
	DIALOG.handler = dialog_event_handler
	RESULT=gom.script.sys.show_user_defined_dialog (dialog=DIALOG)
	
	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%m_%d_%y_%H_%M_%S')
	
	
	os.rename(os.path.join(filepath,"Data"),os.path.join(filepath,"Data {}".format(st)))
	logging.info("----------------------------------------------------------------------------------------------------------------------------------------------")
	gom.script.sys.exit_program()


	


if __name__ == '__main__':
	
	try:
		folder = Legal()
		SetLogger(folder)
		main(folder)
		gom.script.sys.exit_program()
	except Exception as e:
		logging.critical("----------------------------------------------------------------------------------------------------------------------------------------------")
		logging.critical(e)
		logging.critical("----------------------------------------------------------------------------------------------------------------------------------------------")
		gom.script.sys.exit_program()