Elektronik Tablolama Programları:
+++++++++++++++++++++++++++++++++

Hesaplama, grafik, veri analizi yapabileceğimiz programlardır.

Sık kullanılan elektronik tablolama programları şunlardır;

    - Ms Excel(windows)
    - Libre Ofis Calc (linux)
    - E-Tablolar(google)
    - Wps ofis spreadsheeths

Program Ara yüzü:
+++++++++++++++++

.. image:: /_static/images/elektroniktablolama-arayuz.png
	:width: 500
	:alt: Alternative text

Sık Kullanılan Fare İşaretleri:
+++++++++++++++++++++++++++++++

Excelde hücreleri seçili hücrelere göre uyarlama işaretidir. 

.. image:: /_static/images/elektroniktablolama-isaret.png
	:width: 250
	:alt: Alternative text

Formülleri veya verileri diğer hücrelere uyarlar. Bunlar;

    - Sayılar
    - Günler
    - Aylar
    - Formüller
    - Özel Listeler
    - Tarih

Excelde Sayı Uyarlama
++++++++++++++++++++++

Yandaki resimde sayıların hücrelerde uyarlaması gösterilmiştir. Genellikle uyarlama işlemleri üç aşamada yapılır. Ard arda uyarlanacak iki sayı yazılır ve seçilir.
Seçilen hücrelerin en altında bulunan küçük siyah kareye fare getirilir ve + işaretinin çıkması sağlanır.
İstediğimiz sayıya kadar aşağı doğru sürüklenir.

.. image:: /_static/images/elektroniktablolama-sayi.png
	:width: 400
	:alt: Alternative text

Not:
Uyarlama işlemleri pozitif olacağı gibi negatifte olabilir.


Excelde Ay Uyarlama
++++++++++++++++++++
Resimde görüldüğü gibi aylar değer hücrelere uyarlanmıştır.
Uyarlama işlemleri üç adımda gerçekleşmektedir. İstediğiniz bir ay adı yazılır ve hücre seçilir.
Seçili hücrenin alt köşesindeki küçük siyah kare üzerine gelerek + işaretinin çıkması beklenir.
Sol tuşa basılı tutularak istediğimiz aya kadar aşağı doğru sürüklenir.

.. image:: /_static/images/elektroniktablolama-ay.png
	:width: 400
	:alt: Alternative text

Not:
Ay adları özel listelerde bulunmaktadır.
Ayrıca İstediğimiz bir aydan başlayabiliriz.
Son aya gelince liste devam ediyorsa ocak ayına tekrar dönecektir.

Excelde Gün Uyarlama
++++++++++++++++++++

Yandaki resimde üç aşamada günlerin diğer hücrelere uyarlaması gösterilmiştir.
Uyarlama işlemleri üç adımda gerçekleşmektedir. İstediğiniz bir gün adı yazılır ve hücre seçilir.
Seçili hücrenin alt köşesindeki küçük siyah kare üzerine gelerek + işaretinin çıkması beklenir.
Sol tuşa basılı tutularak istediğimiz aya kadar aşağı doğru sürüklenir.

.. image:: /_static/images/elektroniktablolama-gun.png
	:width: 400
	:alt: Alternative text

Not:
Gün adları özel listelerde bulunmaktadır.
Ayrıca istediğimiz bir günden başlayabiliriz.
Son güne gelince liste devam ediyorsa pazartesi gününü tekrar getirecektir.


Hücre İsimlendirmesi ve Seçimi:
 Bir hücrenin adı sütun ve satırların birleşmesinden oluşur. Örneğin aşağıdaki resimde D9 seçilmiş.

.. image:: /_static/images/elektroniktablolama-hucre.png
	:width: 400
	:alt: Alternative text

Sarı Alan: C4:F4
Yeşil Alan: C6:F8
Mavi Alan: H4:H8

.. raw:: pdf

   PageBreak

Temel Formüller:
++++++++++++++++

Formüller = işaretiyle başlar.
Not: Formülleri tek tek yazmak yerine uyarlama **+** işaretini kullanabiliriz.

.. image:: /_static/images/elektroniktablolama-formul.png
	:width: 400
	:alt: Alternative text

Üstte görülen resme göre aşağıdaki formüller yazılmıştır.

Toplama:
--------

- Hücrelerin toplamını alır.
- =topla(Başlangıç Hucre : Bitiş Hucre Adresi)
- =topla(c2:c5)

Ortalama:
---------

- =ortalama(Başlangıç Hucre : Bitiş Hucre Adresi)
- =ortalama(c2:c5)

En Büyük:
---------

- =mak(Başlangıç Hucre : Bitiş Hucre Adresi)
- =mak(c2:c5)

En Küçük:
---------

- =min(Başlangıç Hucre : Bitiş Hucre Adresi)
- =min(c2:c5)

Boş Say:
--------
- =boşluksay(Başlangıç Hucre : Bitiş Hucre Adresi)
- =boşluksay(c2:c5)

Değer Say:
----------

- =bağ_değ_dolu_say(Başlangıç Hucre : Bitiş Hucre Adresi)
- =bağ_değ_say(c2:c5)

.. raw:: pdf

   PageBreak

