import yfinance as yf
import datetime
import requests
import pandas

# 日期
today = datetime.datetime.today # 今天日期

yesterday = (datetime.datetime.now()+datetime.timedelta(days=-7)).strftime('%Y-%m-%d') # 上星期日期

# 道瓊指數(DJI)
df_DJI = yf.Ticker("^DJI").history(period="max") # 道瓊指數資料
DJI_close = round(df_DJI.values[-1][3],2) # 今日道瓊指數
DJI_lestweek_close = round(df_DJI.loc[yesterday][3],2) # 上星期道瓊指數
DJI_Spread = round((DJI_close - DJI_lestweek_close),2) # 道瓊指數價差
DJI_list = [DJI_close , DJI_lestweek_close , DJI_Spread] # 需要道瓊指數之資料

# 那斯達克(IXIC)
df_IXIC = yf.Ticker("^IXIC").history(period="max") # 那斯達克指數資料
IXIC_close = round(df_IXIC.values[-1][3],2) # 今日那斯達克指數
IXIC_lestweek_close = round(df_IXIC.loc[yesterday][3],2) # 上星期那斯達克指數
IXIC_Spread = round((IXIC_close - IXIC_lestweek_close),2) # 那斯達克指數價差
IXIC_list = [IXIC_close , IXIC_lestweek_close , IXIC_Spread] # 需要那斯達克之資料

# 美元匯率(USDTWD=X)
df_usd = yf.Ticker("USDTWD=X").history(period="max") # 美元匯率資料
usd_close = round(df_usd.values[-1][3],2) # 今日美元匯率
usd_lestweek_close = round(df_usd.loc[yesterday][3],2) # 上星期美元匯率
usd_Spread = round((usd_close - usd_lestweek_close),2) # 美元匯率價差
usd_list = [usd_close , usd_lestweek_close , usd_Spread] # 需要美元匯率之資料

# 美國公債10年期(TNX)
df_TNX = yf.Ticker("^TNX").history(period="max") # 美國公債10年期資料
TNX_close = round(df_TNX.values[-1][3],2) # 今日美國公債10年期
TNX_lestweek_close = round(df_TNX.loc[yesterday][3],2) # 上星期美國公債10年期
TNX_Spread = round((TNX_close - TNX_lestweek_close),2) # 美國公債10年期價差
TNX_list = [TNX_close , TNX_lestweek_close , TNX_Spread] # 需要美國公債10年期之資料

# 加權股價指數(TWII)
df_TWII = yf.Ticker("^TWII").history(period="max") # 加權股價指數資料
TWII_close = round(df_TWII.values[-1][3],2) # 今日加權股價指數
TWII_Volme = df_TWII.values[-1][4] # 今日加權股價指數成交量
TWII_lestweek_close = round(df_TWII.loc[yesterday][3],2) # 上星期加權股價指數
TWII_Spread = round((TWII_close - TWII_lestweek_close),2) # 加權股價指數價差
TWII_list = [TWII_close , TWII_Volme , TWII_lestweek_close , TWII_Spread] # 需要加權股價指數之資料

# 西德州原油(WTI)
df_WTI = yf.Ticker("^WTI").history(period="max") # 西德州原油資料
WTI_close = round(df_WTI.values[-1][3],2) # 今日西德州原油
# WTI_lestweek_close = round(df_WTI.loc[yesterday][3],2) # 上星期西德州原油
# WTI_Spread = (WTI_close - WTI_lestweek_close) / WTI_lestweek_close # 西德州原油價差
WTI_list = [WTI_close] # 需要西德州原油之資料

# 傳送line
token = "cWoKoXm8EkdY1APqa3jxTeuXg2dEm7r2vkPnCiw4mEe"
message = ""
message += f"\n★ -> 道瓊指數(DJI)：\n　　　今日收盤價：{DJI_close}\n　　　價差：{DJI_Spread}"
message += f"\n★ -> 那斯達克(IXIC)：\n　　　今日收盤價：{IXIC_close}\n　　　價差：{IXIC_Spread}"
message += f"\n★ -> 美元匯率(USDTWD=X)：\n　　　今日收盤價：{usd_close}\n　　　價差：{usd_Spread}"
message += f"\n★ -> 美國公債10年期(TNX)：\n　　　今日收盤價：{TNX_close}\n　　　價差：{TNX_Spread}"
message += f"\n★ -> 加權股價指數(TWII)：\n　　　今日收盤價：{TWII_close}\n　　　價差：{TWII_Spread}\n　　　成交量：{TWII_Volme}"
message += f"\n★ -> 西德州原油(WTI)：\n　　　今日收盤價：{WTI_close}"

# HTTP 標頭參數與資料
headers = { "Authorization": "Bearer " + token }
data = { 'message': message }

# 以 requests 發送 POST 請求
requests.post("https://notify-api.line.me/api/notify",
    headers = headers, data = data)
