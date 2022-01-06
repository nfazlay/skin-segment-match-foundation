import sys
sys.path.append(".")
import webbrowser
from modules.detectskin import DetectSkin
from modules.domcolor import DominantColors
from modules.predictcolor import PredictColor

def main():
    d = DetectSkin()
    d.run()

    c = DominantColors()
    color = c.run()
    
    p = PredictColor(color)

    foundation = p.run()
    print(foundation)
    webbrowser.open(foundation[2])

if __name__ == "__main__":
    main()





