from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

fortnite_b = InlineKeyboardButton('Fortnite🔥', callback_data='fortnite')
discordN_b = InlineKeyboardButton('Discord Nitro👾', callback_data='discordN')
xbox_b = InlineKeyboardButton('Xbox🟩', callback_data='xbox')
spotify_b = InlineKeyboardButton('Spotify🟢', callback_data='spotify')
faceit_b = InlineKeyboardButton('Faceit🌟', callback_data='faceit')
twitch_b = InlineKeyboardButton('Twitch💜', callback_data='twitch')
back_shop_b = InlineKeyboardButton('Назад🔙', callback_data='start')
shop_markup = InlineKeyboardMarkup(row_width=2).add(
    *[fortnite_b, discordN_b, xbox_b, spotify_b, faceit_b, twitch_b, back_shop_b])

back_to_start_menu_b = InlineKeyboardButton('Назад🔙', callback_data='start')
back_to_start_menu_markup = InlineKeyboardMarkup(row_width=2).add(back_to_start_menu_b)

vb_b = InlineKeyboardButton('В-баксы', callback_data='vb')
rec_b = InlineKeyboardButton('Наборы', callback_data='rec')
back_to_shop_menu_b = InlineKeyboardButton('Назад🔙', callback_data='shop')
service_fort_markup = InlineKeyboardMarkup(row_width=2).add(
    *[vb_b, rec_b, back_to_shop_menu_b])

back_to_shop_menu_markup = InlineKeyboardMarkup(row_width=2).add(back_to_shop_menu_b)

vb1000_b = InlineKeyboardButton('1000 В-баксов', callback_data='1000vb')
vb2800_b = InlineKeyboardButton('2800 В-баксов', callback_data='2800vb')
vb5000_b = InlineKeyboardButton('5000 В-баксов', callback_data='5000vb')
vb13500_b = InlineKeyboardButton('13500 В-баксов', callback_data='13500vb')
vb27000_b = InlineKeyboardButton('🔥27000 В-баксов🔥', callback_data='27000vb')
vb40500_b = InlineKeyboardButton('🔥40500 В-баксов🔥', callback_data='40500vb')
vb54000_b = InlineKeyboardButton('🔥54000 В-баксов🔥', callback_data='54000vb')
vb67500_b = InlineKeyboardButton('🔥67500 В-баксов🔥', callback_data='67500vb')
vb81000_b = InlineKeyboardButton('💥81000 В-баксов💥', callback_data='81000vb')
vb94500_b = InlineKeyboardButton('💥94500 В-баксов💥', callback_data='94500vb')
vb108000_b = InlineKeyboardButton('💥108000 В-баксов💥', callback_data='108000vb')
vb121500_b = InlineKeyboardButton('💥121500 В-баксов💥', callback_data='121500vb')
vb135000_b = InlineKeyboardButton('💎135000 В-баксов💎', callback_data='135000vb')
back_to_service_fort_b = InlineKeyboardButton('Назад🔙', callback_data='fortnite')
fortnite_vb_markup = InlineKeyboardMarkup(row_width=2).add(
    *[vb1000_b, vb2800_b, vb5000_b, vb13500_b, vb27000_b, vb40500_b, vb54000_b, vb67500_b, vb81000_b, vb94500_b,
      vb108000_b, vb121500_b, vb135000_b, back_to_service_fort_b])

rec1_b = InlineKeyboardButton('Мятежный разведчик💥', callback_data='rec1')
rec2_b = InlineKeyboardButton('Мир грез🔥', callback_data='rec2')
rec3_b = InlineKeyboardButton('Ценные агенты🎖️', callback_data='rec3')
rec4_b = InlineKeyboardButton('Прикосновение пустоты👑', callback_data='rec4')
fortnite_rec_markup = InlineKeyboardMarkup(row_width=2).add(*[rec1_b, rec2_b, rec3_b, rec4_b, back_to_service_fort_b])

back_to_service_fort_markup = InlineKeyboardMarkup(row_width=2).add(*[back_to_service_fort_b])
