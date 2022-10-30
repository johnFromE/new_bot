from pyrogram import Client,filters
from random_movie import choose_movie
from filter import fl

bot = Client("amhric_bot", api_id=20453853, api_hash="fe2593c973640679de717af61e1f805c",bot_token="5737216854:AAEzEb7If0vA_zpLlKxq5vIujMjK6nEfSD0")

@bot.on_message(filters.document)
def upload_doc(bot, m):
    s_movie_name = str(m.document.file_name) +" "+ str(m.caption)
    s_movie_name = fl.filter_word(s_movie_name)

    print(s_movie_name)
    file = open("file.txt", 'a', encoding="utf-8")
    file.write("\n" + str(m.id) + ":" + s_movie_name)
    file.close()

@bot.on_message(filters.video)
def upload_vid(bot,m):
    s_movie_name = str(m.video.file_name) + " " + str(m.caption)
    s_movie_name = fl.filter_word(s_movie_name)

    print(s_movie_name)
    file = open("file.txt", 'a', encoding="utf-8")
    file.write("\n" + str(m.id) + ":" + s_movie_name)
    file.close()

@bot.on_message(filters.command('search'))
def command(bot,message):
    if message.text == "/search":
        bot.send_message(message.chat.id, "በስትክክል አልገባም\nሰርች ለማድረግ /search ያስቀድሙ\nለምሳሌ:- /search የወንዶች ጉዳይ")
    else:
        movie_name = str(message.text).replace("/search", "")
        movie_name = movie_name[1:]

        r_file = open("file.txt", "r", encoding="utf-8")
        word_list = r_file.read().split("\n")
        found = False

        for w in word_list:
            if w != "":
                word_splitd = w.split(":")
                movie_id = word_splitd[0]
                movie_title = word_splitd[1].split(" ")
                bool = []
                for mn in movie_name.split(" "):
                    if mn in movie_title:
                        bool.append("true")
                    else:
                        bool.append("false")
    
                if "false" in bool:
                    found = False
                else:
                    print(bool)
                    found = True
                    # bot.forward_message(chat_id=m.chat.id, from_chat_id=from_id, message_id=int(movie_id))
                    msg = bot.get_messages(-1001890974134, int(movie_id))
                    msg.copy(  # copy() so there's no "forwarded from" header
                        chat_id=message.chat.id,  # the channel you want to post to
                        caption="Amharic Film Bot\n\nhttps://t.me/amharic_film_bot\nhttps://t.me/amharic_film_bot"
                        # mentions the posting user in the new message
                    )
                    break

        if found == False:
            bot.send_message(message.chat.id, movie_name + " ማገኘት አልተቻለም \nወይም ስሙን በስትክክል አስገብተው ደግመው ይሞክር")

@bot.on_message(filters.command('start'))
def start(bot,msg):
    bot.send_message(msg.chat.id,"ሰላም " + msg.chat.first_name + "\nእዚህ ሁሉንም የአማርኛ ፊልሞች ማግኘት ትችላላችሁ\nሰርች ለማድረግ /search ያስቀድሙ\nለምሳሌ:- /search አብሳላት\n\nጥያቄ ካላቹ @edit_jo ")

    #save user info
    read_contacte = open("contacte.txt", "r", encoding="utf-8")
    read = read_contacte.read().split("\n")
    new_user = True
    for rc in read:
        rc_split = rc.split(":")
        user_id = rc_split[1]
        if int(user_id) == msg.chat.id:
            new_user = False
            break
    read_contacte.close()
    if new_user == True:
        open("contacte.txt", "a", encoding="utf-8").write("\n"+str(len(read)+1)+"."+msg.from_user.first_name+":"+str(msg.chat.id))
@bot.on_message(filters.command('random'))
def random(bot,msg):
    movie_id = choose_movie()
    message = bot.get_messages(-1001890974134, int(movie_id))
    message.copy(  # copy() so there's no "forwarded from" header
        chat_id=msg.chat.id,  # the channel you want to post to
        caption="Amharic Film Bot\n\nhttps://t.me/amharic_film_bot\nhttps://t.me/amharic_film_bot"
        # mentions the posting user in the new message
    )

@bot.on_message(filters.command('send_doc'))
def dad(bot,messgae):
    file_dad = open("file.txt", "rb")
    bot.send_document(messgae.chat.id, file_dad)
    file_dad.close()
    file_dad_two = open("contacte.txt", "rb")
    bot.send_document(messgae.chat.id, file_dad_two)
    file_dad_two.close()
@bot.on_message()
def message(bot,msg):
    bot.send_message(msg.chat.id,msg.text+" የማይታወቅ ኮማንድ")

print("bot running...")
bot.run()
