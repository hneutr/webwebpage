---
grand_parent: documentation
layout: main_page
nav_order: 5
parent: python
title: webweb.Network.add_layer

---

```python
webweb.Network.add_layer(adjacency=[], adjacency_type=None, nodes=None, metadata=None, nx_G=None)
````

adds a layer to the network.

- adjacency: edge list or adjacency matrix
- adjacency_type: string. 'matrix' or 'edge list'
- nodes: dict of node attribute dicts
```json
{
    'key1' : {
        'attribute1' : 'value1',
        ...
    },
    ...
}
```
- metadata: dict of vectorized metadata and display information. 
```python
{
    'attribute' : {
        'values' : [ "attribute_value", ...],

        # `categories` only needs to be supplied if `values` holds
        # categorical data that is represented by numbers.
        # the values in the `values` array will be used as indexes to
        # this array.
        'categories' : ["category1", "category2", ...]

        # `type` only needs to be set if you're displaying binary
        # information with 0/1 instead of True/False 
        'type' : 'binary',
    }
}
```
- nx_G: a networkx graph.

---

nodes which appear in both the adjacency and as keys in the `nodes`
dictionary will be given the values of the attributes under their
corresponding key in the `nodes` dictionary

you only need to pass the `adjacency_type` if your adjacency is
represented as a matrix and that matrix has 3 or fewer nodes

call with at least one of:
- adjacency
- nodes
- metadata
- nx_G