---
layout: home
nav_order: 2
parent: examples
title: display from adjacency matrix

---

{% include webweb.html webweb_json=site.data.examples.display_from_adjacency_matrix.json %}

webweb'll guess whether you've given it an edge list or adjacency matrix.

{% include code_switcher.html code_options="python---matlab---json" switcher_name="example-code-switcher" %}
<div class='select-code-block example-code-switcher python-code-block select-code-block-visible'></div>
```python
{{site.data.examples.display_from_adjacency_matrix.representations.python}}
```
<div class='select-code-block example-code-switcher matlab-code-block'></div>
```matlab
{{site.data.examples.display_from_adjacency_matrix.representations.matlab}}
```
<div class='select-code-block example-code-switcher json-code-block'></div>
```json
{{site.data.examples.display_from_adjacency_matrix.representations.json}}
```