import csv
import math
from PIL import ImageColor


class PredictColor:

    FILE_PATH = './dataset/allCategories.csv'

    def __init__(self, color):
        self.colorToPredict = color
        self.least = 450 #441.6729559300637
        self.predicted = None

    def run(self):
        with open(self.FILE_PATH, 'r', encoding="utf8") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                hex = str(row[7])
                d = 0
                try:
                    convert = ImageColor.getcolor(hex, "RGB")
                    d = math.sqrt(((convert[0]-self.colorToPredict[0]))**2 + ((convert[1]-self.colorToPredict[1]))**2 + ((convert[2]-self.colorToPredict[2]))**2)
                    if d<self.least:
                        self.least = d
                        self.predicted = row

                except:
                    continue

        return self.predicted
        
