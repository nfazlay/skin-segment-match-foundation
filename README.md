# Skin segment match foundation

# Introduction

The detection of skin color has a wide range of applications, ranging
from diagnostics and human-computer interactions . Skin detectors use
various computing technologies and techniques to differentiate between
skin and non-skin. Artificial Intelligence can leverage skin detection
technology to widen the range of applications to streamline human
tasks. 

# Project Overview

## Use Case(s)

**Name:** Predict foundation shade use case using console  
**Actors:** User (Primary)  
**Precondition:** User is familiar with the environment (console)  
**Description:**  
User runs the main program  
The camera dialog displays, allowing user to position face  
The user presses q once they are satisfied  
The foundation that best matches the user’s skin-tone is displayed on
the environment (console)  
**Postcondition:** The user gets the matched foundation through the link
of the website


## Methods and Discussion

### Color Image Segmentation

Image segmentation is the process of partitioning a digital image into
regions that is easier to analyze . It is a process of labeling every
pixel in an image that shares certain visual characteristics . Various
features found in the image such as color information can be used to
create histograms or extract information about edges, boundaries, or
texture .  
Image segmentation methods are based on two image properties,
discontinuity, and similarity . Boundary-based methods leverages
discontinuity, while region-based methods use similarity . Image
segmentation methods can also be categorized as supervised or
unsupervised. Supervised methods are dependent on known pixel
attributes, while unsupervised methods do not need priori information .
**Thresholding** is an unsupervised region-based method for color image
segmentation.  
Thresholding classifies regions based on range values provided by the
user . Pixels that fall within the range of threshold values are
considered accepted and partitioned from the rest of the image. The
color space that the image uses is important; it determines what
threshold range the user should apply. As different color spaces provide
different results for different images, authors usually specify the
color space that best suits their specifications . The color spaces can
be *RGB, CMY, HSV* etc.  
The project uses *Thresholding* as a color image segmentation method to
filter out skin from the rest of the image. The image is converted from
RGB to HSV color space, similar to the human perception of color . The
range of values that were used to classify skin are as follows:

min HSV = \[0, 48, 80\]  
max HSV = \[20, 255, 255\]

The *Thresholding* method of color image segmentation provides a
computationally inexpensive and fast means to partition images .
However, this is not the optimal solution to detect skin. For instance,
the background may fall within the provided color range, and it would be
classified as skin. The result will vary under a different light source;
hence inconsistency may arise. More importantly, the range is biased
towards a particular skin type and needs to be updated for other skin
types in the [Fitzpatrick skin
phototype](https://dermnetnz.org/topics/skin-phototype).  
An alternative color image segmentation method is the *Split and Merge
technique*. This method continuously splits images depending on some
criterion and then merges them. It then uses standard deviation to
compute similarity. An image of low variance is then output as a result
.

### K-means clustering

Clustering is the process of grouping data into disjoint clusters so
that data in the same cluster are similar . K-means is one of the most
popular clustering methods. K-means uses a relocating and updating
process to cluster data. Each point is relocated to the nearest cluster
center, which is then updated by calculating the mean of all member
points . The initial k-clusters are formed by initializing techniques
such as foggy initialization (randomly choosing k data points) to more
sophisticated methods like density-based initialization .  
The project leverages Python’s SkLearn library to cluster segmented
images, such as that in figure 8. The number of clusters is set to two
as it assumes that only black and skin exists in the image.

One limitation of the above method is that the cluster centers do not
necessarily represent the true skin tone. The predefined number of
clusters means that *mean of all skin shades* is used to calculate the
cluster center(s). This method provides unreliable results when the face
contains different shades due to lighting conditions.

Sinaga et al. proposed an unsupervised K-means clustering algorithm that
does not require initialization with a fixed number of clusters a priori
. The K-means algorithm finds the optimal number of clusters without any
parameter. A Machine Learning approach can filter out clusters that do
not represent skin and provide better results.

### Heuristic search

Heuristic Search finds the optimal solution based on given heuristics. A
greedy heuristic search implements the frontier as a Priority Queue and
estimates the cost to get from n to the goal state using the heuristic
*h(n)*.  

The linear dimensions defining a color space are distances from one
shade to another within the color space. To find the difference between
two colors, measure the *Euclidean* distance between the colors’ RGB
values.

In the project, the euclidean formula is used as a heuristic to
calculate the distance between predicted skin tone and the foundation
shade from the dataset. A lower euclidean distance would signify greater
similarity as RGB values follow a continuous shade. The heuristic is
admissible as *h(n, n) \< h (n, n’)*, where n is the predicted color and
n’ is the foundation shade. 

RGB color values do not consider the degree to which human vision has
tolerance to colors. A limitation of the above algorithm is that the RGB
values do not best fit human perception. The [International Commission
on Illumination](http://cie.co.at/) proposed *Delta E* as a measure of
change in visual perception given two colors. The CIDE2000 color
difference formula, or *Delta E*, could be used as a heuristic as it
measures how the human eye perceives the color difference .

## Dataset

The dataset used was collected from
[data.world](https://data.world/amberthomas/foundation-products). The
dataset contains the links, names, colors for 5308 foundation shades
available online from 93 brands (see allCategories.csv). The Hex value
of each shade was calculated using the *jpeg, magick, and imager*
[packages](https://cran.r-project.org/web/packages/) in R programming
language.

## Results

The expected result of each module has been described in . The predicted
foundation shade that best matches the skin tone and the K-means cluster
centers are is displayed on the console when the main program is run.
The program redirects the user to the webpage of the foundation shade
after extracting the URL from the dataset. The user can view the
original and intermediary images under the *images* directory.

## Measure of Performance

*Mean-square error* between the **predicted skin tone** and **true skin
tone** is used as a measure of performance.

Skin color can be measured using a spectroradiometer and a spheric
lighting device with a CCD camera to ensure reliable imaging and data
acquisition (Observed values) .

The cluster center for skin can be obtained under the same lighting
conditions using the program (predicted values).

# Conclusion

Historically, the primary use of skin color detection was to assist
diagnosis in the medical field . The emergence of new technologies is
widening the applications of skin color detection. For instance, the
detected skin color can be used to augment reality by putting virtual
masks on faces, as seen on various Instagram filters. This project
explores how skin detection and methods from Artificial Intelligence can
automate the human task of finding suitable foundation shade. Avenues
for future development include adding a web crawler that scrapes the
internet for foundation shades rather than a fixed dataset. Collecting
and aggregating Big data and consumer analytics through AI from
different sources can help better understand the user as an individual .
As a result, it will be possible to recommend foundation shades
personalized to the user’s liking. The project will be published on
open-source platform like Github to accommodate future enhancements.

# Acknowledgement

I convey my gratitude to Amber Thomas for creating the Foundations
dataset and sharing it.
