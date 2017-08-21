from PA_graph import *


# Feel free to change this parameters
n = 5000
m = 5


G = pa_graph(m, n)
spectrum = (1/math.sqrt(m*math.sqrt(n))) * nx.adjacency_spectrum(G)

plt.hist(spectrum, bins=100, normed=True, stacked=True)
plt.title(r'Distribution eigenvalues:$\ m=%.0f,\ n=%.0f$' % (m, n))
pylab.savefig('spectrum_G_(m, n)= (%.0f ,%.0f ).png' % (m,n))
plt.show()