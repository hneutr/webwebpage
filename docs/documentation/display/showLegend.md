---
grand_parent: documentation
layout: home
nav_order: 19
parent: display
title: showLegend

---

{% include webweb.html webweb_json=site.data.documentation.display.showLegend.json fix_width=false fix_height=false %}

```json
type: boolean
default: true
````
If `true`, webweb will display a legend describing how nodes are colored and sized.

{% include code_switcher.html code_options="python---json" switcher_name="example-code-switcher" %}
<div class='select-code-block example-code-switcher python-code-block select-code-block-visible'></div>
```python
{{site.data.documentation.display.showLegend.representations.python}}
```
<div class='select-code-block example-code-switcher json-code-block'></div>
```json
{{site.data.documentation.display.showLegend.representations.json}}
```