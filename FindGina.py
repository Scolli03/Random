import os
from LoggerManager import Logger
import timeit

log = Logger().make_logger('FindGina',location=r'C:\Users\shainc\Desktop\Random Scripts')

def file_search_by_ext(rootpath, ext):
    gina_files = []
    count = 0
    ginas = 0
    for root, dirs, files in os.walk(rootpath):
        for file in files:
            count +=1
            print(f'---------- Files Scanned {count} | Gina Files {ginas}', end='\r',flush=True)
            if file.endswith(ext):
                ginas += 1
                log.info(os.path.join(root,file))
                print(f'---------- Files Scanned {count} | Gina Files {ginas}', end='\r',flush=True)

def folder_search_by_name(rootpath, name):
    count = 0
    nf = []
    nfcount = 0
    for root, dirs, files in os.walk(rootpath):
        for folder in dirs:
                count += 1
                print(f'---------- Folders Scanned {count} | New Folders Found {nfcount}----------', end='\r',flush=True)
                if name in folder:
                    nfcount += 1
                    log.info(os.path.join(root,folder))
                    print(f'---------- Folders Scanned {count} | New Folders Found {nfcount}----------', end='\r',flush=True)


if __name__ == "__main__":
    start = timeit.default_timer()
    folder_search_by_name(r'\\dc01\layout_reports','New Folder')
    stop = timeit.default_timer()

