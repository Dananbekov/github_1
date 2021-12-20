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


# ===================================================================LAWASH===================================================================

lawashdagi = InlineKeyboardMarkup(
  inline_keyboard=[
      [	

				InlineKeyboardButton('Tovuqli lawash', callback_data='tovuqli'),
				InlineKeyboardButton('Goshtli lawash', callback_data='glawash')			

      ],
      [
        InlineKeyboardButton("Tovuqli lawash_pishloq bilan", callback_data='tovuqli_sovus'),
				InlineKeyboardButton(" Goshtli lawash_pishloq bilan", callback_data='goshtli_pishloqli'),
      
        InlineKeyboardButton("Ortga", callback_data='ortga20')
          
      ],
    
  ]
)

# ==============================================mini klassik=====================================================================================================

goshtli = InlineKeyboardMarkup(
  inline_keyboard=[
      [	

				InlineKeyboardButton('Mini lawash', callback_data='mini15'),
				  InlineKeyboardButton("Classik lawash", callback_data='big15'),
			],
			[

				InlineKeyboardButton("Ortga", callback_data='ortga11')
			],
  ]
)

gosht1 = InlineKeyboardMarkup(
  inline_keyboard=[
      [	

				InlineKeyboardButton('1', callback_data='bir'),
				InlineKeyboardButton("2", callback_data='ikki'),
				InlineKeyboardButton("3", callback_data='uch'),
			],
			[
				InlineKeyboardButton("4", callback_data='tort'),
				InlineKeyboardButton("5", callback_data='besh'),
				InlineKeyboardButton("6", callback_data='olti'),
			],
			[
				InlineKeyboardButton("7", callback_data='yeti'),
				InlineKeyboardButton("8", callback_data='sakiz'),
				InlineKeyboardButton("9", callback_data='toqiz'),
			],
			[
        
				InlineKeyboardButton("Ortga", callback_data='ortga123')
			],
  ]
)

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

lawash1 = InlineKeyboardMarkup(
  inline_keyboard=[
      [	

				InlineKeyboardButton('Mini lawash', callback_data='mini4'),
				  InlineKeyboardButton("Classik lawash", callback_data='big4'),
			],
			[

				InlineKeyboardButton("Ortga", callback_data='ortga12')
			],
  ]
)


qurt = InlineKeyboardMarkup(
  inline_keyboard=[
      [	

				InlineKeyboardButton('1', callback_data='bir'),
				InlineKeyboardButton("2", callback_data='ikki'),
				InlineKeyboardButton("3", callback_data='uch'),
			],
			[
				InlineKeyboardButton("4", callback_data='tort'),
				InlineKeyboardButton("5", callback_data='besh'),
				InlineKeyboardButton("6", callback_data='olti'),
			],
			[
				InlineKeyboardButton("7", callback_data='yeti'),
				InlineKeyboardButton("8", callback_data='sakiz'),
				InlineKeyboardButton("9", callback_data='toqiz'),
			],
			[
        
				InlineKeyboardButton("Ortga", callback_data='ortga100')
			],
  ]
)

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// 





lawash2 = InlineKeyboardMarkup(
  inline_keyboard=[
      [	

				InlineKeyboardButton('Mini lawash', callback_data='mini5'),
				  InlineKeyboardButton("Classik lawash", callback_data='big5'),
			],
			[

				InlineKeyboardButton("Ortga", callback_data='ortga13')
			],
  ]
)



vip = InlineKeyboardMarkup(
  inline_keyboard=[
      [	

				InlineKeyboardButton('1', callback_data='bir'),
				InlineKeyboardButton("2", callback_data='ikki'),
				InlineKeyboardButton("3", callback_data='uch'),
			],
			[
				InlineKeyboardButton("4", callback_data='tort'),
				InlineKeyboardButton("5", callback_data='besh'),
				InlineKeyboardButton("6", callback_data='olti'),
			],
			[
				InlineKeyboardButton("7", callback_data='yeti'),
				InlineKeyboardButton("8", callback_data='sakiz'),
				InlineKeyboardButton("9", callback_data='toqiz'),
			],
			[
        
				InlineKeyboardButton("Ortga", callback_data='ortga101')
			],
  ]
)



# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



lawash3 = InlineKeyboardMarkup(
  inline_keyboard=[
      [	

				InlineKeyboardButton('Mini lawash', callback_data='mini6'),
				  InlineKeyboardButton("Classik lawash", callback_data='big6'),
			],
			[

				InlineKeyboardButton("Ortga", callback_data='ortga14')
			],
  ]
)





brand = InlineKeyboardMarkup(
  inline_keyboard=[
      [	

				InlineKeyboardButton('1', callback_data='bir'),
				InlineKeyboardButton("2", callback_data='ikki'),
				InlineKeyboardButton("3", callback_data='uch'),
			],
			[
				InlineKeyboardButton("4", callback_data='tort'),
				InlineKeyboardButton("5", callback_data='besh'),
				InlineKeyboardButton("6", callback_data='olti'),
			],
			[
				InlineKeyboardButton("7", callback_data='yeti'),
				InlineKeyboardButton("8", callback_data='sakiz'),
				InlineKeyboardButton("9", callback_data='toqiz'),
			],
			[
        
				InlineKeyboardButton("Ortga", callback_data='ortga110')
			],
  ]
)




# =================================================SHAURMA================================================================================================







gosht2 = InlineKeyboardMarkup(
  inline_keyboard=[
      [	
				InlineKeyboardButton('Shaurma goshtli', callback_data='goshtli'),
     		InlineKeyboardButton("Shayrma achiq", callback_data='achiq'),

      ],
      [
				InlineKeyboardButton("Ortga", callback_data='ortga90')
			
      ],
      
  ]
)




shourma2 = InlineKeyboardMarkup(
  inline_keyboard=[
      [	

				InlineKeyboardButton('1', callback_data='bir'),
				InlineKeyboardButton("2", callback_data='ikki'),
				InlineKeyboardButton("3", callback_data='uch'),
			],
			[
				InlineKeyboardButton("4", callback_data='tort'),
				InlineKeyboardButton("5", callback_data='besh'),
				InlineKeyboardButton("6", callback_data='olti'),
			],
			[
				InlineKeyboardButton("7", callback_data='yeti'),
				InlineKeyboardButton("8", callback_data='sakiz'),
				InlineKeyboardButton("9", callback_data='toqiz'),
			],
			[
        
				InlineKeyboardButton("Ortga", callback_data='ortga9')
			],
  ]
)

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

gosht3 = InlineKeyboardMarkup(
  inline_keyboard=[
      [	
      	InlineKeyboardButton('Classik', callback_data='classik'),
				  InlineKeyboardButton("Katta", callback_data='katta'),
			],
			[	
				InlineKeyboardButton("Ortga", callback_data='ortga9')
			

      ],
  ]
)

real = InlineKeyboardMarkup(
  inline_keyboard=[
      [	

				InlineKeyboardButton('1', callback_data='bir'),
				InlineKeyboardButton("2", callback_data='ikki'),
				InlineKeyboardButton("3", callback_data='uch'),
			],
			[
				InlineKeyboardButton("4", callback_data='tort'),
				InlineKeyboardButton("5", callback_data='besh'),
				InlineKeyboardButton("6", callback_data='olti'),
			],
			[
				InlineKeyboardButton("7", callback_data='yeti'),
				InlineKeyboardButton("8", callback_data='sakiz'),
				InlineKeyboardButton("9", callback_data='toqiz'),
			],
			[
        
				InlineKeyboardButton("Ortga", callback_data='ortga102')
			],
  ]
)

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


qoshq = InlineKeyboardMarkup(
  inline_keyboard=[
      [	
      	InlineKeyboardButton('Classik', callback_data='classik1'),
				InlineKeyboardButton("Katta", callback_data='katta1'),
			],
			[	
				InlineKeyboardButton("Ortga", callback_data='ortga09')
			

      ],
  ]
)

city = InlineKeyboardMarkup(
  inline_keyboard=[
      [	

				InlineKeyboardButton('1', callback_data='bir'),
				InlineKeyboardButton("2", callback_data='ikki'),
				InlineKeyboardButton("3", callback_data='uch'),
			],
			[
				InlineKeyboardButton("4", callback_data='tort'),
				InlineKeyboardButton("5", callback_data='besh'),
				InlineKeyboardButton("6", callback_data='olti'),
			],
			[
				InlineKeyboardButton("7", callback_data='yeti'),
				InlineKeyboardButton("8", callback_data='sakiz'),
				InlineKeyboardButton("9", callback_data='toqiz'),
			],
			[
        
				InlineKeyboardButton("Ortga", callback_data='ortga103')
			],
  ]
)




















# ==================================================BURGER================================================================================================


gosht4 = InlineKeyboardMarkup(
  inline_keyboard=[
      [	

				InlineKeyboardButton('1', callback_data='bir'),
				InlineKeyboardButton("2", callback_data='ikki'),
				InlineKeyboardButton("3", callback_data='uch'),
			],
			[
				InlineKeyboardButton("4", callback_data='tort'),
				InlineKeyboardButton("5", callback_data='besh'),
				InlineKeyboardButton("6", callback_data='olti'),
			],
			[
				InlineKeyboardButton("7", callback_data='yeti'),
				InlineKeyboardButton("8", callback_data='sakiz'),
				InlineKeyboardButton("9", callback_data='toqiz'),
			],
			[
        
				InlineKeyboardButton("Ortga", callback_data='ortga8')
			],
  ]
)













gosht5 = InlineKeyboardMarkup(
  inline_keyboard=[
      [	

				InlineKeyboardButton('Burger gosht', callback_data='pishloq'),
				  InlineKeyboardButton("Даблбургер", callback_data='goshti'),

				InlineKeyboardButton("Ortga", callback_data='ortga105'),
			

      ],
  ]
)




goshit = InlineKeyboardMarkup(
  inline_keyboard=[
      [	

				InlineKeyboardButton('Mini', callback_data='mini7'),
				  InlineKeyboardButton("Classik ", callback_data='big7'),
			],
			[

				InlineKeyboardButton("Ortga", callback_data='ortga11')
			],
  ]
)




goshit1 = InlineKeyboardMarkup(
  inline_keyboard=[
      [	

				InlineKeyboardButton('Mini', callback_data='mini7'),
				  InlineKeyboardButton("Classik ", callback_data='big7'),
			],
			[

				InlineKeyboardButton("Ortga", callback_data='ortga15')
			],
  ]
)







# ====================================DISERT===========================================









gosht6 = InlineKeyboardMarkup(
  inline_keyboard=[
      [	

				InlineKeyboardButton('Asalim', callback_data='asalim'),
				  
				InlineKeyboardButton("Чизкейк", callback_data='chizkeyk'),
				
				InlineKeyboardButton("Choco", callback_data='choco'),
      ],
      [
				InlineKeyboardButton("Ortga", callback_data='ortga01')
			

      ],
  ]
)





gosht7 = InlineKeyboardMarkup(
  inline_keyboard=[
      [	

				InlineKeyboardButton('1', callback_data='bir'),
				InlineKeyboardButton("2", callback_data='ikki'),
				InlineKeyboardButton("3", callback_data='uch'),
			],
			[
				InlineKeyboardButton("4", callback_data='tort'),
				InlineKeyboardButton("5", callback_data='besh'),
				InlineKeyboardButton("6", callback_data='olti'),
			],
			[
				InlineKeyboardButton("7", callback_data='yeti'),
				InlineKeyboardButton("8", callback_data='sakiz'),
				InlineKeyboardButton("9", callback_data='toqiz'),
			],
			[
        
				InlineKeyboardButton("Ortga", callback_data='ortga7')
			],
  ]
)




# ==========================================================SET===============================================================


gosht8 = InlineKeyboardMarkup(
  inline_keyboard=[
      [	
       
			 InlineKeyboardButton('COMBO+', callback_data='combo'),
      ],
      [
				InlineKeyboardButton("Ortga", callback_data='ortga80')
			

      ],
  ]
)





gosht9 = InlineKeyboardMarkup(
  inline_keyboard=[
      [	

				InlineKeyboardButton('1', callback_data='bir'),
				InlineKeyboardButton("2", callback_data='ikki'),
				InlineKeyboardButton("3", callback_data='uch'),
			],
			[
				InlineKeyboardButton("4", callback_data='tort'),
				InlineKeyboardButton("5", callback_data='besh'),
				InlineKeyboardButton("6", callback_data='olti'),
			],
			[
				InlineKeyboardButton("7", callback_data='yeti'),
				InlineKeyboardButton("8", callback_data='sakiz'),
				InlineKeyboardButton("9", callback_data='toqiz'),
			],
			[
        
				InlineKeyboardButton("Ortga", callback_data='ortga6')
			],
  ]
)



# ========================================================BOSHQA==================================================================================================

gosht10 = InlineKeyboardMarkup(
  inline_keyboard=[
      [	

				InlineKeyboardButton('1', callback_data='bir'),
				InlineKeyboardButton("2", callback_data='ikki'),
				InlineKeyboardButton("3", callback_data='uch'),
			],
			[
				InlineKeyboardButton("4", callback_data='tort'),
				InlineKeyboardButton("5", callback_data='besh'),
				InlineKeyboardButton("6", callback_data='olti'),
			],
			[
				InlineKeyboardButton("7", callback_data='yeti'),
				InlineKeyboardButton("8", callback_data='sakiz'),
				InlineKeyboardButton("9", callback_data='toqiz'),
			],
			[
        
				InlineKeyboardButton("Ortga", callback_data='ortga5')
			],
  ]

)



# =====================================DONAR========================================================================


gosht11 = InlineKeyboardMarkup(
  inline_keyboard=[
      [	
       
			 InlineKeyboardButton("Go'shtli", callback_data='gosht0'),
			  InlineKeyboardButton("Tovuqli", callback_data='goshtt'),
      ],
      [
				InlineKeyboardButton("Ortga", callback_data='ortga70')
			

      ],
  ]
)



gosht12 = InlineKeyboardMarkup(
  inline_keyboard=[
      [	

				InlineKeyboardButton('1', callback_data='bir'),
				InlineKeyboardButton("2", callback_data='ikki'),
				InlineKeyboardButton("3", callback_data='uch'),
			],
			[
				InlineKeyboardButton("4", callback_data='tort'),
				InlineKeyboardButton("5", callback_data='besh'),
				InlineKeyboardButton("6", callback_data='olti'),
			],
			[
				InlineKeyboardButton("7", callback_data='yeti'),
				InlineKeyboardButton("8", callback_data='sakiz'),
				InlineKeyboardButton("9", callback_data='toqiz'),
			],
			[
        
				InlineKeyboardButton("Ortga", callback_data='ortga4')
			],
  ]

)


# ===================================================XOT-DOG=========================================================================================


gosht13 = InlineKeyboardMarkup(
  inline_keyboard=[
      [	

				InlineKeyboardButton('Classik xotdog', callback_data='klassik'),
				  
				InlineKeyboardButton("Oddiy", callback_data='prastoy'),
				
				InlineKeyboardButton("Shohona", callback_data='shonona'),
      ],
      [
				InlineKeyboardButton("Ortga", callback_data='ortga04')
			

      ],
  ]
)




gosht14 = InlineKeyboardMarkup(
  inline_keyboard=[
      [	

				InlineKeyboardButton('1', callback_data='bir'),
				InlineKeyboardButton("2", callback_data='ikki'),
				InlineKeyboardButton("3", callback_data='uch'),
			],
			[
				InlineKeyboardButton("4", callback_data='tort'),
				InlineKeyboardButton("5", callback_data='besh'),
				InlineKeyboardButton("6", callback_data='olti'),
			],
			[
				InlineKeyboardButton("7", callback_data='yeti'),
				InlineKeyboardButton("8", callback_data='sakiz'),
				InlineKeyboardButton("9", callback_data='toqiz'),
			],
			[
        
				InlineKeyboardButton("Ortga", callback_data='ortga3')
			],
  ]

)



# ===========================================================ICHIMLIK=================================================================================



gosht15 = InlineKeyboardMarkup(
  inline_keyboard=[
      [	

				InlineKeyboardButton('Suv', callback_data='suv'),
				  
				InlineKeyboardButton("Pepsi", callback_data='pepsi'),
			],	
			[
				InlineKeyboardButton("Issiq ichimlik", callback_data='ichimlik'),

      ],
      [
				InlineKeyboardButton("Ortga", callback_data='ortga300')
			

      ],
  ]
)





gosht16 = InlineKeyboardMarkup(
  inline_keyboard=[
      [	

				InlineKeyboardButton('1', callback_data='bir'),
				InlineKeyboardButton("2", callback_data='ikki'),
				InlineKeyboardButton("3", callback_data='uch'),
			],
			[
				InlineKeyboardButton("4", callback_data='tort'),
				InlineKeyboardButton("5", callback_data='besh'),
				InlineKeyboardButton("6", callback_data='olti'),
			],
			[
				InlineKeyboardButton("7", callback_data='yeti'),
				InlineKeyboardButton("8", callback_data='sakiz'),
				InlineKeyboardButton("9", callback_data='toqiz'),
			],
			[
        
				InlineKeyboardButton("Ortga", callback_data='ortga2')
			],
  ]

)



# ====================================================================GAZAKLAR================================================================================================================




gosht17 = InlineKeyboardMarkup(
  inline_keyboard=[
      [	

				InlineKeyboardButton('Fri', callback_data='fri'),
			 	InlineKeyboardButton("Qish.kartoshkasi", callback_data='kartoshka'),
			],

			[
				InlineKeyboardButton("Salat", callback_data='salat'),
				InlineKeyboardButton("Sous", callback_data='sous'),
			],
      
      [
				InlineKeyboardButton("Guruch", callback_data='guruch'),
      ],
      [
				InlineKeyboardButton("Ortga", callback_data='ortga500')
			

      ],
   ]
)




gosht18 = InlineKeyboardMarkup(
  inline_keyboard=[
      [	

				InlineKeyboardButton('1', callback_data='bir'),
				InlineKeyboardButton("2", callback_data='ikki'),
				InlineKeyboardButton("3", callback_data='uch'),
			],
			[
				InlineKeyboardButton("4", callback_data='tort'),
				InlineKeyboardButton("5", callback_data='besh'),
				InlineKeyboardButton("6", callback_data='olti'),
			],
			[
				InlineKeyboardButton("7", callback_data='yeti'),
				InlineKeyboardButton("8", callback_data='sakiz'),
				InlineKeyboardButton("9", callback_data='toqiz'),
			],
			[
        
				InlineKeyboardButton("Ortga", callback_data='ortga1')
			],
  ]

)


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////




