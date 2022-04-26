def tarjima_qil():
    import translate as t
    a = None
    while a != "yoq":
        matn = str(input("Matnni kiriting:"))
        til = str(input("Qaysi tilga tarjima qilasiz:"))
        
        tarjimon = t.Translator(to_lang = til)
        tarjima = tarjimon.translate(matn)
        
        print(tarjima)
        
        a =input("Davom etanizmi? Tanlang!\Ha yoki Yo'q:")
        
        print('Tashakkur foydalanganingiz uchun ')
        
        tarjima_qil()
        
tarjima_qil()





