---
grand_parent: null
layout: home
nav_order: 2
parent: examples
title: categories

---

{% include webweb.html webweb_json=site.data.examples.categories.json %}

{% include code_switcher.html code_options="python---json" %}
<div id='python-code-block' class='select-code-block select-code-block-visible'></div>
```python
{{site.data.examples.categories.representations.python}}
```
<div id='json-code-block' class='select-code-block'></div>
```json
{{site.data.examples.categories.representations.json}}
```