---
grand_parent: documentation
layout: home
nav_order: 17
parent: display
title: scaleLinkOpacity

---

{% include webweb.html webweb_json=site.data.documentation.display.scaleLinkOpacity.json fix_width=false fix_height=false %}

```json
type: boolean
default: false
````
we can scale link opacities by their weight by setting the `scaleLinkOpacity` parameter.

{% include code_switcher.html code_options="python---json" switcher_name="example-code-switcher" %}
<div class='select-code-block example-code-switcher python-code-block select-code-block-visible'></div>
```python
{{site.data.documentation.display.scaleLinkOpacity.representations.python}}
```
<div class='select-code-block example-code-switcher json-code-block'></div>
```json
{{site.data.documentation.display.scaleLinkOpacity.representations.json}}
```