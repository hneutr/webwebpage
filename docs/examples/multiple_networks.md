---
layout: home
nav_order: 9
parent: examples
title: multiple networks

---

you can give webweb more than one network and toggle between those networks with the up and down arrow keys.

{% include webweb.html webweb_json=site.data.examples.multiple_networks.json %}

{% include code_switcher.html code_options="python---python (networkx)---json" %}
<div id='python-code-block' class='select-code-block select-code-block-visible'></div>
```python
{{site.data.examples.multiple_networks.representations.python}}
```
<div id='python_networkx-code-block' class='select-code-block'></div>
```python
{{site.data.examples.multiple_networks.representations.python_networkx}}
```
<div id='json-code-block' class='select-code-block'></div>
```json
{{site.data.examples.multiple_networks.representations.json}}
```