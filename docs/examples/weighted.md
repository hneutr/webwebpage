---
layout: home
nav_order: 8
parent: examples
title: weighted

---

<div id='webweb-example-visualization' style='width: 100%'></div>
{% assign webweb_json=site.data.examples.weighted.json | jsonify %}
{% include webweb_dependencies.html webweb_json=webweb_json %}

{% include code_switcher.html code_options="python---python (networkx)---json" %}
<div id='python-code-block' class='select-code-block select-code-block-visible'></div>
```python
{{site.data.examples.weighted.representations.python}}
```
<div id='python_networkx-code-block' class='select-code-block'></div>
```python
{{site.data.examples.weighted.representations.python_networkx}}
```
<div id='json-code-block' class='select-code-block'></div>
```json
{{site.data.examples.weighted.representations.json}}
```