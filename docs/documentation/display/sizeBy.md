---
grand_parent: documentation
layout: home
nav_order: 21
parent: display
title: sizeBy

---

{% include webweb.html webweb_json=site.data.documentation.display.sizeBy.json fix_width=false fix_height=false %}

```json
type: string
default: 'none'
````
we can compute node radii by a metadata attribute by setting the `sizeBy` parameter to that attribute's name.



categorical metadata attributes can't be used to compute node sizes.

{% include code_switcher.html code_options="python---json" switcher_name="example-code-switcher" %}
<div class='select-code-block example-code-switcher python-code-block select-code-block-visible'></div>
```python
{{site.data.documentation.display.sizeBy.representations.python}}
```
<div class='select-code-block example-code-switcher json-code-block'></div>
```json
{{site.data.documentation.display.sizeBy.representations.json}}
```