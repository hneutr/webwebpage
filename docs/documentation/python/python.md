---
has_children: true
layout: main_page
nav_order: 2
parent: documentation
permalink: /documentation/python/
title: python

---

full documentation for the python code.

---

you interact with webweb via the `webweb.Web` object, which has the following attributes:

- display: dictionary of webweb display parameters; see the [display](/documentation/display/) documentation
- networks: a dictionary of `webweb.Network` objects

a python `webweb.Network` object has the following attributes:

- layers: a list of dictionaries with the following attributes:

```json
{
    'edgeList' : [[0, 1, .5], ...],
    'nodes' : {
        'key1' : {
            'attribute1' : value1,
            'attribute2' : value2,
            ...
        },
        ...
    },
    'metadata' : {
        'attribute3' : {
            'values' : [1, 2, ...],
            ...
        },
        ...
    },
}
```
