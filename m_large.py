from PA_graph import *


n = 50000

for m in range(int(math.sqrt(n) * math.log(n)), int(math.sqrt(n) * math.log(n))+1, 50):
    G = pa_graph(m, n)
    print("graph created")
    v = nx.eigenvector_centrality_numpy(G)
    v = list(v.values())
    plt.plot(v, "o")
    plt.title(r'Coordinates for the largest eigenvector:$\ n=%.0f,\ m=%.0f$' % (n, m))
    pylab.savefig('largest_vector_m=%.0f .png' % m)
    plt.clf()
