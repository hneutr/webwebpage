---
layout: home
nav_order: 6
parent: display
title: gravity

---

{% include webweb.html webweb_json=site.data.display.gravity.json %}

```type```: positive non-zero float

```synonyms```: g

```default```: ```0.1```

we can change the strength of the force pulling nodes to the center.



the greater the value for `gravity`, the more nodes will be drawn to the center.

{% include code_switcher.html code_options="python---json" switcher_name="example-code-switcher" %}
<div class='select-code-block example-code-switcher python-code-block select-code-block-visible'></div>
```python
{{site.data.display.gravity.representations.python}}
```
<div class='select-code-block example-code-switcher json-code-block'></div>
```json
{{site.data.display.gravity.representations.json}}
```