% ==========================================================================
% handout.cls -- INFO 4617 Web Data Science handouts
%
% Letter-size portrait pages that look like the course's slide frames
% (slides/common: the Gotham beamer theme plus preamble.tex): CU-gold
% frame-title bars with black bold fbb titles, the same gray and gold
% blocks, the slides' colors, and "N of M" at the bottom right.
%
% Write a handout the way you write a deck:
%
%   \makeatletter\def\input@path{{../common/}{handouts/common/}}\makeatother
%   \documentclass{handout}          % other options go to article (11pt, ...)
%   \title[Footer title]{Title}      % the short title goes in the footer
%   \subtitle{Week N · Module · Textbook Chapter N}
%   \author{...}  \institute{...}  \date{...}
%   \begin{document}
%   \maketitle
%   \begin{frame}{A frame title}    % [fragile], [t], <2-> are accepted
%     text, itemize, columns/column, block/alertblock/exampleblock,
%     code/out cells, lstlisting, figures
%   \end{frame}
%   \end{document}
%
% Build from the handout's folder (latexmk -pdf name.tex) or from the repo
% root, as Overleaf does. The \input@path line above finds this class from
% either place. \graphicspath has {./} and {../../}, as in the slides, so
% write image paths from the repo root (handouts/week-NN/img/x.png).
%
% What differs from a beamer frame, on purpose:
%   * Frames flow down the page, one after another, and a long frame
%     continues on the next page. A frame is a titled part of a page, not
%     a page. A frame title never sits alone at the bottom of a page.
%   * Every frame can hold verbatim text and listings; [fragile] is not
%     needed (and is ignored if given).
%   * Overlays do not exist on paper. \pause is ignored; \only, \uncover,
%     \visible, \onslide, and \alert accept an overlay spec and show their
%     content. \item<2-> is not supported: remove the spec.
%   * Code colors are the slides' `wds` palette, darkened for print.
%
% Extra environments for notebook handouts (not in the slides):
%   code    a code cell: gold bar, pale-gold background   (listings)
%   out     what the cell shows back: gray bar            (listings)
%   dfout   a DataFrame as Jupyter shows it: a tabular next to a gray bar;
%           the argument is the column spec, e.g. \begin{dfout}{@{}rll@{}}
%   \ol|text|  one line of output, typed literally (for use inside dfout)
%   \marker{3} or just ③   a numbered marker (handoutmarkers.sty); the
%           characters ① to ⑨ in the source print as markers
%   \breakcode{field--name-x}   a code token that may break after a hyphen
%
% Most handouts are written in Quarto markdown instead: see
% handouts/README.md. handout-template.tex and handout.lua turn a .qmd
% into a document of this class, and make_notebook.py turns the same
% .qmd into a companion notebook.
% ==========================================================================
\NeedsTeXFormat{LaTeX2e}
% \input@path finds this file as ../common/handout or handouts/common/handout,
% and LaTeX compares that path with the name given here; give it the same
% path, so LaTeX does not warn that the two names differ.
\providecommand*\@currpath{}
\edef\handout@name{\@currpath\@currname}
\expandafter\ProvidesClass\expandafter{\handout@name}%
  [2026/09/24 INFO 4617 handouts in the style of the slide frames]

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax
\RequirePackage{fix-cm}
\LoadClass[10pt]{article}

% ---------------------------------------------------------------- packages
\RequirePackage[letterpaper,left=0.75in,right=0.75in,top=0.55in,
                bottom=0.62in,footskip=0.3in]{geometry}
\RequirePackage[scaled=0.92]{helvet}   % sans, for small labels only
\RequirePackage{fbb}                   % the slides' text face
\RequirePackage[T1]{fontenc}
\RequirePackage[varqu,varl,scaled=0.95]{zi4}   % Inconsolata for code
\RequirePackage{microtype}
\RequirePackage{xparse}
\RequirePackage{graphicx}
\RequirePackage{xcolor}
\RequirePackage{array}
\RequirePackage{booktabs}
\RequirePackage{listings}
\RequirePackage{tikz}
\RequirePackage{enumitem}
\RequirePackage{fancyhdr}
\RequirePackage{lastpage}
\RequirePackage[hyphens]{url}
\RequirePackage[hidelinks]{hyperref}
\RequirePackage{accsupp}               % alt text for figures
\RequirePackage{handoutmarkers}        % \marker{n} and TikZ marker styles
\RequirePackage{newunicodechar}

% ①..⑨ in the source print as markers, so a .qmd can use the same
% characters that a notebook shows; → prints as an arrow.
\newunicodechar{①}{\marker{1}}\newunicodechar{②}{\marker{2}}
\newunicodechar{③}{\marker{3}}\newunicodechar{④}{\marker{4}}
\newunicodechar{⑤}{\marker{5}}\newunicodechar{⑥}{\marker{6}}
\newunicodechar{⑦}{\marker{7}}\newunicodechar{⑧}{\marker{8}}
\newunicodechar{⑨}{\marker{9}}
\newunicodechar{→}{\ensuremath{\rightarrow}}
% a code token in running text that may break after a hyphen
\DeclareUrlCommand\breakcode{\urlstyle{tt}}

% Images: the same two dialects as the slides (see header).
\graphicspath{{./}{../../}}

% ------------------------------------------------------------------ colors
% The slides' palette (slides/common/preamble.tex) ...
\definecolor{cugold}{HTML}{CFB87C}
\definecolor{tab-red}{HTML}{E15759}
\definecolor{tab-orange}{HTML}{F28E2B}
\definecolor{tab-blue}{HTML}{4E79A7}
\definecolor{tab-cyan}{HTML}{76B7B2}
\definecolor{tab-green}{HTML}{59A14F}
\definecolor{tab-yellow}{HTML}{EDC948}
\definecolor{tab-purple}{HTML}{B07AA1}
\definecolor{tab-pink}{HTML}{FF9DA7}
\definecolor{tab-brown}{HTML}{9C755F}
\definecolor{tab-gray}{HTML}{BAB0AC}
% ... and the Gotham colors the decks actually render with, sampled from
% the compiled slides: block title and body, pale block text, alert and
% example colors.
\definecolor{handoutblocktitle}{HTML}{757575}
\definecolor{handoutblockbody}{HTML}{BABABA}
\definecolor{handoutpale}{HTML}{FFFFF0}
\definecolor{handoutalert}{HTML}{EB811B}
\definecolor{handoutexample}{HTML}{14B03D}
\colorlet{handoutcodebg}{cugold!10}

% ------------------------------------------------------------ page layout
\setlength{\parindent}{0pt}
\setlength{\parskip}{2.5pt plus 1pt}
\raggedbottom
\newcommand{\handout@shorttitle}{}
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\fancyfoot[L]{\footnotesize\color{black!60}\handout@shorttitle}
\fancyfoot[R]{\footnotesize\thepage{} of \pageref{LastPage}}
\fancypagestyle{plain}{}   % \maketitle's page gets the same footer

% Start a new page only if less than #1 is left on this one. Unlike the
% needspace package, it adds no negative penalty, so on a ragged-bottom
% page LaTeX does not break early just because a frame starts here.
\newcommand{\handoutneedspace}[1]{%
  \par
  \ifdim\pagegoal<\maxdimen
    \dimen@=\pagegoal \advance\dimen@ by -\pagetotal
    \ifdim\dimen@<#1\relax\newpage\fi
  \fi}

% ------------------------------------------------------------------- title
% Beamer's forms: \title[short]{long}, \subtitle, \author, \institute, \date.
\def\handout@subtitle{}\def\handout@institute{}
\RenewDocumentCommand{\title}{ o m }{%
  \gdef\@title{#2}\gdef\handout@shorttitle{\IfValueTF{#1}{#1}{#2}}}
\NewDocumentCommand{\subtitle}{ o m }{\gdef\handout@subtitle{#2}}
\RenewDocumentCommand{\author}{ o m }{\gdef\@author{#2}}
\NewDocumentCommand{\institute}{ o m }{\gdef\handout@institute{#2}}
\RenewDocumentCommand{\date}{ o m }{\gdef\@date{#2}}

% The slides' title page, made compact: centered title and subtitle, a
% gold rule, then author, institute, and date.
\renewcommand{\maketitle}{%
  \par\begingroup\centering
  {\LARGE\bfseries\@title\par}%
  \ifx\handout@subtitle\@empty\else
    \vspace{3pt}{\large\handout@subtitle\par}\fi
  \vspace{5pt}{\color{cugold}\rule{\linewidth}{1.6pt}}\par\vspace{3pt}%
  {\small
   \ifx\@author\@empty\else{\bfseries\@author}\fi
   \ifx\handout@institute\@empty\else
     \ifx\@author\@empty\else\ \textperiodcentered\ \fi\handout@institute\fi
   \par
   \ifx\@date\@empty\else\@date\par\fi}%
  \endgroup
  \vspace{2pt}}

% ------------------------------------------------------------------ frames
\newlength{\handoutbaroutdent} \setlength{\handoutbaroutdent}{0.28in}
\newlength{\handoutbarpad}     \setlength{\handoutbarpad}{8pt}
\newlength{\handoutframeskip}  \setlength{\handoutframeskip}{5pt}
\newlength{\handoutkeep}       \setlength{\handoutkeep}{5\baselineskip}

% The frame-title bar: CU gold, wider than the text by \handoutbaroutdent
% on each side (the slides' bar runs edge to edge), with a black bold
% title inset by \handoutbarpad, the way the slide title sits left of the
% frame's text.
\newcommand{\handout@bar}[1]{%
  \handoutneedspace{\handoutkeep}%
  \noindent\makebox[\linewidth][l]{\hspace*{-\handoutbaroutdent}%
    {\setlength{\fboxsep}{0pt}\colorbox{cugold}{%
      \begin{minipage}{\dimexpr\linewidth+2\handoutbaroutdent\relax}%
        \vspace*{3.5pt}%
        \raggedright\leftskip=\handoutbarpad
        \rightskip=\dimexpr\handoutbarpad\relax plus 1fil\relax
        {\large\bfseries\color{black}#1\strut\par}%
        \vspace*{2.5pt}%
      \end{minipage}}}}%
  \par\nobreak\vspace{2pt}}
\newcommand{\handout@subbar}[1]{%
  {\itshape #1\par}\nobreak}

\let\frame\relax\let\endframe\relax   % the kernel's picture-mode \frame
% \begin{frame}<overlay>[options]{title}{subtitle}; all but the title are
% accepted and ignored.
\NewDocumentEnvironment{frame}{ D<>{} O{} g g }{%
  \par\addvspace{\handoutframeskip}%
  \IfValueT{#3}{\handout@bar{#3}}%
  \IfValueT{#4}{\handout@subbar{#4}}%
  \ignorespaces
}{\par}
\newcommand{\frametitle}[1]{\handout@bar{#1}}
\newcommand{\framesubtitle}[1]{\handout@subbar{#1}}

% A section, like the slides' section page: "N. Title" over a gold bar.
\RenewDocumentCommand{\section}{ s o m }{%
  \par\addvspace{14pt}\handoutneedspace{9\baselineskip}%
  \IfBooleanF{#1}{\refstepcounter{section}}%
  \noindent{\Large\bfseries\IfBooleanF{#1}{\thesection.\ }#3\par}%
  \nobreak\vspace{2pt}\noindent
  \rlap{\color{cugold!20}\rule{\linewidth}{2.5pt}}%
  {\color{cugold}\rule{0.12\linewidth}{2.5pt}}\par\nobreak\vspace{4pt}}

% ----------------------------------------------------------------- columns
% \begin{columns}[T] \begin{column}{0.6\textwidth} ... \end{column} ...
% Columns share the text width with the space between them, as with
% beamer's [onlytextwidth]. Options: T (tops aligned), t, c (default), b.
% Each column is set in its own box, and \end{columns} puts the boxes on one
% line, so blank lines between the columns (which Pandoc writes) do not
% stack them. Columns do not nest.
\newcount\handout@ncols
\def\handout@colpos{c}\def\handout@coltop{}
\newcommand{\handout@setcolpos}[1]{%
  \gdef\handout@colpos{c}\gdef\handout@coltop{}%
  \@for\handout@opt:=#1\do{%
    \def\handout@tmp{T}\ifx\handout@opt\handout@tmp
      \gdef\handout@colpos{t}\gdef\handout@coltop{\vspace{0pt}}\fi
    \def\handout@tmp{t}\ifx\handout@opt\handout@tmp\gdef\handout@colpos{t}\fi
    \def\handout@tmp{b}\ifx\handout@opt\handout@tmp\gdef\handout@colpos{b}\fi}}
\newcommand{\handout@colbox}[1]{\csname handout@colbox@\romannumeral#1\endcsname}
\NewDocumentEnvironment{columns}{ O{} }{%
  \par\addvspace{3pt}%
  \handout@setcolpos{#1}\global\handout@ncols=0\relax\ignorespaces
}{%
  \par\noindent
  \count@=0
  \loop\ifnum\count@<\handout@ncols
    \advance\count@ by 1
    \ifnum\count@>1 \hfill\fi
    \usebox{\handout@colbox{\count@}}%
  \repeat
  \par\addvspace{3pt}\ignorespacesafterend}
\NewDocumentEnvironment{column}{ O{} m }{%
  \global\advance\handout@ncols by 1
  \@ifundefined{handout@colbox@\romannumeral\handout@ncols}%
    {\expandafter\newsavebox\csname handout@colbox@\romannumeral\handout@ncols\endcsname}{}%
  \ifx\relax#1\relax\else\handout@setcolpos{#1}\fi
  \begin{lrbox}{\handout@colbox{\handout@ncols}}%
  \begin{minipage}[\handout@colpos]{#2}\handout@coltop
}{\end{minipage}\end{lrbox}%
  % lrbox fills the box only inside this environment; keep it for \end{columns}
  \global\setbox\handout@colbox{\handout@ncols}=\box\handout@colbox{\handout@ncols}%
  \ignorespacesafterend}

% ------------------------------------------------------------------ blocks
% block: gray title, pale text, gray body (the decks' plain block);
% alertblock: gold title, black text, pale-gold body (preamble.tex);
% exampleblock: green title, pale text, gray body.
\newsavebox{\handout@blockbox}
\newcommand{\handout@block}[4]{% title bg, title fg, body bg, title
  \par\addvspace{5pt}\noindent
  \def\handout@blockbg{#3}%
  \ifx\relax#4\relax\else
    {\setlength{\fboxsep}{0pt}\colorbox{#1}{%
      \begin{minipage}{\linewidth}\vspace*{2.5pt}%
        \leftskip=4pt\rightskip=4pt plus 1fil\relax
        {\bfseries\color{#2}#4\strut\par}\vspace*{1.5pt}%
      \end{minipage}}}\par\nobreak\nointerlineskip\noindent
  \fi
  \begin{lrbox}{\handout@blockbox}%
  \begin{minipage}{\dimexpr\linewidth-8pt\relax}\vspace*{1pt}}
\newcommand{\handout@endblock}{%
  \par\vspace*{1pt}\end{minipage}\end{lrbox}%
  {\setlength{\fboxsep}{4pt}\colorbox{\handout@blockbg}{\usebox{\handout@blockbox}}}%
  \par\addvspace{5pt}}
\newenvironment{block}[1]%
  {\handout@block{handoutblocktitle}{handoutpale}{handoutblockbody}{#1}}%
  {\handout@endblock}
\newenvironment{alertblock}[1]%
  {\handout@block{cugold}{black}{cugold!10}{#1}}{\handout@endblock}
\newenvironment{exampleblock}[1]%
  {\handout@block{handoutexample}{handoutpale}{handoutblockbody}{#1}}%
  {\handout@endblock}

% ---------------------------------------------- beamer commands on paper
\NewDocumentCommand{\alert}{ D<>{} m }{\textcolor{handoutalert}{#2}}
\NewDocumentCommand{\structure}{ D<>{} m }{#2}
\NewDocumentCommand{\only}{ D<>{} m D<>{} }{#2}
\NewDocumentCommand{\uncover}{ D<>{} m }{#2}
\NewDocumentCommand{\visible}{ D<>{} m }{#2}
\NewDocumentCommand{\onslide}{ t+ D<>{} }{}
\newcommand{\pause}[1][]{}
\newcommand{\note}[2][]{}
% From slides/common/preamble.tex:
\newcommand{\dayband}[2]{{\large\textbf{#1}}\;\textcolor{tab-gray}{\textbar}\;#2}
\newcommand{\bottomcite}[1]{\par\vspace{2pt}{\scriptsize
  \color{black!60}\rule{\linewidth}{0.3pt}\\#1\par}}

% ------------------------------------------------------------------- lists
\setlist{topsep=2pt,itemsep=1pt,parsep=0pt}
% the slides' solid round bullets
\setlist[itemize,1]{label=\raisebox{0.28ex}{\tikz\fill(0,0)circle(0.21em);},leftmargin=1.3em}
\setlist[itemize,2]{label=\raisebox{0.32ex}{\tikz\fill(0,0)circle(0.15em);},leftmargin=1.2em}

% ------------------------------------------------------------------- code
% The slides' `wds` style (keywords tab-blue, comments tab-green, strings
% tab-orange), with green and orange darkened for contrast on paper.
\newcommand{\handoutcodefont}{\ttfamily\fontsize{8}{9}\selectfont}
\lstdefinestyle{wds}{
  language=Python,
  basicstyle=\handoutcodefont,
  keywordstyle=\color{tab-blue}\bfseries,
  commentstyle=\color{tab-green!70!black},
  stringstyle=\color{tab-orange!72!black},
  showstringspaces=false,
  breaklines=true,
  columns=fullflexible, keepspaces=true, upquote=true,
  literate={é}{{\'e}}1,
}
\lstset{style=wds}
\lstdefinestyle{handoutcode}{
  style=wds,
  backgroundcolor=\color{handoutcodebg},
  frame=leftline, framerule=2.4pt, rulecolor=\color{cugold},
  xleftmargin=9pt, framexleftmargin=6pt,
  aboveskip=3pt, belowskip=0pt,
}
\lstdefinestyle{handoutout}{
  language={},
  basicstyle=\handoutcodefont\color{black!85},
  columns=fullflexible, keepspaces=true, upquote=true,
  breaklines=true,
  frame=leftline, framerule=2.4pt, rulecolor=\color{handoutblockbody},
  xleftmargin=9pt, framexleftmargin=6pt,
  aboveskip=2pt, belowskip=3pt,
  literate={é}{{\'e}}1,
}
\lstnewenvironment{code}{\lstset{style=handoutcode}}{}
\lstnewenvironment{out}{\lstset{style=handoutout}}{}
\newcommand{\ol}{\lstinline[style=handoutout]}
\newenvironment{dfout}[1]{%
  \par\vspace{1pt}\noindent\hspace{3pt}%
  {\color{handoutblockbody}\vrule width 2.4pt}\hspace{6pt}%
  \fontsize{8}{9.6}\selectfont\begin{tabular}[b]{#1}}%
  {\end{tabular}\par\vspace{3pt}}
\newcommand{\hd}[1]{\textbf{\ttfamily #1}}   % a DataFrame column header

\endinput
