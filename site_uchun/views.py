from django.shortcuts import render

def index_page(request):
    return render(request, 'index.html')

def about_page(request):
    if request.method == 'POST':
        matn = request.POST.get('matn', 'Hech qanday matn kelmadi')
    else:
        matn = 'Bu sahifa to‘g‘ridan-to‘g‘ri ochildi (POST yo‘q).'
    return render(request, 'about.html', {'matn': matn})

dat1 = """Bugungi kunda ko‘pchilik yordamga muhtoj. Lekin ular yordam so‘rashga, odam topishga qiynalishadi. Aynan shuning uchun ushbu ilova yaratildi — yordam so‘rashni va yordam berishni soddalashtirish uchun. Bu ilova orqali muhtoj insonlar e’lon joylaydi. E’londa ularning holati, telefon raqami va karta raqami ochiq ko‘rsatiladi. Har bir e’lon biz tomonidan tekshiriladi, faqat rostgo‘y va ishonchli ma’lumotlargina saytga chiqadi. Yordam bermoqchi bo‘lgan odamlar esa ushbu e’lonlarni ko‘rib chiqadi va o‘z xohishiga ko‘ra yordam beradi. Oraliq odamlar, murakkab jarayonlar yoki shubhali sxemalar yo‘q. Bizning maqsadimiz — insonlarni bir-biriga yaqinlashtirish. Har kimga yordam berish imkonini yaratish. Bu tizim soddaligi, shaffofligi va ishonchliligi bilan ajralib turadi."""
dat2 = """Imkoniyati cheklangan insonlar&content=Bizning ilovamiz — aynan imkoniyati cheklangan, nogironligi rasmiy tarzda tasdiqlangan insonlarga yordam berish uchun yaratilgan. Ushbu odamlar ko‘pincha kundalik hayotda ko‘plab qiyinchiliklarga duch kelishadi. Ular uchun moddiy yordam, dori-darmon, maxsus jihozlar yoki boshqa ko‘mak zarur bo‘lishi mumkin. Ilovamizda faqat tekshirilgan, nogironligi haqiqatan tasdiqlangan insonlar e’lon qoldiradi. Har bir e’lon diqqat bilan ko‘rib chiqilib, rostligi tekshiriladi. Bu yordam beruvchilarga ishonch va osoyishtalik bag‘ishlaydi. Siz, saxovatli inson sifatida, bu erda haqiqiy yordamga muhtojlarni topasiz. Sizning kichik yordamingiz ularga katta kuch beradi. Ilovamiz yordamida imkoniyati cheklangan yurtdoshlarimiz hayotini yaxshilashga hissa qo‘shing — ular bunga chin dildan muhtoj."""
dat3 = """Saxovatli, yordam beruvchi insonlar&content=Ilovamizning yuragi — yordam bermoqchi bo‘lgan saxovatli insonlardir. Ular — yuragi ochiq, boshqalarning qiyinchiliklariga befarq bo‘lmaydigan oddiy odamlar. Siz yoki boshqa har bir inson kichik yordam orqali boshqalar hayotida katta farq yaratishingiz mumkin. Ba’zida bir necha ming so‘m, birovga kerakli dori, kiyim yoki hatto samimiy so‘z katta quvvat beradi. Bu ilova yordam bermoqchi bo‘lganlarga oson yo‘l ko‘rsatadi. Siz e’lonlarni ko‘rib chiqasiz, kimga va qanday yordam kerakligini bilasiz. Telefon qilib, yordam so‘rayotgan inson bilan gaplashib, to‘g‘ri qaror qabul qilishingiz mumkin. Ilovamiz orqali yordam berish — oddiy, shaffof va ishonchli. Oraliq shaxslar yoki murakkab jarayonlarsiz. Har bir saxovatli yurtdosh o‘z imkoniyatiga qarab yordam beradi, kimdir katta, kimdir kichik. Bizning maqsadimiz — insonlarni bir-biriga yaqinlashtirish va birgalikda ijtimoiy yordamni kuchaytirish."""

contents = {
    1: {"title_name": "Ilovaning maqsadi", "content_full_data": dat1, "content_image":"images/pic01.jpg"},
    2: {"title_name": "Imkoniyati cheklangan insonlar", "content_full_data": dat2, "content_image":"images/pic02.jpg"},
    3: {"title_name": "Saxovatli, yordam beruvchi insonlar", "content_full_data": dat3, "content_image":"images/pic03.jpg"},
}


def maqsad(request,content_id):
    content = contents.get(content_id)
    if not content:
        from django.http import Http404
        raise Http404("Content not found")

    return render(request, 'generic.html', {'content': content})
    pass
