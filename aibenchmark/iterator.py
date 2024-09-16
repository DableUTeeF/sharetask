import requests
import json


class iterator:
    def __init__(self, iterable, interval=1, total=None):
        self.iterable = iterable
        self.interval = interval
        self.total = total

    def __len__(self):
        return (
            self.total if self.iterable is None
            else self.iterable.shape[0] if hasattr(self.iterable, "shape")
            else len(self.iterable) if hasattr(self.iterable, "__len__")
            else self.iterable.__length_hint__() if hasattr(self.iterable, "__length_hint__")
            else 0
        )

    def send(self, n, finished=False):
        data = {
            'current': n,
        }
        if len(self) is not None:
            data['total'] = len(self)
        if finished:
            data['finished'] = True
        print(data)
        requests.post(
            'http://linebot.dableuteef.com/',
            data=json.dumps(data),
            # headers={'Content-Type': 'application/json; charset=UTF-8', 'Authorization': authorization}
        )

    def __iter__(self):
        iterable = self.iterable
        n = 0
        try:
            for obj in iterable:
                yield obj
                n += 1
                if n % self.interval == 0:
                    self.send(n)
        finally:
            self.send(n, finished=True)
