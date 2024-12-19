from collections import OrderedDict

def roman_numeral(num):

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
r"""\documentclass[12pt]{book}

\usepackage{marginnote}
\usepackage{microtype}
\usepackage[
  papersize={8.5in,11in},
  layout=letterpaper,
  %right=1in,
  %left=1in,
  inner=1in,
  outer=4.4in,
  top=0.70in,
  bottom=0.70in,
  marginparwidth=3.0in,
  marginparsep=0.4in,
]{geometry}

\pagenumbering{gobble}

\usepackage{fontspec}
%\setmainfont [
%  Path = $DIRFONTS/crimson/OTF/,
%  Extension = .otf,
%  UprightFont = *-Roman,
%  BoldFont = *-Bold,
%  ItalicFont = *-Italic,
%  BoldItalicFont= *-BoldItalic,
%  FontFace={li}{n}{Font=*-Italic},
%  FontFace={li}{it}{Font=*-BoldItalic},
%]{Crimson}

\setmainfont [
  Path = $DIRFONTS/eb-garamond/,
  Extension = .ttf,
  UprightFont = *-Regular,
  BoldFont = *-Bold,
  ItalicFont = *-Italic,
  BoldItalicFont= *-BoldItalic,
  FontFace={c}{n}{Font=*SC08-Regular},
  FontFace={c}{it}{Font=*SC08-Regular},
]{EBGaramond}

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
\titlespacing{\section}{0ex}{8ex}{0ex}

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

\tolerance=1
\emergencystretch=\maxdimen
\hyphenpenalty=10000
\hbadness=10000

\begin{document}
\setstretch{1.1}
"""

  tex_tail = r"""
\end{document}
"""

  def __init__(self):
    super(TeXPrinterOutput, self).__init__()
    self.tex_head = self.tex_head.replace("$DIRFONTS", self.dir_fonts)
    self.tex_head = self.tex_head.replace("$DIRIMAGES", self.dir_images)

  def write_title(self, title):
    tex_title = \
    r"\begin{center} " + \
    r"{\bfseries\addfontfeature{LetterSpace=30.0}\fontdimen2\font=1em " + \
    title.upper() + \
    r"}" + "\n" + r"\vspace{0.08in}" + \
    r"\end{center}"
    self.f.write(tex_title)

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

  def write_section2(self, la, en, title="", inscription="", is_numbered=True, repeated=0):
    la_font = r"\fontseries{c}\selectfont\fontdimen2\font=0.4em "
    en_font = r" \scriptsize "
    insc_font = r" \fontseries{c}\tiny\addfontfeature{LetterSpace=4.0}\fontdimen2\font=1em "
    repeat_font = r" \normalfont\scriptsize\addfontfeature{LetterSpace=12.0} "

    if title:
      tex_section_begin = \
        r"\pagebreak[3]\section{ " + \
        title.upper() + \
        " }" + "\n"
      self.f.write(tex_section_begin)

    if inscription:
      txt = inscription#.upper()
      
      if title:
        self.f.write(r"\vspace{0.05in}" + "\n")
        tex_inscription = \
          r"\begin{center}" + "\n" + \
          r"\parbox[]{2.5in}{ " + \
          r"{" + insc_font + \
          txt + \
          r" }}" + "\n\n" + \
          r"\end{center}"
      else:
        tex_inscription = \
          r"{\tiny\addfontfeature{LetterSpace=4.0}\fontdimen2\font=1em " + \
          txt + \
          r" }" + "\n\n"

      self.f.write(tex_inscription)
      self.f.write(r"\vspace{0.05in}" + "\n")

    elif title:
      self.f.write(r"\vspace{0.1in}")

    else:
      self.f.write(r"\vspace{0.12in}")

    verses = sorted(la, key = int)
    for verse in verses:
      tex_pre = ""
      tex_margin = \
        r" \marginpar{" + \
        r"{\noindent" + en_font + \
        en[verse] + \
        "}} "

      la_lower = la[verse]#.lower()

      if is_numbered:
        tex_pre = \
          r"\hskip0.025in \raisebox{0.75ex}{\footnotesize " + \
          verse + "." + \
          r"} \hskip0.05in "

      elif la_lower.startswith(r"$v"):
        tex_pre = \
          r"\hskip0.05in{\tiny V.}\hskip0.1in "
        la_lower = la_lower.replace("$v", "")

      elif la_lower.startswith(r"$r"): 
        tex_pre = \
          r"\hskip0.05in{\tiny R.}\hskip0.1in "
        la_lower = la_lower.replace("$r", "")

      idx = la_lower.find(" ")
      tex_text = la_lower[:idx] + tex_margin + la_lower[idx+1:]

      if 0 != repeated:
        tex_repeated = \
          r"\newline " + \
          r"\phantom{text} \hfill \phantom{text} \hfill " + \
          r"\phantom{text} \hfill \phantom{text} \hfill " + \
          r"{" + repeat_font + \
          r"- REP. " + str(repeated) + "" + \
          " \hfill \phantom{text}} "
      else:
        tex_repeated = ""

      tex_line = tex_pre + \
        r"{\noindent" + la_font + \
        tex_text + tex_repeated + \
        r" }" + "\n"

      self.f.write(tex_line + r"\Needspace{4\baselineskip}" + "\n\n")

    tex_section_end = r"\Needspace{10\baselineskip}" + "\n"
    self.f.write(tex_section_end)

