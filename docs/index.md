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

## Alright, I have an adjacency matrix, how do I get this webweb thing to show it to me?

{% include code_switcher.html code_options="python---matlab" switcher_name="simple-code" %}

<div class='select-code-block select-code-block-visible python-code-block simple-code'></div>
```python
from webweb import Web

# Connect two nodes
edge_list = [[0, 1]]

# Instantiate webweb object
web = Web(edge_list)

# Launch webbrowser with result
web.draw()
```
<div class='select-code-block matlab-code-block simple-code'></div>
```matlab
A = floor(1.01 * rand(100,100)); 
A = A + A'; 
A(A>0) = 1;
webweb(A);
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
git clone //https://github.com/dblarremore/webweb
```

