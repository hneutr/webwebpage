---
grand_parent: documentation
layout: main_page
nav_order: 1
parent: python
title: webweb.Web

---

```python
webweb.Web(adjacency=[], title='webweb', display={}, adjacency_type=None, nodes={}, metadata=None, nx_G=None, gml_file=None)
````

a webweb object.
a collection of named webweb Network objects, a set of display parameters, and a title

usage:
- `web = Web(adjacency=[[0, 1]], title='a web woohoo')`

parameters:
- `adjacency`: edge list or adjacency matrix
- `title`: string. Will set the html title of the visualization if
  `display.attachWebwebToElementWithId = None`
- `display`: dictionary of display parameters
- `adjacency_type`: string. 'matrix' or 'edge list'
- `nodes`: dict of node attribute dicts
```json
{
    'key1': {
        'attribute1': 'value1',
        ...
    },
    ...
}
```
- `metadata`: dict of vectorized metadata and display information.
```python
{
    'attribute': {
        'values': [ "attribute_value", ...],

        # `categories` only needs to be supplied if `values` holds
        # categorical data that is represented by numbers.
        # the values in the `values` array will be used as indexes to
        # this array.
        'categories': ["category1", "category2", ...]

        # `type` only needs to be set if you're displaying binary
        # information with 0/1 instead of True/False
        'type': 'binary',
    }
}
```
- `nx_G`: a networkx graph.
- `gml_file`: path to a gml file

---

nodes which appear in both the adjacency and as keys in the `nodes`
dictionary will be given the values of the attributes under their
corresponding key in the `nodes` dictionary

`adjacency_type` only needs to be supplied if your adjacency is
represented as a matrix and that matrix has 3 or fewer nodes