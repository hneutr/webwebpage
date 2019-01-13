---
layout: home
nav_order: 3
parent: examples
title: display from weighted edge list

---

if there are multiple edges between two nodes, the first edge's weight is used.



In other words, if you give webweb an edge list like `[[0, 1, .1], [0, 1, 1]]`, it'll make an edge between nodes `0` and `1` with a weight `.1`, not `1`, or `1.1` (this would also be the case for the edge list `[[0, 1, .1], [1, 0, 1]]`)

{% include webweb.html webweb_json=site.data.examples.display_from_weighted_edge_list.json %}

{% include code_switcher.html code_options="python---python (networkx)---json" %}
<div id='python-code-block' class='select-code-block select-code-block-visible'></div>
```python
{{site.data.examples.display_from_weighted_edge_list.representations.python}}
```
<div id='python_networkx-code-block' class='select-code-block'></div>
```python
{{site.data.examples.display_from_weighted_edge_list.representations.python_networkx}}
```
<div id='json-code-block' class='select-code-block'></div>
```json
{{site.data.examples.display_from_weighted_edge_list.representations.json}}
```