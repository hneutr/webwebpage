---
layout: home
nav_order: 4
parent: examples
title: display from weighted adjacency matrix

---

if both edges between two nodes are non-zero in the adjacency matrix, the first edge's weight is used (webweb traverses adjacency matrixes row-wise).



In other words, if you give webweb an adjacency matrix where `matrix[0][1] = .1` and `matrix[1][0] = 1`, it'll make an edge between nodes `0` and `1` with a weight `.1`, and not `1`, or `1.1`

{% include webweb.html webweb_json=site.data.examples.display_from_weighted_adjacency_matrix.json %}

{% include code_switcher.html code_options="python---json" %}
<div id='python-code-block' class='select-code-block select-code-block-visible'></div>
```python
{{site.data.examples.display_from_weighted_adjacency_matrix.representations.python}}
```
<div id='json-code-block' class='select-code-block'></div>
```json
{{site.data.examples.display_from_weighted_adjacency_matrix.representations.json}}
```