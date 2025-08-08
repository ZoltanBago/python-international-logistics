#!/usr/bin/env python
# coding: utf-8

# # Python Pandas Projekt | Nemzetközi logisztika
# ---
# 
# ![](logistics.jpg)
# 
# *Fotó: pixabay.com*
# 
# ---

# ##  1. Feladat – Adatok beolvasása
# Az adatokat az `international_logistics_data.csv` fájlból olvassuk be egy Pandas DataFrame-be.

# ### 1.1. Az adatok beolvasása a CSV fájlból egy Pandas adatkeretbe (DataFrame)
# Importáljuk a Pandas könyvtárat és használjuk az alias `as` elnevezést.
# 
# Hozzunk létre egy változót, `il_data` néven. Érdemes egyszerű és jól megjegyezhető változó nevet választani.  
# 
# Végül jelenítsük meg az adatokat.

# In[ ]:


import pandas as pd

il_data = pd.read_csv("international_logistics_data.csv")
il_data


# ### 1.2. Az adatkeret első 5 sorának megjelenítése
# Az adatkeret első 5 sorának megjelenítéséhez a `head()` metódust kell alkalmaznunk.

# In[ ]:


il_data.head()


# ## 2. Feladat – Az alapinformációk megismerése
# 
# - Az adatkeret (DataFrame) oszlopneveinek megjelenítése
# - Az oszlopok (columns) adattípusának megjelenítése
# - A rekordok vagy sorok (rows) számának megjelenítése

# ### 2.1. Az adatkeret oszlopneveinek megjelenítése
# Az adatkeret oszlopneveit a `columns`, vagyis az oszlop segítségével ismerhetjük meg. 

# In[ ]:


il_data.columns


#     Index(['OrderID', 'Country', 'Product', 'Quantity', 'UnitPriceUSD',
#            'ShipmentMode', 'ShipmentDate'],
#           dtype='object')

# Az oszlopok nevei:
# - **OrderID** 
# - **Country** 
# - **Product**  
# - **Quantity**  
# - **UnitPriceUSD**   
# - **ShipmentMode**   
# - **ShipmentDate**   
# 
# Az `OrderID`, a rendelési azonosító, a `Country`, az ország neve, a `Product`, a termék neve, a `Quantity`, a mennyiséget jelenti, az `UnitPriceUSD` az egységár USD-ben, a `ShipmentMode` a szállítás módja és a `ShipmentDate` a szállítás dátuma.

# ### 2.2. Az oszlopok adattípusainak megjelenítése
# Az oszlopok adattípusait a `dtypes` segítségével jeleníthetjük meg.

# In[ ]:


il_data.dtypes


# A kimenet:  
#   
#     OrderID          int64
#     Country         object
#     Product         object
#     Quantity         int64
#     UnitPriceUSD     int64
#     ShipmentMode    object
#     ShipmentDate    object
#     dtype: object

# ### 2.3. A sorok számának megjelenítése
# A sorok számának megjelenítéséhez a Python `len()` metódusát alkalmazzuk.

# In[ ]:


len(il_data)


# Az adatkészletünkben 10 sor található. A számolás nullától (0) kezdődik és kilencig (9) tart. 

# ## 3. Feladat – A teljes rendelési érték nevű oszlop létrehozása és kiszámítása
# Hozzunk lére egy új oszlopot, amelynek a neve **teljes rendelési érték**, vagyis `TotalValueUSD` lesz.
# 
# A teljes rendelési érték a **mennyiség** `Quantity` és az **egységár USD-ben** `UnitPriceUSD` szorzata.
# 
# > TotalValueUSD = Quantity * UnitPriceUSD

# ### A `TotalValueUSD` új oszlop létrehozása, amely a `Quantity` és `UnitPriceUSD` szorzata

# In[ ]:


il_data["TotalValueUSD"] = il_data["Quantity"] * il_data["UnitPriceUSD"]
il_data.head()


# ## 4. Feladat – A szállítási módok gyakoriságának meghatározása
# A **szállítási módok**, vagyis `ShipmentMode` esetében az `Air`,levegőben a `Sea`, tengeren a `Rail`, vonaton és a `Truck`, kamionon történő szállítás szerepel a ShipmentMode oszlopban.
# 
# Ahhoz, hogy meg tudjuk számolni a szállítási módokat a `value_counts()` metódust kell alkalmazni.

# In[ ]:


il_data["ShipmentMode"].value_counts()


# A kimenet:
# 
#     ShipmentMode
#     Air      4
#     Sea      3
#     Rail     2
#     Truck    1
#     Name: count, dtype: int64

# ## 5. Feladat – A legtöbb rendelést feladó ország meghatározása
# A legtöbb rendelést feladó ország meghatározásához a ``value_counts()`` és az ``idxmax()`` metódusokat kell alkalmazni. 

# In[ ]:


il_data["Country"].value_counts().idxmax()


# A kimenet:    
#     
#     'Germany'

# Ha részletesebb adatokra vagyunk kiváncsiak, akkor azt a `value_counts()` metódus segítségével érhetjük el. 

# In[ ]:


il_data["Country"].value_counts()


# A kimenet:   
#    
#     Country
#     Germany    2
#     USA        2
#     China      2
#     France     2
#     Brazil     1
#     India      1
#     Name: count, dtype: int64

# ## 6. Feladat – Az összes termék átlagos egységárának meghatározása
# Az összes termék átlagos egységárának kiszámításához a `mean()` metodust kell alkalmazni.

# In[ ]:


il_data["UnitPriceUSD"].mean()


# ## 7. Feladat – A teljes rendelési érték meghatározása országonként
# Az országonkénti teljes rendelési értéket a `groupby()` és a `sum()` metódusok segítségével tudjuk meghatározni.   

# In[ ]:


il_data.groupby("Country")["TotalValueUSD"].sum()


# Az adatkeret alapján, országos összesítésben Németország vezet 1.425.000, ezt követi Kína 37.200 és az USA 30.000.
# 
# A kimenet:
# 
#     Country
#     Brazil        3000
#     China        37200
#     France        3850
#     Germany    1425000
#     India        15000
#     USA          30000
#     Name: TotalValueUSD, dtype: int64

# ## 8. Feladat – A legnagyobb értékű rendelést leadó ország meghatározása
# Az `OrderID` alapján kell megkeresni azt az országot, amelynek a legmagasabb a `TotalValueUSD` értéke. 
# 
# Ehhez az `idxmax()` metódust kell alkalmazni.

# In[ ]:


il_data.loc[il_data["TotalValueUSD"].idxmax()]


# A kimenetben látható, hogy ez Németország.
# 
# A kimenet:
# 
#     OrderID                 1007
#     Country              Germany
#     Product          Automobiles
#     Quantity                  70
#     UnitPriceUSD           20000
#     ShipmentMode            Rail
#     ShipmentDate      2025-08-07
#     TotalValueUSD        1400000
#     Name: 6, dtype: object

# ## 9. Feladat – Időbeli sorrend meghatározása
# A rendeléseket a `ShipmentDate` szerint növekvő sorrendbe kell rendezni.
# 
# Ehhez a `sort_values()` metódust kell alkalmazni.

# In[ ]:


il_data.sort_values(["ShipmentDate"])


# ## 10. Feladat – A termékek csoportosítása
# A rendeléseket kell csoportosítani termékenként és kiírni, hogy hány darabot `Quantity` rendeltek az egyes termékekből összesen.
# 
# Ehhez a `groupby()` és a `sum()` metódus eggyüttes használata szükséges.

# In[ ]:


il_data.groupby("Product")["Quantity"].sum()


# A kimenet:    
#     
#     Product
#     Automobiles         70
#     Cheese              90
#     Clothing           100
#     Coffee             200
#     Electronics        110
#     Machinery           30
#     Pharmaceuticals    150
#     Textiles           120
#     Wine                80
#     Name: Quantity, dtype: int64

# ---

# In[ ]:




