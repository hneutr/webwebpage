---
grand_parent: documentation
layout: home
nav_order: 5
parent: display
title: freezeNodeMovement

---

{% include webweb.html webweb_json=site.data.documentation.display.freezeNodeMovement.json %}

```json
type: boolean
default: false
````
If `true`, fixes nodes wherever they are. Drag & drop still works. This is probably not a good idea to set unless we're passing node coordinates as metadata attributes (it'll leave all the nodes at the top left corner of the visualization).

{% include code_switcher.html code_options="python---json" switcher_name="example-code-switcher" %}
<div class='select-code-block example-code-switcher python-code-block select-code-block-visible'></div>
```python
{{site.data.documentation.display.freezeNodeMovement.representations.python}}
```
<div class='select-code-block example-code-switcher json-code-block'></div>
```json
{{site.data.documentation.display.freezeNodeMovement.representations.json}}
```