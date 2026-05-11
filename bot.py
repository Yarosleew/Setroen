import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

# Вставте сюди свій токен
API_TOKEN = "8742759318:AAFPb8YA4nosD5GsXcsjZGvo76SvY6b9ZHc"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


# --- БЛОК КОМАНД ---

# /start
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Привіт, я твій бот! Напиши /help, щоб дізнатися, що я вмію.")


# /help
@dp.message(Command("help"))
async def help_command(message: Message):
    await message.answer(
        "Команди:\n"
        "/start — запуск\n"
        "/help — допомога\n"
        "/joke — жарт\n"
        "/about —  про мене\n"
        "/bye — прощання"
    )


# /joke
@dp.message(Command("joke"))
async def joke_command(message: Message):
    await message.answer("Чому комп’ютер пішов у спортзал? Щоб прокачати свої байти!")

@dp.message(Command("about"))
async def about_command(message: Message):
    await message.answer("Я створений на Python з бібліотекою Aiogram!")


# /bye
@dp.message(Command("bye"))
async def bye_command(message: Message):
    await message.answer("До побачення! Гарного дня 😊")


# --- БЛОК ОБРОБКИ ТЕКСТУ ---
# Цей обробник має бути останнім, бо він "ловить" усе інше
@dp.message()
async def echo_all(message: Message):
    # Якщо повідомлення не текст (наприклад, стікер), ігноруємо, щоб не було помилок
    if not message.text:
        return

    text = message.text.lower()

    if "привіт" in text:
        await message.answer("Привіт! Гарного настрою 😄")

    elif "як справи" in text:
        await message.answer("У мене все супер, дякую! А в тебе?")

    elif "що ти вмієш" in text:
        await message.answer("Я можу відповідати на команди (/help) та просто спілкуватися з тобою!")

    elif "анекдот" in text or "жарт" in text:
        await message.answer("Як називається комп’ютерна миша без хвоста? — Бездротова!")

    elif "мені сумно" in text:
        await message.answer("Не сумуй! Все буде добре 😊")

    elif "бувай" in text or "папа" in text:
        await message.answer("До зустрічі! Заходь ще.")

    else:
        await message.answer("Я ще вчуся, тому не знаю як відповісти на це... 🤔")


# --- ЗАПУСК ---
async def main():
    print("Бот запущений...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())