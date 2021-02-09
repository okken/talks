from tempfile import TemporaryDirectory
import some_db
import unittest

class TestCount(unittest.TestCase):

    def setUp(self):
        global _dir, _db
        self._dir = TemporaryDirectory()
        self._db = some_db.DB(self._dir.name, "my_db")

    def test_count_empty(self):
        self.assertEqual(self._db.count(), 0)

    def tearDown(self):
        self._db.close()
        self._dir.cleanup()








