import os
count = 0
for root, dirs, files in os.walk(r'Z:\Shain'):
    for file in files:
        if file.endswith(".stl"):
                    count += 1

print(count)
                    
