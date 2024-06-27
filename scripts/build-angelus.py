#!/usr/bin/env python3
from prayers import Prayer, Prayers
from texout import TeXPrinterOutput

def write_prayer(out, prayers, prayer, repeated=0):
  la, en = prayers.GetText(prayer)
  #title, insc = prayers.GetTitleInscription(prayer)
  out.write_section2(la, en, "", "", is_numbered=False, repeated=repeated)

prayers = Prayers()
out = TeXPrinterOutput()

out.start()
out.write_title("Angelus")
write_prayer(out, prayers, Prayer.PRINCIPIUM)
write_prayer(out, prayers, Prayer.ANGELUS)
out.finish()
