import os
import re

for root, dirs, files in os.walk(r"\\File02\GE_Layout"):
	for dir in dirs:
		if 'production' not in os.path.join(root,dir).lower():
			if re.match(r'\d+\-\d+',dir):
				print(os.path.join(root,dir))