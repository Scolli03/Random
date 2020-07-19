import os
import statistics
import re
from zipfile import ZipFile as zf, BadZipFile
import timeit
from LoggerManager import make_logger

def sizeof_fmt(num, suffix='B'):
    for unit in ['','KB','MB','GB','TB','PB','EB','ZB']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

def find_by_extenstion(startdir):    
    start = timeit.default_timer()
    count = 0
    sizes = []
    extentions = [".stp",".igs",".prt",".stl",".pdf",".csv",".xls",".xlsx",".xlsm"]
    for ext in extentions:
        for root, dirs, files in os.walk(startdir):
            for file in files:
                if re.search(r'\d+\-\d+',os.path.join(root,file)):
                    if file.endswith('.zip'):
                        try:
                            with zf(os.path.join(root,file)) as myzip:
                                zfiles = myzip.infolist()
                                for zfile in zfiles:
                                    if zfile.filename.endswith(ext):
                                        sizes.append(zfile.file_size)
                                        count += 1
                        except BadZipFile:
                            continue
                    elif file.endswith(ext):
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

    if __name__ == "__main__":
        log = make_logger('LogByExtenstion')
        find_by_extenstion()
