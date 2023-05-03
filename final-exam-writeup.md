# Math 151 Final Project
=====================================================
#### By: Hannah Mandell, Stephen Fatuzzo, Dylan Santa
##### With credit to the original API athors: Julien Odent, Michael Saint-Guillain

## Question 5. 

Try to apply this on a network that hasn't been worked on yet. 
Find a dataset and run this algorithm on it.

## Background Information

### Graph Structure

Graphs are comprised of nodes (vertices) and edges, *G = (V, E)*. Nodes are standalone units than can be weighted or unweigthed. Nodes can be highly connected (having many edges between other nodes) or they can have zero edges. Edges connect nodes to one another, they can also be weighted or unweighted. Edges can be directional or undirectional, where direction implies that the property of the graph only flows from certain edges to others and not necessarily the other way around.

For the sake of community detection, we consider undirectional graphs since community/acquaintance is bidirectional. In our specific example, we are choosing to examine weighted graphs since interaction between nodes can be measured over a range, not just on a binary basis.

### The Louvain Method

The Louvain method for community detection is a greedy optimization method that extracts communities from large networks by maximizing the modularity of a given weighted network. It was created by [Blondel *et al*. (2008)](https://arxiv.org/pdf/0803.0476.pdf) from the University of Louvain. The algorithm runs in time O(n log n) on the number of nodes in the network, n. 

The algorithm proceeds by first detecting small communities via optimization of modularity on all nodes locally, where modularity is a statistical measure of a community partitioning of the nodes. The algorithm then groups each community of nodes into a single node and repeats the modularity optimization on the existing nodes. More specifically:

**Phase 1**
1. Each individual node in the graph is placed in its own individual community.
2. For each node: 
    1. Calculate the change in modularity of moving it from its own community to that of each neighboring node's community
    2. After all values of modularity are computed, we place the node in the community that maximixed its modularity increase.
3. Repeat this process until modularity can no longer increase

**Phase 2**
1. Group nodes that are in the same community
2. Construct a new network where communities are represented as single nodes. Any inter-community edges are represented as self-loops. Weighted edges between communities represent the sum of edge weights from multiple nodes within a community to the same external community
3. Repeat Phase 1 on this new network until no changes are made

### Implementation

The code in `pylouvain.py` implements the above algorithm in Python. Stepping through the file:

##### Object Initialization

`PyLouvain` is defined as a Python class, meaning that the programmer can define instances of `PyLouvain` objects and then call specific methods on those instances. Each `PyLouvain` object must have particular attributes, and from the `__init__` method, we see those attributes are defined by the `self.___` notation, where `self` is the object and the `___` after the `.` is the attribute name. `PyLouvain` objects must have the following attributes:

- `nodes`, a list of ints
- `edges`, a list of ((int, int), weight) pairs
- `m`, the sum of all of the edge weights in the graph
- `k_i`, a list of the sums of the weights of the edges incident to each node
- `edges_of_node`, a list of lists of edges incident to each node
- `w`
- `communities`, a list of all the communities (originally a list of just the nodes)
- `actual_partition`, the partition of nodes that maximizes modularity

##### Reading in a File

Graph-style data can be ingested to the code via both `.txt`  or `.gml` files. The code can run `from_file(cls, path)` or `from_gml_file(cls, path)`, respectively. Both functions return an instance of `PyLouvain` with the attributes described above. 

##### Applying the Louvain Method

The function `apply_method(self)` takes an instance of `PyLouvain`. It runs **Phase 1** (`self.first_phase(network)`) and **Phase 2** (`self.second_phase(network, partition)`) in a `while` loop until the modularity (`self.compute_modularity(partition)`) of the network does not increase from one run to the next (see line 128, `if q == best_q: break`).

It then returns the partitioning of the nodes into communities that maximizes modularity. 

## Example Usage

The wonderful thing about code is that is can translate theory into practice. 

### Dataset

As an example of the application of the Louvain method on maximizing modularity, we looks at a dataset on the characters in Victor Hugo's book, *"Les Miserables"*.

The file `data/lesmis.gml` contains the weighted network of coappearances of characters in *"Les Miserables"*. Nodes represent characters and edges connect any pair of characters that appear in the same chapter of the book. The value of the edge is the number of such coappearances. The data on coappearances were taken from [D. E. Knuth, The Stanford GraphBase: A Platform for Combinatorial Computing, Addison-Wesley, Reading, MA (1993)](https://www-cs-faculty.stanford.edu/~knuth/sgb.html).

### Applying the Code

Via the PyLouvain API documentation in [@patapizza](https://github.com/patapizza)'s [pylouvain/community.pdf](https://github.com/hfmandell/pylouvain/blob/master/community.pdf) writeup, we see that to apply the Louvain method we should first run the following to create the `PyLouvain` object:

```
pyl = PyLouvain.from_gml_file("data/lesmis.gml")
```

And we launch the algorithm with:

```
partition, modularity = pyl.apply_method()
```

### Results

From the 77 nodes and 254 initial edges, we get:

```
[
        [0, 1, 4, 5, 6, 7, 8, 9], 
        [30, 31], 
        [2, 3, 10, 11, 12, 13, 14, 15, 32, 33, 72, 28, 44, 45, 46, 47], 
        [16, 17, 18, 19, 20, 21, 22, 23, 39, 52], 
        [29, 34, 35, 36, 37, 38, 26, 43, 49, 50, 51, 53, 54, 55, 56], 
        [48, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 76, 73, 74, 24, 25, 27, 40, 41, 42, 68, 69, 70, 71, 75]
]
```

We can translate these back to the original characters, and we see that the "communities" are:

```
[
        [Myriel, Napoleon, CountessDeLo, Geborand, Champtercier, Cravatte, Count, OldMan], 

        [Perpetue, Simplice], 

        [MlleBaptistine, MmeMagloire, Labarre, Valjean, Marguerite, MmeDeR, Isabeau, Gervais, Scaufflaire, Woman1, Toussaint, Fauchelevent, MotherInnocent, Gribier, Jondrette, MmeBurgon], 

        [Tholomyes, Listolier, Fameuil, Blacheville, Favourite, Dahlia, Zephine, Fantine, Pontmercy, MmePontmercy], 

        [Bamatabois, Judge, Champmathieu, Brevet, Chenildieu, Cochepaille, Cosette, Woman2, Gillenormand, Magnon, MlleGillenormand, MlleVaubois, LtGillenormand, Marius, BaronessT], 

        [Gavroche, Mabeuf, Enjolras, Combeferre, Prouvaire, Feuilly, Courfeyrac, Bahorel, Bossuet, Joly, Grantaire, MotherPlutarch, MmeHucheloup, Child1, Child2, MmeThenardier, Thenardier, Javert, Boulatruelle, Eponine, Anzelma, Gueulemer, Babet, Claquesous, Montparnasse, Brujon]
]
```

This configuration maximizes the modularity, which ends up at: `0.5555521111042222`.


## Resources:
1. [Automatic detection of community structures in networks, by Julien Odent and Michael Saint-Guillain](https://github.com/patapizza/pylouvain/blob/master/community.pdf)
2. [Implement Louvain Community Detection Algorithm using Python and Gephi with Visualization](https://medium.com/analytics-vidhya/implement-louvain-community-detection-algorithm-using-python-and-gephi-with-visualization-871250fb2f25)
3. [Louvain Method](https://en.wikipedia.org/wiki/Louvain_method)
4. [Network of Thrones](https://www.maa.org/sites/default/files/pdf/Mathhorizons/NetworkofThrones%20%281%29.pdf)

