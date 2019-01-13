---
title: webweb
nav_order: 1
layout: home
permalink: /

---

# webweb!

a tool for creating, displaying, and sharing interactive network visualizations on the web designed for simplicity and ease of use.

{% include webweb.html webweb_json=site.data.infinite_jest width=600 height=600 %}

## features

- draws simple graphs
- can handle multiple networks
- supports layered networks (e.g., networks that change in time)
- creates a single file without dependencies for easy sharing
- embeddable
- language support for [MATLAB](http://danlarremore.com/webweb/) and [python](https://github.com/hneutr/webweb), as well as [networkx](http://networkx.github.io/)

It's mostly written in javascript (making heavy use of [d3js](d3js.org)).

---

## Why though?
Sometimes, you need to see a network _right now_ -- You don't want to finagle 400 libraries or debug, you just want to see it. Right. Now. Enter webweb.

---

## Alright, I have an adjacency matrix, how do I get this webweb thing to show it to me?

<p></p>

{% include code_switcher.html code_options="python---matlab" %}

<div id='python-code-block' class='select-code-block select-code-block-visible'></div>
```python
from webweb import Web

# Connect two nodes
edge_list = [[0, 1]]

# Instantiate webweb object
web = Web(edge_list)

# Launch webbrowser with result
web.draw()
```
<div id='matlab-code-block' class='select-code-block'></div>
```matlab
A = floor(1.01 * rand(100,100)); 
A = A + A'; 
A(A>0) = 1;
webweb(A);
```

---

## How do I install it?

{% include code_switcher.html code_options="python---matlab" %}
<div id='python-code-block' class='select-code-block select-code-block-visible'></div>
```python
pip install webweb
```
<div id='matlab-code-block' class='select-code-block'></div>
```matlab
git clone //https://github.com/dblarremore/webweb
```

