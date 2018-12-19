---
title: webweb
nav_order: 1
layout: home
permalink: /

---

# webweb!

webweb is a tool for displaying interactive network visualizations on the web! It's designed to make showing and sharing networks as easy as possible.

It's mostly written in javascript (making heavy use of [d3js](d3js.org)), and has interfaces for [MATLAB](http://danlarremore.com/webweb/) and [python](https://github.com/hneutr/webweb).

{% include svg/infinite_jest.svg %}

---

## Alright, I have an adjacency matrix, how do I get this webweb thing to show it to me?

<p></p>

{%- capture code_options -%}
python---matlab
{%- endcapture -%}

{% include code_switcher.html code_options=code_options %}

<div id='python-code-block' class='select-code-block select-code-block-visible'></div>
```python
from webweb.webweb import webweb

# Instantiate webweb object
web = webweb()

# Connect two nodes
adjacency_list = [[0, 1]]

# Assign adjaceny lists in network
web.networks.my_network.add_layer(adjaceny_list)

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

xxx
---

## Why though?
Sometimes, you just want to _see_ your adjacency list! You don't want to finagle with 400 libraries and debug, you just want to see it. Enter webweb.

