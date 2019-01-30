---
grand_parent: documentation
layout: home
nav_order: 19
parent: display
title: showNodeNames

---

{% include webweb.html webweb_json=site.data.documentation.display.showNodeNames.json fix_width=false fix_height=false %}

```json
type: boolean
default: false
````
we can show all node names by setting the `showNodeNames` parameter.

{% include code_switcher.html code_options="python---json" switcher_name="example-code-switcher" %}
<div class='select-code-block example-code-switcher python-code-block select-code-block-visible'></div>
```python
{{site.data.documentation.display.showNodeNames.representations.python}}
```
<div class='select-code-block example-code-switcher json-code-block'></div>
```json
{{site.data.documentation.display.showNodeNames.representations.json}}
```