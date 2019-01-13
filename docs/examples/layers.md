---
layout: home
nav_order: 10
parent: examples
title: layers

---

webweb supports adding layers to networks (think timeslices). You can more forward through these with the right arrow key and backwards with the left.

{% include webweb.html webweb_json=site.data.examples.layers.json %}

{% include code_switcher.html code_options="python---python (networkx)---json" %}
<div id='python-code-block' class='select-code-block select-code-block-visible'></div>
```python
{{site.data.examples.layers.representations.python}}
```
<div id='python_networkx-code-block' class='select-code-block'></div>
```python
{{site.data.examples.layers.representations.python_networkx}}
```
<div id='json-code-block' class='select-code-block'></div>
```json
{{site.data.examples.layers.representations.json}}
```