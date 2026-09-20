import pytest
from tempfile import TemporaryDirectory
import some_db


@pytest.fixture(scope="session")
def db_session():
    with TemporaryDirectory() as db_dir:
        _db = some_db.DB(db_dir, "my_db")
        yield _db
        _db.close()


@pytest.fixture()
def db(db_session):
    db_session.delete_all()
    return db_session


def test_count_empty(db):
    assert db.count() == 0
