---
title: about
layout: main_page
nav_order: 8
permalink: /about/

---

## who made it?

[Dan Larremore](http://danlarremore.com) made this! [Hunter Wapman](https://hneutr.github.io) worked on it too. Michael Iuzzolino first made the python interface.

Some other people helped too.

## why though?

Sometimes, you need to see a network _right now_ -- You don't want to finagle 400 libraries or debug, you just want to see it. Right. Now. Enter webweb.

## how?

The driver for webweb is written in javascript, and makes heavy use of [d3js](d3js.org).

The website is made using the static site-generator [jekyll](https://jekyllrb.com/). It uses a customized version of the jekyll theme [just the docs](https://pmarsceill.github.io/just-the-docs/).

## hey, why isn't there an interface for webweb in this other language?

There's no good reason except time and the creators' own preferences -- webweb's built to be as simple as possible on the interface side, and if there's a language you'd like to see supported, build it! We're happy to help with the process.

Really all an interface does is write a json file with a particular format into an html file with a particular format. Building an interface for webweb is as simple as mapping the three or four concepts webweb uses onto the given language. To see what kind of json that is, you can look at the `json` code snippets on every example page.
