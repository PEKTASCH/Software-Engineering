import unittest
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
import base64
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
    "kullanici1": sifrele("sifre1"),
    "kullanici2": sifrele("sifre2"),
    "kullanici3": sifrele("sifre3")
}

# Rastgele 6 haneli kod oluşturma
def kod_olustur():
    return str(random.randint(100000, 999999))

class TestBankaUygulamasi(unittest.TestCase):

    def test_sifrele_sifre_coz(self):
        metin = "test_sifre"
        sifrelenmis_metin = sifrele(metin)
        cozulmus_metin = sifre_coz(sifrelenmis_metin)
        self.assertEqual(metin, cozulmus_metin)

    def test_kullanici_girisi_basarisiz(self):
        kullanici_adi = "kullanici1"
        sifre = "yanlis_sifre"
        self.assertNotEqual(sifre_coz(kullanici_veritabani[kullanici_adi]), sifre)

    def test_kullanici_girisi_basarisiz_olmayan_kullanici(self):
        kullanici_adi = "olmayan_kullanici"
        sifre = "herhangi_bir_sifre"
        self.assertNotIn(kullanici_adi, kullanici_veritabani)

    def test_kod_olustur(self):
        kod = kod_olustur()
        self.assertEqual(len(kod), 6)
        self.assertTrue(kod.isdigit())

if __name__ == "__main__":
    unittest.main()