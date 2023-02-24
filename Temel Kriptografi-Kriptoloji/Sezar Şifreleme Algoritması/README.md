# Sezar Şifrelemesi
Adını ünlü Roma İmporatoru Julius Sezar'dan almış basit bir şifreleme algoritmasıdır. Algoritma her harfin belilrlenen adım sayısı (anahtar) kadar ötelenmesine dayanır. Şifreyi çözmek için mesajın yazıldığı dilin alfabesine göre öteleme işlemi yapılmalıdır, aksi taktirde mesaj bulunulamayabilir. Bu yazıdaki örnekler Türk alfabesini baz alarak hazırlanmıştır.
### Tarihçe
Julius Sezar, MÖ 1. yüzyılda askeri mesajlarının güvenliğini sağlamak için bu yöntemi kullanmıştır. Bilinen en eski şifreleme yöntemlerinden biridir. Kolay bir şifreleme yöntemi olduğu için farklı anahtarlar ile tarih boyunca kullanılmıştır. 
### Uygulanışı
+ Şifrelenecek metin ve anahtar (adım sayısı) belirlenir. Genellikle 3 seçilir.
+ Metnin her karakteri anahtar kadar ötenelenerk şifrelenir. Örnek olarak A harfi 3 adım ötelenerek Ç harfi elde edilir.

Örnek bir uygulama olarak "Enes" kelimesini anahtar değeri 3 olacak şekilde şifreleyelim:

<b>Enes → Ğpğu</b>

### Avantajları:
+ Oldukça basit olması, eğer anahtarı biliyorsanız şifreleme ve çözme işlemleri hızlıca gerçekleştirilebilir.
+ Sezar şifrelemesi sadece alfabedeki harfler için çalışır dolayısıyla sayılar veya diğer işaretler için çalışmaz. Onların şifrelenmemesi şifrelenmiş metinin okunmasını zorlaştırdığı için bir avantaj olarak sayılabilir.

### Dezavantajları:
Esasen avantaj olarak saydığımız şeyler bakış açısına göre dezavantaj olarak da sayılabilir.
+ Basit bir yapısı vardır, deneme yanılma yoluyla kısa bir süre içerisinde çözülebilir. Bu dezavantajı onu güvenli bir algoritma olmaktan uzaklaştırır.
+ Sadece harf karakterler için çalışır dolayısıyla güncel şifreleme ihtiyaçlarını karşılayamaz.
+ Tek anahtarlı, simetrik bir şifreleme yöntemi olduğundan dolayı anahtarın güvenliği sağlanamazsa şifreleme yöntemi tamamen açiğa çıkabilir. (Simetrik şifreleme yöntemi ile kastedilen şey, açık metin (plain text) olarak adlandırılan mesaj, şifreleme anahtarı (secret key) yardımıyla şifrelenir ve şifreli metin (cipher text) olarak adlandırılır. Şifreli metin, aynı şifreleme anahtarı kullanılarak tekrar çözülebilir ve orijinal açık metne geri dönüştürülebilir.)

### Sezar Şifrelemesini Kırmak
Basit bir şifreleme yöntemi olduğu için kırması da oldukça kolaydır. En başlıca yöntemlere bakalım:

<b>1.Kaba kuvvet:</b> Kaba kuvvet (brute-force) yaklaşımı ile kolaylıkla kırılabilir. Türk alfabesini baz aldığımızdan dolayı anahtar uzayımız 29'dur. En fazla 28 defa ileri alındığında mesaj ortaya çıkacaktır, 29. sefere gelindiğinde ise şifrelenmiş mesaja tekrar ulaşılacaktır. Günümüz biligisayarları ile çok kısa sürelerde mesaj deşifre olabilir.

<b>2.Frekans Analizi:</b> Frekans analizi ile en çok geçen harfler tespit edilir. Algoritma öteleme ile çalıştığı için şifresiz metinlerdeki en çok geçen harflere karşılık gelen şifreli metindeki harfler frekans tablosundan tahmin edilerek anahtar bulunabilir.

<b>3.Bilinen açık metin:</b> Şifrelenmeden önce şifrelenecek metnin bir kısmı biliniyorsa (mesela, bir şifreli mesajın ilk kelimesi açık olarak biliniyorsa), bu bilgi kullanılarak metni deşifre etmek daha kolay hale gelir.
