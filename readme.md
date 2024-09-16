# Untitled
Some reason for its existance.
# Installation
```
pip install git+https://github.com/DableUTeeF/sharetask
```
# Usage
Wrap the primary iterator with `aibenchmark.iterator.iterator` object. Sort of like `enumerate` or `tqdm`.
## Single layer wrap
```
from aibenchmark.iterator import iterator

for file in iterator(os.listdir('.')):
    print(file)

for file in iterator(glob.glob('*')):
    print(file)

for file in iterator(Path('.').rglob('*')):
    print(file)
```
## With `enumerate`
```
from aibenchmark.iterator import iterator

for i, file in iterator(enumerate(glob.glob('*'))):
    print(file)

for i, file in enumerate(iterator(Path('.').rglob('*'))):
    print(file)
```
## With Pytorch's DataLoader
```
from aibenchmark.iterator import iterator

for file in iterator(DataLoader(os.listdir('.'), batch_size=2)):
    print(file)
```