---
layout: home
nav_order: 10
parent: examples
title: timeslice

---

<div id='webweb-example-visualization' style='width: 100%'></div>
{% assign webweb_json=site.data.examples.timeslice.json | jsonify %}
{% include webweb_dependencies.html webweb_json=webweb_json %}

{% include code_switcher.html code_options="python---json" %}
<div id='python-code-block' class='select-code-block select-code-block-visible'></div>
```python
{{site.data.examples.timeslice.representations.python}}
```
<div id='json-code-block' class='select-code-block'></div>
```json
{{site.data.examples.timeslice.representations.json}}
```