# Frekans Analizi

Bir şifreli metindeki karakterlerin sıklıklarını inceleyen bir tekniktir. Bu teknik, özellikle monoalfabetik şifrelerin kırılmasında yaygın olarak kullanılır.

Monoalfabetik şifreleme, her harfi sabit bir başka harfe eşleyen bir şifreleme yöntemidir. Bu şifreleme yöntemi kullanıldığında, şifreli metindeki harflerin oranları açık metindeki harflerin oranlarından farklı olacaktır. Frekans analizi, şifreli metindeki harflerin oranlarını analiz ederek, her harfin muhtemel açık metin karakterleriyle eşleştiği sonucuna varabilir. Bu sayede şifrenin kırılması mümkün hale gelir.

## Kodun Çalışma Mantığı

Şifreli bir metini, frekans saldırısı  ile kırmak için basitçe şöyle bir yöntem düşündüm:

1. İlk olarak şifreli metini okusun
2. Metindeki en yüksek frekansa sahip harfleri tespit etsin ve sıralasın
3. Türkçe dilindeki en yüksek frekansa sahip harfler ile metinden bulup sıraladığımız en yüksek harflerin yerlerini değiştirsin
4. Değişim sonrasında bunu yeni bir metin belgesine yazsın ve sonucu döndürsün

Yöntem mantıklı gibi gözükse de kod şifreli metini tam olarak çözemiyor. Burada ciddi bir hata var ona bakalım.

## Hatanın Ele Alınışı

Öncelikle şifreli metin oluşturmak için [buradaki](https://cryptii.com/pipes/alphabetical-substitution) siteyi kullandım. Örnek bir metini şifreledikten sonra yaptığım denemelerde kod şifreli metini hiçbir zaman tam olarak çözemedi bunun sebebinin örneklemin küçüklüğü olduğunu düşündüm ve örneklemin boyutunu artırmaya karar verdim. 80 sayfalık bir kitabın tamamını şifreledim ve bu şekilde denedim. Bu sefer birkaç kelimeyi çözebilsede çok büyük bir kısım hala anlaşılmaz bir şekilde duruyordu.

Burada yaptığım hata sirali_frekans listesinin Türkçe dilinde yazılmış her metindeki harflerin frekanslarının sirali_frekans listesindeki ile aynı olacağını düşünmemdi. 

### Peki bu kanıya nereden vardım?

Türkçe dilindeki en yüksek frekansa sahip harflerin listesini yani sirali_frekans listesini [buradaki](https://tr.wikipedia.org/wiki/T%C3%BCrk_alfabesindeki_harflerin_kullan%C4%B1m_s%C4%B1kl%C4%B1klar%C4%B1) Wkipedia sayfasından edinmiştim ve bu istatistiğin doğru olduğunu düşündüm yani Wkipedia'ya güvendim.

Bir istatistik öğrencisi olarak büyük bir hata yaptım. Örneklemin içeriğine (büyüklük, kullanılan materyaller vb.) bakmadan istatistiğin, kitleyi yani Türkçe dilinde yazılmış bütün metinleri aynı sonuçla tahmin edebileceğini düşündüm. 

Şu anda [buradan](https://tr.wikipedia.org/wiki/T%C3%BCrk_alfabesindeki_harflerin_kullan%C4%B1m_s%C4%B1kl%C4%B1klar%C4%B1) Wkiepedia sayfasına gittiğimizde sayfanın silindiğini görüyoruz. Silinme sebebine [buradan](https://tr.wikipedia.org/wiki/Vikipedi:Silinmeye_aday_sayfalar/T%C3%BCrk_alfabesindeki_harflerin_kullan%C4%B1m_s%C4%B1kl%C4%B1klar%C4%B1) baktığımızda "Nedim Gayet Bir" isimli kullanıcı istatistiğin kitleyi neden tahminleyemediğini çok güzel açıklamış "Evet, birkaç köşe yazısı ile 37 roman kullanılarak böyle bir istatistik elde edilmiş olabilir. Ancak bu rakamlar, çok spesifik bir kriptoloji araştırması neticesinde elde edilmiş kapsamı çok sınırlı veriler. Lakin söz konusu istatistiği 'Türk alfebesindeki harflerin kullanım sıklığı' şeklinde, genelgeçer bir sayı gibi sunamayız, çünkü böyle bir sayıyı ifade etmiyor. Misal, bu istatistik 1800'lü yıllarda kullanılan Türkçe için de geçerli mi? Elbette, değil."

İşin sonunda kullandığım anahtar yani sirali_frekans listesi evrensel bir kesinlik sunamıyor çünkü Türkçe dilindeki en yüksek frekansa sahip harfler örneklemden örnekleme değişebilir. 

## Sonuç

Kodun anahtarını değiştirmedim, Wkipedia'dan aldığım şekliyle duruyor. Bazı şifreli metinlerde birkaç kelimeyi çözdü, geri kalan kelimeler harfleri tahmin yöntemi ile bulunabilir veya muhtemel birkaç anahtar tanımlayıp bunları tek tek deneyebilir, en mantıklı gözüken sonuç üzerinden gidilebilir. Başka bir çözüm tekniği sadece sesli harfler üzerinden gidilebilir ve en nihayetinde ben bu kodu bu şekliyle bırakacağım.

Siz farklı anahtarlar ile şifreyi çözmeye çalışabilirsiniz veya kodu modifiye ederek sonuca gitmeye çalışabilirsiniz, size kalmış.

## Görselleştirme

Silinmeden önce sayfadan aldığım veriyle aşağıdaki sutun grafiğini oluşturmuştum.

![frekans](https://user-images.githubusercontent.com/88631980/227637592-67fb1ec1-50a0-4b73-b759-a245afd722e8.png)
