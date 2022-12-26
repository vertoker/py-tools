from PIL import Image
import easygui as gui
import random

width = 40
height = 40
graphSize = 3
wallThickness = 1
borders = True
length = width * height
offsetSize = graphSize + wallThickness

pathSave = gui.filesavebox(default = 'maze.png')# open(, 'w').write(data[2])
dirs = { 0 : "UP", 1 : "DOWN", 2 : "LEFT", 3 : "RIGHT" }

class Cell:
    def __init__(self):
        self.right = True
        self.bottom = True
        self.visited = False

maze = []
for x in range(width):
    maze.append([])
    for y in range(height):
        maze[x].append(Cell())

currentPoint = [random.randint(0, width - 1), random.randint(0, height - 1)]
maze[currentPoint[0]][currentPoint[1]].visited = True
print(str(currentPoint), end = " ")
visited_cells = 1

print("generate maze")
print("length equals " + str(length))
while visited_cells < length:
    direction = random.randint(0, 3)
    inverseDirection = direction + 1 if direction % 2 == 1 else direction - 1
    lastPoint = [currentPoint[0], currentPoint[1]]

    if direction == 0 and currentPoint[1] > 0:
        currentPoint[1] -= 1
    elif direction == 1 and currentPoint[1] < height - 1:
        currentPoint[1] += 1
    elif direction == 2 and currentPoint[0] > 0:
        currentPoint[0] -= 1
    elif direction == 3 and currentPoint[0] < width - 1:
        currentPoint[0] += 1

    if not maze[currentPoint[0]][currentPoint[1]].visited:
        visited_cells += 1
        print("cell #" + str(visited_cells) + " is add from " + str(dirs[direction]) + " direction")
        #print(str(lastPoint) + " -> " + str(currentPoint), end = " ")
        if direction == 0:
            maze[currentPoint[0]][currentPoint[1]].bottom = False
        elif direction == 1:
            maze[lastPoint[0]][lastPoint[1]].bottom = False
        elif direction == 2:
            maze[currentPoint[0]][currentPoint[1]].right = False
        elif direction == 3:
            maze[lastPoint[0]][lastPoint[1]].right = False
        maze[currentPoint[0]][currentPoint[1]].visited = True

white = (255, 255, 255)
black = (0, 0, 0)

print()
print("generate image")
imgWidth = width * (graphSize + wallThickness) + wallThickness
imgHeight = height * (graphSize + wallThickness) + wallThickness
img = Image.new('RGB', (imgWidth, imgHeight))

data = []
for x in range(imgWidth):
    for y in range(imgHeight):
        data.append(white)

for x in range(width + 1):
    for y in range(height + 1):
        posWidth = x * offsetSize
        posHeight = y * offsetSize
        data[posHeight * imgWidth + posWidth] = black

for x in range(width):
    for y in range(height):
        posWidth = (x + 1) * offsetSize
        posHeight = (y + 1) * offsetSize
        if maze[x][y].right:
            for i in range(1, graphSize + 1):
                data[(posHeight - i) * imgWidth + posWidth] = black
        if maze[x][y].bottom:
            for i in range(1, graphSize + 1):
                data[posHeight * imgWidth + posWidth - i] = black

if borders:
    for x in range(imgWidth):# Top
        data[x] = black
    for x in range(imgWidth):# Bottom
        data[(imgWidth - 1) * imgHeight + x] = black
    for y in range(imgHeight):# Left
        data[y * imgWidth] = black
    for y in range(1, imgHeight + 1):# Right
        data[y * imgWidth - 1] = black

img.putdata(data)
img.save(pathSave, "PNG", optimize=False, compress_level=0)
