---
layout: home
nav_order: 3
parent: examples
title: display from weighted edge list

---

{% include webweb.html webweb_json=site.data.examples.display_from_weighted_edge_list.json %}

if there are multiple edges between two nodes, the first edge's weight is used.



In other words, if you give webweb an edge list like `[[0, 1, .1], [0, 1, 1]]`, it'll make an edge between nodes `0` and `1` with a weight `.1`, not `1`, or `1.1` (this would also be the case for the edge list `[[0, 1, .1], [1, 0, 1]]`)

{% include code_switcher.html code_options="python---python (networkx)---matlab---json" switcher_name="example-code-switcher" %}
<div class='select-code-block example-code-switcher python-code-block select-code-block-visible'></div>
```python
{{site.data.examples.display_from_weighted_edge_list.representations.python}}
```
<div class='select-code-block example-code-switcher python_networkx-code-block'></div>
```python
{{site.data.examples.display_from_weighted_edge_list.representations.python_networkx}}
```
<div class='select-code-block example-code-switcher matlab-code-block'></div>
```matlab
{{site.data.examples.display_from_weighted_edge_list.representations.matlab}}
```
<div class='select-code-block example-code-switcher json-code-block'></div>
```json
{{site.data.examples.display_from_weighted_edge_list.representations.json}}
```