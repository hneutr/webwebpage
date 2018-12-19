---
layout: home
nav_order: 7
parent: examples
title: simple
viewables: ['python', 'matlab', 'json']

---

{% include _option_switcher.html option_values=page.viewables %}

```python
{{site.data.examples.simple.code.python}}
```
```matlab
{{site.data.examples.simple.code.matlab}}
```
```json
{{site.data.examples.simple.json.pretty}}
```
