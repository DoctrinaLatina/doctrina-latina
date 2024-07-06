#!/usr/bin/env python3
from psalms import Psalms
from prayers import Prayer, Prayers
from texout import TeXPrinterOutput

def write_psalm(out, psalms, chapter):
  la, en = psalms.GetChapter(chapter)
  insc, _ = psalms.GetChapterInscription(chapter)
  out.write_section2(la, en, "PSALMUS " + str(chapter), insc)

def write_prayer(out, prayers, prayer, repeated=0):
  la, en = prayers.GetText(prayer)
  title, insc = prayers.GetTitleInscription(prayer)
  out.write_section2(la, en, title, insc, is_numbered=False, repeated=repeated)

psalms = Psalms()
prayers = Prayers()
out = TeXPrinterOutput()

out.start()
out.write_title("COMPLĒTŌRIUM")
write_prayer(out, prayers, Prayer.PRINCIPIUM)
write_prayer(out, prayers, Prayer.REX_CAELESTIS)
write_prayer(out, prayers, Prayer.TRISAGION, 3)
write_prayer(out, prayers, Prayer.GLORIA_PATRI)
write_prayer(out, prayers, Prayer.OMNISANCTA_TRINITAS)
write_prayer(out, prayers, Prayer.KYRIE_ELEISON, 3)
write_prayer(out, prayers, Prayer.GLORIA_PATRI)
write_prayer(out, prayers, Prayer.PATER_NOSTER)
write_prayer(out, prayers, Prayer.KYRIE_ELEISON, 12)
write_prayer(out, prayers, Prayer.GLORIA_PATRI)
write_prayer(out, prayers, Prayer.VENITE)
write_psalm(out, psalms, 4)
write_psalm(out, psalms, 90)
write_psalm(out, psalms, 133)
write_psalm(out, psalms, 148)
write_prayer(out, prayers, Prayer.TE_LUCIS_ANTE_TERMINUM)
write_prayer(out, prayers, Prayer.COMPLETORIUM_LECTIO_BREVIS_2)
write_prayer(out, prayers, Prayer.KYRIE_ELEISON, 3)
write_prayer(out, prayers, Prayer.GLORIA_PATRI)
write_prayer(out, prayers, Prayer.PATER_NOSTER)
write_prayer(out, prayers, Prayer.COMPLETORIUM_ORATIO_1)
write_prayer(out, prayers, Prayer.AVE_MARIA)
write_prayer(out, prayers, Prayer.COMPLETORIUM_ANTIFONA_1)
write_prayer(out, prayers, Prayer.COMPLETORIUM_LECTIO_BREVIS_1)
write_prayer(out, prayers, Prayer.CONFITEOR)
write_prayer(out, prayers, Prayer.CONFITEOR_RESPONSIO)
out.finish()
