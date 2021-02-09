
def test_update(db):
    id = db.create({"foo": [1, 2, 3], "bar": [4, 5, 6]})

    db.update(id, {"bar": "baz"})

    expected = {"foo": [1, 2, 3], "bar": "baz"}
    assert db.read(id) == expected
