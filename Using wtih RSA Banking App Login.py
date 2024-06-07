import tkinter as tk
from tkinter import messagebox
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
import base64
import pyotp
import random

# RSA anahtar çifti oluştur
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()

# Şifreleme ve çözme fonksiyonları
def sifrele(metin):
    sifrelenmis_veri = public_key.encrypt(
        metin.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return base64.b64encode(sifrelenmis_veri).decode()

def sifre_coz(sifrelenmis_veri):
    sifrelenmis_veri = base64.b64decode(sifrelenmis_veri)
    cozulmus_veri = private_key.decrypt(
        sifrelenmis_veri,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return cozulmus_veri.decode()

# Kullanıcı bilgilerini saklayan bir sözlük (şifreler RSA ile şifrelenmiş)
kullanici_veritabani = {
    "12345678": sifrele("sifre1"),
    "87654321": sifrele("sifre2"),
    "01234567": sifrele("sifre3")
}

# Rastgele 6 haneli kod oluşturma
def kod_olustur():
    return str(random.randint(100000, 999999))

# İkinci faktör kodlarını saklamak için bir sözlük
kodlar = {}

def kullanici_girisi():
    kullanici_adi = giris_adi.get()
    sifre = giris_sifresi.get()
    
    if kullanici_adi in kullanici_veritabani and sifre_coz(kullanici_veritabani[kullanici_adi]) == sifre:
        # Kod oluştur ve kullanıcıya gönder (basitleştirilmiş)
        kod = kod_olustur()
        kodlar[kullanici_adi] = kod
        print(f"2FA kodu: {kod}")  # Gerçek uygulamada bu kod SMS veya e-posta ile gönderilir
        ikinci_faktor_penceresi(kullanici_adi)
    else:
        messagebox.showerror("Giriş Başarısız", "Kullanıcı adı veya şifre yanlış. Lütfen tekrar deneyin.")

def ikinci_faktor_penceresi(kullanici_adi):
    # İkinci faktör penceresini oluştur
    faktor_pencere = tk.Toplevel(pencere)
    faktor_pencere.title("İkinci Faktör Doğrulama")
    
    tk.Label(faktor_pencere, text="2FA Kodunu Giriniz:").grid(row=0, column=0)
    kod_giris = tk.Entry(faktor_pencere)
    kod_giris.grid(row=0, column=1)
    
    def dogrula():
        girilen_kod = kod_giris.get()
        if kodlar.get(kullanici_adi) == girilen_kod:
            messagebox.showinfo("Giriş Başarılı", "Bankacılık işlemlerine hoş geldiniz.")
            faktor_pencere.destroy()
        else:
            messagebox.showerror("Doğrulama Başarısız", "Yanlış kod. Lütfen tekrar deneyin.")
    
    dogrula_butonu = tk.Button(faktor_pencere, text="Doğrula", command=dogrula)
    dogrula_butonu.grid(row=1, column=1)

# Ana pencereyi oluştur
pencere = tk.Tk()
pencere.title("Banka Girişi")

# Kullanıcı adı etiketi ve giriş alanı
tk.Label(pencere, text="Kullanıcı Adı:").grid(row=0, column=0)
giris_adi = tk.Entry(pencere)
giris_adi.grid(row=0, column=1)

# Şifre etiketi ve giriş alanı
tk.Label(pencere, text="Şifre:").grid(row=1, column=0)
giris_sifresi = tk.Entry(pencere, show="*")
giris_sifresi.grid(row=1, column=1)

# Giriş butonu
giris_butonu = tk.Button(pencere, text="Giriş Yap", command=kullanici_girisi)
giris_butonu.grid(row=2, column=1)

# Pencereyi çalıştır
pencere.mainloop()
