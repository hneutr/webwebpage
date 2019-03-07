---
layout: home
nav_order: 11
parent: examples
title: kitchen sink

---

{% include webweb.html webweb_json=site.data.examples.kitchen_sink.json fix_width=false fix_height=false %}

an example showing a bunch of ways to set node metadata, display networks, etc.

{% include code_switcher.html code_options="python---matlab---json" switcher_name="example-code-switcher" %}
<div class='select-code-block example-code-switcher python-code-block select-code-block-visible'></div>
```python
{{site.data.examples.kitchen_sink.representations.python}}
```
<div class='select-code-block example-code-switcher matlab-code-block'></div>
```matlab
{{site.data.examples.kitchen_sink.representations.matlab}}
```
<div class='select-code-block example-code-switcher json-code-block'></div>
```json
{{site.data.examples.kitchen_sink.representations.json}}
```