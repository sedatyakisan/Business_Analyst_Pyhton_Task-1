#5 Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.
sayi = input(" sayı girin : ")

palindromsayi = sayi[::-1]

if sayi == palindromsayi:
    print("Girilen sayı  palindrom sayıdır.")
else:
    print("Girilen sayı  palindrom sayı değildir.")