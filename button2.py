from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup



til = ReplyKeyboardMarkup(
	keyboard = [
		[
		KeyboardButton(text="🇺🇿 O'zbekcha"),
		]
	],
	resize_keyboard=True
)

shaharlar = ReplyKeyboardMarkup(
	keyboard = [
		[
		KeyboardButton(text="Toshkent"),
		KeyboardButton(text="Yunsobod"),
		],
		[
		KeyboardButton(text="Chilonzor"),
		KeyboardButton(text="Uch.tepa"),
		],
		[
		KeyboardButton(text="Shoxsaroy"),
		KeyboardButton(text="Olmozor "),
		]
	],
	resize_keyboard=True
)

contact1 = ReplyKeyboardMarkup(
	keyboard = [
		[
		KeyboardButton(text="Mening nomerim",request_contact=True)
		],
	],
		resize_keyboard=True
)



lakatsiya1 = ReplyKeyboardMarkup(
	keyboard = [
		[
		KeyboardButton(text="lokatsiya",request_location=True)
		],
	],
		resize_keyboard=True
)


buyurtma1 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text="Buyurtma",callback_data='buyurtma')
		],
	],
)



menubosilgandagi = InlineKeyboardMarkup(
  inline_keyboard=[
      [
          InlineKeyboardButton("📖 Barcha menyular",url="https://telegra.ph/TASHKENT-EVOS-MENU-02-03"),
          InlineKeyboardButton("🍟🌯🥤 Set", callback_data='set')
      ],
      [
          InlineKeyboardButton("🌯 Lavash", callback_data='lavash'),
          InlineKeyboardButton("Boshqa", callback_data='boshqa')
          
      ],
      [
        InlineKeyboardButton("🥙 Shaurma", callback_data='shaurma'),
          InlineKeyboardButton("🍲 Donar", callback_data='donar'),
          
      ],
      [
        InlineKeyboardButton("🍔 Burger", callback_data='burger'),
          InlineKeyboardButton("🌭 Xot-dog", callback_data='xot-dog'),
         
      ],
      [
        InlineKeyboardButton("🍰 Desertlar", callback_data='desertlar'),
          InlineKeyboardButton("☕️ Ichimliklar", callback_data='ichimliklar'),
      ],
      [
         InlineKeyboardButton("🍟 Gazaklar", callback_data='gazaklar')
      ]

  ]
)


menular = ReplyKeyboardMarkup(
  keyboard = [
    [
    KeyboardButton(text="📍 Manzilni o'zgartirish"),
    KeyboardButton(text="🍴 Menu"),
    ],
    [
    KeyboardButton(text="🛍 Buyurtmalarim"),
    KeyboardButton(text="👪 EVOS Oilasi"),
    ],
    [
    KeyboardButton(text="✍️ Fikr bildirish"),
    KeyboardButton(text="⚙️ Sozlamalar"),
    ],
  ],
  resize_keyboard=True
)
