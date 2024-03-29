import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

df = pd.read_csv("code_4307_plus.csv")
df = df.sort_values(by=["index"], ascending=False)
print(df.tail(20))


df = df.iloc[0:len(df) - 1]
print(df.tail())

df_train = df.iloc[1:len(df)-1]
df_test = df.iloc[len(df)-1:len(df)]

#print("train", df_train)
#print("test", df_test)

xlist = [
#          1305,
#          1309,#上海株式指数・上証50連動型上場投資信託
#          1322,#上場インデックスファンド中国A株（パンダ）CSI300
#          1326,#SPDRゴールド・シェア
#          1343,#NEXT FUNDS 東証REIT指数連動型上場投信
#          1543,#純パラジウム上場信託（現物国内保管型）
#          1551,#JASDAQ-TOP20上場投信
        "diff_1305",
        "diff_1309",
        "diff_1322",
        "diff_1326",
        "diff_1343",
        "diff_1543",
        "diff_1551"
#		"diff_1309"#上海株式指数・上証50連動型上場投資信託
#
#		"diff_1313",#サムスンKODEX200証券上場指数投資信託
#
#		"diff_1314",#上場インデックスファンドS&P日本新興株100
#
#		"diff_1322",#上場インデックスファンド中国A株（パンダ）CSI300
#
#		"diff_1326",#SPDRゴールド・シェア
#
#		"diff_1343",#NEXT FUNDS 東証REIT指数連動型上場投信
#
#		"diff_1543",#純パラジウム上場信託（現物国内保管型）
#
#		"diff_1548",#上場インデックスファンド中国H株（ハンセン中国企業株）
#
#		"diff_1551",#JASDAQ-TOP20上場投信
#
#		"diff_1633",#NEXT FUNDS 不動産（TOPIX-17）上場投信
#
#		"diff_1673",#ETFS 銀上場投資信託
#
#		"diff_1678",#NEXT FUNDS インド株式指数・Nifty 50連動型上場投信
#
#		"diff_1681",#上場インデックスファンド海外新興国株式（MSCIエマージング）
#
#		"diff_1682",#NEXT FUNDS 日経・東商取白金指数連動型上場投信
#
#		"diff_1698",#上場インデックスファンド日本高配当（東証配当フォーカス100）

		]


x_train = []
y_train = []
for s in range(0, len(df_train) - 1):
	print("x_train : ", df_train["Date"].iloc[s])
	print("y_train : ", df_train["Date"].iloc[s + 1])
	print("")
	x_train.append(df_train[xlist].iloc[s])

	if df_train["Close"].iloc[s + 1] > df_train["Close"].iloc[s]:
		y_train.append(1)
	else:
		y_train.append(-1)

x_train = np.array(x_train)
y_train = np.array(y_train)

x_train[np.isnan(x_train)] = 0
y_train[np.isnan(y_train)] = 0

rf = RandomForestClassifier(n_estimators=len(x_train), random_state=0)
rf.fit(x_train, y_train)


test_x = df_test[xlist].iloc[0]
test_y = rf.predict(test_x.values.reshape(1, -1))

print("result : ", test_y[0])
