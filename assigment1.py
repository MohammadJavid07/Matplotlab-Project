#Soru 1: Reklam bütçeleri ile satış hacmi arasındaki ilişkiyi gösteren saçılım grafiği
#Amaç: Advertising.csv dosyasını kullanarak TV, Radio ve Newspaper reklam bütçeleri ile Sales (satış) arasındaki ilişkiyi aynı grafik üzerinde göstermek.

#Gerekli kütüphaneleri içe aktar
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Advertising.csv dosyasını okumak
advertising_df = pd.read_csv(r"D:\Python Codes and Project\Matplotlab-Project\Advertising.csv")

# Veri setinin ilk beş satırını ekrana yazdır
print(advertising_df.head())

print(advertising_df.columns)

#Üç reklam türü için saçılım grafiği çiz
# Grafiğin boyutlarını belirleyelim
plt.figure(figsize=(10,6))

# TV reklam bütçesi ile satış arasındaki ilişkiyi göster
plt.scatter(advertising_df["TV"], advertising_df["Sales"], label = "TV")

# Radyo reklam bütçesi ile satış arasındaki ilişkiyi göster
plt.scatter(advertising_df["Radio"], advertising_df["Sales"], label = "Radio")

# Gazete reklam bütçesi ile satış arasındaki ilişkiyi göster
plt.scatter(advertising_df["Newspaper"], advertising_df["Sales"], label = "Newspaper")

# Grafiğin başlığını belirleyelim
plt.title("Reklam Bütçeleri ve Satış İlişkisi")


# X ve Y eksenlerine açıklama ekliyouruz
plt.xlabel("Reklam Bütçesi")
plt.ylabel("Satış Hacmi")

# Grafik açıklamalarını göster
plt.legend()

# Grafiği ekranda göster
plt.show()

#=================================================================
#Soru 2: Toplam reklam bütçesi ile satış hacmi arasındaki ilişki
#Görev: Advertising.csv veri setini kullanarak toplam reklam bütçesi ile satış hacmi arasındaki ilişkiyi gösteren bir saçılım grafiği (scatter plot) oluşturmak.
advertising_df["Total_Budget"] = (
    advertising_df["TV"] + advertising_df["Radio"] + advertising_df["Newspaper"]
)

# Grafiğin boyutlarını belirle
plt.figure(figsize=(8,5))

# Toplam reklam bütçesi ile satış arasındaki ilişkiyi gösterelim
plt.scatter(advertising_df["Total_Budget"], advertising_df["Sales"])

# Grafiğin başlığını belirleyelim
plt.title("Toplam Reklam Bütçesi ve Satış İlişkisi")

# X ve Y eksenleri
plt.xlabel("Toplam Reklam Bütçesi")
plt.ylabel("Satış Hacmi")

# Grafiği düzenlemesi
plt.tight_layout()

# Grafiği ekranda göstermek
plt.show()


# =======================================================

#Soru 3: TV, Newspaper, Radio ve Sales için histogram çizimi

# Histogramı çizilecek sütunları bir listeye ekle
columns = ["TV", "Radio", "Newspaper", "Sales"]

for column in columns:
    plt.figure(figsize=(8,5))
# İlgili sütunun histogramını çizmesi
    plt.hist(advertising_df[column], bins=15 , edgecolor = "black")
# Grafiğin başlığı
    plt.title(f"{column} histogram")
 # X ve Y eksenleri
    plt.xlabel(column)
    plt.ylabel("frekans")

# Grafik düzeni
    plt.tight_layout()

# Grafiği ekranda göstermek
    plt.show()
# ======================================================
# Question 4: tips.csv dosyası için Boxplot çizimi

# tips.csv dosyasi okumak
tips_df = pd.read_csv(r"D:\Python Codes and Project\Matplotlab-Project\tips.csv")
print(tips_df.columns)

# tip değerleri için kutu grafiğini(Box-Plot) oluştur
plt.figure(figsize=(8,5))
sns.boxplot(data=tips_df["tip"])

# Grafiğin başlığı ve eksen 
plt.title("Boxplot for tip")
plt.ylabel("tip miktari")

# Grafik düzenini ayarlamak
plt.tight_layout()

# Grafiği ekranda göstermek
plt.show()

# ================================================
# Soru 5: OnlineRetail2.csv veri setini kullanarak günlere göre ortalama satışları Türkçe gün isimleriyle gösteren bir çubuk grafik oluşturmak
# OnlineRetail2.csv dosyasi okumak
retail2_df = pd.read_csv(r"D:\Python Codes and Project\Matplotlab-Project\OnlineRetail2.csv")
print(retail2_df.head())

# Fatura tarihini tarih formatına dönüştür
retail2_df["InvoiceDate"] = pd.to_datetime(retail2_df["InvoiceDate"], errors="coerce")

# Satış tutarını hesapla: miktar × birim fiyat
retail2_df["SalesAmount"] = (retail2_df["Quantity"] * retail2_df["UnitPrice"])

# Haftanın günlerini Türkçe olarak tanımlama
turkish_days = {
    0: "Pazartesi",
    1: "Salı",
    2: "Çarşamba",
    3: "Perşembe",
    4: "Cuma",
    5: "Cumartesi",
    6: "Pazar" 
}

# Her satışın haftanın hangi gününde yapıldığını bulalim
retail2_df["DayNumber"] = retail2_df["InvoiceDate"].dt.day_of_week

# Gün numaralarını Türkçe gün adlarına dönüştürmek
retail2_df["Day"] = retail2_df["DayNumber"].map(turkish_days)

# Günlere göre ortalama satış tutarını hesaplama
average_sales = retail2_df.groupby("Day")["SalesAmount"].mean()

# Günleri Pazartesi'den Pazar'a doğru sırala
average_sales = average_sales.reindex(turkish_days.values())

# Çubuk grafiğini oluştur
plt.figure(figsize=(10,6))
plt.bar(average_sales.index, average_sales.values)

# Grafiğin başlığını ve eksen açıklamalarını eklemesi
plt.title("Haftanın Günlerine Göre Ortalama Satış Tutarı")
plt.xlabel("Hafta Günleri")
plt.ylabel("Ortalama Satış Tutarı")

# X eksenindeki gün adlarını döndür
plt.xticks(rotation=45)

# Grafik düzenini ayarlamak
plt.tight_layout()

# Grafiği ekranda göstermek
plt.show()

