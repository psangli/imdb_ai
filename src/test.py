import csv
with open('../movie_metadata.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    i = 0
    movies = []
    for row in reader:
        movie = (row['director_name'], row['num_critic_for_reviews'])
        # print(movie)
        movies.append(movie)
    print(movies)
    