---
layout: home
nav_order: 7
parent: examples
title: 'add node metadata: categorical'

---

{% include webweb.html webweb_json=site.data.examples.add_node_metadata_categorical.json %}

if the set of a metadata attribute's values contains strings (like `cooperativity` here), webweb'll display it as a categorical attribute.



if that set is all numbers (like `alphabeticallity` here), you should tell webweb how to display it by adding that metadata attribute name to the `metadata` key to the `display` attribute with an array under `categories`; a node's value for this metadata attribute should be an index into this array.

{% include code_switcher.html code_options="python---python (networkx)---matlab---json" switcher_name="example-code-switcher" %}
<div class='select-code-block example-code-switcher python-code-block select-code-block-visible'></div>
```python
{{site.data.examples.add_node_metadata_categorical.representations.python}}
```
<div class='select-code-block example-code-switcher python_networkx-code-block'></div>
```python
{{site.data.examples.add_node_metadata_categorical.representations.python_networkx}}
```
<div class='select-code-block example-code-switcher matlab-code-block'></div>
```matlab
{{site.data.examples.add_node_metadata_categorical.representations.matlab}}
```
<div class='select-code-block example-code-switcher json-code-block'></div>
```json
{{site.data.examples.add_node_metadata_categorical.representations.json}}
```