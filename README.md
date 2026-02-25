# To-Do List loyihasi

## Kirish

Har birimizning telefonimizda Telegram o'rnatilgan. Har kuni do'stlar bilan yozishamiz, guruhlardan xabar o'qiymiz, kanallardan yangiliklar ko'ramiz. Lekin Telegram — bu faqat messenger emas. Telegram ichida minglab botlar ishlaydi: ob-havo ko'rsatadigan botlar, valyuta kursini aytadigan botlar, o'yinlar o'ynaydigan botlar. Va eng qiziq joyi shundaki — bu botlarni biz ham yarata olamiz.

Bugungi darsda biz noldan boshlab to'liq ishlaydigan To-Do List (vazifalar ro'yxati) botini yaratamiz. Bu bot foydalanuvchiga kundalik vazifalarini qo'shish, ko'rish, bajarish va o'chirish imkonini beradi. Loyiha oddiy ko'rinsa-da, ichida juda ko'p muhim tushunchalar yashiringan: asinxron dasturlash, ma'lumotlarni saqlash, foydalanuvchi xabarlarini qayta ishlash va xatolardan himoyalanish.

Maqolani o'qib bo'lganingizda siz Aiogram freymworkining asosiy tuzilishini, handler yozish mantiqini va real loyiha qanday qurilishini tushungan bo'lasiz.

---

## Telegram Bot nima va u qanday ishlaydi?

Telegram Bot deganda ko'pchilik murakkab sun'iy intellekt dasturini tasavvur qiladi. Aslida esa bot — bu oddiy dastur bo'lib, u Telegram serveri bilan bog'lanadi va foydalanuvchilar yuborgan xabarlarga javob beradi.

Buni hayotiy misol bilan tushuntiraylik. Tasavvur qiling, siz restoranga keldingiz. Siz ofitsiantga buyurtma berasiz, ofitsiant oshxonaga olib boradi, oshpaz tayyorlaydi, ofitsiant sizga qaytarib olib keladi. Bu jarayonda ofitsiant — bu bot, siz — foydalanuvchi, oshxona — bu sizning kodingiz, restoran esa — Telegram serveri. Bot ham xuddi shunday ishlaydi: foydalanuvchi xabar yozadi, Telegram serveri bu xabarni botga uzatadi, bot javobni qaytaradi, Telegram serveri javobni foydalanuvchiga ko'rsatadi.

Texnik jihatdan bu jarayon quyidagicha sodir bo'ladi. Telegram serverida sizning botingiz uchun maxsus "pochta qutisi" ochiladi. Foydalanuvchi botga xabar yuborganda, bu xabar shu pochta qutisiga tushadi. Sizning dasturingiz esa doimiy ravishda bu pochta qutisini tekshirib turadi — yangi xabar bormi yoki yo'qmi. Yangi xabar topilsa, dastur uni o'qiydi, qayta ishlaydi va javob yuboradi. Bu jarayonga "polling" (so'rab turish) deyiladi.

---

## Aiogram nima va nima uchun aynan u?

Python'da Telegram bot yaratish uchun bir nechta kutubxona mavjud. Eng mashhurlari — python-telegram-bot va Aiogram. Biz Aiogram'ni tanlaymiz, chunki u zamonaviy, tez va asinxron dasturlashga asoslangan.

Asinxron dasturlash nima ekanini tushunish uchun yana hayotiy misol keltiramiz. Tasavvur qiling, siz oshxonada ishlaysiz va sizga bir vaqtda 10 ta buyurtma keldi. Sinxron yondashuv — bu birinchi buyurtmani to'liq tayyorlab bo'lgandan keyin ikkinchisiga o'tish. Bu juda sekin. Asinxron yondashuv esa — birinchi buyurtmaning go'shti qovurilyapti, shu orada ikkinchi buyurtmaning salatini tayyorlash. Ya'ni bo'sh vaqtni behuda kutishga sarflamasdan, boshqa ishlarni bajarib turish.

Aiogram xuddi shunday ishlaydi. Bir foydalanuvchiga javob yuborilayotgan paytda, boshqa foydalanuvchining xabarini ham qabul qilib oladi. Bu ayniqsa ko'p foydalanuvchili botlar uchun muhim.

Biz bugungi darsda Aiogram 3 versiyasidan foydalanamiz. Bu eng so'nggi va barqaror versiya.

---

## Loyihani tayyorlash

### BotFather bilan tanishuv

Har bir Telegram botining hayoti BotFather'dan boshlanadi. BotFather — bu Telegram'ning rasmiy boti bo'lib, u yangi botlar yaratish va ularni sozlash uchun xizmat qiladi. Uni Telegram'da @BotFather deb qidirib topishingiz mumkin.

BotFather'ga /newbot buyrug'ini yuborganingizda, u sizdan ikki narsa so'raydi: botning ko'rsatiladigan nomi (masalan, "Mening vazifalar botim") va botning username'i (masalan, my_todo_list_bot). Username albatta "bot" so'zi bilan tugashi kerak.

Bot yaratilgandan keyin BotFather sizga token beradi. Token — bu botingizning "pasporti", unikal identifikatsiya raqami. U taxminan shunday ko'rinishda bo'ladi: 7123456789:AAHfGxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx. Bu tokenni hech kimga bermang, chunki token kimda bo'lsa, u sizning botingizni boshqara oladi. Xuddi uyingizning kalitini begonaga bermasligingiz kabi, tokenni ham sir saqlang.

### Loyiha papkasini yaratish

Kompyuterda yangi papka yarating va unga "todo_bot" deb nom bering. Bu papka ichida bizga uchta fayl kerak bo'ladi:

Birinchisi — run.py. Bu bizning asosiy fayl, botning butun kodi shu yerda yoziladi.

Ikkinchisi — .env fayl. Bu faylda biz tokenni saqlaymiz. Nima uchun tokenni to'g'ridan-to'g'ri kodga yozmaymiz? Chunki agar siz kodingizni GitHub'ga joylashtirmoqchi bo'lsangiz, token hammaga ko'rinib qoladi. Bu esa havfsizlik muammosi. .env fayl orqali biz tokenni koddan ajratib saqlaymiz.

Uchinchisi — requirements.txt. Bu faylda loyiha uchun kerakli kutubxonalar ro'yxati yoziladi. Bu boshqa dasturchilar loyihani ishga tushirmoqchi bo'lganda ularga qaysi kutubxonalarni o'rnatish kerakligini ko'rsatadi.

### Kutubxonalarni o'rnatish

Terminalni oching va quyidagi buyruqni yozing:

```bash
pip install aiogram python-dotenv
```

Bu yerda ikkita kutubxona o'rnatilmoqda. Birinchisi aiogram — Telegram bot yaratish uchun asosiy freymwork. Ikkinchisi python-dotenv — .env fayldan ma'lumotlarni o'qish uchun kerak bo'ladigan yordamchi kutubxona.

### .env faylni to'ldirish

.env faylni oching va ichiga quyidagini yozing:

```
BOT_TOKEN=7123456789:AAHfGxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

Bu yerda 7123456789:AAHfG... o'rniga BotFather bergan haqiqiy tokeningizni yozing.

---

## Botning asosiy tuzilmasini yozish

Endi eng qiziqarli qismga o'tamiz — kod yozishga. run.py faylni oching va bosqichma-bosqich yozib boramiz.

### Import qilish va sozlamalar

```python
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
import os
```

Dastur birinchi navbatda kerakli kutubxonalarni chaqiradi. Bu xuddi oshpaz ish boshlashdan oldin barcha kerakli masalliqlarni stolga qo'yib olganiga o'xshaydi. asyncio — asinxron dasturlash uchun, logging — xatolarni kuzatish uchun, aiogram'dan Bot, Dispatcher va types — bot yaratish va xabarlar bilan ishlash uchun, Command — buyruqlarni aniqlash uchun, dotenv va os esa .env fayldan tokenni o'qish uchun kerak.

```python
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
```

Bu ikki qatorda biz .env faylni yuklaymiz va undan BOT_TOKEN nomli o'zgaruvchini o'qib olamiz. Natijada BOT_TOKEN o'zgaruvchisi ichida bizning token saqlangan bo'ladi.

```python
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
```

Bu yerda biz ikkita asosiy obyektni yaratamiz. Bot obyekti — Telegram serveri bilan bog'lanish uchun. Uni "telefon" deb tasavvur qiling — u orqali biz Telegram'ga xabar yuboramiz va xabar olamiz. Dispatcher esa "menejer" vazifasini bajaradi — u kelgan xabarlarni to'g'ri handler'ga yo'naltiradi. Masalan, foydalanuvchi /start yuborganda, Dispatcher biladi: "Bu buyruqni cmd_start funksiyasi bajarishi kerak."

```python
logging.basicConfig(level=logging.INFO)
```

Bu qator xatolarni kuzatish tizimini yoqadi. Bot ishlayotganda terminalda nima sodir bo'layotganini ko'rishingiz mumkin. Xato yuz berganda, logging sizga aniq qayerda muammo borligini ko'rsatadi. Bu xuddi mashinadagi diagnostika tizimiga o'xshaydi — muammo bo'lganda signal beradi.

---

## Ma'lumotlarni saqlash

Botimiz foydalanuvchilarning vazifalarini qayerda saqlaydi? Hozircha biz eng oddiy usulni ishlatamiz — Python'ning dictionary (lug'at) ma'lumot turini:

```python
user_todos = {}
```

Bu bo'sh lug'at. Foydalanuvchi birinchi marta vazifa qo'shganda, bu lug'atga uning ID raqami kalit sifatida, vazifalari esa ro'yxat sifatida yoziladi. Masalan:

```python
{
    123456: ["Dars tayyorlash", "Kitob o'qish"],
    789012: ["Bozorga borish", "Narvonda tozalash"]
}
```

Bu yerda 123456 va 789012 — foydalanuvchilarning Telegram ID raqamlari. Har bir foydalanuvchining vazifalari alohida ro'yxatda saqlanadi, shuning uchun bir foydalanuvchining vazifalari boshqasiga ko'rinmaydi.

Bu usulning bir kamchiligi bor: bot o'chirilsa yoki qayta ishga tushsa, barcha ma'lumotlar yo'qoladi. Chunki dictionary kompyuter xotirasida saqlanadi, faylda yoki ma'lumotlar bazasida emas. Buni shunday tasavvur qiling: siz doska (whiteboard)ga yozgan narsalar — elektr o'chsa, doska o'chirilsa, hammasi yo'qoladi. Keyingi darslarda biz ma'lumotlarni bazaga saqlashni o'rganamiz, ya'ni "doskadan" "daftarga" o'tamiz.

---

## Handler'lar — botning "quloqlari" va "og'zi"

Handler — bu bot uchun eng muhim tushuncha. Handler degani "ishlov beruvchi" yoki "qabul qiluvchi" demak. Har bir handler ma'lum bir turdagi xabarga javob berish uchun mo'ljallangan.

Buni pochta bo'limiga o'xshatish mumkin. Pochta bo'limida har xil oynalar bor: biri pochta jo'natish uchun, biri pochta olish uchun, yana biri shikoyatlar uchun. Har bir oynada bitta xodim o'tiradi va faqat o'z ishini bajaradi. Handler'lar ham xuddi shunday — har bir handler faqat o'ziga tayinlangan buyruqqa javob beradi.

### /start buyrug'i — botni birinchi marta ishga tushirish

```python
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Salom! Men To-Do List botman.\n\n"
        "Buyruqlar:\n"
        "/add <vazifa> — Yangi vazifa qo'shish\n"
        "/list — Vazifalar ro'yxati\n"
        "/done <raqam> — Vazifani bajarish\n"
        "/clear — Hammasini o'chirish\n"
        "/help — Yordam"
    )
```

Bu botning "salomlashish" funksiyasi. Foydalanuvchi botni birinchi marta ochib /start bosganda, bot o'zini tanishtiradi va qanday buyruqlar borligini aytib beradi.

@dp.message(Command("start")) — bu dekorator. Dekorator funksiyaga "birka" osib qo'yadi. Bu birka Dispatcher'ga aytadi: "Agar kimdir /start yuborsa, shu funksiyani chaqir." Async def — bu funksiya asinxron ekanligini bildiradi. Await esa xabar yuborilguncha kutish kerakligini aytadi.

### /add buyrug'i — yangi vazifa qo'shish

```python
@dp.message(Command("add"))
async def cmd_add(message: types.Message):
    task_text = message.text.replace("/add", "").strip()

    if not task_text:
        await message.answer("Vazifa matnini kiriting!\nMisol: /add Dars tayyorlash")
        return

    user_id = message.from_user.id

    if user_id not in user_todos:
        user_todos[user_id] = []

    user_todos[user_id].append(task_text)

    count = len(user_todos[user_id])
    await message.answer(f"Vazifa qo'shildi: {task_text}\nJami: {count} ta vazifa")
```

Bu handler eng ko'p mantiq o'z ichiga oladi. Foydalanuvchi "/add Dars tayyorlash" deb yozganda, bot birinchi navbatda xabar matnidan "/add" qismini olib tashlaydi va faqat "Dars tayyorlash" qismini oladi. Bu jarayonni shunday tasavvur qiling: konvertga "Kimga: Aliyev" deb yozilgan. Biz konvertdan faqat "Aliyev" ismini o'qiymiz, "Kimga:" qismini tashlab yuboramiz.

Keyin tekshirish bo'ladi: agar foydalanuvchi faqat "/add" yozib, vazifa matnini unutgan bo'lsa, bot unga ogohlantirish beradi va funksiya to'xtaydi. Bu muhim — har doim foydalanuvchi xato kiritishi mumkinligini hisobga oling.

Undan keyin foydalanuvchining ID raqami olinadi. Bu raqam Telegram'da har bir foydalanuvchiga beriladigan unikal son. Xuddi fuqaroning pasport raqami kabi — ikki kishi bir xil ID ga ega bo'lishi mumkin emas.

Agar bu foydalanuvchi birinchi marta vazifa qo'shayotgan bo'lsa (ya'ni uning ID si lug'atda mavjud emas), uning uchun bo'sh ro'yxat yaratiladi. Keyin vazifa shu ro'yxatga qo'shiladi.

### /list buyrug'i — vazifalarni ko'rish

```python
@dp.message(Command("list"))
async def cmd_list(message: types.Message):
    user_id = message.from_user.id
    tasks = user_todos.get(user_id, [])

    if not tasks:
        await message.answer("Vazifalar ro'yxati bo'sh.\n/add bilan yangi vazifa qo'shing!")
        return

    text = "Sizning vazifalaringiz:\n\n"
    for index, task in enumerate(tasks, start=1):
        text += f"  {index}. {task}\n"

    text += f"\nJami: {len(tasks)} ta vazifa"
    await message.answer(text)
```

Bu handler foydalanuvchining barcha vazifalarini chiroyli ro'yxat shaklida ko'rsatadi.

Bu yerda muhim nuqta — .get() metodi. Oddiy holatda, agar lug'atda mavjud bo'lmagan kalitni so'rasangiz, dastur xato beradi va to'xtab qoladi. Lekin .get(kalit, standart_qiymat) metodi xato bermaydi — kalit topilmasa, o'rniga standart qiymatni qaytaradi. Bizning holatda bo'sh ro'yxat [] qaytadi.

enumerate() funksiyasi esa ro'yxat elementlarini raqam bilan birga beradi. start=1 parametri raqamlashni 0 dan emas, 1 dan boshlashni aytadi. Chunki oddiy odamlar narsalarni 1 dan sanaydi, dasturchilar esa 0 dan. Biz bu yerda foydalanuvchiga qulay bo'lishi uchun 1 dan boshlaymiz.

### /done buyrug'i — vazifani bajarilgan deb belgilash

```python
@dp.message(Command("done"))
async def cmd_done(message: types.Message):
    user_id = message.from_user.id
    tasks = user_todos.get(user_id, [])

    if not tasks:
        await message.answer("Vazifalar ro'yxati bo'sh!")
        return

    try:
        task_number = int(message.text.replace("/done", "").strip())
    except ValueError:
        await message.answer("Raqam kiriting!\nMisol: /done 1")
        return

    if task_number < 1 or task_number > len(tasks):
        await message.answer(f"Noto'g'ri raqam! 1 dan {len(tasks)} gacha kiriting.")
        return

    removed_task = tasks.pop(task_number - 1)
    await message.answer(f"Bajarildi: {removed_task}\nQoldi: {len(tasks)} ta vazifa")
```

Bu handler eng ko'p himoya qatlamlariga ega. Nima uchun? Chunki foydalanuvchi noto'g'ri ma'lumot yuborishi mumkin.

Birinchi himoya: ro'yxat bo'shligini tekshirish. Ikkinchi himoya: try/except bloki. Foydalanuvchi "/done bir" deb yozishi mumkin, "bir" ni songa aylantirish esa imkonsiz, shuning uchun ValueError xatosi yuzaga keladi. try/except bu xatoni ushlab, dasturni to'xtatmasdan foydalanuvchiga tushunarli xabar beradi. Uchinchi himoya: raqam chegarasini tekshirish. Agar ro'yxatda 3 ta vazifa bo'lsa, foydalanuvchi "/done 7" deb yozmasligi kerak.

.pop() metodi haqida alohida to'xtalib o'tamiz. Bu metod ro'yxatdan elementni olib tashlaydi va o'chirilgan elementni qaytaradi. Bu xuddi javondan kitobni olganingizga o'xshaydi — kitob javonda endi yo'q, lekin u sizning qo'lingizda. Biz o'chirilgan vazifani removed_task o'zgaruvchisiga saqlaymiz, keyin foydalanuvchiga "Bu vazifa bajarildi" deb xabar beramiz.

Muhim nuqta: task_number - 1 qismi. Foydalanuvchiga biz vazifalarni 1 dan boshlab ko'rsatamiz, lekin Python ichida ro'yxat 0 dan boshlanadi. Shuning uchun foydalanuvchi "2" deb yozsa, biz 1-indexdagi elementni o'chiramiz.

### /clear buyrug'i — barcha vazifalarni o'chirish

```python
@dp.message(Command("clear"))
async def cmd_clear(message: types.Message):
    user_id = message.from_user.id

    if user_id in user_todos and user_todos[user_id]:
        count = len(user_todos[user_id])
        user_todos[user_id] = []
        await message.answer(f"{count} ta vazifa o'chirildi!")
    else:
        await message.answer("Vazifalar ro'yxati allaqachon bo'sh!")
```

Bu handler oddiy — foydalanuvchining barcha vazifalarini bir yola o'chiradi. Bu yerda ikki shart tekshiriladi: foydalanuvchi lug'atda bormi va uning ro'yxati bo'sh emasmi. Agar ikkalasi ham to'g'ri bo'lsa, ro'yxat bo'sh ro'yxatga almashtiriladi.

### /help buyrug'i — yordam xabari

```python
@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(
        "To-Do List Bot — Yordam\n\n"
        "Mavjud buyruqlar:\n\n"
        "/add <vazifa> — Yangi vazifa qo'shish\n"
        "  Misol: /add Kitob o'qish\n\n"
        "/list — Barcha vazifalarni ko'rish\n\n"
        "/done <raqam> — Vazifani bajarilgan deb belgilash\n"
        "  Misol: /done 2\n\n"
        "/clear — Barcha vazifalarni o'chirish\n\n"
        "/help — Ushbu yordam xabarini ko'rish"
    )
```

Bu handler /start ga o'xshash, lekin batafsilroq. Har bir buyruq uchun misol ham berilgan. Yaxshi bot har doim foydalanuvchiga tushunarli yo'riqnoma berishi kerak.

---

## Botni ishga tushirish

```python
async def main():
    print("Bot ishga tushdi!")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
```

Bu kodning oxirgi qismi — botni haqiqatda ishga tushirish.

delete_webhook(drop_pending_updates=True) — bu qator bot o'chirilgan vaqtda to'plangan eski xabarlarni tashlab yuboradi. Tasavvur qiling, siz 3 kun ta'tilga chiqdingiz va pochta qutingiz xatlarga to'lib ketdi. Ishga qaytganingizda eski xatlar bilan shug'ullanish o'rniga, "barini o'qilgan deb belgilab", faqat yangi xatlar bilan ishlaysiz. Bu qator xuddi shu ishni qiladi.

start_polling(bot) — bu qator botni "tinglash" rejimiga o'tkazadi. Bot doimiy ravishda Telegram serveriga so'rov yuboradi: "Yangi xabar bormi? Yangi xabar bormi?" Bu jarayon bot to'xtatilmaguncha davom etadi.

if __name__ == "__main__" — bu Python'ning standart konstruksiyasi. U shuni bildiradi: "Agar bu fayl to'g'ridan-to'g'ri ishga tushirilsa (import qilinmasa), main() funksiyasini chaqir." asyncio.run() esa asinxron funksiyani oddiy sinxron muhitdan ishga tushirish uchun kerak.

Botni ishga tushirish uchun terminalda quyidagini yozing:

```bash
python run.py
```

Agar hammasi to'g'ri qilingan bo'lsa, terminalda "Bot ishga tushdi!" degan xabar chiqadi. Endi Telegram'da botingizni ochib, /start bosing va sinab ko'ring.

---

## To'liq kod — qatorma-qator tushuntirish

Quyida loyihaning to'liq kodi keltirilgan. Har bir qator raqamlangan va uning ostida batafsil izoh berilgan. Maqolaning oldingi qismlarida biz har bir handler'ni alohida tushuntirib o'tdik. Endi esa butun kodga yaxlit holda qarab, har bir qatorda nima sodir bo'layotganini aniqlaymiz.

```
1  | import asyncio
2  | import logging
3  | from aiogram import Bot, Dispatcher, types
4  | from aiogram.filters import Command
5  | from dotenv import load_dotenv
6  | import os
```

1-qator: asyncio — Python'ning asinxron dasturlash kutubxonasi. Bot bir vaqtda ko'p foydalanuvchiga xizmat ko'rsatishi uchun kerak.

2-qator: logging — dasturda nima sodir bo'layotganini terminal ekraniga chiqarib beruvchi kutubxona. Xatolarni topishda juda foydali.

3-qator: aiogram kutubxonasidan uchta narsa import qilinmoqda. Bot — Telegram bilan bog'lanish uchun. Dispatcher — xabarlarni to'g'ri handler'ga yo'naltirish uchun. types — xabar, foydalanuvchi kabi tushunchalarni ifodalovchi sinflar to'plami.

4-qator: Command — bu filtr sinfi. U xabar oddiy matnmi yoki buyruqmi (/start, /help kabi) ekanligini aniqlaydi.

5-qator: dotenv kutubxonasidan load_dotenv funksiyasini import qilish. Bu funksiya .env fayldagi o'zgaruvchilarni dasturga yuklaydi.

6-qator: os — operatsion tizim bilan ishlash uchun standart kutubxona. Biz undan muhit o'zgaruvchilarini o'qish uchun foydalanamiz.

```
7  | load_dotenv()
8  | BOT_TOKEN = os.getenv("BOT_TOKEN")
```

7-qator: .env faylni o'qiydi va ichidagi barcha o'zgaruvchilarni dastur muhitiga yuklaydi.

8-qator: muhitdan "BOT_TOKEN" nomli o'zgaruvchini o'qib, BOT_TOKEN o'zgaruvchisiga saqlaydi. Endi BOT_TOKEN ichida bizning bot tokeni bor.

```
9  | bot = Bot(token=BOT_TOKEN)
10 | dp = Dispatcher()
```

9-qator: Bot sinfidan yangi obyekt yaratildi. Token parametri sifatida berildi — bu bot qaysi Telegram bot hisobiga ulanishini aniqlaydi.

10-qator: Dispatcher obyekti yaratildi. U barcha handler'larni ro'yxatga olib, kelgan xabarlarni mos handler'ga uzatadi.

```
11 | logging.basicConfig(level=logging.INFO)
```

11-qator: logging tizimini INFO darajasida sozlash. Bu daraja xatolar, ogohlantirishlar va umumiy ma'lumotlarni ko'rsatadi.

```
12 | user_todos = {}
```

12-qator: bo'sh dictionary yaratish. Bu yerda har bir foydalanuvchining vazifalari saqlanadi. Kalit — foydalanuvchi ID si (son), qiymat — vazifalar ro'yxati (list).

```
13 | @dp.message(Command("start"))
14 | async def cmd_start(message: types.Message):
15 |     await message.answer(
16 |         "Salom! Men To-Do List botman.\n\n"
17 |         "Buyruqlar:\n"
18 |         "/add <vazifa> — Yangi vazifa qo'shish\n"
19 |         "/list — Vazifalar ro'yxati\n"
20 |         "/done <raqam> — Vazifani bajarish\n"
21 |         "/clear — Hammasini o'chirish\n"
22 |         "/help — Yordam"
23 |     )
```

13-qator: dekorator — Dispatcher'ga aytadi: "/start buyrug'i kelganda quyidagi funksiyani chaqir."

14-qator: asinxron funksiya e'lon qilish. message parametri — foydalanuvchi yuborgan xabar haqidagi barcha ma'lumot (matn, kim yubordi, qachon yubordi va hokazo).

15-23-qator: foydalanuvchiga javob xabari yuborish. answer() metodi xabarni o'sha chatga qaytaradi. \n — yangi qatorga o'tish belgisi.

```
24 | @dp.message(Command("add"))
25 | async def cmd_add(message: types.Message):
26 |     task_text = message.text.replace("/add", "").strip()
```

24-qator: /add buyrug'i uchun handler.

25-qator: funksiya e'loni.

26-qator: xabar matnidan "/add" so'zini olib tashlab, qolgan matnni olish. strip() bosh va oxiridagi bo'sh joylarni olib tashlaydi. Masalan, "/add  Dars tayyorlash  " dan "Dars tayyorlash" olinadi.

```
27 |     if not task_text:
28 |         await message.answer("Vazifa matnini kiriting!\nMisol: /add Dars tayyorlash")
29 |         return
```

27-qator: agar task_text bo'sh bo'lsa (foydalanuvchi faqat "/add" yozgan bo'lsa).

28-qator: xatolik xabarini yuborish.

29-qator: funksiyadan chiqish. return dan keyingi kodlar bajarilmaydi.

```
30 |     user_id = message.from_user.id
```

30-qator: xabar yuborgan foydalanuvchining Telegram ID raqamini olish.

```
31 |     if user_id not in user_todos:
32 |         user_todos[user_id] = []
```

31-qator: bu foydalanuvchi avval hech qachon vazifa qo'shmaganmi tekshirish.

32-qator: agar qo'shmagan bo'lsa, u uchun bo'sh ro'yxat yaratish.

```
33 |     user_todos[user_id].append(task_text)
```

33-qator: yangi vazifani foydalanuvchining ro'yxati oxiriga qo'shish.

```
34 |     count = len(user_todos[user_id])
35 |     await message.answer(f"Vazifa qo'shildi: {task_text}\nJami: {count} ta vazifa")
```

34-qator: foydalanuvchining jami vazifalar sonini hisoblash.

35-qator: tasdiqlash xabarini yuborish. f-string ichida {task_text} va {count} o'z qiymatlari bilan almashtiriladi.

```
36 | @dp.message(Command("list"))
37 | async def cmd_list(message: types.Message):
38 |     user_id = message.from_user.id
39 |     tasks = user_todos.get(user_id, [])
```

36-37-qator: /list buyrug'i uchun handler.

38-qator: foydalanuvchi ID sini olish.

39-qator: foydalanuvchining vazifalar ro'yxatini olish. .get() metodi kalit topilmasa xato bermaydi, o'rniga bo'sh ro'yxat qaytaradi.

```
40 |     if not tasks:
41 |         await message.answer("Vazifalar ro'yxati bo'sh.\n/add bilan yangi vazifa qo'shing!")
42 |         return
```

40-42-qator: ro'yxat bo'sh bo'lsa, xabar berib funksiyadan chiqish.

```
43 |     text = "Sizning vazifalaringiz:\n\n"
44 |     for index, task in enumerate(tasks, start=1):
45 |         text += f"  {index}. {task}\n"
```

43-qator: javob matnini boshlash.

44-qator: har bir vazifani raqam bilan birga ko'rish. enumerate() funksiyasi 1 dan boshlab (index, task) juftligini beradi.

45-qator: har bir vazifani "raqam. vazifa" formatida matnga qo'shish.

```
46 |     text += f"\nJami: {len(tasks)} ta vazifa"
47 |     await message.answer(text)
```

46-qator: oxiriga jami sonini qo'shish.

47-qator: tayyor matnni foydalanuvchiga yuborish.

```
48 | @dp.message(Command("done"))
49 | async def cmd_done(message: types.Message):
50 |     user_id = message.from_user.id
51 |     tasks = user_todos.get(user_id, [])
```

48-51-qator: /done handler'i. Foydalanuvchi ID si va vazifalar ro'yxati olinadi.

```
52 |     if not tasks:
53 |         await message.answer("Vazifalar ro'yxati bo'sh!")
54 |         return
```

52-54-qator: ro'yxat bo'sh bo'lsa, xabar berish va chiqish.

```
55 |     try:
56 |         task_number = int(message.text.replace("/done", "").strip())
57 |     except ValueError:
58 |         await message.answer("Raqam kiriting!\nMisol: /done 1")
59 |         return
```

55-qator: xatoga chidamli blok boshlanishi. Bu blok ichidagi kod xato berishi mumkin.

56-qator: xabar matnidan raqamni ajratib olish va songa aylantirish.

57-qator: agar 56-qatorda xato bo'lsa (masalan, "bir" ni songa aylantirish mumkin emas), shu yerga tushadi.

58-59-qator: foydalanuvchiga xatolik haqida xabar berish va funksiyadan chiqish.

```
60 |     if task_number < 1 or task_number > len(tasks):
61 |         await message.answer(f"Noto'g'ri raqam! 1 dan {len(tasks)} gacha kiriting.")
62 |         return
```

60-62-qator: raqam chegarasini tekshirish. 0 dan kichik yoki ro'yxat uzunligidan katta bo'lmasligi kerak.

```
63 |     removed_task = tasks.pop(task_number - 1)
64 |     await message.answer(f"Bajarildi: {removed_task}\nQoldi: {len(tasks)} ta vazifa")
```

63-qator: vazifani ro'yxatdan olib tashlash. pop() metodi elementni o'chiradi va qaytaradi. task_number - 1 chunki foydalanuvchi 1 dan sanaydi, Python esa 0 dan.

64-qator: bajarilgan vazifa nomini va qolgan vazifalar sonini ko'rsatish.

```
65 | @dp.message(Command("clear"))
66 | async def cmd_clear(message: types.Message):
67 |     user_id = message.from_user.id
```

65-67-qator: /clear handler'i va foydalanuvchi ID sini olish.

```
68 |     if user_id in user_todos and user_todos[user_id]:
69 |         count = len(user_todos[user_id])
70 |         user_todos[user_id] = []
71 |         await message.answer(f"{count} ta vazifa o'chirildi!")
72 |     else:
73 |         await message.answer("Vazifalar ro'yxati allaqachon bo'sh!")
```

68-qator: ikki shart tekshiriladi — foydalanuvchi lug'atda bormi VA uning ro'yxati bo'sh emasmi.

69-qator: o'chirilayotgan vazifalar sonini saqlash (xabar uchun kerak).

70-qator: ro'yxatni bo'sh ro'yxatga almashtirish — ya'ni hammasini o'chirish.

71-qator: nechta vazifa o'chirilganini xabar qilish.

72-73-qator: agar ro'yxat bo'sh bo'lsa yoki foydalanuvchi hali vazifa qo'shmagan bo'lsa.

```
74 | @dp.message(Command("help"))
75 | async def cmd_help(message: types.Message):
76 |     await message.answer(
77 |         "To-Do List Bot — Yordam\n\n"
78 |         "Mavjud buyruqlar:\n\n"
79 |         "/add <vazifa> — Yangi vazifa qo'shish\n"
80 |         "  Misol: /add Kitob o'qish\n\n"
81 |         "/list — Barcha vazifalarni ko'rish\n\n"
82 |         "/done <raqam> — Vazifani bajarilgan deb belgilash\n"
83 |         "  Misol: /done 2\n\n"
84 |         "/clear — Barcha vazifalarni o'chirish\n\n"
85 |         "/help — Ushbu yordam xabarini ko'rish"
86 |     )
```

74-86-qator: /help handler'i. Barcha buyruqlar va ularning misollarini batafsil ko'rsatadi. Bu handler /start ga o'xshash, lekin har bir buyruq uchun qo'shimcha misol ham berilgan.

```
87 | async def main():
88 |     print("Bot ishga tushdi!")
89 |     await bot.delete_webhook(drop_pending_updates=True)
90 |     await dp.start_polling(bot)
```

87-qator: asosiy funksiya e'loni.

88-qator: terminalga xabar chiqarish — bot muvaffaqiyatli ishga tushganini tasdiqlash.

89-qator: eski webhook'ni o'chirish va to'planib qolgan xabarlarni tashlab yuborish. Bot o'chirilgan paytda foydalanuvchilar yuborgan xabarlar to'planib qolishi mumkin. Bu qator o'sha xabarlarni e'tiborsiz qoldiradi.

90-qator: polling rejimini ishga tushirish — bot doimiy ravishda Telegram serveridan yangi xabarlarni so'rab turadi.

```
91 | if __name__ == "__main__":
92 |     asyncio.run(main())
```

91-qator: bu fayl to'g'ridan-to'g'ri ishga tushirilganini tekshirish. Agar boshqa fayl bu faylni import qilsa, main() avtomatik ishga tushmaydi.

92-qator: asinxron main() funksiyani ishga tushirish. asyncio.run() sinxron muhitdan asinxron funksiyani chaqirish imkonini beradi. Bu qator bot ishini boshlaydi va u to'xtatilmaguncha davom ettiradi.

---

## Xulosa

Bugungi darsda biz Aiogram freymworki bilan tanishdik va noldan to'liq ishlaydigan To-Do List bot yaratdik. Bu oddiy loyiha orqali biz quyidagi muhim tushunchalarni o'rgandik:

Birinchidan, Telegram bot qanday ishlashini — foydalanuvchi xabar yuboradi, Telegram serveri uni botga uzatadi, bot qayta ishlab javob qaytaradi. Ikkinchidan, Aiogram'ning asosiy tuzilishini — Bot, Dispatcher, Handler'lar. Uchinchidan, asinxron dasturlashning asoslarini — async, await, asyncio. To'rtinchidan, xavfsiz kod yozishni — try/except bilan xatolarni ushlash, foydalanuvchi kiritgan ma'lumotni tekshirish, .env fayl orqali maxfiy ma'lumotlarni himoyalash.

Bu bot oddiy bo'lsa-da, u kelajakda murakkab loyihalar uchun mustahkam poydevor bo'lib xizmat qiladi. Keyingi darslarda biz inline tugmalar, ma'lumotlar bazasi, state management va boshqa ilg'or mavzularni o'rganamiz.

---

## Uy vazifasi

Birinchi daraja (oson): /count buyrug'ini qo'shing. Bu buyruq foydalanuvchining jami nechta vazifasi borligini ko'rsatsin. Bu oddiy handler yozish amaliyoti.

Ikkinchi daraja (o'rta): /edit buyrug'ini qo'shing. Foydalanuvchi "/edit 2 Yangi matn" yozganda, 2-raqamli vazifa matni o'zgarsin. Bu yerda siz matnni ajratish va ro'yxatda elementni almashtirish mantiqini o'rganasiz.

Uchinchi daraja (qiyin): Vazifalarni JSON faylga saqlashni amalga oshiring. Bot qayta ishga tushganda ham ma'lumotlar saqlanib qolsin. Buning uchun Python'ning json kutubxonasidan foydalaning.
