from tortoise import Tortoise, fields, models


class User(models.Model):
    id = fields.BigIntField(primary_key=True)
    username = fields.CharField(max_length=256)
    
    class Meta():
        table = 'users'

class Stat(models.Model):
    ident = fields.BigIntField()
    stats = fields.IntField()
    
    class Meta():
        table = 'stats'


async def start_db():
    await Tortoise.init(
        db_url="sqlite://db.sqlite3",
        modules={'models':['app.models']}
    )
    await Tortoise.generate_schemas()