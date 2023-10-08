import pandas as pd
import numpy as np
import seaborn as sns

# GÖREV 1 : List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük
# harfe çeviriniz ve başına NUM ekleyiniz.

df = sns.load_dataset("car_crashes")

deneme = ["NUM_" + i if df[i].dtype != "O" else i.upper() for i in df.columns]

# veya

deneme2 = [i.upper() if df[i].dtype == "O" else "NUM_" + i for i in df.columns]

# GÖREV 2: List Comprehension yapısı kullanarak car_crashes verisinde isminde "no" barındırmayan
# değişkenlerin isimlerinin sonuna "FLAG" yazınız.

deneme3 = [i + "_FLAG" if "no" not in i else i.upper() for i in df.columns]

# GÖREV 3: List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan
# değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.

og_list = ["abbrev", "no_previous"]

new_cols = [i for i in df.columns if i not in og_list]
new_df = df[new_cols]
new_df.head()

# GÖREV 4: PANDAS ALIŞTIRMALARI

pd.set_option('display.max_row', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# 1. Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.
df1 = sns.load_dataset("titanic")
df1.head()

# 2. Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz
df1["sex"].value_counts()

# 3. Her bir sutuna ait unique değerlerin sayısını bulunuz
df1.nunique()

# 4. pclass değişkeninin unique değerlerinin sayısını bulunuz
df1["pclass"].unique()

# 5. pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.
df1[["pclass", "parch"]].nunique()

# 6. embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz ve tekrar kontrol ediniz
df1["embarked"].dtype
df1["embarked"] = df1["embarked"].astype("category")
df1["embarked"].dtype
df1.info()

# 7. embarked değeri C olanların tüm bilgelerini gösteriniz
df1[df1["embarked"] == "C"].head()

# 8. embarked değeri S olmayanların tüm bilgelerini gösteriniz
df1[df1["embarked"] != "S"].head()

# 9. Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.
df1[(df1["age"] < 30) & (df1["sex"] == "female")].head()

# 10. Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniZ.
df1[(df1["fare"] > 500) | (df1["age"] > 70)].head()

# 11. Her bir değişkendeki boş değerlerin toplamını bulunuz
df1.isnull().sum()

# 12. who değişkenini dataframe’den çıkarınız
df1.drop("who", axis=1, inplace=True) # kalıcı olarak, sütun silmek istediğimizden axis=1
df.head()

# 13. deck değikenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz
df1["deck"].mode()  # mod C çıktı
df1["deck"].mode()[0]  # seri olduğu için modu birden fazla değere sahip olabilir bu yüzden
                       # [0] kullanarak ilk (en sık tekrar eden) değeri seçiyoruz.
df1["deck"].fillna(df1["deck"].mode()[0], inplace=True)  # deck'in mode'u C ile boş olanları doldur, kalıcı olarak
df1["deck"].isnull().sum()

# 14. age değikenindeki boş değerleri age değişkenin medyanı ile doldurunuz
df1["age"].median()
df1["age"].fillna(df1["age"].median(), inplace=True)  # deck'in mode'u C ile boş olanları doldur, kalıcı olarak
df1["age"].isnull().sum()

# 15. survived değişkeninin pclass ve cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.
df1.groupby(["pclass","sex"]).agg({"survived": ["sum", "count", "mean"]})

# 16. 30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazın. Yazdığınız fonksiyonu kullanarak titanik veri
#setinde age_flag adında bir değişken oluşturunuz oluşturunuz. (apply ve lambda yapılarını kullanınız)
def age_control(age):
    if age < 30:
        return 1
    else:
        return 0

df1["age_flag"] = df1["age"].apply(lambda i : age_control(i))

# HİÇ FONKSİYON KULLANMADAN
df1["age_flag"] = df1["age"].apply(lambda i : 1 if i<30 else 0)

# 17. Seaborn kütüphanesi içerisinden Tips veri setini tanımlayın.
df2 = sns.load_dataset("tips")
df2.head()

# 18. Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz
df2.groupby("time").agg({"total_bill": ["sum","min", "max", "mean"]})

# 19. Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
df2.groupby(["time", "day"]).agg({"total_bill": ["sum","min", "max", "mean"]})

# 20. Lunch zamanına ve kadın müşterilere ait total_bill ve tip değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz
df2[(df2["time"] == "Lunch") & (df2["sex"] == "Female")].groupby("day").agg({"total_bill": ["sum","min", "max", "mean"],
                                                                             "tip": ["sum","min", "max", "mean"]})

# 21. size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir? (loc kullanınız)
df2.loc[(df2["size"] < 3) & (df2["total_bill"] > 10), "total_bill"].mean()

# 22. total_bill_tip_sum adında yeni bir değişken oluşturunuz. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.
df2["total_bill_tip_sum"] = df2["total_bill"] + df2["tip"]
df2.head()

# 23. total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız.
yeni_frame = df2.sort_values("total_bill_tip_sum", ascending=False)[:30]  # false dediğimizde >> büyükten küçüğe
yeni_frame.shape  # 30 kişi olduğunu gördük