import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import tkinter
from mpl_toolkits.mplot3d import Axes3D

class DominantColors:

    CLUSTERS = None
    IMAGE = "./images/test.png"
    COLORS = None
    COLOR = None
    LABELS = None

    
    def __init__(self, clusters=2):
        self.CLUSTERS = clusters
        
    def run(self):
    
        #read image
        img = cv2.imread(self.IMAGE)
        
        #convert to rgb from bgr
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                
        #reshaping to a list of pixels
        img = img.reshape((img.shape[0] * img.shape[1], 3))
        
        #save image after operations
        self.IMAGE = img
        
        #using k-means to cluster pixels
        kmeans = KMeans(n_clusters = self.CLUSTERS)
        kmeans.fit(img)

        
        #the cluster centers are the dominant colors.
        self.COLORS = kmeans.cluster_centers_

        #save labels
        self.LABELS = kmeans.labels_

        
        #returning after converting to integer from float
        self.COLORS = self.COLORS.astype(int)

        print(self.COLORS)

        self.COLOR = np.add(self.COLORS[0], self.COLORS[1])

        return self.COLOR