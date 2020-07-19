import os
import statistics
import re
from zipfile import ZipFile as zf, BadZipFile
import timeit
from LoggerManager import make_logger
from datetime import datetime
import csv
import sys
log = make_logger("SizeByExtenstion")

def getextenstion(file,filepath = None):
	try:
		return re.search(r'\.\w+$',file).group()
	except AttributeError as e:
		if filepath == None:
			log.info(f"{e},{file}")
		else:
			log.info(f"{e},{filepath} | {file}")
		return None

def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

def search_directory(rootpath):
	extentions = [".stp",".igs",".prt",".stl",".pdf",".csv",".xls",".xlsx",".xlsm"]
	fileinfo = []
	count = 0
	for root, dirs, files in os.walk(rootpath):
		for file in files:
			fullpath = os.path.join(root,file)
			count += 1
			print(f"---------- Files Scanned {count} ----------", end='\r',flush=True)
			ext = getextenstion(fullpath)
			if ext == None:
				continue			
			if file.endswith('.zip'):
				try:
					with zf(os.path.join(root,file)) as myzip:
						zfiles = myzip.infolist()
						for zfile in zfiles:
							count += 1
							print(f"---------- Files Scanned {count} ----------", end='\r',flush=True)
							zext = getextenstion(zfile.filename, fullpath)
							if zext == None:
								continue
							if zext in extentions:
								date = datetime(year=zfile.date_time[0],
												month=zfile.date_time[1],
												day=zfile.date_time[2]
												).date()
								fileinfo.append([date,
												f"{fullpath} ({zfile.filename.replace('Ω','')})",
												zext,
												sizeof_fmt(zfile.file_size)])
				except BadZipFile:
					continue
			elif ext in extentions:
				fileinfo.append([datetime.fromtimestamp(os.path.getmtime(fullpath)).strftime('%Y-%m-%d'),
				fullpath.replace('Ω',''),
				ext,
				sizeof_fmt(os.path.getsize(os.path.join(root,file)))])
	return fileinfo, count

def write_csv(infolists):
	with open('SizeByExtenstion.csv','w', newline='') as file:
		writer = csv.writer(file)
		writer.writerow(['Date','File','Type','Size'])
		for row in infolists:
			try:
				writer.writerow(row)
			except Exception as e:
				log.error(f"Failed to write {row}")

if __name__ == "__main__":
	start = timeit.default_timer()
	rootpath = r"Your\starting\location"	
	log.info('---------------------------Start---------------------------')		
	data,count = search_directory(rootpath)
	write_csv(data)
	stop = timeit.default_timer()
	log.info(f'Root: {rootpath} | Time: {(stop-start)/60} min. | Total Findings: {len(data)} | Total Checked: {count}')