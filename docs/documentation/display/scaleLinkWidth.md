---
grand_parent: documentation
layout: home
nav_order: 18
parent: display
title: scaleLinkWidth

---

{% include webweb.html webweb_json=site.data.documentation.display.scaleLinkWidth.json %}

```json
type: boolean
default: false
````
we can scale link widths by their weight by setting the `scaleLinkWidth` parameter.

{% include code_switcher.html code_options="python---json" switcher_name="example-code-switcher" %}
<div class='select-code-block example-code-switcher python-code-block select-code-block-visible'></div>
```python
{{site.data.documentation.display.scaleLinkWidth.representations.python}}
```
<div class='select-code-block example-code-switcher json-code-block'></div>
```json
{{site.data.documentation.display.scaleLinkWidth.representations.json}}
```