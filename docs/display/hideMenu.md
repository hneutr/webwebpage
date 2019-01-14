---
layout: home
nav_order: 8
parent: display
title: hideMenu

---

{% include webweb.html webweb_json=site.data.display.hideMenu.json %}

Boolean.



If `true`, webweb's menu's will be hidden and only the network visualization will be shown.

{% include code_switcher.html code_options="python---json" %}
<div id='python-code-block' class='select-code-block select-code-block-visible'></div>
```python
{{site.data.display.hideMenu.representations.python}}
```
<div id='json-code-block' class='select-code-block'></div>
```json
{{site.data.display.hideMenu.representations.json}}
```