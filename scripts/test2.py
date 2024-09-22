#!/usr/bin/env python3
from psalms import Psalms
from texout import TeXPrinterOutput

ps = Psalms()
out = TeXPrinterOutput()

out.start()

for n in range(1, 151):
  print(n)
  la, en = ps.GetChapter(n)
  insc, _ = ps.GetChapterInscription(n)
  out.write_section2(la, en, "PSALMUS " + str(n), insc)

out.finish()
