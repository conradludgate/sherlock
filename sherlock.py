import collections
import math
import os
import random
import zipfile
import string

import numpy as np
from six.moves import urllib
from six.moves import xrange  # pylint: disable=redefined-builtin
import tensorflow as tf

# Step 1: Download the data.
url = 'https://sherlock-holm.es/stories/plain-text/'
filedir = 'files/'

def maybe_download(filename, expected_bytes):
  """Download a file if not present, and make sure it's the right size."""
  if not os.path.exists(filename):
    filename, _ = urllib.request.urlretrieve(url + filename, filedir + filename)
  else:
    filename = filedir + filename

  statinfo = os.stat(filename)
  if statinfo.st_size == expected_bytes:
    print('Found and verified', filename)
  
  else:
    print(statinfo.st_size)
  
    raise Exception(
        'Failed to verify ' + filename + '. Can you get to it with a browser?')
  
  return filename

story_files = [
  maybe_download('scan.txt', 51437),
  maybe_download('redh.txt', 54183),
  maybe_download('iden.txt', 41693),
  maybe_download('bosc.txt', 56261),
  maybe_download('five.txt', 43432),
  maybe_download('twis.txt', 53975),
  maybe_download('blue.txt', 46351),
  maybe_download('spec.txt', 58073),
  maybe_download('engr.txt', 48964),
  maybe_download('nobl.txt', 48555),
  maybe_download('bery.txt', 55920),
  maybe_download('copp.txt', 58076),
  maybe_download('silv.txt', 57581),
  maybe_download('yell.txt', 42980),
  maybe_download('stoc.txt', 40344),
  maybe_download('glor.txt', 45503),
  maybe_download('musg.txt', 44740),
  maybe_download('reig.txt', 43730),
  maybe_download('croo.txt', 42228),
  maybe_download('resi.txt', 40253),
  maybe_download('gree.txt', 42498),
  maybe_download('nava.txt', 74802),
  maybe_download('fina.txt', 42667),
  maybe_download('empt.txt', 51780),
  maybe_download('norw.txt', 55262),
  maybe_download('danc.txt', 57315),
  maybe_download('soli.txt', 46474),
  maybe_download('prio.txt', 68510),
  maybe_download('blac.txt', 48081),
  maybe_download('chas.txt', 40475),
  maybe_download('sixn.txt', 49288),
  maybe_download('3stu.txt', 38813),
  maybe_download('gold.txt', 53063),
  maybe_download('miss.txt', 48518),
  maybe_download('abbe.txt', 53377),
  maybe_download('seco.txt', 58393),
  maybe_download('wist.txt', 68296),
  maybe_download('card.txt', 50228),
  maybe_download('redc.txt', 43857),
  maybe_download('bruc.txt', 64986),
  maybe_download('dyin.txt', 34742),
  maybe_download('lady.txt', 46272),
  maybe_download('devi.txt', 60324),
  maybe_download('last.txt', 36480),
  maybe_download('illu.txt', 57510),
  maybe_download('blan.txt', 45383),
  maybe_download('maza.txt', 34547),
  maybe_download('3gab.txt', 36008),
  maybe_download('suss.txt', 35941),
  maybe_download('3gar.txt', 36831),
  maybe_download('thor.txt', 56728),
  maybe_download('cree.txt', 46444),
  maybe_download('lion.txt', 42982),
  maybe_download('veil.txt', 26268),
  maybe_download('shos.txt', 36863),
  maybe_download('reti.txt', 33432)
]
