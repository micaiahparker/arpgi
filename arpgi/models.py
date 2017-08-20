from uuid import UUID, uuid4
from datetime import datetime
from pony.orm import Database, PrimaryKey, Optional, Required, Json, db_session


db = Database('sqlite', ':memory:')

class Game(db.Entity):
    id = PrimaryKey(UUID, default=uuid4)
    created_date = Required(datetime, default=datetime.now)
    last_modified = Required(datetime, default=datetime.now)
    schema = Required(Json)
    title = Required(str)

    def __set__(self, *args, **kwargs):
        with db_session:
            super().__init__(*args, **kwargs)
            self.last_modified = datetime.now()

db.bind()
db.generate_mapping(create_tables=True)