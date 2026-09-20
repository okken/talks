import pytest


@pytest.fixture()
def some_dict():
    return {"foo": [1, 2, 3]}


def test_create(db, some_dict):
    id = db.create(some_dict)
    assert db.count() == 1
    assert db.read(id) == some_dict


def test_read(db, some_dict):  # too redundant?
    id = db.create(some_dict)

    assert db.read(id) == some_dict


def test_update(db):
    id = db.create({"foo": [1, 2, 3], "bar": [4, 5, 6]})

    db.update(id, {"bar": "baz"})

    expected = {"foo": [1, 2, 3], "bar": "baz"}
    assert db.read(id) == expected


def test_delete(db, some_dict):
    id = db.create(some_dict)

    db.delete(id)
    assert db.count() == 0


def test_read_exception(db):
    any_number = 100  # as db is empty
    with pytest.raises(KeyError):
        db.read(any_number)


def test_delete_exception(db):
    any_number = 100
    with pytest.raises(KeyError):
        db.delete(any_number)


def test_update_exception(db):
    any_number = 100
    with pytest.raises(KeyError):
        db.update(any_number, {"foo": 1})
