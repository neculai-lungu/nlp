import spacy

nlp = spacy.load("en_core_web_md")

#Text file is opened and stored in to a list
f = open("movies.txt", "r")
movies = []
for line in f:
    movies.append(line)
f.close()

hulk_movie = nlp("Planet Hulk :Will he save their world or destroy it? When the Hulk " \
             "becomes too dangerous for the Earth, the illuminati trick Hulk into a " \
             "shuttle and launch him into space to a planet where the Hulk can live " \
             "in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold " \
             "into slavery and trained as a galdiator.")

#Funtion created to print the most similar movie to hulk_movie
def watch_next():
    #Index and similarity value are stored in a dictionary
    movie_index = {}
    for index, movie in enumerate(movies):
        similarity = nlp(movie).similarity(hulk_movie)
        movie_index[index] = similarity
        print(index,"|", movie[:7], ":", similarity)
    #Highest value is stored in a variable and printed
    max_similarity = max(movie_index, key=movie_index.get)
    print(f"The movie most similar to {hulk_movie[:2]} is {movies[max_similarity][:7]}")

watch_next()

