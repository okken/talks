from tempfile import TemporaryDirectory
import some_db


def setup_function(function):
    global _dir, _db
    _dir = TemporaryDirectory()
    _db = some_db.DB(_dir.name, "my_db")


def test_count_empty():
    assert _db.count() == 0


def teardown_function(function):
    _db.close()
    _dir.cleanup()




