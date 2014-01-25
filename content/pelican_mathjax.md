Title: Pelican for Math-based Blogs
Date: 2014-01-25
Slug: pelican_mathjax
Tags: blog, math, tool


I recently moved from Haskell-based [Hakyll](http://jaspervdj.be/hakyll/) to Python-based [Pelican](http://docs.getpelican.com/) for my web site. 
Both of them are flexible static site generators. 
The following is a summary of important points to set up a [Mathjax](http://www.mathjax.org/)-based blog with Pelican.

* **Start**: Start by following this official [guide](http://docs.getpelican.com/en/3.3.0/getting_started.html). 
At this point, you should be able to have a simple blog running.

* **Setting**: Almost all customizations can be done in `pelicanconf.py`. See [settings documentation](http://docs.getpelican.com/en/3.3.0/settings.html) and add relevant variables you want to change. See also this [example settings](http://docs.getpelican.com/en/3.3.0/settings.html#example-settings).

* **Theme**: To change themes, first clone the pre-made themes from [this Git repository](https://github.com/getpelican/pelican-themes). In `pelicanconf.py`, set 

		THEME = '<path_to_theme_folder>/<theme_name>'
  Theme previews can be found [here](http://pelicanthemes.com/).

* **First page**: Some theme comes with its own first page. In fact most of them set the homepage as a list of blog entries. To have your own static homepage, see this [FAQ](http://docs.getpelican.com/en/3.3.0/faq.html#how-can-i-use-a-static-page-as-my-home-page).

* **Custom menu**: Most likely your chosen theme will put one post category as one menu item in the navigation bar. If this is not what you want, check the key `DISPLAY_CATEGORIES_ON_MENU` in the setting. For extra menu items, use 

		MENUITEMS = [ ('item1', 'link to item1'), ('item2', 'link to item2') ]

## Pelican with Mathjax

Using Pelican with Mathjax can be tricky. This is especially the case if posts are written in Markdown. 
Symbols like * and _ in your equations can confuse the Markdown parser. To set up Mathjax in your Pelican system, follow these steps.

1. Install [Latex plugin for Pelican](https://github.com/barrysteyn/pelican_plugin-latex). Follow the guide on the web. 
At this point Mathjax will work unless you use * or _ (well who doesn't ?) in your equations which will interfere with the Markdown parser and break everything.

2. To solve the problem, we need to add an extension to the `python-markdown` (the underlying Markdown parser) so that it knows about Mathjax. 
So, install this [python-markdown-mathjax](https://github.com/mayoff/python-markdown-mathjax) extension. The Mathjax should work perfectly at this point. If you do not have a root access to the system-wide `python-markdown`, you will not be able to put `python-markdown-mathjax` into `extension` folder. In that case, simply install `python-markdown` locally in your home and modify `PYTHONPATH` to include it. This is described in the homepage of python-markdown-mathjax. 


