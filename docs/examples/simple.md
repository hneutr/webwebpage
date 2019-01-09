---
layout: home
nav_order: 5
parent: examples
title: simple

---

<div id='webweb-example-visualization' style='width: 100%'></div>
{% assign webweb_json=site.data.examples.simple.json | jsonify %}
{% include webweb_dependencies.html webweb_json=webweb_json %}

{% include code_switcher.html code_options="python---python (networkx)---matlab---json" %}
<div id='python-code-block' class='select-code-block select-code-block-visible'></div>
```python
{{site.data.examples.simple.representations.python}}
```
<div id='python_networkx-code-block' class='select-code-block'></div>
```python
{{site.data.examples.simple.representations.python_networkx}}
```
<div id='matlab-code-block' class='select-code-block'></div>
```matlab
{{site.data.examples.simple.representations.matlab}}
```
<div id='json-code-block' class='select-code-block'></div>
```json
{{site.data.examples.simple.representations.json}}
```
