import telebot
import sys

from_id = "-1001890974134"
my_id = "432175862"

Token = '5737216854:AAEzEb7If0vA_zpLlKxq5vIujMjK6nEfSD0'
bot = telebot.TeleBot(Token)

try:

	@bot.message_handler(commands=["start"])
	def start(msg):
		bot.send_message(msg.chat.id,"ሰላም "+msg.chat.first_name+"\nእዚህ ሁሉንም የአማርኛ ፊልሞች ማግኘት ትችላላችሁ\nሰርች ለማድረግ /search ያስቀድሙ\nለምሳሌ:- /search አብሳላት\n\nጥያቄ ካላቹ @edit_jo ")
		contct_file = open("contacte.txt","a",encoding="utf-8")
		contct_file.write("\n"+str(msg.chat.id))
		contct_file.close()

	@bot.message_handler(commands=["its_jo_send_doc"])
	def dad(messgae):
		file_dad = open("file.txt","rb")
		bot.send_document(messgae.chat.id,file_dad)
		file_dad.close()
		file_dad_two = open("contacte.txt", "rb")
		bot.send_document(messgae.chat.id, file_dad_two)
		file_dad_two.close()
		print("file sent to dad!")

	@bot.channel_post_handler(content_types=['document'])
	def upload(m):
		s_movie_name = str(m.document.file_name) +" "+ str(m.caption)
		s_movie_name = s_movie_name.replace(".mp4","")
		s_movie_name = s_movie_name.replace(".mkv","")
		s_movie_name = s_movie_name.replace(".avi","")
		s_movie_name = s_movie_name.replace("\n", " ")
		s_movie_name = s_movie_name.replace(":", " ")
		s_movie_name = s_movie_name.replace("_", " ")
		s_movie_name = s_movie_name.replace("-", " ")
		s_movie_name = s_movie_name.replace("#", " ")
		s_movie_name = s_movie_name.replace("@", " ")
		s_movie_name = s_movie_name.replace("/", " ")
		s_movie_name = s_movie_name.replace("  ", " ")

		file = open("file.txt", 'a', encoding="utf-8")
		file.write("\n" + str(m.message_id) + ":" + s_movie_name)
		file.close()

	@bot.channel_post_handler(content_types=['video'])
	def upload(m):
		s_movie_name = str(m.video.file_name) +" "+ str(m.caption)
		s_movie_name = s_movie_name.replace(".mp4", "")
		s_movie_name = s_movie_name.replace(".mkv", "")
		s_movie_name = s_movie_name.replace(".avi", "")
		s_movie_name = s_movie_name.replace("\n"," ")
		s_movie_name = s_movie_name.replace(":", " ")
		s_movie_name = s_movie_name.replace("_", " ")
		s_movie_name = s_movie_name.replace("-", " ")
		s_movie_name = s_movie_name.replace("#", " ")
		s_movie_name = s_movie_name.replace("@", " ")
		s_movie_name = s_movie_name.replace("/", " ")
		s_movie_name = s_movie_name.replace("  ", " ")

		file = open("file.txt", 'a', encoding="utf-8")
		file.write("\n"+str(m.message_id)+":"+s_movie_name)
		file.close()

	@bot.message_handler(commands=['search'])
	def search(m):
		if m.text == "/search":
			bot.send_message(m.chat.id,"በስትክክል አልገባም\nሰርች ለማድረግ /search ያስቀድሙ\nለምሳሌ:- /search የወንዶች ጉዳይ")
		else:
			movie_name = str(m.text).replace("/search","")
			movie_name = movie_name[1:]

			r_file = open("file.txt","r",encoding="utf-8")
			word_list = r_file.read().split("\n")
			found = False

			for w in word_list:
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
					found=False
				else:
					found=True
					bot.forward_message(chat_id=m.chat.id, from_chat_id=from_id, message_id=int(movie_id))
					break


			if found==False:
				bot.send_message(m.chat.id,movie_name+" ማገኘት አልተቻለም \nወይም ስሙን በስትክክል አስገብተው ደግመው ይሞክር")


except:
	bot.send_message(my_id, "Oops! "+sys.exc_info()[0])
print("bot running...")
bot.polling()
bot.send_message(my_id,"hy jo the bot stoped running!")
