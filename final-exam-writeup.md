# Math 151 Final Project
==========================
#### By: Hannah Mandell, Stephen Fatuzzo, Dylan Santa

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

The code in `pylouvain.py` implements the above algorithm in Python. Stepping through the file function-by-function:

`PyLouvain` is defined as a Python class, meaning that the programmer can define instances of `PyLouvain` objects and then call specific methods on those instances. Each `PyLouvain` object must have particular attributes, and from the `__init__` method, we see those attributes are defined by the `self.___` notation, where `self` is the object and the `___` after the `.` is the attribute name. `PyLouvain` objects must have the following attributes:

- `nodes`, a list of ints
- `edges`, a list of ((int, int), weight) pairs
- `m`, the sum of all of the edge weights in the graph
- `k_i`, a list of the sums of the weights of the edges incident to each node
- `edges_of_node`, a list of lists of edges incident to each node
- `w`, a list of 
- `communities`, a list of all the communities (originally a list of just the nodes)
- `actual_partition`, the partition of nodes that maximizes modularity

##### Reading in a File

Graph-style data can be ingested to the code via both `.txt`  or `.gml` files. The code can run `from_file(cls, path)` or `from_gml_file(cls, path)`, respectively. Both functions return an instance of `PyLouvain` with the attributes described above. 

##### Applying the Louvain Method

The function `apply_method(self)` takes an instance of `PyLouvain`. It runs **Phase 1** (`self.first_phase(network)`)and **Phase 2** (`self.second_phase(network, partition)`) in a `while` loop until the modularity (`self.compute_modularity(partition)`) of the network does not increase from one run to the next (see line 128, `if q == best_q: break`).

It then returns the partitioning of the nodes into communities that maximizes modularity. 

## Example Usage

### Dataset

### Applying the Code

## Resources:
1. [Implement Louvain Community Detection Algorithm using Python and Gephi with Visualization](https://medium.com/analytics-vidhya/implement-louvain-community-detection-algorithm-using-python-and-gephi-with-visualization-871250fb2f25)
2. [Louvain Method](https://en.wikipedia.org/wiki/Louvain_method)
3. [Network of Thrones](https://www.maa.org/sites/default/files/pdf/Mathhorizons/NetworkofThrones%20%281%29.pdf)

