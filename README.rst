====================
Yield Curve Dynamics
====================


.. image:: https://img.shields.io/pypi/v/yield_curve_dynamics.svg
        :target: https://pypi.python.org/pypi/yield_curve_dynamics

.. image:: https://travis-ci.com/luphord/yield_curve_dynamics.svg
        :target: https://travis-ci.com/luphord/yield_curve_dynamics

.. image:: https://readthedocs.org/projects/yield-curve-dynamics/badge/?version=latest
        :target: https://yield-curve-dynamics.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




A cursory look at the dynamics of zero coupon bond yield curves.

* Data source: Zero coupon bond yield curve data published by European Central Bank (ECB)
* Visualization: Animated plot shows a video of historic yield curves
* Analysis: Principal Component Analysis (PCA) is applied to (shifted) log diffs of keyrates in order to reduce the dimensionality of curve movements
* Key insight: Three factors (parallel shift, steepening and hump) can capture the majority of curve movements
* Structure: Functionality is contained in the `yield_curve_dynamics` Python package, presentation is performed using Jupyter notebooks in the `notebooks` directory
* Free software: MIT license
* Documentation: https://yield-curve-dynamics.readthedocs.io.
* Slides_

.. _Slides: https://rawcdn.githack.com/luphord/yield_curve_dynamics/5d435148137b815b2bcc9d48244a1356253defd1/lightning_talk_2019-04-04/Yield%20Curve%20Dynamics.slides.html


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
