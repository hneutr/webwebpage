---
layout: home
nav_order: 4
parent: examples
title: display from weighted adjacency matrix

---

{% include webweb.html webweb_json=site.data.examples.display_from_weighted_adjacency_matrix.json %}

if the adjacency matrix we pass has multiple edges between two nodes, the weight of the edge webweb creates between those two nodes will be the sum of those edges' weights. However, webweb won't do this with symmetric matrices.

{% include code_switcher.html code_options="python---matlab---json" switcher_name="example-code-switcher" %}
<div class='select-code-block example-code-switcher python-code-block select-code-block-visible'></div>
```python
{{site.data.examples.display_from_weighted_adjacency_matrix.representations.python}}
```
<div class='select-code-block example-code-switcher matlab-code-block'></div>
```matlab
{{site.data.examples.display_from_weighted_adjacency_matrix.representations.matlab}}
```
<div class='select-code-block example-code-switcher json-code-block'></div>
```json
{{site.data.examples.display_from_weighted_adjacency_matrix.representations.json}}
```