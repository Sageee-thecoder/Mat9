sayi1 = int(input("Sayı giriniz: "))
islem = input("Bir işlem işareti giriniz (e.g: +, -, ÷,  /, ×, x....): ")
sayi2 = int(input("Sayı giriniz: "))

if islem == "+":  #"==" ifadesi eşit ise anlamında kullanılır, örneğin aralık gösteriminde kullandığımız ≤ veya ≥ ifadeleri Python'da >= veya <= olarak gösterilir.'
	print("Sonuç: ", sayi1 + sayi2)

elif islem == "-":
	print("Sonuç: ", sayi1 - sayi2)

elif islem == "÷" or islem == "/":
	if sayi2 == 0:
		print("Hata! Bir sayıyı sıfıra bölemezsiniz.")
	else:
		 print("Sonuç: ", sayi1 / sayi2)

elif islem == "×" or islem == "x" or islem == "*":
	print("Sonuç: ", sayi1 * sayi2)
	
#Burada aldığımız sayi1 ve sayi2 variable'lar olarak geçer. İçlerinde veri veya bir birim bulundururlar. Fonksiyonlarda bir input veririz, variable'larda verdiğimiz gibi, ve print fonksiyonunda aldığımız gibi bir output alırız.