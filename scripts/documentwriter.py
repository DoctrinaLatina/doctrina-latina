from enum import Enum, auto
from fileio import *


class PageSize(Enum):
  PRINTER = auto()
  BOOK_A5 = auto()

class Prayer(Enum):
  PRINCIPIUM = auto()
  REX_CAELESTIS = auto()
  OMNISANCTA_TRINITAS = auto()
  TRISAGION = auto()
  VENITE = auto()
  GLORIA_PATRI = auto()
  KYRIE_ELEISON_3 = auto()
  KYRIE_ELEISON_12 = auto()
  PATER_NOSTER = auto()
  AVE_MARIA = auto()
  TE_LUCIS_ANTE_TERMINUM = auto()
  CONFITEOR = auto()
  CONFITEOR_RESPONSIO = auto()
  COMPLETORIUM_LECTIO_BREVIS_1 = auto()
  COMPLETORIUM_LECTIO_BREVIS_2 = auto()
  COMPLETORIUM_ORATIO_1 = auto()
  COMPLETORIUM_ANTIFONA_1 = auto()

class DocumentWriter:

  __tex_page_size_printer = r"""\documentclass[12pt]{article}

\usepackage[
  papersize={8.5in,11in},
  layout=letterpaper,
  right=1in,
  left=1in,
  top=0.75in,
  bottom=0.75in,
  marginparwidth=0.4in,
  marginparsep=0.0in
]{geometry}

\pagenumbering{gobble}
"""
  __tex_page_size_book_a5 = r"""\documentclass[12pt,openany]{book}

\usepackage[
  paperwidth=6.08in,
  paperheight=8.52in,
  right=0.75in,
  left=0.75in,
  top=0.9in,
  bottom=0.5in,
  headsep=0.12in,
]{geometry}

\usepackage{fancyhdr}
\usepackage{extramarks}
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0.0pt}
\renewcommand{\footrulewidth}{0.0pt}
\renewcommand{\sectionmark}[1]{
  \markboth{\addfontfeature{LetterSpace=20.0} #1}
           {\addfontfeature{LetterSpace=20.0} #1}
}
\fancyhead[LO]{\small{\thepage}}
\fancyhead[LE]{\scriptsize{\emph\firstrightmark}}
\fancyhead[RE]{\small{\thepage}}
\fancyhead[RO]{\scriptsize{\emph\firstrightmark}}
"""
  __tex_head_template = r"""$PAGESIZE

\usepackage{fontspec}

\defaultfontfeatures{Ligatures={NoCommon}}

%\setmainfont [
%  Path = $DIRFONTS/charis-sil/,
%  Extension = .ttf,
%  UprightFont = *-Regular,
%  BoldFont = *-Bold,
%  ItalicFont = *-Italic,
%  BoldItalicFont= *-BoldItalic
%]{CharisSIL}

%\setmainfont [
%  Path = $DIRFONTS/eb-garamond/,
%  Extension = .ttf,
%  UprightFont = *-Regular,
%  BoldFont = *-Bold,
%  ItalicFont = *-Italic,
%  BoldItalicFont= *-BoldItalic
%]{EBGaramond}

%\setmainfont [
%  Path = $DIRFONTS/noticia-text/,
%  Extension = .ttf,
%  UprightFont = *-Regular,
%  BoldFont = *-Bold,
%  ItalicFont = *-Italic,
%  BoldItalicFont= *-BoldItalic
%]{NoticiaText}

\setmainfont [
  Path = $DIRFONTS/eczar/,
  Extension = .ttf,
  UprightFont = *-Regular,
  BoldFont = *-Bold,
  ItalicFont = *-Regular,
  BoldItalicFont= *-Bold
]{Eczar}

\usepackage{graphicx}
\graphicspath{{$DIRIMAGES}}

\newenvironment{absolutelynopagebreak}
  {\par\nobreak\vfil\penalty0\vfilneg
   \vtop\bgroup}
  {\par\xdef\tpd{\the\prevdepth}\egroup
   \prevdepth=\tpd}

\hyphenpenalty 10000
\exhyphenpenalty 10000

\usepackage{indentfirst}
\usepackage[skip=10pt plus1pt, indent=0pt]{parskip}

\usepackage[explicit]{titlesec}
\usepackage{needspace}

\titleformat{\section}[block]
  {\addfontfeature{LetterSpace=30.0}\bfseries\filcenter}
  {\thesection}{}{ #1 }[]
\titlespacing{\section}{0ex}{3ex}{0ex}

\setcounter{secnumdepth}{0}
\usepackage{setspace}
\begin{document}
\begin{flushleft}

% Slightly increase space between words
%\fontdimen2\font=20.9pt
\begin{spacing}{0.9}
"""

  __tex_head = ""
  __tex_tail = r"""
\end{spacing}
\end{flushleft}
\end{document}
"""

  __dir_fonts = "./../fonts"
  __dir_images = "./../images"
  __dir_prayers = "./../oratio/"
  __file_tex_out = "out.tex"

  def __init__(self):
    self.__tex_head = self.__tex_head_template.replace( \
      r"$PAGESIZE", \
      self.__tex_page_size_printer)

    self.__tex_head = self.__tex_head.replace("$DIRFONTS", self.__dir_fonts)
    self.__tex_head = self.__tex_head.replace("$DIRIMAGES", self.__dir_images)
    resetFile(self.__file_tex_out)

  def GeneratePDF(self):
    import subprocess
    subprocess.run(["xelatex", "-halt-on-error", self.__file_tex_out])

  def WriteTitle(self, title):
    tex_title = r"""
    \begin{center}
    {\bfseries\addfontfeature{LetterSpace=30.0} $TITLE}
    \vspace{0.12in}
    \end{center}
    """
    self.__f.write(tex_title.replace(r"$TITLE", title))

  def WritePsalm(self, chapter, verse_range=range(0, 1)):
    chapter_str = str(chapter)
    chapter_idx = chapter - 1

    if verse_range.start == 0:
      verses_total = len(self.__psalms_la[chapter_idx])
      verse_range = range(1, verses_total + 1)

    inscription = ""
    if chapter_str in self.__psalm_inscriptions_la:
      inscription = self.__psalm_inscriptions_la[chapter_str]

    self.__WriteTexSection(self.__psalms_la[chapter_idx], \
                           self.__psalms_en[chapter_idx], \
                           "PSALMUS " + chapter_str, \
                           inscription)

  def WritePrayer(self, prayer):
    file_name = ""
    title = ""
    inscription = ""

    if Prayer.PRINCIPIUM == prayer:
      file_name = "principium"
    elif Prayer.REX_CAELESTIS == prayer:
      file_name = "rex-caelestis"
    elif Prayer.OMNISANCTA_TRINITAS == prayer:
      file_name = "omnisancta-trinitas"
    elif Prayer.TRISAGION == prayer:
      file_name = "trisagion"
    elif Prayer.VENITE == prayer:
      file_name = "venite"
    elif Prayer.GLORIA_PATRI == prayer:
      file_name = "gloria-patri"
    elif Prayer.KYRIE_ELEISON_3 == prayer:
      file_name = "kyrie-eleison-3"
    elif Prayer.KYRIE_ELEISON_12 == prayer:
      file_name = "kyrie-eleison-12"
    elif Prayer.PATER_NOSTER == prayer:
      file_name = "pater-noster"
    elif Prayer.AVE_MARIA == prayer:
      file_name = "ave-maria"
    elif Prayer.TE_LUCIS_ANTE_TERMINUM == prayer:
      file_name = "te-lucis-ante-terminum"
      title = "HIMNUS"
    elif Prayer.CONFITEOR == prayer:
      file_name = "confiteor"
      title = "CONFITEOR"
    elif Prayer.CONFITEOR_RESPONSIO == prayer:
      file_name = "confiteor-responsio"
      inscription = "Respónsio:"
    elif Prayer.COMPLETORIUM_LECTIO_BREVIS_1 == prayer:
      file_name = "completorium-lectio-brevis-1"
      title = "LECTIO BREVIS"
      inscription = "1 Petri 5:8-9"
    elif Prayer.COMPLETORIUM_LECTIO_BREVIS_2 == prayer:
      file_name = "completorium-lectio-brevis-2"
      title = "LECTIO BREVIS"
      inscription = "Jeremías 14:9"
    elif Prayer.COMPLETORIUM_ORATIO_1 == prayer:
      file_name = "completorium-oratio-1"
      inscription = "Orátio:"
    elif Prayer.COMPLETORIUM_ANTIFONA_1:
      file_name = "completorium-antifona-1"
      inscription = "Antifona:"

    la = {}
    en = {}
    self.__ReadCSV(self.__dir_prayers + file_name + ".csv", la, en)

    self.__WriteTexSection(la, \
                           en, \
                           title, \
                           inscription=inscription, \
                           is_numbered=False)
