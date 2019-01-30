---
grand_parent: documentation
layout: home
nav_order: 11
parent: display
title: linkLength

---

{% include webweb.html webweb_json=site.data.documentation.display.linkLength.json fix_width=false fix_height=false %}

```json
type: positive non-zero integer
synonyms: l
default: 20
````
we can change the length of link edges by setting the `display.linkLength` parameter.

{% include code_switcher.html code_options="python---json" switcher_name="example-code-switcher" %}
<div class='select-code-block example-code-switcher python-code-block select-code-block-visible'></div>
```python
{{site.data.documentation.display.linkLength.representations.python}}
```
<div class='select-code-block example-code-switcher json-code-block'></div>
```json
{{site.data.documentation.display.linkLength.representations.json}}
```