import csv
import math
from PIL import ImageColor

file = './allCategories.csv'

color = (157, 133, 122)
#color = (255, 255, 255)
least = 450 #441.6729559300637
prow = None


with open(file, 'r', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        hex = str(row[7])
        d = 0
        try:
            convert = ImageColor.getcolor(hex, "RGB")
            d = math.sqrt(((convert[0]-color[0]))**2 + ((convert[1]-color[1]))**2 + ((convert[2]-color[2]))**2)
            if d<least:
                least = d
                prow = row

        except:
            continue

print(prow)
        
