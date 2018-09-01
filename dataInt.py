import pandas as pd


df = pd.read_csv("code_4307.csv", header=0)
df.columns=["Date", "Open", "High", "Low", "Close", "Volume", "Trading Value"]
df["index"] = [i for i in range(len(df))]
print(df.head(20))

etf_list = [
          1305,
          1309,#上海株式指数・上証50連動型上場投資信託
          1322,#上場インデックスファンド中国A株（パンダ）CSI300
          1326,#SPDRゴールド・シェア
          1343,#NEXT FUNDS 東証REIT指数連動型上場投信
          1543,#純パラジウム上場信託（現物国内保管型）
          1551#JASDAQ-TOP20上場投信
		]

for etf in etf_list:
	#print(etf)
	df_etf = pd.read_csv("etf_" + str(etf) + ".csv", header=0)
	df_etf.columns=["Date", "Open", "High", "Low", "Close", "Volume", "Trading Value"]

	dates = []
	closeis = []
	print(etf)
	for d in df["Date"]:
		#try:
		date = df_etf.loc[(df_etf.Date == d), "Date"]
		print(date.values)
		if bool(date.values) is False:
				continue
            
		dates.append(date.values[0])

		close = df_etf.loc[(df_etf.Date == d), "Close"]
		if str(close.values[0]) != str("nan"):
			yesterday_close = close.values[0]
			closeis.append(close.values[0])	

		else:
			#print("nan")
			closeis.append(yesterday_close)
		
	df_etf2 = pd.DataFrame({"Date_" + str(etf) : dates,
							"Close_" + str(etf) : closeis})

	df = pd.concat([df, df_etf2], axis=1)
	df["diff_" + str(etf)] = (df["Close_" + str(etf)] / df["Close_" + str(etf)].shift(-1)) - 1
	#print(df)

df.to_csv("code_4307_plus.csv")