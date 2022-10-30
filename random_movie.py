import random

def choose_movie():
    r_file = open("file_random.txt","r",encoding="utf-8")
    rand_movie = r_file.read().split("\n")
    random_num = random.randrange(1,92)
    r_movie = rand_movie[random_num]

    movie_splited = r_movie.split(":")
    movie_name = movie_splited[0]

    return movie_splited[0]
