import telebot
from telebot import types
import requests
import json
from datetime import datetime


Data_tariff = {
    "1": "1000",
    "2": "1500",
    "3": "2000",
}

Data_bot = {
    "/help": 'Для оплаты напишите "оплата" или /pay',
    "/ping": "работаю йоу",
}


def get_api_domain(host, api_token):
    url = f"{host}/{api_token}"
    try:
        response = requests.get(url)
    except:
        return "err1"
    else:
        return response.text


def post_req(link, domain, money, id, chat_id):
    url = f"https://{domain}/{link}"


    m_id = 160
    m_token = "e727eeefef11b6249b043f9d9de253d7"

    body = {
        "merchant_id": m_id,  # ID Мерчанта
        "merchant_token": m_token,  # Токен мерчанта, можно узнать при редактировании мерчанта.
        "ip": id,  # IP покупателя или какой-то идентификатор
        "amount": money,  # Сумма заказа в формате 1000 или 1000.00
        "merchant_order": id,  # ID заказа в вашей систме (должно быть уникальное ваше значение)
        "callback_url": "https://callback_url/",  # ссылка для callback об успешных платежах
    }

    headers = {"Content-Type": "application/json"}
    bot.send_message(
        chat_id,
        text="Ожидайте получения реквизитов для пополнения",
    )
    try:
        temp = requests.post(url=url, data=json.dumps(body), headers=headers)
    except:
        return "err2"
    else:
        if temp.json()['status'] == "success":
            return temp.json()
        elif temp.json()['card'] == 0:
            return "err5"
        else:
            return "err4"


# {
#     "status": "success",
#     "card": "4584432993791061",
#     "endTimeOfPaymentCheck": 1737299354,
#     "sign": "CRKH2H5d5a161db057a00bf3ec23bc23889e39"
# }


def pay_op(tariff, chat_id):
    a = "https://corkpay.cc/api/getPayApiDomain/"
    b = "81ac4e9cbd3a95eb5253e3fb5d8e1714"
    money = Data_tariff[tariff]
    token = get_api_domain(a, b)
    id = str(round(datetime.now().timestamp()))
    if id in operations:
        bot.send_message(
            chat_id,
            text="Произошла ошибка. Повторите попытку оплаты выбрав тариф ещё раз.",
        )
        return
    operations.append(id)
    pay_data = post_req("h2h/p2p", token, money=money, id=id, chat_id=chat_id)
    if pay_data == "err2":

        bot.send_message(
            chat_id,
            text="Произошла ошибка при попытке получить реквизиты для оплаты. Повторите попытку оплаты выбрав тариф ещё раз.",
        )
        return "err3"
    elif pay_data == "err5":
        bot.send_message(
            chat_id,
            text="Произошла ошибка на стороне сервисва для оплаты. Попробуйте ещё раз",
        )
        return "err3"
    elif pay_data == "err4":
        bot.send_message(
            chat_id,
            text="Произошла ошибка при попытке получить реквизиты для оплаты. Повторите попытку оплаты выбрав тариф ещё раз.",
        )
        return "err3"
    elif pay_data.status_code == 200:
        keyboard3 = types.InlineKeyboardMarkup(row_width=1)
        check_button = types.InlineKeyboardButton("Проверить оплату")
        keyboard3.add(check_button,callback_data=f'4{tariff}{pay_data.json()["sign"]}')
        bot.send_message(
            chat_id,
            text=f'Пополните данные реквизиты на сумму {money}. \n {pay_data['card']}',
            reply_markup = keyboard3
        )
    else:
        bot.send_message(
            chat_id,
            text=f'ОШИБКА',
        )
    # post_req("h2h/p2p",token,money,)


operations = []
bot = telebot.TeleBot("7270152731:AAEC0Let7smDFhQrtHaRqjMd55jGnZB8g4g")

# token = get_api_domain(a, b)
# print(token)
# answer = post_req("/h2h/p2p",token,"10","6534")
# print(answer)

# @bot.callback_query_handler(func=lambda call: True)
# def check(callback):




@bot.callback_query_handler(func=lambda call: True)
def choose_tariff(callback):
    if callback.message:
        if callback.data == "1":
            pay_op("1", callback.message.chat.id)
        elif callback.data == "2":
            pay_op("1", callback.message.chat.id)
        elif callback.data == "3":
            pay_op("3", callback.message.chat.id)
        if callback.message:
            if callback.data[0] == "4":
                body = {
                    "merchant_token" : 160,
                    "sign" : callback.data[2:],  
                }
                try:
                    response = requests.post(url="https://corkpay.cc/api/apiOrderStatus",data=json.dumps(body))
                except:
                    bot.send_message(
                        callback.message.chat.id, f"Ошибка при попытке проверить оплату"
                    )
                else:
                    if response["status"] == "success":
                        if callback[1] in ["1","2"]:
                            bot.send_message(
                                callback.message.chat.id, f"Оплата произведена успешно. https://t.me/+6JTh6u2Hon0zZjQx")
                        else:
                            bot.send_message(
                                callback.message.chat.id, f"Оплата произведена успешно. https://t.me/+dHtV7PjtUB43MWEx")
                    else:
                        bot.send_message(
                            callback.message.chat.id, f"Оплата ожидается"
                        )
        else:
            bot.send_message(
                callback.message.chat.id, f"Ошибка"
            )


@bot.message_handler(content_types=["text"])
def get_text_messages(message):

    if message.text == "/help":
        bot.send_message(
            message.from_user.id,
            Data_bot["/help"],
        )
    elif message.text == "q":
        bot.send_message(
            message.from_user.id,
            text="temp",
        )
    elif message.text in [
        "/тарифы",
        "тарифы",
        "/оплата",
        "оплата",
        "тарифы",
        "/pay",
        "pay",
        "tariff",
        "/tariff",
    ]:
        keyboard2 = types.InlineKeyboardMarkup(row_width=2)
        # наша клавиатураvvvvvvvvvvvvvvvvvvvvvvvvvv
        tariff_1 = types.InlineKeyboardButton("1. 1000₽", callback_data="1")
        tariff_2 = types.InlineKeyboardButton("2. 1500₽", callback_data="2")
        tariff_3 = types.InlineKeyboardButton("3. 2000₽", callback_data="3")
        keyboard2.add(tariff_1, tariff_2, tariff_3)
        bot.send_message(
            message.from_user.id, "Выберите тариф: ", reply_markup=keyboard2
        )

    else:
        bot.send_message(
            message.from_user.id,
            Data_bot["/help"],
        )


bot.polling()  # none_stop=True, interval=5)
