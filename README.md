# Botary SDCP Kütüphanesi


<p>Botary SDCP kütüphanesi sayesinde uygulamalarınıza botary'den çektiğiniz verileri kolayca işleyebilirsiniz.</p>

<h2>Nasıl Kullanılır?</h2>

<ol>
    <li>
        <h3>Kurulum</h3>
        <ul>
            <li>İndirdiğiniz klasörü çalışma alanınıza yükleyin ve python dosyalarınıza <i>import</i> yapmak isterseniz şu kodları sayfanıza yazmalısınız:</li>
            <code>from botary.main import *</code>
        </ul>
    </li>
    <li>
        <h3>Kullanım</h3>
        <ul>
            <li>
                <p>Botary SDCP'ye erişmek için, öncelikle bir SDCP anahtarı almanız gerekmektedir. SDCP anahtarınızı <a href="https://www.botary.projectbo.com.tr/">Botary'nin resmi websitesinden</a> edinebilirsiniz.</p>
<pre>
<code>   

# SDCP Kodunuzu JSON Dosyasına Kaydedin

{
    "SDCP": "SDCP_KODUNUZ_BURAYA_YAZILACAK"
}
</code>
</pre>

<p>Kütüphaneyi projenize dahil ettikten sonra, aşağıdaki örnek kodu kullanarak botary'den veri çekebilirsiniz:</p>
<pre><code>from botary.main import *

# Ne Tür Bir Çekme İşlemi Kullanacağınızı Yazın
veri = GetBotaryTitle("random")

# Çekilecek Kitabın Kategorisini Belirleyin
veri = GetBotaryTitle("defined","Makale")

# Çekilecek Kitabın Kodunu Yazın
veri = GetBotaryTitle("defined","","{kitabın_kodu}")

# Gelen veriyi işleyin
print(veri)
</code></pre>
            </li>
        </ul>
    </li>
</ol>
<h1>Veri Çekme Türleri</h1>
<p>Botary'den veri çekerken verilerin nasıl çekileceğini ayarlamak için sunduğumuz yöntem sayesinde verileri daha iyi bir şekilde yönetebileceksiniz.</p>
<ul>
  <li>Verileri Rastgele Çekmek İstiyorsanız: <code>GetBotaryTitle("random","","")</code></li>
  <li>Son Veriyi Çekmek İstiyorsanız: <code>GetBotaryTitle("last","","")</code></li>
  <li>İlk Veriyi Çekmek İstiyorsanız: <code>GetBotaryTitle("first","","")</code></li>
  <li>Belirli Bir Veriyi Çekmek İstiyorsanız: <code>GetBotaryTitle("defined","","")</code></li>
</ul>
<p>Not: Belirli bir veriyi çekmek istiyorsanız sonraki iki boşluktan en az birini doldurmalısınız. Eğer Belirli bir veriyi çekmek istemiyorsanız diğer iki boşluğu doldurmanız hiçbir anlam ifade etmeyecektir.</p>

<h1>Şablon</h1>
<ul>
  <li>
Kitap Başlığı İçin: <code>GetBotaryTitle("Çekilecek_Tür","Kategori","Kitabın_Kodu")</code>
  </li><li>
Kitap İçeriği İçin: <code>GetBotaryContent("Çekilecek_Tür","Kategori","Kitabın_Kodu")</code>
  </li><li>
Kitabın Yazarı İçin: <code>GetBotaryOwner("Çekilecek_Tür","Kategori","Kitabın_Kodu")</code></li>
<li>
Kitabın Yazılış Tarihi İçin: <code>GetBotaryDate("Çekilecek_Tür","Kategori","Kitabın_Kodu")</code></li>
    <li>
Kitap Hakkında İçin: <code>GetBotaryInfo("Çekilecek_Tür","Kategori","Kitabın_Kodu")</code></li>
    <li>
Kitabın Öngösterimi İçin: <code>GetBotaryPreview("Çekilecek_Tür","Kategori","Kitabın_Kodu")</code></li>
</ul>
<h2>Notlar:</h2>
<ul>
    <li>SDCP anahtarınızı gizli tutun ve kodunuzda doğrudan yazmayın.</li>
    <li><code>GetBotaryTitle()</code> fonksiyonu örnektir, gerçek istekleri ihtiyacınıza göre uyarlayabilirsiniz.</li>
    <li>SDCP kullanım başına kullanan kişinin hem kullanıcının güvenliği hem SDCP sahibinin güvenliği için IP adresi sistemimize kaydedilmektedir, bunu kabul ederek kütüphanemizi kullanıyorsunuz.</li>
    <li>Projeyi kendinize göre özelleştirebilirsiniz ancak istediğimiz bilgileride aksama olması halinde yapılacak yaptırımlardan sorumlu olacağınızı bildirmek isteriz.</li>
    <li>Taklit bilgi farkedilmesi durumunda yapılacak yaptırımlardan sorumlusunuz.</li>
</ul>

<h2>Destek</h2>
<p>Herhangi bir sorunuz veya geri bildiriminiz varsa, lütfen <b>destek@projectbo.com.tr</b> mail adresiyle destek ekibimize başvurun.</p>


