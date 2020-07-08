import os
import pyodbc

import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=SQLPC\SQL17;'
                      'Database=KIOSK_TestDB;'
                      'uid=kiosk;'
					  'pwd=Pyth0nr0x1318')
 
cursor = conn.cursor()


root = r'\\dc01\layout_reports\Kiosk'

dict

items_dict = {'Card':'Cardigan','Tee':'T-Shirt','Zip':'Hoodie(Zipped)','Hood':'Hoodie','Polo':'Polo','Heavy':'Heavy Jacket','Vest':'Vest'}
color_list = ['Black','Blue','White','Purple','Gray','Grey','Red','Orange','Green','Brown']


for file in os.listdir(root):
	sex = None
	modifier = None
	color = None
	item = None
	
	if file.startswith('W '):
		sex = "Women''s"
	elif file.startswith('M '):
		sex = "Men''s"

	if 'Dk' in file:
		modifier = 'Dark'
	elif 'Lt' in file:
		modifier = 'Lite'

	for key,value in items_dict.items():
		if key in file:
			item = items_dict[key]

	if item == None:
		item = 'Pullover'

	for c in color_list:
		if c in file:
			color = c

	if modifier != None:
		color = f"{modifier} {color}"

	if sex != None:
		item = f"{sex} {item}"

	file = os.path.join(root,file)

	cursor.execute(f"insert into ApparelPhotos (Item,Color,Photo) VALUES('{item}','{color}',(SELECT BulkColumn FROM Openrowset( Bulk '{file}', Single_Blob) as img))")

	conn.commit()