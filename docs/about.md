---
title: about
layout: main_page
nav_order: 8
permalink: /about/

---

## who made it?

[Dan Larremore](http://larremorelab.github.io) made webweb in 2013 as a quick and easy way to visualize networks from matlab. [Michael Iuzzolino](https://www.linkedin.com/in/michael-iuzzolino-3a060696/) built the first python version. [Hunter Wapman](https://hneutr.github.io) upgraded everything to d3.v5, rebuilt the code to be smarter, faster, and more intuitive, and unified the way matlab and python work with the javascript. He also added all the colormaps, `networkx`, and multi-layer network support.

## why?

People learn a lot from visualizing a network, exploring it interactively, and sharing it with others. But if this comes at the cost of a huge number of clicks, the intuitive and exploratory loops get cut! We built webweb to make it easy to visualize a network, interactively, in as little as a single line of code.

## how?

At its core, webweb is written in javascript, and makes heavy use of [d3js](d3js.org). The python and matlab files simply write a correctly html and json, and when the html is opened, the webweb javascript builds the UI and renders the data.

The website is made using the static site-generator [jekyll](https://jekyllrb.com/). It uses a customized version of the jekyll theme [just the docs](https://pmarsceill.github.io/just-the-docs/).

## when will there be an R/stata/??? version?

As soon as someone builds one, of course! :) If there’s a language you’d like to see supported, we’d love for you to build it! We’re happy to help with the process.

If you open the hood on the existing python or matlab code, you’ll find that there’s not a whole lot to it: just a bit of error checking on the incoming data, and then writing correctly formatted json into a particular html file. This means that building an interface for webweb is as simple as mapping the three or four concepts webweb uses onto the given language. To see what kind of json that is, you can look at the `json` code snippets on every example page.

## license

GNU General Public License v3+
