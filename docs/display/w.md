---
layout: home
nav_order: 21
parent: display
title: w (width)

---

{% include webweb.html webweb_json=site.data.display.w.json %}

you can change the width of the visualization by setting the `display.w` property.

{% include code_switcher.html code_options="python---json" switcher_name="example-code-switcher" %}
<div class='select-code-block example-code-switcher python-code-block select-code-block-visible'></div>
```python
{{site.data.display.w.representations.python}}
```
<div class='select-code-block example-code-switcher json-code-block'></div>
```json
{{site.data.display.w.representations.json}}
```