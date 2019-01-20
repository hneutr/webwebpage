---
grand_parent: documentation
layout: main_page
nav_order: 5
parent: python
title: Web.networks.name.add_layer

---

```python
Web.networks.name.add_layer(adjacency=None, adjacency_type=None, nodes=None, metadata=None, nx_G=None)
````

adds a layer to the network.

- adjacency: edge list or adjacency matrix
- adjacency_type: string. 'matrix' or 'edge list'. Supply if passing an adjacency matrix with fewer than 3 nodes
- nodes: dict of node attribute dicts
- metadata: dict of vectorized metadata and display information. 
```{
    'attribute' : {
        'values' : [ "attribute_value", ...],
        'categories' : ["category1", "category2", ...] (supply if values is categorical but contains numbers; values in the `values` array will be used as indexes to this array)
        'type' : string. Only necessary if displaying binary information with 0/1 and not True/False.
    }
}```
- nx_G: a networkx graph.

call with at least one of:
- adjacency
- nodes
- metadata
- nx_G