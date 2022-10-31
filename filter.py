class fl:
    def filter_word(word):
        word = word.replace("\n", " \n ")

        word_splited = word.split(" ")
        # counting \n
        count_nl = 0
        for mnn in word_splited:
            if mnn == "\n":
                count_nl = count_nl + 1

        movie_n_name_two = []
        if count_nl > 2:
            count_nl_2 = 0
            con = True
            for mnn in word_splited:
                if mnn == "\n":
                    count_nl_2 = count_nl_2 + 1
                if count_nl_2 == 2 and con == True:
                    mnn = "="
                    con = False
                movie_n_name_two.append(mnn)
        else:
            for mnn in word_splited:
                if mnn == "\n":
                    mnn = "="
                movie_n_name_two.append(mnn)

        word = " ".join(movie_n_name_two)
        symbols = ["/", "@", "#", "-", "_", ":", "\n", ".avi", ".mkv", ".mp4", "-", "–", "🎬", "🎞", "📥", "🌼", "｜",
                   "😭", "/", "@", "💿", "none", "🔊", "━", "   ", "  ", "  ", "   "]
        for s in symbols:
            word = word.replace(s, " ")
            word = word.replace(": ", ":")

        word = word.lower()  # making all english words to lower case

        movie_eng = ["adey", "eregnaye", "besintu", "askuala"]  # list of english and amharic word
        movie_amh = ["አደይ", "እረኛዬ", "በስንቱ", "አስኳላ"]

        movie_n_name = word.split(" ")
        m_n = word

        # algortithm that add english name to amhric name of movie title
        for num in range(0, len(movie_amh)):
            if movie_amh[num] in movie_n_name:
                m_n = movie_eng[num] + " " + m_n

        m_n = m_n.replace("  "," ")
        return m_n
