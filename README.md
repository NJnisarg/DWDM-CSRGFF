## Data Warehousing Data Mining Mini Project

### Members
- Nisarg S. Joshi (171CO226)
- Yash M. Agarwal (171CO253)

### Introduction
This project is with respect to the course CO461-Data Warehousing and Data Mining(DWDM). The aim of the project is to carry out the analysis, implementation and reproduce the results of the following research work in the domain of hyperspectral image classification:
[Cascade Superpixel Regularized Gabor Feature
Fusion for Hyperspectral Image Classification](CSRGFF.pdf)

### Overview of the research paper
A 3-D Gabor wavelet provides an effective way to obtain the spectral–spatial-fused features for hyperspectral image, which has shown advantageous performance for material classification and recognition. In this paper, instead of separately employing the Gabor magnitude and phase features, which, respectively, reflect the intensity and variation of surface materials in local area, a cascade superpixel regularized Gabor feature fusion (CSRGFF) approach has been proposed. First, the Gabor filters with particular orientation are utilized to obtain Gabor features (including magnitude and phase) from the original hyperspectral image. Second, a support vector machine (SVM)-based probability representation strategy is developed to fully exploit the decision information in SVM output, and the achieved confidence score can make the following fusion with Gabor phase more effective. Meanwhile, the quadrant bit coding and Hamming distance metric are applied to encode the Gabor phase features and measure sample similarity in sequence. Third, the carefully defined characteristics of two kinds of features are directly combined together without any weighting operation to describe the weight of samples belonging to each class. Finally, a series of superpixel graphs extracted from the raw hyperspectral image with different numbers of superpixels are employed to successively regularize the weighting cube from over-segmentation to under-segmentation, and the classification performance gradually improves with the decrease in the number of superpixels in the regularization procedure. Four widely used real hyperspectral images have been conducted, and the experimental results constantly demonstrate the superiority of the CSRGFF approach over several state-of-the-art methods.

### Project goals
The goals of the project is to analyze, implement and reproduce the results of the proposed method. We try to divide the work into different components and try to analyze and implement each component and them build the entire model. We have identified the following components:

1.) 3D Gabor Filter convolution
2.) Entropy Rate Superpixel Segmentation
3.) SVM based confidence Cube from Magnitude features
4.) Quadrant bit encoding and hamming distance cube from Phase features
5.) Cascading of the weighing cube with the superpixel graphs and carrying out classification

We will try to implement 1-2 features every week with the following schedule described in next section

### Schedule

#### Week 0 (14th Oct - 20th Oct)
- Read about hyperspectral images
- Read about classification of hyperspectral images
- Read the given paper in detail
- Read about superpixel clustering
- Read about SVM and Confidence scores
- Read about Gabor filters

#### Week 1 (21st Oct - 28th Oct)
- Read in detail about 3D Gabor Filter and how to build one
- Coded a 3D Gabor Filter for hyperspectral images
- Read about Entropy Rate Superpixel(ERS) Clustering
- Implemented and tweaked ERS for hyperspectral images

#### Week 2 (29th Oct - 3rd Nov)
- Read in detail about SVM based confidence cube formation
- Implement the SVM based confidence Cube
- Read about Quadrant Bit Encoding and Hamming distance
- Implement Quadrant Bit Encoding and Hamming distance

#### Week 3 (4th Nov - 11th Nov)
- Read about cascading of the weighing cube with the superpixel graphs and carrying out classification.
- Implement cascading of the weighing cube with the superpixel graphs and carrying out classification.
- Generate the results and graphs for the entire model.

#### Week 4 (12th Nov - 16th Nov)

- Complete the report along with all the literature, code, graphs and results.
- Final Submission