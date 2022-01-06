import csv
import math
from PIL import ImageColor
from queue import PriorityQueue


class PredictColor:

    FILE_PATH = './dataset/allCategories.csv'

    def __init__(self, color):
        self.colorToPredict = color

    def run(self):
        q = PriorityQueue()
        with open(self.FILE_PATH, 'r', encoding="utf8") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                hex = str(row[7])
                try:
                    convert = ImageColor.getcolor(hex, "RGB")
                    d = math.sqrt(((convert[0]-self.colorToPredict[0]))**2 + ((convert[1]-self.colorToPredict[1]))**2 + ((convert[2]-self.colorToPredict[2]))**2)
                    q.put((d, row))

                except:
                    continue

        return q.get()[1]
        
