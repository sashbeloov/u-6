# git init .
# git config --global user.name 'sashbeloov'
# git config --global user.email 'beloovsasha23@gmail.com'
# cd .\.git\
# git config --list  ---> user.name=sashbeloov user.email=beloovsasha23@gmail.com akauntni tekshirib olamiza va agar to'gri bolsa .\.git\ dan chiqamiz
# # git sozlandi#
# papkalar qizil bolib qolgan bolsa biz working directorydamiz yani ishlash muhitidamiz
# git status ----> bu yerda staging ereaga tushishi kerak bolgan faylar chiqib keladi
# git add . -----> staging eraga o'tadi,agar git add . deb yozsak barcha fayllar qoshilib ketadi staging eraga
# git status --> yashilga otsa demak staging ereage otdi degani
# git commit -m 'first commit' ----> bu local repoga projectni suratini joylab qoyamiz yani local repoga proejctni saqlab qoydik degani
# git log ----> commitlar royhatini korishi va ular haqida ma'lumot olish
# git show 7b9bade7674f11c960d2d9bdc6b14a914d190269)-- bu ozgaradi ---> (optional) ozgarishlarni korish
# ide ven faylarni githubda ketib qolishi kerak emas buning uchun .gitignore faylida fayylarni nomi yozib ketish kerak
# .gitignore fayli ----> .idea
# 		       stay.py
# git reset ----> staging areadan orqadagi faylga qaytaradi va shunda korib olsak boladi qaysi fayllar ketishi kerak emasligin, ularning rangi sariq ranga otib qoladi
# git branch -M main
# git remote add origin https://github.com/sashbeloov/(name repo).git <----> local repo bilan global reponi bog'lash
#
# git remote -v
# origin  https://github.com/sashbeloov/u-6.git (fetch)
# origin  https://github.com/sashbeloov/u-6.git (push)  ---> local va global repolarni bog'langanin tekshirish
#
# git remote remove
# usage: git remote remove <name>  ----> local va gloab repolarni ochirib tashlash agar boshidan ulamoqchi bolsak quyidagi kod yoziladi
# git remote add origin https://github.com/sashbeloov/(name repo).git <----> local repo bilan global reponi bog'lash
#
# BU SSH KALIT BILAN ULASH ---> SSH DEGANI MA'LUMOTLAR SHIFIRLANGAN KORINISHDA OTADI DEGANI
# SSH GENERATE QILISH
#
# ssh-keygen -t rsa -b 4096 -C "beloovsasha23@gmail.com"
#
# GitLab yordamida shaxsiy cloudni yaratsa boladi bulardan tashqaru butbucket ham bor va github
#
# git checkout -b (branch-name) ---> yangi branch yaratish
# git checkout (branch-name) ---> boshqa branchga o'tish
#
# misol uchu main branchdan boshqa branchga otganda ozgarishlar qilsak ozgarishlar faqat osha branchga otganda korinadi boshqasida korinmaydi
# agar birlashtirmoqchi bolsak git merge bilan birlash tiramiz
# git merge (features/rewivew) qavs ichiga main bilan qaysi branchni birlashtirmoqchi bolsak shu branch nomini yozamiz
#
# clone qilingandan keyin
#
# kerakli kodlar yozib bolgandan song
#
# git add .
# git commit -m 'commit'
# git push origin (branch-name)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# print("hello")
# print(24)