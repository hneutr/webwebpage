---
grand_parent: documentation
layout: home
nav_order: 9
parent: display
title: invertBinaryColors

---

{% include webweb.html webweb_json=site.data.documentation.display.invertBinaryColors.json %}

```json
type: boolean
default: false
````
we can flip the colors used for `True` and `False` if we're coloring nodes by a binary attribute.

{% include code_switcher.html code_options="python---json" switcher_name="example-code-switcher" %}
<div class='select-code-block example-code-switcher python-code-block select-code-block-visible'></div>
```python
{{site.data.documentation.display.invertBinaryColors.representations.python}}
```
<div class='select-code-block example-code-switcher json-code-block'></div>
```json
{{site.data.documentation.display.invertBinaryColors.representations.json}}
```