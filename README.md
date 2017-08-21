# pa_graphs
Some python (3.x) code to create preferential attachment random graphs. 

We are going to use the networkx library to create some preferential attachment random graphs. 
We will be using the definition in here (pg 341): https://www.math.cmu.edu/~af1p/BOOK.pdf

The file PA_graph.py contains the graph generator. We feed it two inputs: m and n (see def of model). 
and it returns a networkx graph object. 

The file spectrum.py creates a histogram of the eigenvalues of a PA random graph. 

The file eigenvectors.py plots the coordinates for the first k eigenvectors of a PA random graph, and saves the plots. 


Note that you can play around with the values of m, n, and k. The convergence for the eigenvectors to the eigenvectors 
of a star is sort of slow, so try it for a large number of n and a small number of k (n = 100,000 and k = 5 gives nice plots). 

Best, 
Daniel
