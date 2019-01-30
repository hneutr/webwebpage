---
grand_parent: documentation
layout: home
nav_order: 14
parent: display
title: networkLayer

---

{% include webweb.html webweb_json=site.data.documentation.display.networkLayer.json %}

```json
type: positive integer (an index)
default: 0
````
webweb will by default display the first layer, but if we'd like to show a particular one we can do so by setting the `display.networkLayer` property to the index of the layer we want to show.

{% include code_switcher.html code_options="python---json" switcher_name="example-code-switcher" %}
<div class='select-code-block example-code-switcher python-code-block select-code-block-visible'></div>
```python
{{site.data.documentation.display.networkLayer.representations.python}}
```
<div class='select-code-block example-code-switcher json-code-block'></div>
```json
{{site.data.documentation.display.networkLayer.representations.json}}
```