#Soru 1: Reklam bütçeleri ile satış hacmi arasındaki ilişkiyi gösteren saçılım grafiği
#Amaç: Advertising.csv dosyasını kullanarak TV, Radio ve Newspaper reklam bütçeleri ile Sales (satış) arasındaki ilişkiyi aynı grafik üzerinde göstermek.

#Gerekli kütüphaneleri içe aktar
import pandas as pd
import matplotlib.pyplot as plt

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