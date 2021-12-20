# import random
# print("Kompyuterda o'yinchida 3 ochkodan bor")
# a=3
# i=3
# while a>0 and i>0:
#     ran=["tosh","qaychi","qog'oz"]
#     com=random.choice(ran)
#     print(com)
#     play=None
#     while play not in ran:
#         play=input("tosh/qaychi/qog'oz? >>  ")
#     if com==play:
#         yana=input("Yana urinib ko'rasizmi?")
#         if yana!="ha":
#             break
#     elif com=="tosh" and play=="qaychi":
#         a=a-1
#         i=i+1
#         print(f"Men  yutim {a} \t{i}")
#     elif com=="tosh" and play=="qog'oz":
#         a=a+1
#         i=i-1
#         print(f"Siz yutingiz {a} \t{i}")
#     elif com=="qog'oz" and play=="qaychi":
#         a=a+1
#         i=i-1
#         print(f"Siz yutingizi {a} \t{i}")
#     elif com=="qog'oz" and play=="tosh":
#         a=a-1
#         i=i+1
#         print(f"Siz yutingiz {a} \t{i}")
#     elif com=="qaychi" and play=="tosh":
#         a=a+1
#         i=i-1
#         print(f"Siz yutingiz {a} \t{i}")
#     elif com=="qaychi" and play=="qog'oz":
#         a=a-1
#         i=i+1
#         print(f"Siz yutingiz {a} \t{i}")
#     davom=input("Davom etasizmi? >>  ")
#     if davom!="ha":
#         break
# print("Uchrashguncha xayr!!")




mevalar=['anor,gilos,nok']
for i in mevalar:
    if "a"  in i:
        print(i)