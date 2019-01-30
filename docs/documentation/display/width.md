---
grand_parent: documentation
layout: home
nav_order: 21
parent: display
title: width

---

{% include webweb.html webweb_json=site.data.documentation.display.width.json %}

```json
type: positive non-zero float
synonyms: w
````
we can change the width of the visualization by setting the `display.width` property.

{% include code_switcher.html code_options="python---json" switcher_name="example-code-switcher" %}
<div class='select-code-block example-code-switcher python-code-block select-code-block-visible'></div>
```python
{{site.data.documentation.display.width.representations.python}}
```
<div class='select-code-block example-code-switcher json-code-block'></div>
```json
{{site.data.documentation.display.width.representations.json}}
```