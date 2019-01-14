---
layout: home
nav_order: 5
parent: examples
title: add node names

---

{% include webweb.html webweb_json=site.data.examples.add_node_names.json %}

we can add node names by setting the `nodes` attribute in the `display` variable



a node in the adjacency list (e.g., `0` here) will have the metadata of the entry under the same key in the `nodes` dictionary (if one exists)

{% include code_switcher.html code_options="python---python (networkx)---json" %}
<div id='python-code-block' class='select-code-block select-code-block-visible'></div>
```python
{{site.data.examples.add_node_names.representations.python}}
```
<div id='python_networkx-code-block' class='select-code-block'></div>
```python
{{site.data.examples.add_node_names.representations.python_networkx}}
```
<div id='json-code-block' class='select-code-block'></div>
```json
{{site.data.examples.add_node_names.representations.json}}
```