---
layout: home
nav_order: 3
parent: display
title: colorBy

---

{% include webweb.html webweb_json=site.data.display.colorBy.json %}

any metadata attribute can be used to compute node size.

{% include code_switcher.html code_options="python---json" switcher_name="example-code-switcher" %}
<div class='select-code-block example-code-switcher python-code-block select-code-block-visible'></div>
```python
{{site.data.display.colorBy.representations.python}}
```
<div class='select-code-block example-code-switcher json-code-block'></div>
```json
{{site.data.display.colorBy.representations.json}}
```