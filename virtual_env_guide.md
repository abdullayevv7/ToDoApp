# Python Virtual Muhit (Virtual Environment)

## Virtual muhit nima?

Virtual muhit — bu loyihangiz uchun alohida, mustaqil Python muhiti yaratish usuli.
Har bir loyiha o'zining kutubxonalariga ega bo'ladi va boshqa loyihalarni buzib qo'ymaydi.

Masalan, bitta loyihangizda `aiogram 3.0` kerak, boshqasida `aiogram 2.0` kerak.
Agar hammasi bitta joyga o'rnatilsa, ular bir-biriga xalaqit beradi.
Virtual muhit bu muammoni hal qiladi.

---

## 1. Virtual muhit yaratish

Terminalni oching va loyiha papkasiga kiring:

```
cd d:\Desktop\ToDoApp
```

Keyin quyidagi buyruqni yozing:

```
python -m venv .venv
```

Bu yerda:
- `python -m venv` — Python ichidagi virtual muhit yaratish moduli
- `.venv` — yaratiladigan papka nomi (nuqta bilan boshlanadi, shuning uchun yashirin papka bo'ladi)

Buyruq bajarilgandan keyin loyiha papkasida `.venv` nomli yangi papka paydo bo'ladi.

---

## 2. Virtual muhitni faollashtirish (activate)

### Windows (CMD):
```
.venv\Scripts\activate
```

### Windows (PowerShell):
```
.venv\Scripts\Activate.ps1
```

Agar PowerShell da xatolik chiqsa, avval quyidagini bir marta bajaring:
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Windows (Git Bash):
```
source .venv/Scripts/activate
```

### macOS / Linux:
```
source .venv/bin/activate
```

Faollashtirilgandan keyin terminal boshida `(.venv)` yozuvi paydo bo'ladi.
Bu virtual muhit ishlayotganini bildiradi.

---

## 3. Kutubxonalarni o'rnatish

Virtual muhit faollashtirilgan holda kutubxonalarni o'rnating:

```
pip install aiogram python-dotenv
```

Bu kutubxonalar faqat shu virtual muhit ichiga o'rnatiladi,
kompyuteringizdagi boshqa loyihalarga ta'sir qilmaydi.

O'rnatilgan kutubxonalarni ko'rish uchun:

```
pip list
```

---

## 4. requirements.txt fayli

Boshqa dasturchilar ham loyihangizni ishga tushira olishi uchun
o'rnatilgan kutubxonalar ro'yxatini faylga saqlash kerak:

```
pip freeze > requirements.txt
```

Bu buyruq `requirements.txt` faylini yaratadi. Fayl ichida barcha
kutubxonalar va ularning versiyalari yozilgan bo'ladi. Masalan:

```
aiogram==3.15.0
python-dotenv==1.0.1
```

Boshqa odam loyihani yuklab olib, kutubxonalarni bir buyruq bilan o'rnatishi mumkin:

```
pip install -r requirements.txt
```

---

## 5. Virtual muhitni o'chirish (deactivate)

Ishni tugatgandan keyin virtual muhitdan chiqish uchun:

```
deactivate
```

Terminal boshidagi `(.venv)` yozuvi yo'qoladi.

---

## 6. VS Code da virtual muhitni tanlash

VS Code avtomatik ravishda virtual muhitni topa olmasligi mumkin.
Qo'lda tanlash uchun:

1. `Ctrl + Shift + P` tugmalarini bosing
2. `Python: Select Interpreter` deb yozing va tanlang
3. Ro'yxatdan `.\.venv\Scripts\python.exe` ni tanlang

Shundan keyin VS Code shu virtual muhitdagi Python va kutubxonalarni ishlatadi.
Import qilingan kutubxonalar ostidagi sariq chiziqlar ham yo'qoladi.

---

## 7. .gitignore ga qo'shish

Virtual muhit papkasini git ga yuklash shart emas,
chunki u juda katta va har kim o'zi yaratishi mumkin.

`.gitignore` fayliga quyidagini qo'shing:

```
.venv/
```

---

## 8. Xulosa

Virtual muhit bilan ishlash tartibi quyidagicha:

```
# 1. Loyiha papkasiga kiring
cd d:\Desktop\ToDoApp

# 2. Virtual muhit yarating (faqat bir marta)
python -m venv .venv

# 3. Har safar ishga tushirishdan oldin faollashtiring
.venv\Scripts\activate

# 4. Kerakli kutubxonalarni o'rnating (faqat bir marta)
pip install aiogram python-dotenv

# 5. Kutubxonalar ro'yxatini saqlang
pip freeze > requirements.txt

# 6. Botni ishga tushiring
python run.py

# 7. Ishni tugatgach
deactivate
```

Har bir yangi loyiha uchun alohida virtual muhit yaratish tavsiya etiladi.
Bu professional dasturlash standartlaridan biri hisoblanadi.
