---
layout: home
nav_order: 8
parent: examples
title: 'add node metadata: scalar'

---

If nodes are indexes, we can add metadata as a vector, like we've done here for the `velocity` attribute. A node's value for this attribute will be the value at its id's index in this array.

{% include webweb.html webweb_json=site.data.examples.add_node_metadata_scalar.json %}

{% include code_switcher.html code_options="python---python (networkx)---json" %}
<div id='python-code-block' class='select-code-block select-code-block-visible'></div>
```python
{{site.data.examples.add_node_metadata_scalar.representations.python}}
```
<div id='python_networkx-code-block' class='select-code-block'></div>
```python
{{site.data.examples.add_node_metadata_scalar.representations.python_networkx}}
```
<div id='json-code-block' class='select-code-block'></div>
```json
{{site.data.examples.add_node_metadata_scalar.representations.json}}
```