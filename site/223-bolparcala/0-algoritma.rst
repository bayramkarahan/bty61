
**Algoritma Nedir?**
--------------------

Algoritma bir işlemi mantık sırasıyla maddeler halinde yazma işlemidir. 
Tarihte ilk defa Harezmi tarafından matematik problemlerini çözmek için kullanılmıştır. 
Algoritma her iş alanında işlemleri anlatmak için kullanılabilir. En sık yemek tariflerinde, bir cihaz kullanım kılavuzunda vb. örneklerde görmekteyiz. 
Bunların dışında bir program yazarken ilk olarak problemin mantık sırasıyla çözümlenmesinde kullanılmaktadır. Algoritma programlamada ilk yapılması gereken adım olarak kabul edilmektedir.


**Harezmi Kimdir?**
-------------------

Harezmi matematik alanında birçok keşfi bulunan bilim adamıdır. Sıfır rakamını bulmuştur. Matematik problemlerini belirli bir mantık sırasıyla çözümleneceğini tarif etmiştir. Bu çözümleme yöntemini günümüzde  algoritma  olarak yazılım geliştirmenin temel adımı olarak kullanmaktayız.

**Algoritma Nasıl Yazılır:**
----------------------------

Algoritma yapacağımız işlemleri sırasıyla yapma işlemidir. Bir önceki konuda kütüphaneden kitap alıp okumak isteyen kişinin yapması gerekenleri hatırlayalım. Bunun için aşağıda bir algoritma oluşturalım.

Öncelikle ilk maddemiz Başla ifadesi ve son maddemizde Son ifadesi olacak şekilde yapalım.

.. image:: /_static/images/algoritma-1.svg
  :width: 600
  :alt: Alternative text


1. Başla
2. Kitap Ara Bul
3. Kitabı Bulduğun Yerden Al
4. Kitabı görevliye Götür ve İzin Al
5. Kitabı Oku
6. Son

Şeklinde olmalıdır. 

.. raw:: pdf

   PageBreak
   
**Örnek:**
----------

Kurt, kuzu ve ot zarar görmeden karşı kıyıya geçmesi için algoritma yazınız.. İşlem adımları resimle aşağıda gösterilmiştir.

.. image:: /_static/images/algoritma-kk0-1.svg
  :width: 600
  :alt: Alternative text

**İşlem Adımları:**
--------------------

.. image:: /_static/images/algoritma-kk0-2.svg
  :width: 600
  :alt: Alternative text

**Çözümü:**
-----------

1. Başla
2. adam, kuzu <--
3. adam -->
4. adam, ot <--
5. adam, kuzu --> 
6. adam, kurt <--
7. adam -->
8. adam, kuzu <--
9. Son

.. raw:: pdf

   PageBreak

**Algoritma Özellikleri:**
--------------------------

Buna benzer şekilde yapacağımız işlemleri algoritmaya dökmemiz gerekmektedir.
Algoritmalar yazılırken şunlara dikkat etmeliyiz.

    1. Basit olmalı
    2. Sade olmalı
    3. Net olmalı
    4. Anlaşılır olmalı
    5. Sembolik olmalı
    6. Mantık sırasıyla


Şimdi Kurt, Kuzu Ot problemini algoritma kurallarına göre yazalım.

.. image:: /_static/images/algoritma-kk0-1.svg
  :width: 600
  :alt: Alternative text

**Problem Çözümü:**
-------------------

Kurt yerine K1, Sandal yerine S, Ot yerine O, Kuzu yerine K2, karşıya gitme yerine >, geri gelme yerine < ifdelerini kullanalım..

1. Başla
2. S, K2 >
3. S<
4. S, O >
5. S, K2 <
6. S, K1 > 
7. S <
8. S K2 >
9. Son

.. raw:: pdf

   PageBreak


