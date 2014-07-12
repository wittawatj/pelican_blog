==========
Water-Iris
==========

What is water-iris?
-------------------

Water-Iris is a `pelican <http://getpelican.com>`_ theme based on the `iris <http://github.com/slok/iris>`_ theme and the `waterspill <https://github.com/getpelican/pelican-themes/tree/master/waterspill-en>`_ theme.

It follows the same idea behind Iris with some of the visual style in waterspill.

- For social icons: `Font awesome <http://fortawesome.github.com/Font-Awesome/>`_
- For the title: `Gabriela <http://www.google.com/webfonts/specimen/Gabriela>`_
- For the soure code: `Inconsolata <http://www.google.com/webfonts/specimen/Inconsolata>`_

Preview
-------

.. image:: https://raw.github.com/jarv/water-iris/master/preview.png
    :align: center

Variables
---------

Some of the variables that could be used:

- ``DISQUS_SITENAME``: For the disqus comments
- ``GOSQUARED_SITENAME``: For the Go squared analytics
- ``EMAIL``: For the email "mailto:"
- ``SOCIAL``: for github, twitter

Installation
------------

To install, clone the repo and add it as a new theme:

example::
    
    $ git clone https://github.com/jarv/water-iris.git
    $ pelican-themes -s path/to/water-iris

Set the variable ``THEME`` to ``water-iris`` in your pelican settings, like this::

    THEME = "water-iris"

Notes
-----

The theme navigation bar does a fade in if you scroll more than 300 pixels to
increase the readability of an article.

ReStructuredText creates ``tt`` with ````something```` that is equivalent to  markdown ``code``
that is created wit ```something```. This renders inline source code. So I added ``tt`` to the
css also, not only ``code`` like most themes. Example:



License
-------

This theme is under the `3 clause BSD license <http://opensource.org/licenses/bsd-3-clause>`_
