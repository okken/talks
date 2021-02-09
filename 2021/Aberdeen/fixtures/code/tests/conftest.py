import pytest
import some_db


@pytest.fixture(scope="session")
def db_session(tmp_path_factory):
    """Session db connection"""
    path = tmp_path_factory.mktemp("db_dir")
    _db = some_db.DB(path, "my_db")
    yield _db
    _db.close()


@pytest.fixture()
def db(db_session):
    """Clean db per test"""
    db_session.delete_all()
    return db_session

