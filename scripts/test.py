#!/usr/bin/env python3
from psalms import Psalms
from texout import TeXPrinterOutput

ps = Psalms()
out = TeXPrinterOutput()

out.start()

chapter = 50
la, en = ps.GetChapter(chapter)
insc, _ = ps.GetChapterInscription(chapter)

out.write_section2(la, en, "PSALMUS L.", insc)

out.finish()
