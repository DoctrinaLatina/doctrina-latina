from collections import OrderedDict

def write_roman(num):

    roman = OrderedDict()
    roman[1000] = "M"
    roman[900] = "CM"
    roman[500] = "D"
    roman[400] = "CD"
    roman[100] = "C"
    roman[90] = "XC"
    roman[50] = "L"
    roman[40] = "XL"
    roman[10] = "X"
    roman[9] = "IX"
    roman[5] = "V"
    roman[4] = "IV"
    roman[1] = "I"

    def roman_num(num):
        for r in roman.keys():
            x, y = divmod(num, r)
            yield roman[r] * x
            num -= (r * x)
            if num <= 0:
                break

    return "".join([a for a in roman_num(num)])

class TeXOutput:
  def __init__(self):
    self.dir_fonts = "./../fonts"
    self.dir_images = "./../images"
    self.file_path = "out.tex"

  def start(self):
    self.f = open(self.file_path, "w")
    self.f.write(self.tex_head)

  def finish(self):
    self.f.write(self.tex_tail)
    self.f.flush()
    import subprocess
    subprocess.run(["xelatex", "-halt-on-error", self.file_path])


class TeXPrinterOutput(TeXOutput):
  tex_head = \
r"""\documentclass[10pt]{book}

\usepackage{marginnote}
\usepackage[
  papersize={8.5in,11in},
  layout=letterpaper,
  %right=1in,
  %left=1in,
  inner=1in,
  outer=4.4in,
  top=0.70in,
  bottom=0.70in,
  marginparwidth=2.80in,
  marginparsep=0.6in,
]{geometry}

\pagenumbering{gobble}

\setmainfont [
  Path = $DIRFONTS/crimson/OTF/,
  Extension = .otf,
  UprightFont = *-Roman,
  BoldFont = *-Bold,
  ItalicFont = *-Italic,
  BoldItalicFont= *-BoldItalic,
  FontFace={li}{n}{Font=*-Italic},
  FontFace={li}{it}{Font=*-BoldItalic},
]{Crimson}

\usepackage{graphicx}
\graphicspath{{$DIRIMAGES}}

\newenvironment{absolutelynopagebreak}
  {\par\nobreak\vfil\penalty0\vfilneg
   \vtop\bgroup}
  {\par\xdef\tpd{\the\prevdepth}\egroup
   \prevdepth=\tpd}

%\hyphenpenalty 10000
%\exhyphenpenalty 10000

\usepackage{indentfirst}
\usepackage[skip=8pt plus1pt, indent=0pt]{parskip}

\usepackage[explicit]{titlesec}
\usepackage{needspace}

\titleformat{\section}[block]
  {\addfontfeature{LetterSpace=30.0}\bfseries\filcenter\small\fontdimen2\font=1em }
  {\thesection}{}{ #1 }[]
\titlespacing{\section}{0ex}{3ex}{0ex}

\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0.0pt}
\renewcommand{\footrulewidth}{0.0pt}

\setcounter{secnumdepth}{0}
\usepackage{paracol}
\twosided[pc]
\usepackage{ragged2e}
\usepackage{setspace}
\begin{document}
%\begin{flushleft}
\onehalfspacing

\sloppy\hyphenpenalty=10000 \emergencystretch\textwidth
"""

  tex_tail = r"""
%\end{flushleft}
\end{document}
"""

  tex_section_begin = r"""
\pagebreak[3]\section{$TITLE}
"""

  tex_section_end = r"""
\Needspace{8\baselineskip}
"""

  tex_inscription = r"""
\parbox{2.5in}{\sc\scriptsize $INSCRIPTION }
"""

  tex_verse_number = \
r"""\hskip0.025in \raisebox{0.75ex}{\tiny $VERSE.} \hskip0.05in"""

  tex_line_la = r"""
\begin{absolutelynopagebreak} 
$TEX_VERSE { $LA }\newline"""

  tex_line_en = r"""
\noindent\emph{\fontseries{li}\selectfont\scriptsize $EN }
\end{absolutelynopagebreak}\vspace{0.08in}
"""

  def __init__(self):
    super(TeXPrinterOutput, self).__init__()
    self.tex_head = self.tex_head.replace("$DIRFONTS", self.dir_fonts)
    self.tex_head = self.tex_head.replace("$DIRIMAGES", self.dir_images)

  def write_section(self, la, en, title="", inscription="", is_numbered=True):
    if title:
      self.f.write(self.tex_section_begin.replace(r"$TITLE", title))

    if inscription:
      if title: self.f.write(r"\begin{center}")
      self.f.write(self.tex_inscription.replace(r"$INSCRIPTION", inscription))
      if title: self.f.write(r"\end{center}")
      self.f.write(r"\vspace{0.12in}")
    elif title:
      self.f.write(r"\vspace{0.30in}")
    else:
      self.f.write(r"\vspace{0.12in}")

    verses = sorted(la, key = int)
    for verse in verses:
      line = self.tex_line_la.replace("$LA", la[verse]) + \
             self.tex_line_en.replace("$EN", en[verse])

      if is_numbered:
        line_verse = self.tex_verse_number.replace("$VERSE", verse)
        line = line.replace("$TEX_VERSE", line_verse)
      else:
        line = line.replace("$TEX_VERSE", "")

      self.f.write(line)

    self.f.write(self.tex_section_end)

  def write_section1(self, la, en, title="", inscription="", is_numbered=True):
    if title:
      self.f.write(self.tex_section_begin.replace(r"$TITLE", title))

    if inscription:
      if title: self.f.write(r"\begin{center}")
      self.f.write(self.tex_inscription.replace(r"$INSCRIPTION", inscription))
      if title: self.f.write(r"\end{center}")
      self.f.write(r"\vspace{0.12in}")
    elif title:
      self.f.write(r"\vspace{0.30in}")
    else:
      self.f.write(r"\vspace{0.12in}")

    verses = sorted(la, key = int)
    for verse in verses:
      self.f.write("\columnratio{0.58}")
      self.f.write(r"\begin{paracol}{2}")
      self.f.write("\n")
      line = self.tex_verse_number.replace("$VERSE", verse) + la[verse]
      self.f.write(line)
      self.f.write("\n")
      self.f.write(r"\switchcolumn")
      self.f.write("\n")
      self.f.write(r"\emph{\fontseries{li}\selectfont\scriptsize " + en[verse] + "}")
      self.f.write("\n")
      self.f.write(r"\end{paracol}")
      self.f.write("\n" + r"\end{absolutelynopagebreak}" + "\n")

  def write_section2(self, la, en, title="", inscription="", is_numbered=True):
    if title:
      self.f.write(self.tex_section_begin.replace(r"$TITLE", title))
      self.f.write(r"\vspace{0.05in}")
    if inscription:
      if title: self.f.write(r"\begin{center}")
      self.f.write(self.tex_inscription.replace(r"$INSCRIPTION", inscription.lower()))
      if title: self.f.write(r"\end{center}")
      self.f.write(r"\vspace{0.001in}")
    elif title:
      self.f.write(r"\vspace{0.1in}")
    else:
      self.f.write(r"\vspace{0.12in}")

    verses = sorted(la, key = int)
    for verse in verses:
      margin = r" \marginpar{\addfontfeature{LetterSpace=2.0}\fontseries{li}\selectfont\scriptsize\raggedright " + en[verse] + "} "
      line = self.tex_verse_number.replace("$VERSE", write_roman(int(verse))) + \
        margin + \
        r"{\sc " + la[verse].lower() + " }"

      self.f.write(line + r"\Needspace{3\baselineskip}" + "\n\n")
      #self.f.write("\n\n")

