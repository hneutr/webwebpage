---
grand_parent: documentation
layout: main_page
nav_order: 1
parent: python
title: Web

---

```python
Web(adjacency=None, title='webweb', display={}, **kwargs)
````

a webweb object. 
a collection of named webweb Network objects, a set of display parameters, and a title

parameters:
- adjacency: adjacency to make a visulization from. see `Network.add_layer`
- title: string. Will set the html title of the visualization if display.attachWebwebToElementWithId = None
- display: dictionary of display parameters
- see `Network.add_layer` for all other parameters.