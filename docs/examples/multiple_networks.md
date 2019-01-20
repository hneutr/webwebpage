---
layout: home
nav_order: 9
parent: examples
title: multiple networks

---

{% include webweb.html webweb_json=site.data.examples.multiple_networks.json %}

you can give webweb more than one network and toggle between those networks with the up and down arrow keys.

{% include code_switcher.html code_options="python---python (networkx)---matlab---json" switcher_name="example-code-switcher" %}
<div class='select-code-block example-code-switcher python-code-block select-code-block-visible'></div>
```python
{{site.data.examples.multiple_networks.representations.python}}
```
<div class='select-code-block example-code-switcher python_networkx-code-block'></div>
```python
{{site.data.examples.multiple_networks.representations.python_networkx}}
```
<div class='select-code-block example-code-switcher matlab-code-block'></div>
```matlab
{{site.data.examples.multiple_networks.representations.matlab}}
```
<div class='select-code-block example-code-switcher json-code-block'></div>
```json
{{site.data.examples.multiple_networks.representations.json}}
```