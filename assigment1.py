#Soru 1: Reklam bütçeleri ile satış hacmi arasındaki ilişkiyi gösteren saçılım grafiği
#Amaç: Advertising.csv dosyasını kullanarak TV, Radio ve Newspaper reklam bütçeleri ile Sales (satış) arasındaki ilişkiyi aynı grafik üzerinde göstermek.

#Gerekli kütüphaneleri içe aktar
import pandas as pd
import matplotlib.pyplot as plt

# Advertising.csv dosyasını okumak
advertising_df = pd.read_csv(r"D:\Python Codes and Project\Matplotlab-Project\Advertising.csv")

# Veri setinin ilk beş satırını ekrana yazdır
print(advertising_df.head())
