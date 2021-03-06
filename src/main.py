import pandas as pd

my_data = pd.read_csv('../movie_metadata.csv', delimiter=",")
uniqueGenres = []
for genre in my_data['genres']:
    set = genre.split('|')
    for item in set:
        if item not in uniqueGenres:
            uniqueGenres.append(item)

for item in uniqueGenres:
    data = []
    for genre in my_data['genres']:
        set = genre.split('|')
        if(item in set):
            data.append(1)
        else:
            data.append(0)
    dat = pd.DataFrame({item: data})
    my_data = my_data.join(dat)

uniqueRatings = ['PG-13', 'PG', 'G', 'R']

for item in uniqueRatings:
    data = []
    for rating in my_data['content_rating']:
        if(rating == item):
            data.append(1)
        else:
            data.append(0)
    dat = pd.DataFrame({item: data})
    my_data = my_data.join(dat)

my_data = my_data.apply(pd.to_numeric, errors='coerce')
my_data = my_data.dropna(axis=1, how='all')
my_data = my_data.dropna(axis=0, how='any')

print(my_data)
