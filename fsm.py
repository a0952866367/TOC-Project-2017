from transitions.extensions import GraphMachine
import telegram
API_TOKEN = '395510710:AAHiqg1igsLyQTv4351NBANe0UNM5Bq3zKg'

bot = telegram.Bot(token=API_TOKEN)
rank = 1
atp_rank_table = [
                  ['Andy Murray','England','30','191','84'],
                  ['Novak Djokovic','Serbia','30','188','77'],
                  ['Stan Wawrinka','Switzerland','32','183','81'],
                  ['Rafael Nadal','Spain','30','185','85'],
                  ['Roger Federer','Switzerland','35','185','85'],
                  ['Milos Raonic','Canada','26','196','98'],
                  ['Dominic Thiem','Austria','23','185','82'],
                  ['Marin Cilic','Herzegovina','28','198','89'],
                  ['Kei Nishikori','Japan','27','178','75'],
                  ['Alexander Zverev','Germany','20','198','86']
                ]

wta_rank_table = [
                  ['Angelique Kerber','Germany','29','173'],
                  ['Serena Williams','America','35','175'],
                  ['Karolina Pliskova','Czech','25','186'],
                  ['Simona Halep','Romania','25','168'],
                  ['Garbine Muguruza','Spain','23','182'],
                  ['Elina Svitolina','Ukraine','22','174'],
                  ['Dominika Cibulkova','Slovakia','28','161'],
                  ['Johanna Konta','England','26','180'],
                  ['Svetlana Kuznetsova','Russia','31','174'],
                  ['Agnieszka Radwanska','Polan','28','173']
                ]

tournament = 1
tournament_table = [
                    ['Australian Open','Melbourne , Australia','Last fortnight of January','Hard Court'],
                    ['French Open','Paris , France','late May / early June','Clay Court'],
                    ['Wimbledon','London , England','late June / early July','Grass Court'],
                    ['US Open','New York , America','late August / early September','Hard Court']
                ]

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )
    
    def is_going_to_state0(self, update):
        text = update.message.text
        return text.lower() == '/start'
    
    def is_going_to_state1(self, update):
        text = update.message.text
        if "women" in text.lower():
            return True
        elif "wta" in text.lower():
            return True
        elif "2" in text.lower():
            return True

    def is_going_to_state3(self, update):
        text = update.message.text
        if "tennis" in text.lower():
            return True
        elif "tournament" in text.lower():
            return True
        elif "3" in text.lower():
            return True

    def is_going_to_state1_2(self, update):
        text = update.message.text
        if 1 <= int(text) <= len(wta_rank_table):
            global rank
            rank = int(text)
            return True
    
    def is_going_to_state1_3(self, update):
        text = update.message.text
        if "y" in text.lower():
            return True
    
    def state1_2_back_to_state0(self, update):
        text = update.message.text
        if "n" in text.lower():
            return True

    def state1_3_back_to_state0(self, update):
        text = update.message.text
        if "n" in text.lower():
            return True
    
    def is_going_to_state1_4(self, update):
        text = update.message.text
        if "y" in text.lower():
            return True

    def is_going_to_state2(self, update):
        text = update.message.text
        if "men" in text.lower():
            return True
        elif "atp" in text.lower():
            return True
        elif "1" in text.lower():
            return True

    def is_going_to_state2_2(self, update):
        text = update.message.text
        if 1 <= int(text) <= len(atp_rank_table):
            global rank
            rank = int(text)
            return True
    
    def is_going_to_state2_3(self, update):
        text = update.message.text
        if "y" in text.lower():
            return True

    def state2_2_back_to_state0(self, update):
        text = update.message.text
        if "n" in text.lower():
            return True

    def state2_3_back_to_state0(self, update):
        text = update.message.text
        if "n" in text.lower():
            return True

    def is_going_to_state2_4(self, update):
        text = update.message.text
        if "y" in text.lower():
            return True

    def is_going_to_state3_2(self, update):
        text = update.message.text
        if 1 <= int(text) <= len(tournament_table):
            global tournament
            tournament = int(text)
            return True

    def is_going_to_state3_3(self, update):
        text = update.message.text
        if "y" in text.lower():
            return True

    def state3_2_back_to_state0(self, update):
        text = update.message.text
        if "n" in text.lower():
            return True

    def on_enter_state0(self, update):
        update.message.reply_text("Welcome to Tennis Good Good!")
        update.message.reply_text("You may search:\n1. ATP Rankings (Men)\n2. WTA Rankings (Women)\n3. Tennis Tournaments")
        self.go_back(update)
    def on_exit_state0(self, update):
        print('Leaving state0')


    def on_enter_state1(self, update):
        update.message.reply_text("WTA Rankings\n--------------------\n1. Angelique Kerber\n2. Serena Williams\n3. Karolina Pliskova\n4. Simona Halep\n5. Garbine Muguruza\n6. Elina Svitolina\n7. Dominika Cibulkova\n8. Johanna Konta\n9. Svetlana Kuznetsova\n10. Agnieszka Radwanska")
        update.message.reply_text("Type a ranking number (1~10) \nfor more info")
    def on_exit_state1(self, update):
        print('Leaving state1')

    def on_enter_state1_2(self, update):
        bot.send_message(chat_id=update.message.chat_id,text=wta_rank_table[rank-1][0])
        image_name = wta_rank_table[rank-1][0]
        file_name = "images/"+image_name+".jpg"
        bot.send_photo(chat_id=update.message.chat_id,photo=open(file_name,'rb'))
        update.message.reply_text("More info? Yes / No")
    def on_exit_state1_2(self, update):
        print('Leaving state1_2')
    
    def on_enter_state1_3(self, update):
        bot.send_message(chat_id=update.message.chat_id,text=wta_rank_table[rank-1][0]+"\nRanking : "+str(rank)+"\nCountry : "+wta_rank_table[rank-1][1]+"\nAge : "+wta_rank_table[rank-1][2]+"\nHeight : "+wta_rank_table[rank-1][3]+" cm")
        update.message.reply_text("More WTA players? Yes / No")
    def on_exit_state1_3(self, update):
        print('Leaving state1_3')
    
    def on_enter_state1_4(self, update):
        bot.send_message(chat_id=update.message.chat_id,text='<a href="http://www.wtatennis.com/rankings">More WTA players</a>',parse_mode=telegram.ParseMode.HTML)
        self.go_back(update)
    def on_exit_state1_4(self, update):
        print('Leaving state1_4')

    def on_enter_state2(self, update):
        update.message.reply_text("ATP Rankings\n--------------------\n1. Andy Murray\n2. Novak Djokovic\n3. Stan Wawrinka\n4. Rafael Nadal\n5. Roger Federer\n6. Milos Raonic\n7. Dominic Thiem\n8. Marin Cilic\n9. Kei Nishikori\n10. Alexander Zverev")
        update.message.reply_text("Type a ranking number (1~10) \nfor more info")
    def on_exit_state2(self, update):
        print('Leaving state2')

    def on_enter_state2_2(self, update):
        bot.send_message(chat_id=update.message.chat_id,text=atp_rank_table[rank-1][0])
        image_name = atp_rank_table[rank-1][0]
        file_name = "images/"+image_name+".png"
        bot.send_photo(chat_id=update.message.chat_id,photo=open(file_name,'rb'))
        update.message.reply_text("More info ? Yes / No")
    def on_exit_state2_2(self, update):
        print('Leaving state2_2')
    
    def on_enter_state2_3(self, update):
        bot.send_message(chat_id=update.message.chat_id,text=atp_rank_table[rank-1][0]+"\nRanking : "+str(rank)+"\nCountry : "+atp_rank_table[rank-1][1]+"\nAge : "+atp_rank_table[rank-1][2]+"\nHeight : "+atp_rank_table[rank-1][3]+" cm\nWeight : "+atp_rank_table[rank-1][4]+" kg")
        update.message.reply_text("More ATP players ? Yes / No")
    def on_exit_state2_3(self, update):
        print('Leaving state2_3')

    def on_enter_state2_4(self, update):
        bot.send_message(chat_id=update.message.chat_id,text='<a href="http://www.atpworldtour.com/en/rankings/singles">More ATP players</a>',parse_mode=telegram.ParseMode.HTML)
        self.go_back(update)
    def on_exit_state2_4(self, update):
        print('Leaving state2_4')

    def on_enter_state3(self, update):
        update.message.reply_text("Tennis Grand Slam tournaments\n1. Australian Open\n2. French Open\n3. Wimbledon\n4. US Open")
        update.message.reply_text("Type 1-4 for more info")
    def on_exit_state3(self, update):
        print('Leaving state3')

    def on_enter_state3_2(self, update):
        image_name = tournament_table[tournament-1][0]
        file_name = "images/"+image_name+".png"
        bot.send_photo(chat_id=update.message.chat_id,photo=open(file_name,'rb'))
        bot.send_message(chat_id=update.message.chat_id,text=tournament_table[tournament-1][0]+"\nPlace : "+tournament_table[tournament-1][1]+"\nDates: "+tournament_table[tournament-1][2]+"\nCourts : "+tournament_table[tournament-1][3])
        update.message.reply_text("Learn more ? Yes / No")
    def on_exit_state3_2(self, update):
        print('Leaving state3_2')

    def on_enter_state3_3(self, update):
        bot.send_message(chat_id=update.message.chat_id,text='<a href="https://en.wikipedia.org/wiki/Grand_Slam_(tennis)">More about Grand Slam</a>',parse_mode=telegram.ParseMode.HTML)
        self.go_back(update)
    def on_exit_state3_3(self, update):
        print('Leaving state3_3')
