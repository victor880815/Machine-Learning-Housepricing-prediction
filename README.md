# taichung-house-price

Model 以 xgboost XGBRegressor 訓練

# Demo link
https://taichunghouseprice.herokuapp.com/model_api?city=B&district=B03&year=108&lat=24.124566887961176&lon=120.67507110914983&bs=0.6&g=0&l=1&room=2&living=1&toilet=1&s=50&real_s=30

https://taichunghouseprice.herokuapp.com/model_api?city=B&district=B03&year=108&lat=24.124566887961176&lon=120.67507110914983

# Result
{"p":306097,"tp":1435}\
p : 估計每坪單價(單位:新台幣元)\
tp : 估計交易總價(單位:新台幣萬元)

# Parameters
city      縣市(必填,目前只提供 B = 台中)\
district  行政區(必填,目前只提供 B03南區、B04西區、B05北區、B06西屯區、B07南屯區、B08北屯區、B23烏日區、B27太平區、B28大里區)\
year      估價年度(必填,101~109年)

bs      主建物比(預設=0.5)\
g       屋齡(預設=0)\
l       車位數(預設=0)\
lat     緯度(必填)\
lon     經度(必填)\
s       總坪數(預設=50)\
room    房(預設=3)\
living  廳(預設=2)\
toilet  衛(預設=2)\
real_s  主建物坪數(預設=bs * s)

# 前端 - django 3.2.4

以django前端製作使用者串接API之介面

請參考 datascience2.zip

demo 帳戶資訊 \
帳號；123456 \
密碼；abcabcabc
