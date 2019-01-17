---
layout: home
nav_order: 15
parent: display
title: networkName

---

{% include webweb.html webweb_json=site.data.display.networkName.json %}

webweb will by default display the first network you add to it, but if you'd like to show a particular one you can do so by setting the `display.networkName` property to name of the network you'd like to show.

{% include code_switcher.html code_options="python---json" switcher_name="example-code-switcher" %}
<div class='select-code-block example-code-switcher python-code-block select-code-block-visible'></div>
```python
{{site.data.display.networkName.representations.python}}
```
<div class='select-code-block example-code-switcher json-code-block'></div>
```json
{{site.data.display.networkName.representations.json}}
```