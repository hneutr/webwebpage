---
layout: home
nav_order: 10
parent: examples
title: timeslice

---

{%- capture code_options -%}
python---json
{%- endcapture -%}
{% include code_switcher.html code_options=code_options %}
<div id='python-code-block' class='select-code-block select-code-block-visible'></div>
```python
{{site.data.examples.timeslice.code.python}}
```
<div id='json-code-block' class='select-code-block'></div>
```json
{{site.data.examples.timeslice.json.pretty}}
```