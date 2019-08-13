---
title: webweb
nav_order: 1
layout: home
permalink: /

---

# webweb

webweb is a tool for creating, displaying, and sharing interactive network visualizations on the web, designed for simplicity and ease of use. With just a few lines of `python`, `networkx`, or `matlab`, webweb will build and launch a visualization in your browser.

Here’s an example of webweb’s style and functionality. The network itself comes from [Hunter Wapman](http://hneutr.github.io/) et al.’s analysis of character co-occurrences in the novel _Infinite Jest_.

{% include webweb.html webweb_json=site.data.infinite_jest responsive=true %}

## features

- simple, lightweight, intuitive, and configurable
- `python`, `networkx`, and `MATLAB` support
- easy to share (visualizations are contained in a single html file that has no dependencies)
- easy to embed
- supports metadata, communities, weighted networks, and multi-layer networks

---

## the simplest example

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

## installation

{% include code_switcher.html code_options="python---matlab" switcher_name="install-switcher" %}
<div class='select-code-block python-code-block select-code-block-visible install-switcher'></div>

```python
# requires numpy
pip install webweb
```
<div class='select-code-block matlab-code-block install-switcher'></div>
```matlab
git clone https://github.com/dblarremore/webweb
```

## citing webweb

{% include webweb_citation.html %}
