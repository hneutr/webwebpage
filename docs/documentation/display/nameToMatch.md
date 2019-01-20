---
grand_parent: documentation
layout: home
nav_order: 13
parent: display
title: nameToMatch

---

{% include webweb.html webweb_json=site.data.documentation.display.nameToMatch.json %}

```type```: string

```default```: ""

we can show nodes whose name matches a given value by setting the `nameToMatch` parameter.

{% include code_switcher.html code_options="python---json" switcher_name="example-code-switcher" %}
<div class='select-code-block example-code-switcher python-code-block select-code-block-visible'></div>
```python
{{site.data.documentation.display.nameToMatch.representations.python}}
```
<div class='select-code-block example-code-switcher json-code-block'></div>
```json
{{site.data.documentation.display.nameToMatch.representations.json}}
```