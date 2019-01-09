---
grand_parent: null
layout: home
nav_order: 7
parent: examples
title: weights

---

{% include webweb.html webweb_json=site.data.examples.weights.json %}

{% include code_switcher.html code_options="python---python (networkx)---json" %}
<div id='python-code-block' class='select-code-block select-code-block-visible'></div>
```python
{{site.data.examples.weights.representations.python}}
```
<div id='python_networkx-code-block' class='select-code-block'></div>
```python
{{site.data.examples.weights.representations.python_networkx}}
```
<div id='json-code-block' class='select-code-block'></div>
```json
{{site.data.examples.weights.representations.json}}
```