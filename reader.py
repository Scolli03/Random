import sys
import mmap

exec(mmap.mmap(-1,int(sys.argv[1]),"inspectScript",mmap.ACCESS_READ).read(int(sys.argv[1])).decode('utf-8').strip('\x00'))





