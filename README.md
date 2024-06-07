# Software-Engineering-Project

## Bankacılık Uygulamalarında Güvenli Yazılım Tasarımı İncelemesi
### RSA şifreleme algoritması kullanılarak bankaya giriş uygulaması yapılmıştır. Uygulamayı kullanacak kişi öncelikle kullanıcı adı ve şifresini girer. Sonrasında ise kullanıcıyı doğrulamak için çift taraflı kimlik doğrulama kodu gönderilir. Eğer kullanıcı kodu doğru girerse hesabına giriş yapabilir. Uygulamaya giriş güvenliği arttırılmış olur. 

### Uygulamanın güvenilir ve hatasız çalıştığını tespit etmek için fonksiyonlarına birim testleri uygulanmış ve başarılı test sonuçları elde edilmiştir.

### Kullanılan Dil Ve Kütüphaneler: 
#### Python dili 
#### Tkinder kütüphanesi
#### cryptography.hazmat.primitives.asymmetric: Bu kütüphane, RSA şifrelemesi gibi asimetrik kriptografik işlemler için fonksiyonlar sağlar.
#### cryptography.hazmat.primitives.serialization: Bu kütüphane, RSA anahtarlarını kodlama ve kod çözme için fonksiyonlar sağlar.
#### base64: Bu kütüphane, binary verileri metne dönüştürmek ve metni binary verilere dönüştürmek için fonksiyonlar sağlar.
#### random: Bu kütüphane, rastgele sayılar ve kodlar oluşturmak için fonksiyonlar sağlar.
#### pyotp: Bu kütüphane, tek seferlik şifreler (OTP) oluşturmak ve doğrulamak için fonksiyonlar sağlar.

### RSA şifrelemesi kullanarak iki faktörlü kimlik doğrulama (2FA) ile banka giriş sistemini simüle eden bir GUI uygulaması oluşturmaktadır.

### Kodun İşlevi:

### RSA Anahtar Çifti Oluşturma:
#### private_key ve public_key değişkenleri, 2048 bitlik RSA anahtar çifti oluşturmak için kullanılır.
#### public_key, kullanıcıların verilerini şifrelemek için kullanılır.
#### private_key, şifrelenmiş verileri çözmek için kullanılır.

### Şifreleme ve Çözme Fonksiyonları:
#### sifrele fonksiyonu, bir metni public_key ile RSA şifrelemesi kullanarak şifreler.
#### sifre_coz fonksiyonu, şifrelenmiş metni private_key ile RSA şifrelemesi kullanarak çözer.

### Kullanıcı Veri Tabanı:
#### kullanici_veritabani sözlüğü, kullanıcı adlarını ve şifrelerini (RSA ile şifrelenmiş) saklar.

### Kod Oluşturma:
#### kod_olustur fonksiyonu, 6 haneli rastgele bir kod oluşturur.

### İkinci Faktör Kodları:
#### kodlar sözlüğü, kullanıcı adlarına karşılık gelen 2FA kodlarını saklar.


### Kullanıcı Girişi:
#### kullanici_girisi fonksiyonu: Kullanıcı adını ve şifreyi giriş alanlarından alır. Kullanıcı adını kullanici_veritabaninda arar. Şifreyi sifre_coz fonksiyonu ile çözer ve doğru olup olmadığını kontrol eder.
#### Doğruysa:
#### 2FA kodu oluşturur ve kodlar sözlüğüne kaydeder. Kullanıcıya kodu gösterir. İkinci faktör doğrulama penceresini açar.

#### Yanlışsa: Hata mesajı gösterir.

### İkinci Faktör Doğrulama:
#### ikinci_faktor_penceresi fonksiyonu: İkinci faktör doğrulama penceresini oluşturur. Kullanıcıdan 2FA kodunu girmesini ister. Girilen kodu kodlar sözlüğündeki kodla karşılaştırır.
#### Doğruysa:
#### Başarılı giriş mesajı gösterir ve pencereyi kapatır.

#### Yanlışsa: 
#### Hata mesajı gösterir.