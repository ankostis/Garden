# Scientific authoring

- Papers are written either the *LaTeX*-way or the *MS*-way.
- In the meantime, *Jupiter notebooks* became the de facto *data publication medium*
  (ever since the biggest breakthrough in Astrophysics [was made live with a notebook](https://gwosc.org/s/events/GW150914/GW150914_tutorial.html))
  - ...where *Markdown* is the de facto *text* medium around scientific calculations.
  - BUT remains the tedious and error-prone task of porting jupyter *diagrams & calculations*
    into *MS Word*.
- In the parallel universe, programmers had figured out that the *ReSTructuredText*
  in Python's *Spinx* was *extensible* enough to match many essential LaTeX features,
  like cross-referencing figures, formulas, sections & bibliography, CSS theming,
  exporting to PDF/epub/LaTex, etc,
  - ...but RsT is not as simple as *Markdown*, and setting up Sphinx is a pain...
- Since 2 years ago, this applies no more:
  - **[Jupyter Book](https://jupyterbook.org/)** offers the best from both worlds:
    - [extensible](https://myst-parser.readthedocs.io/en/v0.17.1/syntax/syntax.html)
      & [capable Markdown](https://commonmark.org/) based on **MyST**,
    - coupled with Jupyter's live data processing & diagrams,
    - packaged in an easy to setup **Sphinx** installation.
- Practically, in a couple of years you may be authoring your papers
  completly in *Jupyter Book*.
- Resources:
  - [Jupyter Book 101 (28:09)](https://www.youtube.com/watch?v=lZ2FHTkyaMU)

## Publishing

- LaTeX --> pdf
- html --> pdf - so [CSS apply](https://jupyterbook.org/en/stable/advanced/pdf.html#control-the-look-of-pdf-via-html)
