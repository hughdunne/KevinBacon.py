Calculate the Kevin Bacon number of a given actor.

The problem can be represented as an undirected graph where each node
is an actor and each edge is a movie. An edge connects two nodes if
the two actors corresponding to the nodes both appear in the movie
corresponding to the edge. The Kevin Bacon number of an actor is
therefore the shortest path through the graph connecting the actor's
node to Kevin Bacon's node. By convention, Kevin Bacon's Kevin Bacon
number is zero.

The adjacency matrix of the graph is the matrix where element (i,j)
is the number of edges connecting nodes i and j, i.e. the number of
movies that both i and j have acted in.

It follows that the square of the adjacency matrix is a matrix where
element (i,j) is the number of paths of length 2 connecting nodes i
and j. In general, the Nth power of the adjacency matrix gives the
number of paths of length N connecting any two nodes. Note that the
adjacency matrix is symmetric and so are higher powers of it.

The Kevin Bacon number of actor j is thus the smallest value of N
such that M(i,j) > 0 (or equivalently, M(j,i) > 0) where i is Kevin
Bacon and M is the Nth power of the adjacency matrix.

**NOTE:** This is strictly a proof of concept and would be horribly
inefficient in practice!

@TODO: Use the fact that matrices are symmetric to reduce number of
computations (if possible).
