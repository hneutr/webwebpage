---
layout: home
nav_order: 7
parent: display
title: height

---

{% include webweb.html webweb_json=site.data.display.height.json %}

```type```: positive non-zero integer

```synonyms```: h

you can change the height of the visualization by setting the `display.height` property.

{% include code_switcher.html code_options="python---json" switcher_name="example-code-switcher" %}
<div class='select-code-block example-code-switcher python-code-block select-code-block-visible'></div>
```python
{{site.data.display.height.representations.python}}
```
<div class='select-code-block example-code-switcher json-code-block'></div>
```json
{{site.data.display.height.representations.json}}
```