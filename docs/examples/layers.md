---
layout: home
nav_order: 10
parent: examples
title: layers

---

{% include webweb.html webweb_json=site.data.examples.layers.json %}

webweb supports adding layers to networks (think timeslices). You can more forward through these with the right arrow key and backwards with the left.

{% include code_switcher.html code_options="python---python (networkx)---matlab---json" switcher_name="example-code-switcher" %}
<div class='select-code-block example-code-switcher python-code-block select-code-block-visible'></div>
```python
{{site.data.examples.layers.representations.python}}
```
<div class='select-code-block example-code-switcher python_networkx-code-block'></div>
```python
{{site.data.examples.layers.representations.python_networkx}}
```
<div class='select-code-block example-code-switcher matlab-code-block'></div>
```matlab
{{site.data.examples.layers.representations.matlab}}
```
<div class='select-code-block example-code-switcher json-code-block'></div>
```json
{{site.data.examples.layers.representations.json}}
```