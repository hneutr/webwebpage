---
layout: home
nav_order: 5
parent: examples
title: add node names

---

{% include webweb.html webweb_json=site.data.examples.add_node_names.json %}

we can add node names by setting the `nodes` attribute in the `display` variable



a node in the adjacency list (e.g., `0` here) will have the metadata of the entry under the same key in the `nodes` dictionary (if one exists)

{% include code_switcher.html code_options="python---python (networkx)---matlab---json" switcher_name="example-code-switcher" %}
<div class='select-code-block example-code-switcher python-code-block select-code-block-visible'></div>
```python
{{site.data.examples.add_node_names.representations.python}}
```
<div class='select-code-block example-code-switcher python_networkx-code-block'></div>
```python
{{site.data.examples.add_node_names.representations.python_networkx}}
```
<div class='select-code-block example-code-switcher matlab-code-block'></div>
```matlab
{{site.data.examples.add_node_names.representations.matlab}}
```
<div class='select-code-block example-code-switcher json-code-block'></div>
```json
{{site.data.examples.add_node_names.representations.json}}
```