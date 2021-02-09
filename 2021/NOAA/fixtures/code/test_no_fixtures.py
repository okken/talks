from tempfile import TemporaryDirectory
import some_db


def test_count_empty():
    with TemporaryDirectory() as db_dir:
        db = some_db.DB(db_dir, "my_db")

        assert db.count() == 0

        db.close()
