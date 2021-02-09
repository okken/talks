import pytest
from tempfile import TemporaryDirectory
import some_db


@pytest.fixture()
def db():
    with TemporaryDirectory() as db_dir:
        _db = some_db.DB(db_dir, "my_db")
        yield _db  # yield separates setup & teardown
        _db.close()


def test_count_empty(db):
    assert db.count() == 0
