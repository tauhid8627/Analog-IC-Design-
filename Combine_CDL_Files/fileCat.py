import os
import re
import sys

if len(sys.argv) != 4:
	print("///Syntax: fileCat.py <fileRegeX> <outputFileName> <Directory>///")
	sys.exit(1)

pattern = sys.argv[1]
output_name = sys.argv[2]
directory = sys.argv[3]

output_path = os.path.join(directory, output_name)
files = os.listdir(directory)
contents = []

print("//////////////////////////////////")
print("Files Found:")

for filename in files:
	if re.search(pattern, filename):
		inFile = os.path.join(directory, filename)
		try:
			with open(inFile, encoding="utf-8") as f:
				filecont = f.read()
			print(f"\t{filename}")
			contents.append("####"+filename+"####")
			contents.append(filecont)
		except Exception as e:
			print(f"\tError reading {filename}: {e}")

with open(output_path, "w", encoding="utf-8") as f:
	f.write("\n".join(contents))

print("//////////////////////////////////")
print("Combined file saved as:")
print(os.path.realpath(output_path))
print("//////////////////////////////////")