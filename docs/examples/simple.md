---
layout: home
nav_order: 8
parent: examples
title: simple

---

{%- capture code_options -%}
python---matlab---json
{%- endcapture -%}
{% include code_switcher.html code_options=code_options %}
<div id='python-code-block' class='select-code-block select-code-block-visible'></div>
```python
{{site.data.examples.simple.code.python}}
```
<div id='matlab-code-block' class='select-code-block'></div>
```matlab
{{site.data.examples.simple.code.matlab}}
```
<div id='json-code-block' class='select-code-block'></div>
```json
{{site.data.examples.simple.json.pretty}}
```