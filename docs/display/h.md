---
layout: home
nav_order: 7
parent: display
title: h (height)

---

{% include webweb.html webweb_json=site.data.display.h.json %}

you can change the height of the visualization by setting the `display.h` property.

{% include code_switcher.html code_options="python---json" switcher_name="example-code-switcher" %}
<div class='select-code-block example-code-switcher python-code-block select-code-block-visible'></div>
```python
{{site.data.display.h.representations.python}}
```
<div class='select-code-block example-code-switcher json-code-block'></div>
```json
{{site.data.display.h.representations.json}}
```