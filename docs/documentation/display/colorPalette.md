---
grand_parent: documentation
layout: home
nav_order: 4
parent: display
title: colorPalette

---

{% include webweb.html webweb_json=site.data.documentation.display.colorPalette.json %}

```json
type: string
default: 'Set1'
````
we can change the color palette webweb uses to color categorical nodes with the `colorPalette` parameter.

{% include code_switcher.html code_options="python---json" switcher_name="example-code-switcher" %}
<div class='select-code-block example-code-switcher python-code-block select-code-block-visible'></div>
```python
{{site.data.documentation.display.colorPalette.representations.python}}
```
<div class='select-code-block example-code-switcher json-code-block'></div>
```json
{{site.data.documentation.display.colorPalette.representations.json}}
```