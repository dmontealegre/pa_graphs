import scipy
from PA_graph import *


# Feel free to mess with different values for m, n and k.
n = 100000
m = 5
k = 5
G = pa_graph(m, n)

A = nx.adjacency_matrix(G)

A = A.asfptype()
A = scipy.sparse.coo_matrix.asfptype(A)
vals, vecs = scipy.sparse.linalg.eigs(A, k) # here k is the number of eigenvectors you wan


for i in range(k):
    v = vecs[:, i]
    plt.plot(v, "o")
    plt.title(r'Coordinates for the %.0f -th eigenvector:$\ n=%.0f,\ m=%.0f$' % (i+1, n, m))
    plt.show()
    pylab.savefig('%i-th_vector.png' % (i+1))
    plt.clf()
