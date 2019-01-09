---
layout: home
nav_order: 3
parent: examples
title: named nodes

---

<div id='webweb-example-visualization' style='width: 100%'></div>
{% assign webweb_json=site.data.examples.named_nodes.json | jsonify %}
{% include webweb_dependencies.html webweb_json=webweb_json %}

{% include code_switcher.html code_options="python---json" %}
<div id='python-code-block' class='select-code-block select-code-block-visible'></div>
```python
{{site.data.examples.named_nodes.representations.python}}
```
<div id='json-code-block' class='select-code-block'></div>
```json
{{site.data.examples.named_nodes.representations.json}}
```