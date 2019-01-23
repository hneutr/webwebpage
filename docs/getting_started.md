---
title: getting started
layout: main_page
nav_order: 2
permalink: /getting-started/
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

Check out the [examples](/examples/) page for more usecases!
