Şifreleme Yöntemleri
++++++++++++++++++++

Sezar Şifreleme
---------------

Sezar şifrelemesi, metinleri şifrelemek veya şifrelenmiş metinleri çözmek için kullanılan basit bir şifreleme yöntemidir. Bu yöntem, Julius Sezar tarafından kullanıldığı için onun adını almıştır.

Sezar şifrelemesi, her harfi belirli bir sayıyla kaydırarak metni şifreler. Örneğin, bir harfi 1 birim kaydırmak için, A harfi B'ye, B harfi C'ye ve benzer şekilde devam eder. Bu kaydırma miktarı, şifreleme veya çözme işlemi için kullanılan anahtar olarak bilinir.

Örnek olarak, "BABA" kelimesini 1 birim kaydırarak şifreleyelim. B harfi C'ye, A harfi B'y dönüşecektir. Sonuç olarak, şifrelenmiş metin "CBCB" olacaktır.

Sezar şifrelemesi, basit ve hızlı bir şifreleme yöntemi olmasına rağmen, güvenlik açısından çok zayıftır. Çünkü şifreleme anahtarı kolayca tahmin edilebilir ve tüm olası kaydırma miktarları denenebilir. Bu nedenle, güvenli iletişim için daha karmaşık şifreleme yöntemleri kullanılması önerilir.

.. image:: /_static/images/zararliyazilim-sifre.png
  :width: 400
  :alt: Alternative text
  

Md5 Şifeleme
------------

MD5 (Message Digest Algorithm 5), bir mesajın veya verinin benzersiz bir karmasını oluşturmak için kullanılan bir kriptografik karma işlemidir. MD5, 128 bitlik bir karma değeri üretir ve genellikle parola veya veri bütünlüğünü doğrulamak için kullanılır.

MD5, bir girdi mesajını alır ve onu bir dizi işlemden geçirerek sabit bir uzunlukta bir çıktı üretir. Bu çıktı, girdi mesajının benzersiz bir temsilidir ve aynı girdiye her zaman aynı çıktıyı üretir. Bu nedenle, MD5, veri bütünlüğünü doğrulamak veya parolaları saklamak için kullanılabilir.

Ancak, MD5 artık güvenli bir şifreleme yöntemi olarak kabul edilmez. Çünkü MD5, çeşitli güvenlik açıklarına sahiptir ve çarpışma saldırılarına karşı savunmasızdır. Çarpışma saldırıları, farklı girdi mesajlarının aynı MD5 çıktısını üretebileceği durumları ifade eder. Bu nedenle, MD5 yerine daha güvenli şifreleme algoritmaları kullanılması önerilir, örneğin SHA-256.

.. image:: /_static/images/zararliyazilim-md5.png
  :width: 500
  :alt: Alternative text
  


.. raw:: pdf

   PageBreak

