---
layout: home
nav_order: 3
parent: examples
title: display from weighted edge list

---

{% include webweb.html webweb_json=site.data.examples.display_from_weighted_edge_list.json fix_width=false fix_height=false %}

if the edge list we pass has multiple edges between two nodes, the weight of the edge webweb creates between those two nodes will be the sum of those edges' weights.

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