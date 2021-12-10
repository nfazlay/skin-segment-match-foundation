import sys
sys.path.append(".")
import numpy as np
from modules.detectskin import DetectSkin
from modules.domcolor import DominantColors
from modules.predictcolor import PredictColor

def main():
    d = DetectSkin()
    d.run()

    c = DominantColors()
    color = c.run()
    
    p = PredictColor(color)
    print(p.run())

if __name__ == "__main__":
    main()





