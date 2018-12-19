---
layout: home
nav_order: 7
parent: examples
title: show web only

---

{%- capture code_options -%}
python---json
{%- endcapture -%}
{% include code_switcher.html code_options=code_options %}
<div id='python-code-block' class='select-code-block select-code-block-visible'></div>
```python
{{site.data.examples.show_web_only.code.python}}
```
<div id='json-code-block' class='select-code-block'></div>
```json
{{site.data.examples.show_web_only.json.pretty}}
```