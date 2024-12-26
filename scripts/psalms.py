from fileio import read_csv

class Psalms:
  __dir_psalms = "./../vulgata/01-vetus-testamentum/21-psalmi/"
  __file_antifons = "antifonae.csv"
  __file_inscriptions = "inscriptiones.csv"

  __antifons_la = {}
  __antifons_en = {}
  __inscriptions_la = {}
  __inscriptions_en = {}
  __la = []
  __en = []

  def __init__(self):
    read_csv( \
      self.__dir_psalms  + self.__file_antifons, \
      self.__antifons_la, \
      self.__antifons_en)
    read_csv( \
      self.__dir_psalms  + self.__file_inscriptions, \
      self.__inscriptions_la, \
      self.__inscriptions_en)

    for n in range(1, 151):
      chapter = str(n)
      la = {}
      en = {}
      read_csv(self.__dir_psalms + chapter.zfill(3) + ".csv", la, en)
      self.__la.append(la)
      self.__en.append(en)

  def GetChapter(self, chapter):
    chapter_idx = chapter - 1

    return \
      self.__la[chapter_idx], \
      self.__en[chapter_idx]

  def GetChapterInscription(self, chapter):
    chapter_str = str(chapter)

    if chapter_str not in self.__inscriptions_la:
      return "", ""

    print("HERE")

    return \
      self.__inscriptions_la[chapter_str], \
      self.__inscriptions_en[chapter_str]

  def GetAntifon(self, chapter):
    chapter_str = str(chapter)

    if chapter not in self.__antifons_la:
      return "", ""

    return \
      self.__antifons_la[chapter_str], \
      self.__antifons_en[chapter_str]
