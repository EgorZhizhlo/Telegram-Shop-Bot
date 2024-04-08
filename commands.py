from aiogram import types
from aiogram.types import InputFile, InlineKeyboardButton, InlineKeyboardMarkup, InputMedia
from aiogram.utils.callback_data import CallbackData

import sqlite3 as sql

from create_bots import market_bot, market_dp, lava
import markups as m

connect = sql.connect('order.db')
cursor = connect.cursor()


# MENU

@market_dp.message_handler(text=['/start', '/menu'])
async def start(message: types.Message):
    shop_b = InlineKeyboardButton('Магазин🛒', callback_data='shop')
    freq_quest_b = InlineKeyboardButton('Частые вопросы❓', callback_data='freq_quest')
    guar_b = InlineKeyboardButton('Гарантии✅', callback_data='guardian')
    rev_b = InlineKeyboardButton('Отзывы🌟', callback_data='rev')
    help_b = InlineKeyboardButton('Поддержка🤝', callback_data='help')
    rules_b = InlineKeyboardButton('Правила📕', callback_data='rules')
    admin_b = InlineKeyboardButton('Тикеты', callback_data='admin')

    query = "SELECT id FROM admins;"
    admins = cursor.execute(query).fetchall()

    if (str(message.chat.id),) in admins:
        await market_bot.send_photo(
            message.chat.id,
            photo=InputFile('files/main_logo.png'),
            reply_markup=InlineKeyboardMarkup(row_width=2).add(
                *[shop_b, freq_quest_b, guar_b, rev_b, help_b, rules_b, admin_b]),
            caption=f"""🖐Привет, <b>{message.chat.first_name}</b>!\nГлавное меню бота <b>Hayan Shop</b>"""
        )
    else:
        await market_bot.send_photo(
            message.chat.id,
            photo=InputFile('files/main_logo.png'),
            reply_markup=InlineKeyboardMarkup(row_width=2).add(
                *[shop_b, freq_quest_b, guar_b, rev_b, help_b, rules_b]),
            caption=f"""🖐Привет, <b>{message.chat.first_name}</b>!\nГлавное меню бота <b>Hayan Shop</b>"""
        )


@market_dp.callback_query_handler(text="start")
async def start_c(callback_query: types.CallbackQuery):
    shop_b = InlineKeyboardButton('Магазин🛒', callback_data='shop')
    freq_quest_b = InlineKeyboardButton('Частые вопросы❓', callback_data='freq_quest')
    guar_b = InlineKeyboardButton('Гарантии✅', callback_data='guardian')
    rev_b = InlineKeyboardButton('Отзывы🌟', callback_data='rev')
    help_b = InlineKeyboardButton('Поддержка🤝', callback_data='help')
    rules_b = InlineKeyboardButton('Правила📕', callback_data='rules')
    admin_b = InlineKeyboardButton('Тикеты', callback_data='admin')

    query = "SELECT id FROM admins;"
    admins = cursor.execute(query).fetchall()

    if (str(callback_query.message.chat.id),) in admins:
        await market_bot.answer_callback_query(callback_query.id)
        await callback_query.message.edit_media(
            InputMedia(media=InputFile('files/main_logo.png'),
                       caption=f'🖐Привет, <b>{callback_query.message.chat.first_name}</b>!\n'
                               f'Главное меню бота <b>Hayan Shop</b>\n'),
            reply_markup=InlineKeyboardMarkup(row_width=2).add(
                *[shop_b, freq_quest_b, guar_b, rev_b, help_b, rules_b, admin_b])
        )
    else:
        await market_bot.answer_callback_query(callback_query.id)
        await callback_query.message.edit_media(
            InputMedia(media=InputFile('files/main_logo.png'),
                       caption=f'🖐Привет, <b>{callback_query.message.chat.first_name}</b>!\n'
                               f'Главное меню бота <b>Hayan Shop</b>\n'),
            reply_markup=InlineKeyboardMarkup(row_width=2).add(
                *[shop_b, freq_quest_b, guar_b, rev_b, help_b, rules_b])
        )


@market_dp.callback_query_handler(text="admin")
async def shop(callback_query: types.CallbackQuery):
    new_ticket_b = InlineKeyboardButton('Новый тикет', callback_data='new_ticket')
    back_b = InlineKeyboardButton('Назад🔙', callback_data='start')

    await market_bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_media(
        InputMedia(media=InputFile('files/main_logo.png'),
                   caption='Добро пожаловать в админ панель <b>HayanShop</b>\n'),
        reply_markup=InlineKeyboardMarkup(row_width=2).add(*[new_ticket_b, back_b])
    )


call = CallbackData("close_ticket", "id")


@market_dp.callback_query_handler(text="new_ticket")
async def new_ticket(callback_query: types.CallbackQuery):
    ticket = cursor.execute("SELECT * FROM tickets WHERE status = 0 LIMIT 1;").fetchall()
    if len(ticket) != 0:
        close_ticket_b = InlineKeyboardButton(text='Закрыть тикет', callback_data=call.new(id=ticket[0][0]))
        new_ticket_b = InlineKeyboardButton('Новый тикет', callback_data='new_t')
        close_ticket_markup = InlineKeyboardMarkup(row_width=2).add(*[close_ticket_b, new_ticket_b])

        await market_bot.answer_callback_query(callback_query.id)
        await callback_query.message.edit_media(
            InputMedia(media=InputFile('files/main_logo.png'),
                       caption=f"Ticket id: <b>{ticket[0][0]}</b>\n"
                               f"Username: <b>@{ticket[0][1]}</b>\n"
                               f"Product: <b>{ticket[0][2]}</b>"),
            reply_markup=close_ticket_markup
        )
        cursor.execute("UPDATE tickets SET status = 1 WHERE id = ?", (ticket[0][0],))
        connect.commit()
    else:
        new_ticket_b = InlineKeyboardButton('Новый тикет', callback_data='new_ticket')
        back_b = InlineKeyboardButton('Назад🔙', callback_data='start')
        new_ticket_markup = InlineKeyboardMarkup(row_width=2).add(*[new_ticket_b, back_b])

        await market_bot.answer_callback_query(callback_query.id)
        await callback_query.message.edit_media(
            InputMedia(media=InputFile('files/main_logo.png'),
                       caption="<b>ТИКЕТОВ НЕТ</b>\n"),
            reply_markup=new_ticket_markup
        )


@market_dp.callback_query_handler(text="new_t")
async def new_ticket(callback_query: types.CallbackQuery):
    ticket = cursor.execute("SELECT * FROM tickets WHERE status = 0 LIMIT 1;").fetchall()
    if len(ticket) != 0:
        close_ticket_b = InlineKeyboardButton(text='Закрыть тикет', callback_data=call.new(id=ticket[0][0]))
        new_ticket_b = InlineKeyboardButton('Новый тикет', callback_data='new_t')
        close_ticket_markup = InlineKeyboardMarkup(row_width=2).add(*[close_ticket_b, new_ticket_b])

        await market_bot.send_photo(
            callback_query.message.chat.id,
            photo=InputFile('files/main_logo.png'),
            reply_markup=close_ticket_markup,
            caption=f"Ticket id: <b>{ticket[0][0]}</b>\n"
                    f"Username: <b>@{ticket[0][1]}</b>\n"
                    f"Product: <b>{ticket[0][2]}</b>"
        )
        cursor.execute("UPDATE tickets SET status = 1 WHERE id = ?", (ticket[0][0],))
        connect.commit()
    else:
        new_ticket_b = InlineKeyboardButton('Новый тикет', callback_data='new_ticket')
        back_b = InlineKeyboardButton('Назад🔙', callback_data='start')
        new_ticket_markup = InlineKeyboardMarkup(row_width=2).add(*[new_ticket_b, back_b])

        await market_bot.send_photo(
            callback_query.message.chat.id,
            photo=InputFile('files/main_logo.png'),
            reply_markup=new_ticket_markup,
            caption="<b>ТИКЕТОВ НЕТ</b>\n"
        )


@market_dp.callback_query_handler(call.filter())
async def new_ticket(callback_query: types.CallbackQuery, callback_data: call):
    new_ticket_b = InlineKeyboardButton('Новый тикет', callback_data='new_ticket')
    back_b = InlineKeyboardButton('Назад🔙', callback_data='start')
    new_ticket_markup = InlineKeyboardMarkup(row_width=2).add(*[new_ticket_b, back_b])

    await market_bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_media(
        InputMedia(media=InputFile('files/main_logo.png'),
                   caption="<b>ТИКЕТ ЗАКРЫТ</b>\n"
                           "Откройте <b>новый тикет</b>"),
        reply_markup=new_ticket_markup
    )
    cursor.execute("DELETE FROM tickets WHERE id = ? and status = 1;", (callback_data.get("id"),))
    connect.commit()


@market_dp.callback_query_handler(text="shop")
async def shop(callback_query: types.CallbackQuery):
    await market_bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_media(
        InputMedia(media=InputFile('files/shop_logo.png'),
                   caption='💡Выберите интересующий товар '),
        reply_markup=m.shop_markup
    )


@market_dp.callback_query_handler(text="help")
async def help(callback_query: types.CallbackQuery):
    await market_bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_media(
        InputMedia(media=InputFile('files/h_logo.png'),
                   caption=f"🌟Дорогой <b>{callback_query.message.chat.first_name}</b>!"
                           "\nКонтакт поддержки: <b>@ova46</b>\n"
                           "Разработчик магазина Hayan Shop: <b>zhizhloegor_r@mail.ru</b>"),
        reply_markup=m.back_to_start_menu_markup
    )


@market_dp.callback_query_handler(text="freq_quest")
async def freq_quest(callback_query: types.CallbackQuery):
    await market_bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_media(
        InputMedia(media=InputFile('files/fq_logo.png'),
                   caption=f'Ответы на частые вопросы - '
                           f'<a href="https://telegra.ph/Otvety-na-chastye-voprosy-01-06-2"><b>тут</b></a>'),
        reply_markup=m.back_to_start_menu_markup
    )


@market_dp.callback_query_handler(text="guardian")
async def guardian(callback_query: types.CallbackQuery):
    await market_bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_media(
        InputMedia(media=InputFile('files/guar_logo.png'),
                   caption=f"Гарантии честности и надежности - "
                           f'<a href="https://telegra.ph/Garantii-Hayan-Shop-01-13"><b>тут</b></a>'),
        reply_markup=m.back_to_start_menu_markup
    )


@market_dp.callback_query_handler(text="rev")
async def rev(callback_query: types.CallbackQuery):
    await market_bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_media(
        InputMedia(media=InputFile('files/rev_logo.png'),
                   caption=f'Прочитать или оставить отзыв можно - '
                           f'<a href="https://t.me/oztiv_hayan"><b>тут</b></a>'),
        reply_markup=m.back_to_start_menu_markup
    )


@market_dp.callback_query_handler(text="rules")
async def shop(callback_query: types.CallbackQuery):
    await market_bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_media(
        InputMedia(media=InputFile('files/rules_logo.png'),
                   caption='Правила можно прочитать - <a href="https://telegra.ph/Pravila-02-04-56"><b>тут</b></a>'),
        reply_markup=m.back_to_start_menu_markup
    )


# ********

# SHOP MENU

@market_dp.callback_query_handler(text="fortnite")
async def fortnite(callback_query: types.CallbackQuery):
    await market_bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_media(
        InputMedia(media=InputFile('files/main_logo.png'),
                   caption='Выберите категорию товара '),
        reply_markup=m.service_fort_markup
    )


@market_dp.callback_query_handler(text="discordN")
async def discordN(callback_query: types.CallbackQuery):
    basic_b = InlineKeyboardButton('BASIC', callback_data='basic')
    full_b = InlineKeyboardButton('🔥FULL🔥', callback_data='full')
    back_b = InlineKeyboardButton('Назад🔙', callback_data='shop')

    await market_bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_media(
        InputMedia(media=InputFile('files/all_d.png'),
                   caption='Выберите категорию'),
        reply_markup=InlineKeyboardMarkup(row_width=2).add(*[basic_b, full_b, back_b])
    )


@market_dp.callback_query_handler(text="xbox")
async def xbox(callback_query: types.CallbackQuery):
    await market_bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_media(
        InputMedia(media=InputFile('files/main_logo.png'),
                   caption='Услуга находится в разработке'),
        reply_markup=m.back_to_shop_menu_markup
    )


@market_dp.callback_query_handler(text="faceit")
async def faceit(callback_query: types.CallbackQuery):
    await market_bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_media(
        InputMedia(media=InputFile('files/main_logo.png'),
                   caption='Услуга находится в разработке'),
        reply_markup=m.back_to_shop_menu_markup
    )


@market_dp.callback_query_handler(text="twitch")
async def twitch(callback_query: types.CallbackQuery):
    await market_bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_media(
        InputMedia(media=InputFile('files/main_logo.png'),
                   caption='Услуга находится в разработке'),
        reply_markup=m.back_to_shop_menu_markup
    )


@market_dp.callback_query_handler(text="spotify")
async def playstation(callback_query: types.CallbackQuery):
    await market_bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_media(
        InputMedia(media=InputFile('files/main_logo.png'),
                   caption='Услуга находится в разработке'),
        reply_markup=m.back_to_shop_menu_markup
    )


# ********

products_price = {
    "1000vb": 229,
    "2800vb": 449,
    "5000vb": 549,
    "13500vb": 1349,
    "27000vb": 2499,
    "40500vb": 3749,
    "54000vb": 4999,
    "67500vb": 6249,
    "81000vb": 7499,
    "94500vb": 8749,
    "108000vb": 9999,
    "121500vb": 11249,
    "135000vb": 11999,
    "rec1": 599,
    "rec2": 249,
    "rec3": 499,
    "rec4": 349,
    'd30b': 249,
    'd30f': 349,
    'd365b': 1499,
    'd365f': 2499,
}

products = {
    "1000vb": "1000 В-баксов",
    "2800vb": "2800 В-баксов",
    "5000vb": "5000 В-баксов",
    "13500vb": "13500 В-баксов",
    "27000vb": "27000 В-баксов",
    "40500vb": "40500 В-баксов",
    "54000vb": "54000 В-баксов",
    "67500vb": "67500 В-баксов",
    "81000vb": "81000 В-баксов",
    "94500vb": "94500 В-баксов",
    "108000vb": "108000 В-баксов",
    "121500vb": "121500 В-баксов",
    "135000vb": "135000 В-баксов",
    "rec1": "Мятежный разведчик",
    "rec2": "Мир грез",
    "rec3": "Ценные агенты",
    "rec4": "Прикосновение пустоты",
    'd30b': 'Nitro Basic 30 дней',
    'd30f': 'Nitro Full 30 дней',
    'd365b': 'Nitro Basic 365 дней',
    'd365f': 'Nitro Full 365 дней',
}


# FORTNITE

@market_dp.callback_query_handler(text="vb")
async def vb(callback_query: types.CallbackQuery):
    await market_bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_media(
        InputMedia(media=InputFile('files/all_vb.png'),
                   caption='Выберите товар '),
        reply_markup=m.fortnite_vb_markup
    )


@market_dp.callback_query_handler(text="rec")
async def rec(callback_query: types.CallbackQuery):
    await market_bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_media(
        InputMedia(media=InputFile('files/rec_logo.png'),
                   caption='Выберите товар '),
        reply_markup=m.fortnite_rec_markup
    )


# DISCORD NITRO

@market_dp.callback_query_handler(text="basic")
async def basic(callback_query: types.CallbackQuery):
    d30b_b = InlineKeyboardButton('Nitro Basic 30 дней', callback_data='d30b')
    d365b_b = InlineKeyboardButton('💥Nitro Basic 365 дней💥', callback_data='d365b')
    back_b = InlineKeyboardButton('Назад🔙', callback_data='discordN')

    await market_bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_media(
        InputMedia(media=InputFile('files/all_basic.png'),
                   caption='Выберите товар '),
        reply_markup=InlineKeyboardMarkup(row_width=2).add(*[d30b_b, d365b_b, back_b])
    )


@market_dp.callback_query_handler(text="full")
async def full(callback_query: types.CallbackQuery):
    d30_b = InlineKeyboardButton('Nitro Full 30 дней', callback_data='d30f')
    d365_b = InlineKeyboardButton('💎Nitro Full 365 дней💎', callback_data='d365f')
    back_b = InlineKeyboardButton('Назад🔙', callback_data='discordN')

    await market_bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_media(
        InputMedia(media=InputFile('files/all_full.png'),
                   caption='Выберите товар '),
        reply_markup=InlineKeyboardMarkup(row_width=2).add(*[d30_b, d365_b, back_b])
    )


# ////
product_data = CallbackData('1', "product_name", "payment_service")


@market_dp.callback_query_handler(text=products.keys())
async def choose_p_method(callback_query: types.CallbackQuery):
    aaio_pay_b = InlineKeyboardButton('LAVA', callback_data=product_data.new(product_name=callback_query.data,
                                                                             payment_service='LAVA')
                                      )
    lava_pay_b = InlineKeyboardButton('ANYPAY', callback_data=product_data.new(product_name=callback_query.data,
                                                                               payment_service='ANYPAY')
                                      )
    back_b = InlineKeyboardButton('Назад🔙', callback_data='shop')
    pay_markup = InlineKeyboardMarkup(row_width=2).add(*[aaio_pay_b, lava_pay_b, back_b])

    await market_bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_media(
        InputMedia(media=InputFile(f'files/pay_logo.png'),
                   caption='<b>Выберите способ оплаты.</b>'),
        reply_markup=pay_markup
    )


lava_payment_data = CallbackData('2', "order_id", "product_name")


@market_dp.callback_query_handler(product_data.filter())
async def create_payment(callback_query: types.CallbackQuery, callback_data: product_data):
    if callback_data.get('payment_service') == 'LAVA':
        invoice = await lava.create_invoice(amount=products_price[callback_data.get("product_name")], expire=20)

        pay_b = InlineKeyboardButton('Оплата', url=invoice.url)
        check_payment_b = InlineKeyboardButton(
            'Проверка оплаты', callback_data=lava_payment_data.new(
                order_id=invoice.invoice_id,
                product_name=callback_data.get("product_name")
            )
        )
        back_b = InlineKeyboardButton('Назад🔙', callback_data='shop')
        await market_bot.answer_callback_query(callback_query.id)
        await callback_query.message.edit_media(
            InputMedia(media=InputFile(f'files/{callback_data.get("product_name")}_logo.png'),
                       caption=f'Выбран товар: {products[callback_data.get("product_name")]}'),
            reply_markup=InlineKeyboardMarkup(row_width=2).add(*[pay_b, check_payment_b, back_b])
        )
    elif callback_data.get('payment_service') == 'ANYPAY':
        await market_bot.answer_callback_query(callback_query.id)
        await callback_query.message.edit_media(
            InputMedia(media=InputFile('files/main_logo.png'),
                       caption='Услуга находится в разработке'),
            reply_markup=m.back_to_shop_menu_markup
        )


@market_dp.callback_query_handler(lava_payment_data.filter())
async def check_lava(callback_query: types.CallbackQuery, callback_data: lava_payment_data):
    status = await lava.invoice_status(invoce_id=callback_data.get('order_id'))
    if status == "success":
        h_b = InlineKeyboardButton('Оставить отзыв❤️', callback_data='rev')
        back_b = InlineKeyboardButton('Назад🔙', callback_data='vb')
        success_markup = InlineKeyboardMarkup(row_width=2).add(*[back_b, h_b])

        await market_bot.answer_callback_query(callback_query.id)
        await callback_query.message.edit_media(
            InputMedia(media=InputFile(f'files/{callback_data.get("product_name")}_logo.png'),
                       caption=f"<b>ОПЛАТА ПРОШЛА УСПЕШНО</b>\n"
                               f"Скоро с вами свяжется администратор <b>Hayan Shop</b>.\n"
                               f"❤️Будем рады твоему отзыву!"
                       ),
            reply_markup=success_markup
        )
        cursor.execute('INSERT INTO tickets VALUES(null, ?, ?, ?)',
                       (callback_query.message.chat.username, products[callback_data.get("product_name")], 0))
        connect.commit()
    elif status == "expired":
        pay_b = InlineKeyboardButton('Повторить оплату🔄', callback_data='shop')
        expired_markup = InlineKeyboardMarkup(row_width=2).add(*[pay_b])

        await market_bot.answer_callback_query(callback_query.id)
        await callback_query.message.edit_media(
            InputMedia(media=InputFile(f'files/{callback_data.get("product_name")}_logo.png'),
                       caption=f"<b>ОПЛАТА НЕ БЫЛА ПРОИЗВЕДЕНА ВОВРЕМЯ.</b>\n"
                               f"Для создания новой формы оплаты воспользуйтесь кнопкой: <b>Повторить оплату</b>🔄."
                       ),
            reply_markup=expired_markup
        )
    else:
        pay_b = InlineKeyboardButton('Оплата',
                                     url=f"https://pay.lava.ru/invoice/{callback_data.get('order_id')}?lang=ru")
        check_payment_b = InlineKeyboardButton(
            'Проверка оплаты', callback_data=lava_payment_data.new(
                product_name=callback_data.get("product_name"),
                order_id=callback_data.get('order_id')
            )
        )
        back_b = InlineKeyboardButton('Назад🔙', callback_data='shop')

        await market_bot.answer_callback_query(callback_query.id)
        await callback_query.message.edit_media(
            InputMedia(media=InputFile(f'files/{callback_data.get("product_name")}_logo.png'),
                       caption=f"<b>ОПЛАТА ЕЩЕ НЕ ПРОШЛА.</b>\n"
                               f"Оплатите заказ и пройдите проверку заново."
                       ),
            reply_markup=InlineKeyboardMarkup(row_width=2).add(*[pay_b, check_payment_b, back_b])
        )
