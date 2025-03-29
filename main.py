import telebot
from bot_logic import gen_pass, gen_emodji, flip_coin  # Импортируем функции из bot_logic

# Замени 'TOKEN' на токен твоего бота
bot = telebot.TeleBot("7948714437:AAHPuvo4b6107hQMkSdaJ57qqadnxkrXMow")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я Telegram бот. Напиши команду /Fakts, /Ecoactivists, /Environmentaltrips, /Actionsthatsavetheenvironment ")

@bot.message_handler(commands=['Fakts'])
def send_fakts(message):
    bot.reply_to(message, """Несколько фактов об экологии:

Ежегодно в воды Мирового океана сбрасывается свыше 6 млрд кг отходов, основную часть из которых составляет пластик. 
Примерно каждый 8-й житель Земли не имеет доступа к чистой питьевой воде. 1
Из каждого перевезённого 1 млн тонн нефти 1 тонна попадает в океан. 1
В акватории Тихого океана существует огромный мусорный остров, так называемый «материк» из пластиковых отходов, площадь которого превосходит территорию США. 
За последние полвека количество пресной воды на каждого жителя планеты сократилось примерно на 60%. 
Озеро Карачай (Челябинская обл.) загрязнено так сильно, что 1 час проведённый в его воде может обернуться для человека летальным исходом. 
Ежегодно на Земле высаживается лишь около 10% деревьев от того их числа, которое вырубается за тот же срок. 
Уборка опавшей листвы осенью вредит, а не помогает природе. В ней живут мелкие животные, а плотный слой листьев защищает почву и корни деревьев от переохлаждения. 
Озоновый слой Земли полностью восстановится в течение 50 лет, считают специалисты из ООН.""")

@bot.message_handler(commands=['Ecoactivists'])
def send_ecoact(message):
    bot.reply_to(message, """Самые мощные эко-активисты на земле:

Филлис Омидо , Эмма Уотсон , Леонардо Ди Каприо, Грета Тунберг""")
    
@bot.message_handler(commands=['Environmentaltrips'])
def send_trips(message):
    bot.reply_to(message, """Для того чтобы отправится в нужную вам точку необходим

транспорт (то есть машины и автобусы)  но этот транспорт влияет на глобальное потепление своим углекислым газом подробнее: https://en.wikipedia.org/wiki/Health_and_environmental_effects_of_transport""")

@bot.message_handler(commands=['Actionsthatsavetheenvironment'])
def send_bye(message):
    bot.reply_to(message, """Некоторые действия, которые помогают экологии:

Экономить воду и электроэнергию. Это можно делать за счёт выключения воды и света, установки энергоэффективных приборов, утепления квартир, офисов и производственных помещений. 
Отказаться от пластика. В качестве альтернативы использовать многоразовые сумки, бутылки, стаканы, контейнеры. 
Сортировать мусор. Отходы нужно собирать дома, сортировать их по отдельным категориям и сдавать в пункты приёма. 
Сдавать использованные батарейки в пункты приёма для последующей переработки. Это поможет предотвратить накопление тяжёлых металлов в почве и водоносных слоях.""")
# Запускаем бота
bot.polling()
