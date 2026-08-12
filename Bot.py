import gspread
from google.oauth2.service_account import Credentials
import telebot

# --- Настройки Google Sheets ---
SHEET_FILE = "rating-urmed-65989136bc19.json"  # файл JSON с ключами сервисного аккаунта
SHEET_NAME = "УМ журнал 25-26 1 взвод"
RANGE = "S4:S41"  # диапазон ячеек, который хотим получить

# Авторизация
scopes = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
creds = Credentials.from_service_account_file(SHEET_FILE, scopes=scopes)
gc = gspread.authorize(creds)

# Получаем лист и данные
sheet = gc.open(SHEET_NAME).sheet1  # можно заменить на .worksheet("Название листа")
data = sheet.get(RANGE)

# Превращаем данные в текст
message_text = ""
for row in data:
    message_text += " | ".join(row) + "\n"

# --- Настройки Telegram ---
TOKEN = "8265664998:AAF2MCKqXjpXDUfbwr6bHDArfcC8Hh_iRcw"
CHAT_ID = "-1002763683887_60"

bot = telebot.TeleBot(TOKEN)

# Отправка сообщения
bot.send_message(CHAT_ID, message_text)