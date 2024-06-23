#!/usr/bin/env python3
from psalms import Psalms
from prayers import Prayer, Prayers
from texout import TeXPrinterOutput

psalms = Psalms()
prayers = Prayers()
out = TeXPrinterOutput()

out.start()

chapter = 50
la, en = psalms.GetChapter(chapter)
insc, _ = psalms.GetChapterInscription(chapter)

out.write_section2(la, en, "PSALMUS 50", insc)

out.finish()
