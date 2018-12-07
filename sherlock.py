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

def maybe_download(filename, expected_bytes):
  """Download a file if not present, and make sure it's the right size."""
  if not os.path.exists(filename):
    filename, _ = urllib.request.urlretrieve(url + filename, filename)

  statinfo = os.stat(filename)
  if statinfo.st_size == expected_bytes:
    print('Found and verified', filename)
  
  else:
    print(statinfo.st_size)
  
    raise Exception(
        'Failed to verify ' + filename + '. Can you get to it with a browser?')
  
  return filename

filename = maybe_download('cano.txt', 3868223)