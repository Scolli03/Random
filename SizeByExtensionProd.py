import os
import statistics
import re
from zipfile import ZipFile as zf, BadZipFile
import timeit
from datetime import datetime as dt
from LoggerManager import Logger

log = Logger().make_logger('Customers2',location=r"C:\Users\shainc\Desktop\Random Scripts")
start = timeit.default_timer()
count = 0
sizes = []
fileinfo = {}
extentions = [".stp",".igs",".prt",".stl",".pdf",".csv",".xls",".xlsx",".xlsm"]

for root, dirs, files in os.walk(r"\\File02\GE_Layout"):
    for file in files:
        fullpath = os.path.join(root,file)
        ext = re.search(r'\.\w+$',file).group()
        if ext == '.zip':
            try:
                with zf(os.path.join(root,file)) as myzip:
                    zfiles = myzip.infolist()
                    for zfile in zfiles:
                        zext = re.search(r'\.\w+$',zfile.filename).group()
                        if zext in extentions:
                            fileinfo[f'{zfile.filename}-{zfile.date_time}'] = [zext,round(zfile.file_size/(1024^3))]
                            sizes.append(zfile.file_size)
                            count += 1
            except BadZipFile:
                continue
        elif ext in extentions:
            datemod = dt.fromtimestamp(os.path.getmtime(fullpath)).date()
            fileinfo[f'{file}--{datemod}'] = [ext,round(os.path.getsize(fullpath)/(1024^3))]
            sizes.append(os.path.getsize(os.path.join(root,file)))
            count += 1
if len(sizes) != 0:
    log.info(f"Filetype: {ext}")
    log.info(f"Count: {count}")
    log.info(f"Sum: {round(sum(sizes)/(1024*1024*1024),4)} GB")
    log.info(f"Max: {round(max(sizes)/(1024*1024*1024),4)} GB")
    log.info(f"Avg: {round(statistics.mean((sizes))/(1024*1024*1024),4)} GB")
    log.info("")

count = 0
sizes = []

stop = timeit.default_timer()
log.info(f'Time: {stop-start}')  
                    
