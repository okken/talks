def test_count_empty(db):
    assert db.count() == 0


def test_count_one(db):
    item = {"foo": [1, 2, 3]}
    db.create(item)
    assert db.count() == 1


