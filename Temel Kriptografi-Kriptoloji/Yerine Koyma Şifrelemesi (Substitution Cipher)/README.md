# Yerine Koyma Şifrelemesi
Adından da anlaşılacağı üzere alfabedeki her bir karakterin yerine, alfabedeki başka bir karakteri atamaya dayanır. Sezar şifrelemesinde genellikle 3 birim kaydırılırken bu algoritmada anahtarın belirlenmesinde belirli bir kural yoktur. Yani anahtar mesajı şifrelemek isteyen kişi tarafından tamamıyla rastgele seçilebilir.

## Uygulanışı
Şifrelenecek metin ve anahtar belirlenir. Anahtar belirlemekte belirli bir kural olmadığı için bizde kafamıza göre bir anahtar oluşturalım.

<b>Anahtar:</b>
<b>`abcçdefgğhıijklmnoöprsştuüvyz`</b>
<b>`müfıvejihpğaodyrubşgzcötsçlnk`</b>

Örnek bir uygulama olarak "Enes Fehmi" kelimelerini şifreleyelim:
<b>Enes → Euec Jepra </b>

Şifreleyeceğimiz metindeki karakterin karşısındaki karakteri anahtarımızdan bulduk ve yerine koyarak şifreledik.

## Avantajları:
+ Oldukça basit olması, eğer anahtarı biliyorsanız şifreleme ve çözme işlemleri hızlıca gerçekleştirilebilir.

## Dezavantajları:
+ Anahtarın güvenliği ve yönetimi, her kullanıcı için ayrı bir anahtar oluşturulması ve güvenli bir şekilde paylaşılması gereklidir. Ayrıca, anahtarların düzenli olarak değiştirilmesi de gereklidir. Dolayısıyla bu aşamalarda yaşanacak bir güvenlik zafiyeti anahtarın açığa çıkmasına neden olabilir.
+ Basit saldırı tekniklerine açıktır. En basitinden frekans analizi saldırısı ile anahtar tahmin edilebilir. Bu saldırı türünde, şifrelenmiş metindeki harf veya karakter sıklıkları analiz edilerek, şifreleme tablosu tahmin edilmeye çalışılır. Dolayısıyla, yerine koyma şifrelemesi, modern kriptografi standartlarına göre yetersiz bir güvenlik sağlar.

## Yerine Koyma Şifrelemesini Kırmak
En başlıca bilinen basit yöntemlere bakalım:

<b>1. Frekans analizi:</b> Yukarıda da belirtildiği gibi frekans analiziyle kolaylıkla kırılabilir.

<b>2. Deneme yanılma yöntemi: </b> Şifrelenmiş metnin bir kısmının bilindiği durumlarda deneme yanılma yöntemi ile devamıda tahmin edilebilir.

<b>3. Düz metin saldırıları: </b> Şifreleme tablosunun yani anahtarın bir kısmı biliniyorsa, bu bilgiden yararlanarak geri kalan kısmının tahmin edilmesi esasına dayanan bir saldırı türüdür. 
