---
grand_parent: documentation
layout: home
nav_order: 16
parent: display
title: radius

---

{% include webweb.html webweb_json=site.data.documentation.display.radius.json %}

```json
type: positive non-zero float
synonyms: r
default: 5
````
we can change the radius of the nodes by setting the `display.radius` parameter.

{% include code_switcher.html code_options="python---json" switcher_name="example-code-switcher" %}
<div class='select-code-block example-code-switcher python-code-block select-code-block-visible'></div>
```python
{{site.data.documentation.display.radius.representations.python}}
```
<div class='select-code-block example-code-switcher json-code-block'></div>
```json
{{site.data.documentation.display.radius.representations.json}}
```