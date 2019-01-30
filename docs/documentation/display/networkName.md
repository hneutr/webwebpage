---
grand_parent: documentation
layout: home
nav_order: 15
parent: display
title: networkName

---

{% include webweb.html webweb_json=site.data.documentation.display.networkName.json fix_width=false fix_height=false %}

```json
type: string
````
webweb will by default display the first network we add to it, but if we'd like to show a particular one we can do so by setting the `display.networkName` property to name of the network we'd like to show.

{% include code_switcher.html code_options="python---json" switcher_name="example-code-switcher" %}
<div class='select-code-block example-code-switcher python-code-block select-code-block-visible'></div>
```python
{{site.data.documentation.display.networkName.representations.python}}
```
<div class='select-code-block example-code-switcher json-code-block'></div>
```json
{{site.data.documentation.display.networkName.representations.json}}
```