---
layout: home
nav_order: 2
parent: display
title: c (charge)

---

{% include webweb.html webweb_json=site.data.display.c.json %}

we can change how much nodes repulse each other.



the greater the value for `c`, the stronger the nodes will repel each other.

{% include code_switcher.html code_options="python---json" switcher_name="example-code-switcher" %}
<div class='select-code-block example-code-switcher python-code-block select-code-block-visible'></div>
```python
{{site.data.display.c.representations.python}}
```
<div class='select-code-block example-code-switcher json-code-block'></div>
```json
{{site.data.display.c.representations.json}}
```