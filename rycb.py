import os

def get_path():
	path = input("Enter path to directory: ")
	if os.path.exists(path):
		return path
	return get_path()


def get_all_filenames(path):
	filenames = []
	for x in os.walk(path):
		filenames.extend([os.path.join(x[0], y) for y in x[2]])
	return filenames

path = get_path()
print("Get all filenames...")
filenames = get_all_filenames(path)

# Analyzing
print("Analyzing...")
# [count, countOfLines, countOfSymbols]
data = {}

for name in filenames:
	extension = name.split('.')[-1]
	try:
		lines = open(name, 'r').readlines()

		if extension not in data:
			data.update({extension: [0, 0, 0]})

		data[extension][0] += 1
		data[extension][1] += len(lines)
		data[extension][2] += sum(len(line) for line in lines)
	except:
		pass

# Output
print("/////////////////////////////////")
print("REPORT")
print("/////////////////////////////////")
print()

all_extensions = [0, 0, 0]
for extension in data:
	print('.', extension, sep = '')
	print("Count of files:", data[extension][0])
	print("Count of lines in files:", data[extension][1])
	print("Count of symbols in files:", data[extension][2])
	print()
	all_extensions[0] += data[extension][0]
	all_extensions[1] += data[extension][1]
	all_extensions[2] += data[extension][2]

print("/////////////////////////////////")
print("Count of all files:", all_extensions[0])
print("Count of all lines in files:", all_extensions[1])
print("Count of all symbols in files:", all_extensions[2])

input("\n\nEnter to close... ")
