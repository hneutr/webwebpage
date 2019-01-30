---
grand_parent: documentation
layout: home
nav_order: 2
parent: display
title: charge

---

{% include webweb.html webweb_json=site.data.documentation.display.charge.json %}

```json
type: positive non-zero integer
synonyms: c
default: 60
````
we can change how much nodes repulse each other.



the greater the value for `charge`, the more nodes will repel each other.

{% include code_switcher.html code_options="python---json" switcher_name="example-code-switcher" %}
<div class='select-code-block example-code-switcher python-code-block select-code-block-visible'></div>
```python
{{site.data.documentation.display.charge.representations.python}}
```
<div class='select-code-block example-code-switcher json-code-block'></div>
```json
{{site.data.documentation.display.charge.representations.json}}
```