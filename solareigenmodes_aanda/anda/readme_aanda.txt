LaTeX2e v8.2 class for Astronomy & Astrophysics 
(c) EDP Sciences, 2013
What's New in AA v8.2 (April 2013)

Main change in the 8.x versions 
A&A now accepts TeX files designed for LaTeX as well as PDFLaTeX. 
Depending on your preferred LaTeX engine (LaTeX or pdfLaTeX), figures should be sent as encapsulated PostScript files or in any other format as PDF, JPG, TIF, BMP, and GIF (compatible with pdfLaTeX).
The new macro does not include the classes traditabstract and structabstract anymore. They are replaced by the command \abstract. See new instructions for details.
Change between 8.1 and 8.2 
To enable compatibility with 7.x versions, an option has been added. If you don't write structured references (according to to the author-year natbib style), use this option:
\documentclass[bibyear]{aa}

The following files are part of the macro package AA

readme.txt: Information (equivalent to this page)
aa.cls: The document class file
aadoc.pdf: User's Guide (pdf)
aa.dem: Example of an article (LaTeX source)
Directory for BIBTeX style
aa.bst: Bibliography style file
natbib.sty: This package reimplements the LaTeX \cite command
natnotes.pdf: Brief reference sheet for Natbib (pdf)
Remember to transfer dvi and pdf files as binaries!
All files are compressed in a single archive:
aa-package.tar.gz

Tips
How to add in-text citation clickers that link to the corresponding ADS abstract pages. 
Contributed by Robert J. Rutten of Utrecht University.
This is a latex recipe to turn the in-text citations into clickers (in xdvi and the pdf or html output file) that link into ADS, opening the corresponding abstract page in the browser. In this manner, an on-screen reader of your paper may open the cited abstract or download the cited paper in parallel to reading your paper, without jumping to the reference list of the latter.

Insert the following commands into the preamble of your latex file:

\usepackage{natbib,twoopt}
\usepackage[breaklinks=true]{hyperref} %% to avoid \citeads line fills
\bibpunct{(}{)}{;}{a}{}{,} %% natbib format for A&A and ApJ
\makeatletter
\newcommandtwoopt{\citeads}[3][][]{\href{http://adsabs.harvard.edu/abs/#3}%
{\def\hyper@linkstart##1##2{}%
\let\hyper@linkend\@empty\citealp[#1][#2]{#3}}}
\newcommandtwoopt{\citepads}[3][][]{\href{http://adsabs.harvard.edu/abs/#3}%
{\def\hyper@linkstart##1##2{}%
\let\hyper@linkend\@empty\citep[#1][#2]{#3}}}
\newcommandtwoopt{\citetads}[3][][]{\href{http://adsabs.harvard.edu/abs/#3}%
{\def\hyper@linkstart##1##2{}%
\let\hyper@linkend\@empty\citet[#1][#2]{#3}}}
\newcommandtwoopt{\citeyearads}[3][][]%
{\href{http://adsabs.harvard.edu/abs/#3}
{\def\hyper@linkstart##1##2{}%
\let\hyper@linkend\@empty\citeyear[#1][#2]{#3}}}
\makeatother
Usage: use ADS biblabels and enter one per \citeads command, as in:

The existence of two emission features in the solar spectrum near
12~$\mu$m was announced by
\citetads{1981ApJ...247L..97M}. %% Murcray+others, MgI features
We explained them long ago
\citepads[see][]{1992A&A...253..567C}, %% Carlsson+Rutten+Shchukina MgI
using the standard model of the solar atmosphere formulated in the
monumental papers by Vernazza et al.\ 
(\citeyearads{1973ApJ...184..605V}, % VALI 
\citeyearads{1976ApJS...30....1V}, % VALII 
\citeyearads{1981ApJS...45..635V}). % VALIII 
This trick was contributed by Robert J. Rutten of Utrecht University. The above example of its usage is taken from his latex manual and template for students at http://www.staff.science.uu.nl/~rutte101/Report_recipe.html 
History
The new 2001 Astronomy and Astrophysics journal. 
In order to ensure the smoothest transition for both authors and publishers, Springer-Verlag has kindly granted EDP Sciences the permission to use the LaTeX macro package that they developed for A&A Main journal. 
Only minor changes have been incorporated between the Springer class (1999) and the EDP Sciences class for the new journal. 
Please, note: 
- that the abstract is now a command (\abstract{...}) and not an environment, so the \maketitle command has to be placed after the abstract and the keywords 
- and that the command \thesaurus does no longer exist. 
The journal is now printing using the Postscript TX Times-fonts. 
The TX fonts consist of virtual text roman fonts using Adobe Times with some modified and additional text symbols. 
The TX fonts are distributed under the GNU public license and are available in the LaTeX distributions since December 2000. 
In any case, these fonts and the installation guide are also available in every public TeX archive server, i.e.: 
http://www.tug.org/tex-archive/fonts/txfonts/ 
ftp://ftp.dante.de/tex-archive/fonts/txfonts/ 
ftp://ftp.tex.ac.uk/tex-archive/fonts/txfonts/ 
Please contact your system administrator to install it. 
Since this change of fonts results in a slightly different page make-up from CM fonts, we encourage you to use TX fonts. To proceed, all you need is: 
\documentclass{aa} 
\usepackage{txfonts} 
... 
