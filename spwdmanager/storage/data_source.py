import sqlite3


class DataSource(object):
    def __init__(self, path):
        self._path = path
        self._connection = None

    def __del__(self):
        if self._connection:
            self._connection.close()

    @property
    def connection(self):
        if not self._connection:
            self._connection = sqlite3.connect(self._path)

        return self._connection
