import os
import shutil

def get_path(message):
    path = input(message)
    if os.path.exists(path):
        return path
    return get_path()

def get_all_files(path):
    paths = []
    for x in os.walk(path):
        paths.extend([os.path.join(x[0], y) for y in x[2]])
    return paths

sourceFrom = get_path("Enter sourceFrom directory: ")
sourceTo = get_path("Enter sourceTo directory: ")

print("Get all filenames...")
paths = get_all_files(sourceFrom)

names = []
for srcPath in paths:
    name = srcPath.replace(sourceFrom, '')#os.path.basename()
    name = name.replace('/', '.').replace('\\', '.')
    names.append(name)
    
    dstPath = sourceTo + "/" + name
    shutil.copyfile(srcPath, dstPath)
    
    print(srcPath)
    #shutil.copy(srcPath, sourceTo)
    #print(os.path.basename(path))

#dublicates = {i:names.count(i) for i in names}
#print(dublicates)
#for x, y in dublicates.items():
    #if y > 1:
        #print(x, y)
