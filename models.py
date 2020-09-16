import peewee

# Criamos o banco de dados
db = peewee.SqliteDatabase('movies.db')


'''
class: Base Model
'''
class BaseModel(peewee.Model):

  class Meta:
    # Indica em qual banco de dados a tabela sera criada (obrigatorio). Neste caso, utilizamos o banco 'movies.db'
    database = db


'''
class: Movie Category
'''
class MovieCategory(BaseModel):

  name = peewee.CharField(unique=True)


'''
class: Movie
'''
class Movie(BaseModel):

  name = peewee.CharField()
  category = peewee.ForeignKeyField(MovieCategory, backref='movies')

# simple utility function to create tables
def create_tables():
    with db:
        db.create_tables([MovieCategory, Movie])