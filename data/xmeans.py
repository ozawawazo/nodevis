import numpy as np
from scipy import stats
from sklearn.cluster import KMeans
import csv

directory = 'pen/'

class XMeans:
 
    def __init__(self, k_init = 4, **k_means_args):
        self.k_init = k_init
        self.k_means_args = k_means_args
 
    def fit(self, X):
        self.__clusters = [] 
 
        clusters = self.Cluster.build(X, KMeans(self.k_init, **self.k_means_args).fit(X))
        self.__recursively_split(clusters)
 
        self.labels_ = np.empty(X.shape[0], dtype = np.intp)
        for i, c in enumerate(self.__clusters):
            self.labels_[c.index] = i
 
        self.cluster_centers_ = np.array([c.center for c in self.__clusters])
        print('hoge')
        print(self.__clusters)
        self.cluster_log_likelihoods_ = np.array([c.log_likelihood() for c in self.__clusters])
        self.cluster_sizes_ = np.array([c.size for c in self.__clusters])
 
        return self
 
    def __recursively_split(self, clusters):
        for cluster in clusters:
            if cluster.size <= 3:
                self.__clusters.append(cluster)
                continue
 
            k_means = KMeans(2, **self.k_means_args).fit(cluster.data)
            c1, c2 = self.Cluster.build(cluster.data, k_means, cluster.index)
           
            beta = np.linalg.norm(c1.center - c2.center) / np.sqrt(np.linalg.det(c1.cov) + np.linalg.det(c2.cov))
            alpha = 0.5 / stats.norm.cdf(beta)
            bic = -2 * (cluster.size * np.log(alpha) + c1.log_likelihood() + c2.log_likelihood()) + 2 * cluster.df * np.log(cluster.size)
 
            if bic < cluster.bic():
                self.__recursively_split([c1, c2])
            else:
                self.__clusters.append(cluster)
 
    class Cluster:
        @classmethod
        def build(cls, X, k_means, index = None):
            if index == None:
                index = np.array(range(0, X.shape[0]))
            labels = range(0, k_means.get_params()["n_clusters"])
 
            return tuple(cls(X, index, k_means, label) for label in labels)
 
        def __init__(self, X, index, k_means, label):
            self.data = X[k_means.labels_ == label]
            self.index = index[k_means.labels_ == label]
            self.size = self.data.shape[0]
            self.df = self.data.shape[1] * (self.data.shape[1] + 3) / 2
            self.center = k_means.cluster_centers_[label]
            self.cov = np.cov(self.data.T)
 
        def log_likelihood(self):
            return sum(stats.multivariate_normal.logpdf(x, self.center, self.cov) for x in self.data)
 
        def bic(self):
            return -2 * self.log_likelihood() + self.df * np.log(self.size)
 
if __name__ == "__main__":
    import matplotlib.pyplot as plt
    x = []
    y = []
    count = 0
    for line in open( directory + "mds.csv"):
        if count != 0:
            a = line.rfind(r",")
            aa = line.find(r",")
            print(x)
            print(y)

            x.append(round(float(line[aa+1:a]),6))
            y.append(round(float(line[a+1:]),6))
        count += 1
    x = np.array(x)
    y = np.array(y)
    print (x)
    print(y)
    x_means = XMeans(random_state = 1).fit(np.c_[x,y])
    print("2")
    clu = ["cluster"]
    clus = np.r_[clu, x_means.labels_]
    print(np.r_[clu, x_means.labels_])
    print(x_means.labels_)
    print(x_means.cluster_centers_)
    print(x_means.cluster_log_likelihoods_)
    print(x_means.cluster_sizes_)

    fout = open( directory + "mds-clu.csv", "w")
    for line,cluster  in zip(open( directory + "mds.csv"), clus):
        line = line.replace('\n','')
        line = line.replace('\r','')
        fout.write(line)
        fout.write("," + cluster + "\n")


"""
    x = np.array([np.random.normal(loc, 0.1, 20) for loc in np.repeat([1,2], 2)]).flatten()
    y = np.array([np.random.normal(loc, 0.1, 20) for loc in np.tile([1,2], 2)]).flatten()
"""
