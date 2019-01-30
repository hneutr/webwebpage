---
grand_parent: documentation
layout: home
nav_order: 12
parent: display
title: linkStrength

---

{% include webweb.html webweb_json=site.data.documentation.display.linkStrength.json fix_width=false fix_height=false %}

```json
type: positive non-zero float
default: 1
````
we can adjust how much links resist deformation.



This number should be between `0` and `1`.



{% include code_switcher.html code_options="python---json" switcher_name="example-code-switcher" %}
<div class='select-code-block example-code-switcher python-code-block select-code-block-visible'></div>
```python
{{site.data.documentation.display.linkStrength.representations.python}}
```
<div class='select-code-block example-code-switcher json-code-block'></div>
```json
{{site.data.documentation.display.linkStrength.representations.json}}
```