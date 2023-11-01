# class Book:
#      def __init__(self,nomi,muallifi,narxi,janri):
#          self.nomi=nomi
#          self.muallifi=muallifi
#          self.narxi=narxi
#          self.janri=janri
#
#      def get_nomi(self):
#           return self.nomi
#
# book1=Book("Sariq devni minib","Xudoyberdi To'xtaboyev",24000,"Badiy")
# book2=Book("O'tkan kunlar","Muallif",40000,"Badiy")
# print(book1.get_nomi())
#
#
#
# class Kutubxona:
#     def __init__(self,nomi):
#         self.nomi=nomi
#         self.kitoblar=[]
#         self.kitoblar_soni=0
#
#     def nomi(self):
#         return self.nomi
#     def addbook(self,kitob):
#         self.kitoblar.append(kitob)
#         self.kitoblar_soni+=1
#
#     def get_count(self):
#         return self.kitoblar_soni
#     def info (self):
#         return [kitob.get_nomi()for kitob in self.kitoblar]
#
# kutubxona1=Kutubxona("Kutubxona UZB")
# kutubxona2=Kutubxona("Alisher Navoiy")
# kutubxona1.addbook(book1)
# kutubxona2.addbook(book2)
# print(kutubxona1.kitoblar[0].nomi)

# class talabalar:
#     def __init__(self,nomi):
#         self.nomi=nomi
#     def get_nomi(self):
#
# talaba1=("Farux")
# talaba2=("Jurabek")
# talaba3=("Ramiz")
# talaba4=("Aziz")
#
# class Fan:
#     def __init__(self,nomi):
#         self.nomi=nomi
#         self.fanlar=[]#
#         self.talabalar_soni=0
#
#     def nomi (self):
#         return self.nomi
#     def addFan(self,fan):
#         self.fanlar.append(Fan)
#         self.talabalar_soni+=1
#     def get_count(self):
#         return self.talabalar_soni
#     def Coder(self):
#         return [Fan.get_nomi() for Fan in self.fanlar]
# Fan1=Fan("Algebra")
# Fan2=Fan("Ximiya")
# print(Fan1.fanlar[0].nomi)



son=int(input("son kiriting"))
if son>0:
    print(son+10)
else:
    print(son-10)





























































































































































































































































































































































































