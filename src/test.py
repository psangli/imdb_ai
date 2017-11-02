import csv
import re
import random

with open('../movie_metadata.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    i = 0
    movies = []
    for row in reader:

        #initializing variables

        duration = row['duration']
        director_facebook_likes = row['director_facebook_likes']
        actor_3_facebook_likes = row['actor_3_facebook_likes']
        actor_1_facebook_likes = row['actor_1_facebook_likes']
        genres = row['genres']
        cast_total_facebook_likes = row['cast_total_facebook_likes']
        facenumber_in_poster = row['facenumber_in_poster']
        content_rating = row['content_rating']
        budget = row['budget']
        title_year = row['title_year']
        actor_2_facebook_likes = row['actor_2_facebook_likes']
        imdb_score = row['imdb_score']
        aspect_ratio = row['aspect_ratio']

        #omitting rows with no data
        if(duration == ''
           or director_facebook_likes == ''
           or actor_3_facebook_likes == ''
           or actor_1_facebook_likes == ''
           or genres == ''
           or cast_total_facebook_likes == ''
           or facenumber_in_poster == ''
           or content_rating == ''
           or budget == ''
           or title_year == ''
           or actor_2_facebook_likes == ''
           or imdb_score == ''
           or aspect_ratio == ''):
            continue
        gen = re.split('\|', genres)

        #Initialize the genres
        Action = 0
        Adventure = 0
        Animation = 0
        Biography = 0
        Comedy = 0
        Crime = 0
        Documentary = 0
        Drama = 0
        Family = 0
        Fantasy = 0
        History = 0
        Horror = 0
        Musical = 0
        Mystery = 0
        Romance = 0
        SciFi = 0
        Sport = 0
        Thriller = 0
        War = 0
        Western = 0

        if('Action' in gen):
            Action = 1

        if ('Adventure' in gen):
            Adventure = 1

        if ('Animation' in gen):
            Animation = 1

        if ('Biography' in gen):
            Biography = 1

        if ('Comedy' in gen):
            Comedy = 1

        if ('Crime' in gen):
            Crime = 1

        if ('Documentary' in gen):
            Documentary = 1

        if ('Drama' in gen):
            Drama = 1

        if ('Family' in gen):
            Family = 1

        if ('Fantasy' in gen):
            Fantasy = 1

        if ('History' in gen):
            History = 1

        if ('Horror' in gen):
            Horror = 1

        if ('Musical' in gen):
            Musical = 1

        if ('Mystery' in gen):
            Mystery = 1

        if ('Romance' in gen):
            Romance = 1

        if ('Sci-Fi' in gen):
            SciFi = 1

        if ('Sport' in gen):
            Sport = 1

        if ('Thriller' in gen):
            Thriller = 1

        if ('War' in gen):
            War = 1

        if ('Western' in gen):
            Western = 1

        #Initialize Ratings
        PG13 = 0
        PG = 0
        G = 0
        R = 0

        if (content_rating == 'PG-13'):
            PG13 = 1
        elif (content_rating == 'PG'):
            PG = 1
        elif (content_rating == 'R'):
            R = 1
        elif (content_rating == 'G'):
            G = 1


        movie = (duration, director_facebook_likes,
                 actor_3_facebook_likes,
                 actor_1_facebook_likes,
                 cast_total_facebook_likes,
                 facenumber_in_poster,
                 budget,
                 title_year,
                 actor_2_facebook_likes,
                 imdb_score,
                 aspect_ratio,
                 Action,
                 Adventure,
                 Animation,
                 Biography,
                 Comedy,
                 Crime,
                 Documentary,
                 Drama,
                 Family,
                 Fantasy,
                 History,
                 Horror,
                 Musical,
                 Mystery,
                 Romance,
                 SciFi,
                 Sport,
                 Thriller,
                 War,
                 Western,
                 PG13,
                 PG,
                 G,
                 R)

        movies.append(movie)

    testing = []
    training = []
    i = 0

    #spliting into training and testing set
    print len(movies)
    for i in range(len(movies)):
        movie = random.choice(movies)
        movies.remove(movie)
        if(i % 10 == 0):
            testing.append(movie)
        else:
            training.append(movie)

    print(len(testing))
    print(len(training))