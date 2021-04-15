

print("----------------------")
print("Sayı tahmin oyununa hoşgeldiniz!")
print("----------------------")

 
 
import random
a=random.randint(1,100)


print("Şuan ki puanınız = 100 ----- 5 hakkınız vardır.--- Her yanlış cevap 20 puanınızı siler.----")
print("0 ile 100 arasında bir sayı üretildi amacınız bu sayıyı tahmin etmektir.")



for i in range(1,6):
    
  
  sayi=int(input(str(i)+'. hak >> Sayıyı Girin :'))
  
  if(sayi>a):
    if(i>=5):
      print("Hakkınız kalmadı" )
      print("Tutulan Sayı",a)
      break
    puan=100-(i*20)  
    print("Şuan ki puanınız =",puan,"Lütfen daha küçük bir sayı giriniz.")
    
  elif(sayi<a):
    if(i>=5):
      print("Hakkınız kalmadı")
      print("Tutulan Sayı : ",a)
      break
    puan=100-(i*20)    
    print("Şuan ki puanınız =",puan,"Lütfen daha büyük bir sayı giriniz.")
    
  else:
    puan=100-((i-1)*20)  
    print("TEBRİKLER BİLDİNİZ! Kazandığınız Puan=",puan)
    break
 