---
grand_parent: documentation
layout: home
nav_order: 8
parent: display
title: hideMenu

---

{% include webweb.html webweb_json=site.data.documentation.display.hideMenu.json %}

```type```: boolean

```default```: false

If `true`, webweb's interactive menu will be hidden and only the network visualization will be shown.

{% include code_switcher.html code_options="python---json" switcher_name="example-code-switcher" %}
<div class='select-code-block example-code-switcher python-code-block select-code-block-visible'></div>
```python
{{site.data.documentation.display.hideMenu.representations.python}}
```
<div class='select-code-block example-code-switcher json-code-block'></div>
```json
{{site.data.documentation.display.hideMenu.representations.json}}
```