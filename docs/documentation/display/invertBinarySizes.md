---
grand_parent: documentation
layout: home
nav_order: 10
parent: display
title: invertBinarySizes

---

{% include webweb.html webweb_json=site.data.documentation.display.invertBinarySizes.json %}

```json
type: boolean
default: false
````
If we're sizing nodes by a binary attribute, by default nodes with a value of `True` will be big and nodes with a value of `False` will be small, but if we want to, we can flip that.

{% include code_switcher.html code_options="python---json" switcher_name="example-code-switcher" %}
<div class='select-code-block example-code-switcher python-code-block select-code-block-visible'></div>
```python
{{site.data.documentation.display.invertBinarySizes.representations.python}}
```
<div class='select-code-block example-code-switcher json-code-block'></div>
```json
{{site.data.documentation.display.invertBinarySizes.representations.json}}
```