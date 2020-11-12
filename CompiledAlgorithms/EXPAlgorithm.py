import matplotlib.pyplot as plt
import pandas
import csv
import datetime
import numpy as np
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.cluster import OPTICS
from sklearn.decomposition import PCA
from tqdm import tqdm

from .elbowMethod import Elbow
from .ENVI_Files import Envi
from .ClusteringAlgorithm import ClusteringAlgorithm


class DominantColorsEXP(ClusteringAlgorithm):

    def __init__(self, path, imageName, resultFolderDir, cluster_override, decimate_factor):
        super().__init__(path, imageName, resultFolderDir, cluster_override, decimate_factor)
        self.ALG = 'EXP'

    def cluster(self, img):
        # Runs the Scikitlearn algorithm with the determined number of clusters
        clustering = OPTICS(min_samples=2).fit(img)
        # Centroids are the "average clusters" of each cluster
        # Labels are numbers denoting which cluster each pixel belongs to (Pixel location corresponds with the label's
        # index.
        # Ex. Label = [0, 4, 1, 2, 3, 1, 4, 0, 0..... 1, 2], where 0 would be cluster 0, 1 would be cluster 1, etc...
        # and pixel at (0, 0) would belong to cluster 0.
        self.LABELS = clustering.labels_
        self.CENTROIDS = self.find_centers()

    def findDominant(self):
        img = super().findDominant()
        try:
            self.cluster(img)
        except NameError:
            print("not found")
        self.plot()
        return self.RESULT_PATH
