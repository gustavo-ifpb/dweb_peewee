import models as db

db.create_tables()

'''
Inserindo novos dados
'''
# cat_1 = db.MovieCategory.create(name='Terror')

# cat_2 = db.MovieCategory(name='Ação')
# cat_2.save()

# Bulk insert
# cat_3 = {
#   'name': 'Comédia'
# }

# cat_4 = {
#   'name': 'Ficção'
# }

# categories = [cat_3, cat_4]
# db.MovieCategory.insert_many(categories).execute()

# movie = db.Movie.create(name='Gremlins', category=1)
# movie = db.Movie.create(name='Duro de Matar', category=2)

# category = db.MovieCategory.get()
# movie = db.Movie.create(name='Gremlins 2', category=category)

'''
Consultando os dados
'''
# category = db.MovieCategory.get(db.MovieCategory.name == 'Terror')
# for movie in category.movies:
#   print(movie.name)


# categories = db.MovieCategory.select().order_by(db.MovieCategory.name.desc())
# for category in categories:
#   print(category.name)

# movie = db.Movie.get()
# print(movie.category.name)

# movies = db.Movie.select().join(db.MovieCategory).where(db.MovieCategory.name == 'Ação')
# for movie in movies:
#   print(movie.name)

'''
Atualizando os dados
'''
movie = db.Movie.get(db.Movie.id == 3)
movie.name = 'Duro de Matar'
movie.save()

movies = db.Movie.select().join(db.MovieCategory).where(db.MovieCategory.name == 'Ação')
for movie in movies:
  print(movie.name)

'''
Removendo os dados
'''
# movie = db.Movie.get(db.Movie.id == 3)
# movie.delete_instance()