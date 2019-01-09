---
grand_parent: null
layout: home
nav_order: 1
parent: examples
title: advanced

---

{% include webweb.html webweb_json=site.data.examples.advanced.json %}

{% include code_switcher.html code_options="python---json" %}
<div id='python-code-block' class='select-code-block select-code-block-visible'></div>
```python
{{site.data.examples.advanced.representations.python}}
```
<div id='json-code-block' class='select-code-block'></div>
```json
{{site.data.examples.advanced.representations.json}}
```