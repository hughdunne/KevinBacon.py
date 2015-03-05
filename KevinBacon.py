#!/usr/bin/env python
"""
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

    NOTE: This is strictly a proof of concept and would be horribly
    inefficient in practice!

    @TODO: Use the fact that matrices are symmetric to reduce number of
    computations (if possible).
"""
import numpy as np

# Dummy data
imdb = {
    'Footloose': ['Kevin Bacon', 'John Lithgow'],
    'Cliffhanger': ['John Lithgow', 'Sylvester Stallone'],
    'The Specialists': ['Sylvester Stallone', 'Sharon Stone'],
    'Basic Instinct': ['Sharon Stone', 'Michael Douglas'],
    'Wall Street': ['Michael Douglas', 'Charlie Sheen']
}

def getCast(movie):
    global imdb
    return imdb[movie]

def getFilmography(actor):
    global imdb
    s = []
    for movie, cast in imdb.iteritems():
        if actor in cast:
            s.append(movie)
    return s

def init_global_data():
    global actorList
    global adjacencyMatrix
    global cache

    # Get a list of casts and flatten to a single list.
    # Convert to set and back to list to remove duplicates.
    actorList = list(set([actor for cast in imdb.values() for actor in cast]))
    N = len(actorList)

    # Initialize the adjacency matrix as an N by N matrix of zeroes.
    adjacencyMatrix = np.array([0] * (N * N)).reshape(N, N)

    # Now populate it.
    for i, actor in enumerate(actorList):
        for movie in getFilmography(actor):
            for costar in getCast(movie):
                j = actorList.index(costar)
                adjacencyMatrix[i,j] += 1

    # Initialize the cache.
    cache = [None, adjacencyMatrix]

def get_power(N):
    """
        Get the Nth power of the adjacency matrix.
        Cache the result to minimize the number of
        matrix multiplications we have to perform.
    """
    global adjacencyMatrix
    global cache

    while len(cache) < N + 1:
        # Take a copy of the highest power we have calculated so far.
        last = np.copy(cache[-1])

        # Calculate the next power and add the matrix to the cache.
        cache.append(np.dot(last, adjacencyMatrix))

    # Return a reference to a matrix in the cache.
    return cache[N]

def KevinBaconNumber(actor):
    """
        Calculate the actor's Kevin Bacon number.
    """
    global actorList
    i = actorList.index('Kevin Bacon')
    j = actorList.index(actor)
    if i == j:
        return 0
    power = 1
    A = get_power(power)
    while A[i,j] <= 0:
        power += 1
        if power > 10:
            # Quick and dirty check against hanging.
            raise Exception("Infinite loop")
        A = get_power(power)
    return power

if __name__ == "__main__":
    init_global_data()
    for actor in actorList:
        print actor, KevinBaconNumber(actor)
