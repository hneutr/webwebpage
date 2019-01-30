---
layout: home
nav_order: 8
parent: examples
title: 'add node metadata: scalar'

---

{% include webweb.html webweb_json=site.data.examples.add_node_metadata_scalar.json fix_width=false fix_height=false %}

If nodes are indexes, we can add metadata as a vector, like we've done here for the `velocity` attribute. A node's value for this attribute will be the value at its id's index in this array.

{% include code_switcher.html code_options="python---python (networkx)---matlab---json" switcher_name="example-code-switcher" %}
<div class='select-code-block example-code-switcher python-code-block select-code-block-visible'></div>
```python
{{site.data.examples.add_node_metadata_scalar.representations.python}}
```
<div class='select-code-block example-code-switcher python_networkx-code-block'></div>
```python
{{site.data.examples.add_node_metadata_scalar.representations.python_networkx}}
```
<div class='select-code-block example-code-switcher matlab-code-block'></div>
```matlab
{{site.data.examples.add_node_metadata_scalar.representations.matlab}}
```
<div class='select-code-block example-code-switcher json-code-block'></div>
```json
{{site.data.examples.add_node_metadata_scalar.representations.json}}
```