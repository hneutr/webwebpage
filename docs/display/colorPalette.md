---
layout: home
nav_order: 4
parent: display
title: colorPalette

---

{% include webweb.html webweb_json=site.data.display.colorPalette.json %}

{% include code_switcher.html code_options="python---json" switcher_name="example-code-switcher" %}
<div class='select-code-block example-code-switcher python-code-block select-code-block-visible'></div>
```python
{{site.data.display.colorPalette.representations.python}}
```
<div class='select-code-block example-code-switcher json-code-block'></div>
```json
{{site.data.display.colorPalette.representations.json}}
```