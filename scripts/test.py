#!/usr/bin/env python

from psalms import Psalms
from texout import TeXPrinterOutput

p = Psalms()
chapter = 50
la, en = p.GetChapter(chapter)
insc, _ = p.GetChapterInscription(chapter)

out = TeXPrinterOutput()
out.write_section(la, en, "PSALMUS " + str(chapter), insc)
out.finish()
