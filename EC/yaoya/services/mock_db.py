from collections.abc import Generator
from pathlib import Path
import dataset
from contextlib import contextmanager

_ = '''
「MockDB は dataset の Wrapper です。
DB の初期化、DB への接続が主な責務になります。」
'''

class MockDB:
    def __init__(self, dbpath: Path) -> None:
        s_dbpath = str(dbpath)
        self._dbname = f"sqlite:///{s_dbpath}"
        self._init_mock_db()

    @contextmanager
    def connect(self) -> Generator[dataset.Database, None, None]:
        db = dataset.connect(self._dbname)
        db.begin()
        try:
            yield db
            db.commit()
        except Exception as e:
            db.rollback()
            raise e