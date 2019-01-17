---
layout: home
nav_order: 6
parent: examples
title: 'add node metadata: binary'

---

{% include webweb.html webweb_json=site.data.examples.add_node_metadata_binary.json %}

webweb'll display a metadata attribute as binary if every node's value for that attribute is either `True` or `False`.



`True` values will be "big" and `False` values small, but if we want the opposite, we can do the following:



```web.display.invertBinarySizes = True```

{% include code_switcher.html code_options="python---python (networkx)---json" switcher_name="example-code-switcher" %}
<div class='select-code-block example-code-switcher python-code-block select-code-block-visible'></div>
```python
{{site.data.examples.add_node_metadata_binary.representations.python}}
```
<div class='select-code-block example-code-switcher python_networkx-code-block'></div>
```python
{{site.data.examples.add_node_metadata_binary.representations.python_networkx}}
```
<div class='select-code-block example-code-switcher json-code-block'></div>
```json
{{site.data.examples.add_node_metadata_binary.representations.json}}
```