# GÖREV 1:
# Soru 1: miuul_gezinomi.xlsx dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.

import pandas as pd
pd.set_option("display.max_rows", None)
pd.set_option("display.float_format", lambda x: '%.2f' % x)

df = pd.read_excel(r"C:\Users\nazli\Desktop\case_studies_miuul\gezinomi_tantm-230304-111358\gezinomi_tanitim\miuul_gezinomi.xlsx")
df.head()
df.shape
df.info()

# Soru 2: Kaç unique şehir vardır? Frekanslarınedir?
df["SaleCityName"].nunique()
df["SaleCityName"].value_counts()

# Soru 3:Kaç unique Concept vardır?
df["ConceptName"].nunique()

# Soru4: Hangi Concept’den kaçar tane satış gerçekleşmiş?
df["ConceptName"].value_counts()

# Soru5: Şehirlere göre satışlardan toplam ne kadar kazanılmış?
df.groupby("SaleCityName").agg({"Price": "sum"})

# Soru6: Concept türlerine göre göre ne kadar kazanılmış?
df.groupby("ConceptName").agg({"Price": "sum"})

# Soru7: Şehirlere göre PRICE ortalamaları nedir?
df.groupby("SaleCityName").agg({"Price": "mean"})

# Soru 8: Conceptlere göre PRICE ortalamaları nedir?
df.groupby("ConceptName").agg({"Price": "mean"})

# Soru 9: Şehir-Concept kırılımında PRICE ortalamaları nedir?
df.groupby(by=["SaleCityName", "ConceptName"]).agg({"Price": "mean"})

# GÖREV 2: : SaleCheckInDayDiff değişkenini kategorik bir değişkene çeviriniz.

bins = [0, 7, 30, 90, df["SaleCheckInDayDiff"].max()]
labels = ["Last Minuters", "Potential Planners", "Planners", "Early Bookers"]

df["EB_Score"] = pd.cut(df["SaleCheckInDayDiff"], bins, labels = labels)

# GÖREV 3: COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?
# Şehir-Concept-EB Score, Şehir-Concept- Sezon, Şehir-Concept-CInDay kırılımında ortalama ödenen ücret ve yapılan işlem sayısı cinsinden inceleyiniz.

# Şehir-Concept-EB Score

# Şehir-Concept- Sezon
df.groupby(by=["SaleCityName", "ConceptName", "Seasons"]).agg({"Price":"mean","count"})

# Şehir-Concept-CInDay
df.groupby(by=["SaleCityName", "ConceptName", "CInDay"]).agg({"Price": ["mean", "count"]})

# GÖREV 4: City-Concept-Season kırılımının çıktısını PRICE'a göre sıralayınız.
# • Elde ettiğiniz çıktıyı agg_df olarak kaydediniz.

agg_df = df.groupby(by=["SaleCityName", "ConceptName", "Seasons"]).agg({"Price":"mean"}).sort_values("Price", ascending=False)
agg_df.head()

# GÖREV 5: Indekste yer alan isimleri değişken ismine çeviriniz
# Üçüncü sorunun çıktısında yer alan PRICE dışındaki tüm değişkenler index isimleridir. Bu isimleri değişken isimlerine çeviriniz.

agg_df.reset_index(inplace=True)  # Price gibi eşit sırada değildi sütun adları onları ayarladık

agg_df.head()

# GÖREV 6: Yeni seviye tabanlı müşterileri (persona) tanımlayınız.
# Yeni seviye tabanlı satışları tanımlayınız ve veri setine değişken olarak ekleyiniz.
# • Yeni eklenecek değişkenin adı: sales_level_based
# • Önceki soruda elde edeceğiniz çıktıdaki gözlemleri bir araya getirerek sales_level_based değişkenini oluşturmanız gerekmektedir.

agg_df["sales_level_based"] = agg_df[["SaleCityName", "ConceptName", "Seasons"]].agg(lambda x:'_'.join(x).upper(), axis=1)

# GÖREV 7: Yeni müşterileri (personaları) segmentlere ayırınız.
# Yeni personaları PRICE’a göre 4 segmente ayırınız.
# • Segmentleri SEGMENT isimlendirmesi ile değişken olarak agg_df’e ekleyiniz.
# • Segmentleri betimleyiniz (Segmentlere göre group by yapıp price mean, max, sum’larını alınız).

agg_df["Segment"] = pd.qcut(agg_df["Price"], 4, labels = ["A", "B", "C", "D"])

agg_df.groupby("Segment").agg({"Price": ["mean", "max", "sum"]})

# GÖREV 8: Yeni gelen müşterileri sınıflandırıp, ne kadar gelir getirebileceklerini tahmin ediniz.
# Antalya’da herşey dahil ve yüksek sezonda tatil yapmak isteyen bir kişinin ortalama ne kadar gelir kazandırması beklenir?
# • Girne’de yarım pansiyon bir otele düşük sezonda giden bir tatilci hangi segmentte yer alacaktır?

new_user = "ANTALYA_HERŞEY DAHIl_HIGH"
agg_df[agg_df["sales_level_based"] == new_user]
