import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
import os

# ==============================
# 1-BOSQICH: Muhit sozlash
# ==============================

# .env fayldan tokenni yuklash
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Bot va Dispatcher yaratish
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Logging sozlash
logging.basicConfig(level=logging.INFO)

# ==============================
# 2-BOSQICH: Ma'lumotlar bazasi
# ==============================

# Har bir foydalanuvchi uchun alohida ro'yxat
user_todos = {}


# ==============================
# 3-BOSQICH: Handler'lar
# ==============================

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "👋 Salom! Men To-Do List botman.\n\n"
        "📌 Buyruqlar:\n"
        "/add <vazifa> — Yangi vazifa qo'shish\n"
        "/list — Vazifalar ro'yxati\n"
        "/done <raqam> — Vazifani bajarish\n"
        "/clear — Hammasini o'chirish\n"
        "/help — Yordam"
    )


@dp.message(Command("add"))
async def cmd_add(message: types.Message):
    # /add dan keyingi matnni olish
    task_text = message.text.replace("/add", "").strip()

    if not task_text:
        await message.answer("❌ Vazifa matnini kiriting!\nMisol: /add Dars tayyorlash")
        return

    user_id = message.from_user.id

    # Foydalanuvchi uchun ro'yxat yaratish (agar yo'q bo'lsa)
    if user_id not in user_todos:
        user_todos[user_id] = []

    # Vazifani qo'shish
    user_todos[user_id].append(task_text)

    count = len(user_todos[user_id])
    await message.answer(f"✅ Vazifa qo'shildi: {task_text}\n📊 Jami: {count} ta vazifa")


@dp.message(Command("list"))
async def cmd_list(message: types.Message):
    user_id = message.from_user.id
    tasks = user_todos.get(user_id, [])

    if not tasks:
        await message.answer("📭 Vazifalar ro'yxati bo'sh.\n/add bilan yangi vazifa qo'shing!")
        return

    # Ro'yxatni chiroyli formatda chiqarish
    text = "📋 Sizning vazifalaringiz:\n\n"
    for index, task in enumerate(tasks, start=1):
        text += f"  {index}. {task}\n"

    text += f"\n📊 Jami: {len(tasks)} ta vazifa"
    await message.answer(text)


@dp.message(Command("done"))
async def cmd_done(message: types.Message):
    user_id = message.from_user.id
    tasks = user_todos.get(user_id, [])

    if not tasks:
        await message.answer("📭 Vazifalar ro'yxati bo'sh!")
        return

    # Raqamni olish
    try:
        task_number = int(message.text.replace("/done", "").strip())
    except ValueError:
        await message.answer("❌ Raqam kiriting!\nMisol: /done 1")
        return

    # Raqamni tekshirish
    if task_number < 1 or task_number > len(tasks):
        await message.answer(f"❌ Noto'g'ri raqam! 1 dan {len(tasks)} gacha kiriting.")
        return

    # Vazifani o'chirish
    removed_task = tasks.pop(task_number - 1)
    await message.answer(f"🎉 Bajarildi: {removed_task}\n📊 Qoldi: {len(tasks)} ta vazifa")


@dp.message(Command("clear"))
async def cmd_clear(message: types.Message):
    user_id = message.from_user.id

    if user_id in user_todos and user_todos[user_id]:
        count = len(user_todos[user_id])
        user_todos[user_id] = []
        await message.answer(f"🗑 {count} ta vazifa o'chirildi!")
    else:
        await message.answer("📭 Vazifalar ro'yxati allaqachon bo'sh!")


@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(
        "🤖 To-Do List Bot — Yordam\n\n"
        "📌 Mavjud buyruqlar:\n\n"
        "/add <vazifa> — Yangi vazifa qo'shish\n"
        "  Misol: /add Kitob o'qish\n\n"
        "/list — Barcha vazifalarni ko'rish\n\n"
        "/done <raqam> — Vazifani bajarilgan deb belgilash\n"
        "  Misol: /done 2\n\n"
        "/clear — Barcha vazifalarni o'chirish\n\n"
        "/help — Ushbu yordam xabarini ko'rish"
    )


# ==============================
# 4-BOSQICH: Botni ishga tushirish
# ==============================

async def main():
    print("✅ Bot ishga tushdi!")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("🛑 Bot to'xtatildi!")
