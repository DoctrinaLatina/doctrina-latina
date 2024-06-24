from enum import Enum, auto
from fileio import read_csv

class Prayer(Enum):
  PRINCIPIUM = auto()
  REX_CAELESTIS = auto()
  OMNISANCTA_TRINITAS = auto()
  TRISAGION = auto()
  VENITE = auto()
  GLORIA_PATRI = auto()
  KYRIE_ELEISON = auto()
  PATER_NOSTER = auto()
  AVE_MARIA = auto()
  TE_LUCIS_ANTE_TERMINUM = auto()
  CONFITEOR = auto()
  CONFITEOR_RESPONSIO = auto()
  COMPLETORIUM_LECTIO_BREVIS_1 = auto()
  COMPLETORIUM_LECTIO_BREVIS_2 = auto()
  COMPLETORIUM_ORATIO_1 = auto()
  COMPLETORIUM_ANTIFONA_1 = auto()

class Prayers:
  __dir_prayers = "./../oratio/"

  def __GetFileNameTitleInscription(self, prayer):
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
    elif Prayer.KYRIE_ELEISON == prayer:
      file_name = "kyrie-eleison"
    elif Prayer.PATER_NOSTER == prayer:
      file_name = "pater-noster"
    elif Prayer.AVE_MARIA == prayer:
      file_name = "ave-maria"
    elif Prayer.TE_LUCIS_ANTE_TERMINUM == prayer:
      file_name = "te-lucis-ante-terminum"
      title = "Himnus"
    elif Prayer.CONFITEOR == prayer:
      file_name = "confiteor"
      title = "Confiteor"
    elif Prayer.CONFITEOR_RESPONSIO == prayer:
      file_name = "confiteor-responsio"
      inscription = "Respōnsiō:"
    elif Prayer.COMPLETORIUM_LECTIO_BREVIS_1 == prayer:
      file_name = "completorium-lectio-brevis-1"
      title = "Lectiō Brevis"
      inscription = "1 Petrī 5:8-9"
    elif Prayer.COMPLETORIUM_LECTIO_BREVIS_2 == prayer:
      file_name = "completorium-lectio-brevis-2"
      title = "Lectiō Brevis"
      inscription = "Jēremīās 14:9"
    elif Prayer.COMPLETORIUM_ORATIO_1 == prayer:
      file_name = "completorium-oratio-1"
      inscription = "Ōrātiō:"
    elif Prayer.COMPLETORIUM_ANTIFONA_1:
      file_name = "completorium-antifona-1"
      inscription = "Antifōna:"
    
    return file_name, title, inscription

  def GetText(self, prayer):
    file_name, _, _ = self.__GetFileNameTitleInscription(prayer)

    la = {}
    en = {}
    read_csv(self.__dir_prayers + file_name + ".csv", la, en)
    return la, en
  
  def GetTitleInscription(self, prayer):
    _, title, inscription = self.__GetFileNameTitleInscription(prayer)
    return title, inscription
