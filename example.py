from aibenchmark.iterator import iterator
import os
import glob
from pathlib import Path


for file in iterator(os.listdir('.')):
    print(file)

for file in iterator(glob.glob('*')):
    print(file)

for file in iterator(Path('.').rglob('*'), interval=20):
    print(file)
