import logging
import sqlite3

from aiogram import Bot, Dispatcher , executor,types
from config import API_TOKEN
from button import *
from aiogram.types import Message,CallbackQuery

logging.basicConfig(level=logging.INFO)


bot=Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start','help'])
async def send_welcome(message: types.Message):
  await message.reply("Assalomu aleykum",reply_markup=til)

@dp.message_handler(text="🇺🇿 O'zbekcha")
async def menu(message: Message):
  await message.answer("""<b>Shaharni tanlag</b>""",parse_mode='HTML',reply_markup=shaharlar)


@dp.message_handler(text="Toshkent")
async def menu(message: Message):
  await message.answer("""<b>Telefon raqmingizni yuboring</b>""",parse_mode='HTML',reply_markup=contact1)



@dp.message_handler(text="Yunsobod")
async def menu(message: Message):
  await message.answer("""<b>Telefon raqmingizni yuboring</b>""",parse_mode='HTML',reply_markup=contact1)





@dp.message_handler(text="Chilonzor")
async def menu(message: Message):
  await message.answer("""<b>Telefon raqmingizni yuboring</b>""",parse_mode='HTML',reply_markup=contact1)




@dp.message_handler(text="Shoxsaroy")
async def menu(message: Message):
  await message.answer("""<b>Telefon raqmingizni yuboring</b>""",parse_mode='HTML',reply_markup=contact1)


@dp.message_handler(text="Uch.tepa")
async def menu(message: Message):
  await message.answer("""<b>Telefon raqmingizni yuboring</b>""",parse_mode='HTML',reply_markup=contact1)







@dp.message_handler(text="Olmozor")
async def menu(message: Message):
  await message.answer("""<b>Telefon raqmingizni yuboring</b>""",parse_mode='HTML',reply_markup=contact1)





# =========================================================================LAWASH====================================================================






@dp.message_handler(content_types=['contact'])
async def contact(message):
  await message.answer("Manzilni yuborish",reply_markup=buyurtma1)





# ===============================================LAWASHNI BOSGANDA BUTTONNI============================================================================================================



@dp.callback_query_handler(text="lavash")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer("Quydagilardan birini tanlang")
  await call.message.answer("""<b>Kategoriyalardan birini tanlang</b><a href="https://telegra.ph/EVOS-MENU-04-05-2">.</a>""",parse_mode='HTML',reply_markup=lawashdagi)
  

@dp.callback_query_handler(text="ortga20")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer("Quydagilardan birini tanlang")
  await call.message.answer("""<b>Kategoriyalardan birini tanlang</b><a href="https://telegra.ph/EVOS-MENU-04-05-2">.</a>""",parse_mode='HTML',reply_markup=menubosilgandagi)

# =========================================BUYURTMANI BOSGANDAGI BUTTRONI===================================================================================


@dp.callback_query_handler(text="buyurtma")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer("Quydagilardan birini tanlang",reply_markup=menular,parse_mode="HTML")
  await call.message.answer("""<b>Kategoriyalardan birini tanlang</b><a href="https://telegra.ph/EVOS-MENU-04-05-2">.</a>""",parse_mode='HTML',reply_markup=menubosilgandagi)
  
 # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////





@dp.callback_query_handler(text="tovuqli")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer("Quydagilardan birini tanlang")
  await call.message.answer("""<b>Kategoriyalardan birini tanlang</b><a href="https://telegra.ph/EVOS-MENU-04-05-2">.</a>""",parse_mode='HTML',reply_markup=goshtli)
  





@dp.callback_query_handler(text="mini15")
async def till_tanlash(call: CallbackQuery):
    await call.message.answer_photo(
    photo=open('foto/lawash_tovuqmini.jpg','rb'),
    caption="""Narxi:   18 000 so'm
Tarkibi: Xamir, tovuq go`sht, chips, pomidor, bodring, sous, mayonez
Miqdorini tanlang yoki kiriting""",reply_markup=gosht1)






@dp.callback_query_handler(text="big15")
async def till_tanlash(call: CallbackQuery):
   await call.message.answer_photo(
    photo=open('foto/lawash_tovuqmini.jpg','rb'),
    caption="""Narxi:   19 000 so'm
Tarkibi: Xamir, tovuq go`sht, chips, pomidor, bodring, sous, mayonez
Miqdorini tanlang yoki kiriting""",reply_markup=gosht1)
 



@dp.callback_query_handler(text="ortga11")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer("Quydagilardan birini tanlang")
  await call.message.answer("""<b>Kategoriyalardan birini tanlang</b><a href="https://telegra.ph/EVOS-MENU-04-05-2">.</a>""",parse_mode='HTML',reply_markup=lawashdagi)



@dp.callback_query_handler(text="ortga123")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer("Quydagilardan birini tanlang")
  await call.message.answer("""<b>Kategoriyalardan birini tanlang</b><a href="https://telegra.ph/EVOS-MENU-04-05-2">.</a>""",parse_mode='HTML',reply_markup=goshtli)



# ///////////////////////////////////////////////////////////////////////////glawash/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////








@dp.callback_query_handler(text="glawash")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer("Quydagilardan birini tanlang")
  await call.message.answer("""<b>Kategoriyalardan birini tanlang</b><a href="https://telegra.ph/EVOS-MENU-04-05-2">.</a>""",parse_mode='HTML',reply_markup=lawash1)





@dp.callback_query_handler(text="mini4")
async def till_tanlash(call: CallbackQuery):
    await call.message.answer_photo(
    photo=open('foto/lawash1.jpg','rb'),
    caption="""Narxi:   19 000 so'm
Tarkibi: Xamir, tovuq go`sht, chips, pomidor, bodring, sous, mayonez
Miqdorini tanlang yoki kiriting""",reply_markup=qurt)






@dp.callback_query_handler(text="big4")
async def till_tanlash(call: CallbackQuery):
   await call.message.answer_photo(
    photo=open('foto/lawash1.jpg','rb'),
    caption="""Narxi:   21 000 so'm
Tarkibi: Xamir, tovuq go`sht, chips, pomidor, bodring, sous, mayonez
Miqdorini tanlang yoki kiriting""",reply_markup=qurt)
 




@dp.callback_query_handler(text="ortga12")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer("Quydagilardan birini tanlang")
  await call.message.answer("""<b>Kategoriyalardan birini tanlang</b><a href="https://telegra.ph/EVOS-MENU-04-05-2">.</a>""",parse_mode='HTML',reply_markup=lawashdagi)



@dp.callback_query_handler(text="ortga100")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer("Quydagilardan birini tanlang")
  await call.message.answer("""<b>Kategoriyalardan birini tanlang</b><a href="https://telegra.ph/EVOS-MENU-04-05-2">.</a>""",parse_mode='HTML',reply_markup=lawash1)


# //////////////////////////////////////////////////////////////////////////////////////////////////////tlovuqpishloq////////////////////////////////////////////////////////////////






@dp.callback_query_handler(text="tovuqli_sovus")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer("Quydagilardan birini tanlang")
  await call.message.answer("""<b>Kategoriyalardan birini tanlang</b><a href="https://telegra.ph/EVOS-MENU-04-05-2">.</a>""",parse_mode='HTML',reply_markup=lawash2)



@dp.callback_query_handler(text="mini5")
async def till_tanlash(call: CallbackQuery):
    await call.message.answer_photo(
    photo=open('foto/lawashpishloq.jpg','rb'),
    caption="""Narxi:   19 000 so'm
Tarkibi: Xamir, tovuq go`sht, chips, pomidor, bodring, sous, mayonez, pishloq
Miqdorini tanlang yoki kiriting""",reply_markup=vip)






@dp.callback_query_handler(text="big5")
async def till_tanlash(call: CallbackQuery):
   await call.message.answer_photo(
    photo=open('foto/lawashpishloq.jpg','rb'),
    caption="""Narxi:   21 000 so'm
Tarkibi: Xamir, tovuq go`sht, chips, pomidor, bodring, sous, mayonez, pishloq
Miqdorini tanlang yoki kiriting""",reply_markup=vip)





@dp.callback_query_handler(text="ortga13")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer("Quydagilardan birini tanlang")
  await call.message.answer("""<b>Kategoriyalardan birini tanlang</b><a href="https://telegra.ph/EVOS-MENU-04-05-2">.</a>""",parse_mode='HTML',reply_markup=lawashdagi)




@dp.callback_query_handler(text="ortga101")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer("Quydagilardan birini tanlang")
  await call.message.answer("""<b>Kategoriyalardan birini tanlang</b><a href="https://telegra.ph/EVOS-MENU-04-05-2">.</a>""",parse_mode='HTML',reply_markup=lawash2)


# /////////////////////////////////////////////////////////////////////////glawashpishloq///////////////////////////////////////////////////////////////////////////////////////////////////////





@dp.callback_query_handler(text="goshtli_pishloqli")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer("Quydagilardan birini tanlang")
  await call.message.answer("""<b>Kategoriyalardan birini tanlang</b><a href="https://telegra.ph/EVOS-MENU-04-05-2">.</a>""",parse_mode='HTML',reply_markup=lawash3)




@dp.callback_query_handler(text="mini6")
async def till_tanlash(call: CallbackQuery):
    await call.message.answer_photo(
    photo=open('foto/lawashgpishloq.jpg','rb'),
    caption="""Narxi:   19 000 so'm
Tarkibi: Xamir, tovuq go`sht, chips, pomidor, bodring, sous, mayonez, pishloq
Miqdorini tanlang yoki kiriting""",reply_markup=brand)






@dp.callback_query_handler(text="big6")
async def till_tanlash(call: CallbackQuery):
   await call.message.answer_photo(
    photo=open('foto/lawashgpishloq.jpg','rb'),
    caption="""Narxi:   21 000 so'm
Tarkibi: Xamir, tovuq go`sht, chips, pomidor, bodring, sous, mayonez, pishloq
Miqdorini tanlang yoki kiriting""",reply_markup=brand)



@dp.callback_query_handler(text="ortga14")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer("Quydagilardan birini tanlang")
  await call.message.answer("""<b>Kategoriyalardan birini tanlang</b><a href="https://telegra.ph/EVOS-MENU-04-05-2">.</a>""",parse_mode='HTML',reply_markup=lawashdagi)


@dp.callback_query_handler(text="ortga110")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer("Quydagilardan birini tanlang")
  await call.message.answer("""<b>Kategoriyalardan birini tanlang</b><a href="https://telegra.ph/EVOS-MENU-04-05-2">.</a>""",parse_mode='HTML',reply_markup=lawash3)













# =========================================================================SHOURMA========================================================================================================


@dp.callback_query_handler(text="shaurma")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer("Quydagilardan birini tanlang")
  await call.message.answer("""<b>Kategoriyalardan birini tanlang</b><a href="https://telegra.ph/EVOS-MENU-04-05-2">.</a>""",parse_mode='HTML',reply_markup=gosht2)

# ==========================GOSHTLI SHAURMA============================================================================================================================================


@dp.callback_query_handler(text="goshtli")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer("Nechta olasiz ",reply_markup=menular,parse_mode="HTML")
  await call.message.answer("""<b>Kategoriyalardan birini tanlang</b><a href="https://telegra.ph/EVOS-MENU-04-05-2">.</a>""",parse_mode='HTML',reply_markup=gosht3)


@dp.callback_query_handler(text="classik")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer_photo(
    photo=open('foto/shaurmaclassik.jpg','rb'),
    caption="""Narxi:   17 000 so'm
Tarkibi: Xamir, go`sht, chips, pomidor, bodring, sous
Miqdorini tanlang yoki kiriting""",reply_markup=real)
  await call.message.delete()




@dp.callback_query_handler(text="katta")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer_photo(
    photo=open('foto/shaurmaclassik.jpg','rb'),
    caption="""Narxi:   21 000 so'm
Tarkibi: Xamir, go`sht, chips, pomidor, bodring, sous
Miqdorini tanlang yoki kiriting""",reply_markup=real)
  await call.message.delete()



@dp.callback_query_handler(text="ortga9")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer("Quydagilardan birini tanlang")
  await call.message.answer("""<b>Kategoriyalardan birini tanlang</b><a href="https://telegra.ph/EVOS-MENU-04-05-2">.</a>""",parse_mode='HTML',reply_markup=gosht2)




@dp.callback_query_handler(text="ortga102")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer("Quydagilardan birini tanlang")
  await call.message.answer("""<b>Kategoriyalardan birini tanlang</b><a href="https://telegra.ph/EVOS-MENU-04-05-2">.</a>""",parse_mode='HTML',reply_markup=gosht3)
  
  
# =========================ACHIQ SHAURMA===============================================================================================================================================================================


@dp.callback_query_handler(text="achiq")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer("Nechta olasiz ",reply_markup=menular,parse_mode="HTML")
  await call.message.answer("""<b>Kategoriyalardan birini tanlang</b><a href="https://telegra.ph/EVOS-MENU-04-05-2">.</a>""",parse_mode='HTML',reply_markup=qoshq)

@dp.callback_query_handler(text="classik1")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer_photo(
    photo=open('foto/shourmaachiq.jpg','rb'),
    caption="""Narxi:   17 000 so'm
Tarkibi: Xamir, go`sht, chips, pomidor, bodring, sous
Miqdorini tanlang yoki kiriting""",reply_markup=city)
  await call.message.delete()




@dp.callback_query_handler(text="katta1")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer_photo(
    photo=open('foto/shourmaachiq.jpg','rb'),
    caption="""Narxi:   21 000 so'm
Tarkibi: Xamir, go`sht, chips, pomidor, bodring, sous
Miqdorini tanlang yoki kiriting""",reply_markup=city)
  await call.message.delete()



@dp.callback_query_handler(text="ortga09")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer("Quydagilardan birini tanlang",reply_markup=menular,parse_mode="HTML")
  await call.message.answer("""<b>Kategoriyalardan birini tanlang</b><a href="https://telegra.ph/EVOS-MENU-04-05-2">.</a>""",parse_mode='HTML',reply_markup=gosht2)


@dp.callback_query_handler(text="ortga103")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer("Quydagilardan birini tanlang",reply_markup=menular,parse_mode="HTML")
  await call.message.answer("""<b>Kategoriyalardan birini tanlang</b><a href="https://telegra.ph/EVOS-MENU-04-05-2">.</a>""",parse_mode='HTML',reply_markup=qoshq)
  

@dp.callback_query_handler(text="ortga90")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer("Quydagilardan birini tanlang",reply_markup=menular,parse_mode="HTML")
  await call.message.answer("""<b>Kategoriyalardan birini tanlang</b><a href="https://telegra.ph/EVOS-MENU-04-05-2">.</a>""",parse_mode='HTML',reply_markup=menubosilgandagi)


# =======================================================================================================================================================================
                                                    # gamburger


@dp.callback_query_handler(text="burger")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer("Quydagilardan birini tanlang")
  await call.message.answer("""<b>Kategoriyalardan birini tanlang</b><a href="https://telegra.ph/EVOS-MENU-04-05-2">.</a>""",parse_mode='HTML',reply_markup=gosht5)


@dp.callback_query_handler(text="ortga105")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer("Quydagilardan birini tanlang",reply_markup=menular,parse_mode="HTML")
  await call.message.answer("""<b>Kategoriyalardan birini tanlang</b><a href="https://telegra.ph/EVOS-MENU-04-05-2">.</a>""",parse_mode='HTML',reply_markup=menubosilgandagi)

# ================================================PISHLOQNI B OSGANDA====================================================================================================

@dp.callback_query_handler(text="pishloq")
async def till_tanlash(call: CallbackQuery):
   await call.message.answer_photo(
    photo=open('foto/gamburger.jpg','rb'),
    caption="""Narxi:   21 000 so'm
Tarkibi: Xamir, go`sht, chips, pomidor, bodring, sous
Miqdorini tanlang yoki kiriting""",reply_markup=gosht4)




@dp.callback_query_handler(text="goshti")
async def till_tanlash(call: CallbackQuery):
   await call.message.answer_photo(
    photo=open('foto/dablburger.jpg','rb'),
    caption="""Narxi:   21 000 so'm
Tarkibi: Xamir, go`sht, chips, pomidor, bodring, sous
Miqdorini tanlang yoki kiriting""",reply_markup=gosht4)



@dp.callback_query_handler(text="ortga8")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer("Quydagilardan birini tanlang",reply_markup=menular,parse_mode="HTML")
  await call.message.answer("""<b>Kategoriyalardan birini tanlang</b><a href="https://telegra.ph/EVOS-MENU-04-05-2">.</a>""",parse_mode='HTML',reply_markup=gosht5)




# ==============================================================================================================================================================================================
                                                    
                                           # disert


@dp.callback_query_handler(text="desertlar")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer("Quydagilardan birini tanlang")
  await call.message.answer("""<b>Kategoriyalardan birini tanlang</b><a href="https://telegra.ph/EVOS-MENU-04-05-2">.</a>""",parse_mode='HTML',reply_markup=gosht6)

# ===================================================================asalim===================================================================================================================



@dp.callback_query_handler(text="asalim")
async def till_tanlash(call: CallbackQuery):
 await call.message.answer_photo(
    photo=open('foto/Asalim.jpg','rb'),
    caption="""Narxi:   15 000 so'm
Tarkibi: Молоко, мука, сахар, масло слив., яйцо кур., мед-соты, мед
Miqdorini tanlang yoki kiriting""",reply_markup=gosht7)

# ====================================================================chizkeyk===============================================================================================================================


@dp.callback_query_handler(text="chizkeyk")
async def till_tanlash(call: CallbackQuery):
 await call.message.answer_photo(
    photo=open('foto/chizkeyk.jpg','rb'),
    caption="""Narxi:   14 000 so'm
Tarkibi: Сахар, сливки, сыр слив., яйцо кур., ванилин евро, мука, желатин кур., миндаль, масло слив.
Miqdorini tanlang yoki kiriting""",reply_markup=gosht7)


# ==============================================================================choco============================================================================================================================



@dp.callback_query_handler(text="choco")
async def till_tanlash(call: CallbackQuery):
 await call.message.answer_photo(
    photo=open('foto/choco.jpg','rb'),
    caption="""Narxi:   14 000 so'm
Miqdorini tanlang yoki kiriting""",reply_markup=gosht7)

# =============================================================================asalik chizkeyk chocni bosganda dagi ortga=========================================================================================

@dp.callback_query_handler(text="ortga01")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer("Quydagilardan birini tanlang",reply_markup=menular,parse_mode="HTML")
  await call.message.answer("""<b>Kategoriyalardan birini tanlang</b><a href="https://telegra.ph/EVOS-MENU-04-05-2">.</a>""",parse_mode='HTML',reply_markup=menubosilgandagi)

# ======================================================sonlardagi mini klassikga qaytadigan ortga========================================================================================================================

@dp.callback_query_handler(text="ortga7")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer("Quydagilardan birini tanlang",reply_markup=menular,parse_mode="HTML")
  await call.message.answer("""<b>Kategoriyalardan birini tanlang</b><a href="https://telegra.ph/EVOS-MENU-04-05-2">.</a>""",parse_mode='HTML',reply_markup=gosht6)



 # ====================================================================mini============================================================================================================================






# ==========================================================SET================================================================================


@dp.callback_query_handler(text="set")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer("Quydagilardan birini tanlang")
  await call.message.answer("""<em>Kategoriyalardan birini tanlang</em><a href="https://telegra.ph/EVOS-MENU-04-05-2">.</a>""",parse_mode='HTML',reply_markup=gosht8)


# <em>Hi there!</em>



@dp.callback_query_handler(text="combo")
async def till_tanlash(call: CallbackQuery):
   await call.message.answer_photo(
    photo=open('foto/combo+.jpg','rb'),
    caption="""Narxi:   14 000 so'm
Miqdorini tanlang yoki kiriting""",reply_markup=gosht9)




@dp.callback_query_handler(text="ortga6")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer("test")
  await call.message.answer("""<b>Kategoriyalardan birini tanlang</b><a href="https://telegra.ph/EVOS-MENU-04-05-2">.</a>""",parse_mode='HTML',reply_markup=gosht8)

@dp.callback_query_handler(text="ortga80")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer("test")
  await call.message.answer("""<b>Kategoriyalardan birini tanlang</b><a href="https://telegra.ph/EVOS-MENU-04-05-2">.</a>""",parse_mode='HTML',reply_markup=menubosilgandagi)

# =====================================================================BOSHQA=================================================================



@dp.callback_query_handler(text="boshqa")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer_photo(
    photo=open('foto/boshqa.jpg','rb'),
    caption="""Narxi:  300 so'm
Miqdorini tanlang yoki kiriting""",reply_markup=gosht10)



@dp.callback_query_handler(text="ortga5")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer("test")
  await call.message.answer("""<b>Kategoriyalardan birini tanlang</b><a href="https://telegra.ph/EVOS-MENU-04-05-2">.</a>""",parse_mode='HTML',reply_markup=menubosilgandagi)

# =================================================DONAR================================================================================================================




@dp.callback_query_handler(text="donar")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer("test")
  await call.message.answer("""<b>Kategoriyalardan birini tanlang</b><a href="https://telegra.ph/EVOS-MENU-04-05-2">.</a>""",parse_mode='HTML',reply_markup=gosht11)




@dp.callback_query_handler(text="gosht0")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer_photo(
    photo=open('foto/danargoshtli.jpg','rb'),
    caption="""Narxi:  36 000 so'm
Tarkibi: Mol yoki tovuq go`shti, Kartoshka fri, Guruch, Maxsus sous, Karam salat, Bodring, Piyoz, Sabzi, Ko`katlar
Miqdorini tanlang yoki kiriting""",reply_markup=gosht12)

@dp.callback_query_handler(text="goshtt")
async def till_tanlash(call: CallbackQuery):
   await call.message.answer_photo(
    photo=open('foto/danartovuq.jpg','rb'),
    caption="""Narxi:  36 000 so'm
Tarkibi: Mol yoki tovuq go`shti, Kartoshka fri, Guruch, Maxsus sous, Karam salat, Bodring, Piyoz, Sabzi, Ko`katlar
Miqdorini tanlang yoki kiriting""",reply_markup=gosht12)


@dp.callback_query_handler(text="ortga4")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer("test")
  await call.message.answer("""<b>Kategoriyalardan birini tanlang</b><a href="https://telegra.ph/EVOS-MENU-04-05-2">.</a>""",parse_mode='HTML',reply_markup=gosht11)



@dp.callback_query_handler(text="ortga70")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer("test")
  await call.message.answer("""<b>Kategoriyalardan birini tanlang</b><a href="https://telegra.ph/EVOS-MENU-04-05-2">.</a>""",parse_mode='HTML',reply_markup=menubosilgandagi)


# ==============================================XOT-DOG==================================================================================================================================



@dp.callback_query_handler(text="xot-dog")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer("test")
  await call.message.answer("""<b>Kategoriyalardan birini tanlang</b><a href="https://telegra.ph/EVOS-MENU-04-05-2">.</a>""",parse_mode='HTML',reply_markup=gosht13)







@dp.callback_query_handler(text="prastoy")
async def till_tanlash(call: CallbackQuery):
   await call.message.answer_photo(
    photo=open('foto/oddiy.jpg','rb'),
    caption="""Narxi:  11 000 so'm
Tarkibi: Kunjutli bulochka, Sosiska, Tuzlangan bodring, Pomidor, Ketchup, Mayonez, 
Miqdorini tanlang yoki kiriting""",reply_markup=gosht14)



@dp.callback_query_handler(text="shonona")
async def till_tanlash(call: CallbackQuery):
   await call.message.answer_photo(
    photo=open('foto/shohona.jpg','rb'),
    caption="""Narxi:  16 000 so'm
Tarkibi: Kunjutli bulochka, Sosiska, Tuzlangan bodring, Pomidor, Ketchup, Mayonez, 
Miqdorini tanlang yoki kiriting""",reply_markup=gosht14)


@dp.callback_query_handler(text="klassik")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer_photo(
    photo=open('foto/klassikxot.jpg','rb'),
    caption="""Narxi:  16 000 so'm
Tarkibi: Kunjutli bulochka, Sosiska, Tuzlangan bodring, Pomidor, Ketchup, Mayonez, 
Miqdorini tanlang yoki kiriting""",reply_markup=gosht14)






@dp.callback_query_handler(text="ortga3")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer("test")
  await call.message.answer("""<b>Kategoriyalardan birini tanlang</b><a href="https://telegra.ph/EVOS-MENU-04-05-2">.</a>""",parse_mode='HTML',reply_markup=gosht13)




@dp.callback_query_handler(text="ortga04")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer("test")
  await call.message.answer("""<b>Kategoriyalardan birini tanlang</b><a href="https://telegra.ph/EVOS-MENU-04-05-2">.</a>""",parse_mode='HTML',reply_markup=menubosilgandagi)






# ======================================================================ICHIMLIK===============================================================================================






@dp.callback_query_handler(text="ichimliklar")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer("Quydagilardan birini tanalang")
  await call.message.answer("""<b>Kategoriyalardan birini tanlang</b><a href="https://telegra.ph/EVOS-MENU-04-05-2">.</a>""",parse_mode='HTML',reply_markup=gosht15)


@dp.callback_query_handler(text="ortga300")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer("Quydagilardan birini tanalang")
  await call.message.answer("""<b>Kategoriyalardan birini tanlang</b><a href="https://telegra.ph/EVOS-MENU-04-05-2">.</a>""",parse_mode='HTML',reply_markup=menubosilgandagi)




@dp.callback_query_handler(text="suv")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer_photo(
    photo=open('foto/suv.jpg','rb'),
    caption="""Narxi:  2 000 so'm
Tarkibi: 0,5 
Miqdorini tanlang yoki kiriting""",reply_markup=gosht16)







@dp.callback_query_handler(text="pepsi")
async def till_tanlash(call: CallbackQuery):
   await call.message.answer_photo(
    photo=open('foto/pepsi.jpg','rb'),
    caption="""Narxi:  12 000 so'm
Tarkibi: 1,5 
Miqdorini tanlang yoki kiriting""",reply_markup=gosht16)





@dp.callback_query_handler(text="ichimlik")
async def till_tanlash(call: CallbackQuery):
   await call.message.answer_photo(
    photo=open('foto/kofe.jpg','rb'),
    caption="""Coffe \nNarxi:  7 000 so'm
Tarkibi: 0,4
Miqdorini tanlang yoki kiriting""",reply_markup=gosht16)



@dp.callback_query_handler(text="ortga2")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer("test")
  await call.message.answer("""<b>Kategoriyalardan birini tanlang</b><a href="https://telegra.ph/EVOS-MENU-04-05-2">.</a>""",parse_mode='HTML',reply_markup=gosht15)





# ===========================================================================GAZAKLAR=======================================================================================================







@dp.callback_query_handler(text="gazaklar")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer("test gazak")
  await call.message.answer("""<b>Kategoriyalardan birini tanlang</b><a href="https://telegra.ph/EVOS-MENU-04-05-2">.</a>""",parse_mode='HTML',reply_markup=gosht17)


@dp.callback_query_handler(text="ortga500")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer("test gazak")
  await call.message.answer("""<b>Kategoriyalardan birini tanlang</b><a href="https://telegra.ph/EVOS-MENU-04-05-2">.</a>""",parse_mode='HTML',reply_markup=menubosilgandagi)





@dp.callback_query_handler(text="fri")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer_photo(
    photo=open('foto/fri.jpg','rb'),
    caption="""Narxi:  10 000 so'm
Tarkibi: Karto'shka
Miqdorini tanlang yoki kiriting""",reply_markup=gosht18)







@dp.callback_query_handler(text="kartoshka")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer_photo(
    photo=open('foto/qkartoshka.jpg','rb'),
    caption="""Narxi:  11 000 so'm
Tarkibi: Karto'shka
Miqdorini tanlang yoki kiriting""",reply_markup=gosht18)





@dp.callback_query_handler(text="salat")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer_photo(
    photo=open('foto/salat.jpg','rb'),
    caption="""Narxi:  9 000 so'm
Tarkibi: Qizil karam, Ziravorlar, Bodring, Ko`katlar, Limon sok
Miqdorini tanlang yoki kiriting""",reply_markup=gosht18)



@dp.callback_query_handler(text="sous")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer_photo(
    photo=open('foto/kechup.jpg','rb'),
    caption="""Narxi:  9 000 so'm
Tarkibi: TOMAT
Miqdorini tanlang yoki kiriting""",reply_markup=gosht18)





@dp.callback_query_handler(text="guruch")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer_photo(
    photo=open('foto/guruch.jpg','rb'),
    caption="""Narxi:  6 000 so'm
Tarkibi: guruch
Miqdorini tanlang yoki kiriting""",reply_markup=gosht18)


@dp.callback_query_handler(text="ortga1")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer("test")
  await call.message.answer("""<b>Kategoriyalardan birini tanlang</b><a href="https://telegra.ph/EVOS-MENU-04-05-2">.</a>""",parse_mode='HTML',reply_markup=gosht17)

# ===============================================================================================================================================================================





@dp.callback_query_handler(text="Menu")
async def till_tanlash(call: CallbackQuery):
  await call.message.answer("test")
  await call.message.answer("""<b>Kategoriyalardan birini tanlang</b><a href="https://telegra.ph/EVOS-MENU-04-05-2">.</a>""",parse_mode='HTML',reply_markup=menular)

































if __name__ == '__main__':
  executor.start_polling(dp,skip_updates=True)



