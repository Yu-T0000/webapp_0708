from collections.abc import Generator
from pathlib import Path
from contextlib import contextmanager

import dataset
from tinydb import TinyDB

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
        db = dataset.connect(self._dbname)  #SQLiteデータベースに接続して結果をdbに代入
        db.begin()  #データベーストランザクション開始
        try:
            yield db
            db.commit()
        except Exception as e:
            db.rollback()   #様子がおかしかったら変更破棄
            raise e #デバッグ用？

dbpath = Path("sample.db")
mock_db = MockDB(dbpath)    #sample.dbを参照するインスタンス

with mock_db.connect() as db:
    table: dataset.Table = db["samples"]
    print(table.find_one(id= "001"))