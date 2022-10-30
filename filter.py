class fl:
    def filter_word(word):
        #removing unwanted symbols and spaces form movie title
        symbols = ["/", "@", "#", "-", "_", ":", "\n", ".avi", ".mkv",".mp4","-","–","🎬","🎞","📥","🌼","｜","😭","/","@","💿","none","🔊","━","   ","  ","  ","   "]
        for s in symbols:
            word = word.replace(s," ")
            word = word.replace(": ",":")

        word = word.lower()             #making all english words to lower case

        movie_eng = ["adey","eregnaye","besintu","askuala"]             #list of english and amharic word
        movie_amh = ["አደይ","እረኛዬ","በስንቱ","አስኳላ"]

        movie_n_name = word.split(" ")
        m_n = " ".join(movie_n_name)

        #algortithm that add english name to amhric name of movie title
        for num in range(0, len(movie_amh)):
            if movie_amh[num] in movie_n_name:
                m_n =  movie_eng[num] +" "+ m_n

        return m_n
