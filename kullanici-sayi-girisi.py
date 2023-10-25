# Kullanıcının girdiği 3 sayı arasından , en büyük olanı bulun ve sonuca yazdırın.

sayi1 = int(input("ilk sayıyı yazın : "))
sayi2 = int(input("ikinci sayıyı yazın : "))
sayi3 = int(input("üçüncü sayıyı yazın : "))


if (sayi1 > sayi2) and (sayi1 > sayi3) :
    print("Sayı1 En Büyük Sayıdır : " , sayi1)

elif (sayi2 > sayi3):
    print("Sayı2 En Büyük SayIdır : " , sayi2)

else :
    print("sayı3 En Büyük sayıdır : " , sayi3)