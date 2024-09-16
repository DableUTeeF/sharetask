from aibenchmark.iterator import iterator
import os
import glob
from pathlib import Path
from torch.utils.data import DataLoader

for file in iterator(os.listdir('.')):
    print(file)

for i, file in iterator(enumerate(glob.glob('*'))):
    print(file)

for i, file in enumerate(iterator(Path('.').rglob('*'))):
    print(file)

for file in iterator(DataLoader(os.listdir('.'), batch_size=2)):
    print(file)
