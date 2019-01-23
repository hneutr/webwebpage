---
title: webweb
nav_order: 1
layout: home
permalink: /

---

# webweb!

a tool for creating, displaying, and sharing interactive network visualizations on the web designed for simplicity and ease of use.

{% include webweb.html webweb_json=site.data.infinite_jest responsive=true %}

## features

- simple and configurable model
- easy to share (one file, no dependencies)
- easy to embed
- does what you need it to (multiple networks, layered networks)
- interfaces for multiple languages (`python`, `MATLAB`) and libraries (`networkx`)

---

## How do I run it?

{% include code_switcher.html code_options="python---matlab" switcher_name="simple-code" %}

<div class='select-code-block select-code-block-visible python-code-block simple-code'></div>
```python
from webweb import Web

# make a list of unweighted edges
edge_list = [[1, 2], [2, 3], [3, 4]]

# instantiate webweb and show the result
Web(edge_list).show()
```
<div class='select-code-block matlab-code-block simple-code'></div>
```matlab
% make a list of unweighted edges
edge_list = [...
    1, 2;
    2, 3;
    3, 4;
    ];
webweb(edge_list);
```

---

## How do I install it?

{% include code_switcher.html code_options="python---matlab" switcher_name="install-switcher" %}
<div class='select-code-block python-code-block select-code-block-visible install-switcher'></div>
```python
pip install webweb
```
<div class='select-code-block matlab-code-block install-switcher'></div>
```matlab
git clone https://github.com/dblarremore/webweb
```
