import pandas as pd
import chardet

df = pd.read_csv('total_unmarket_backmonth.csv',encoding = 'utf-8-sig')

l=[]
for i in df.values:
    l.append(i[-1].replace('-','/'))

df['時間'] = l


df_241 =pd.read_csv('三重241.csv',encoding = 'big5')
df_400 =pd.read_csv('台中400.csv',encoding = 'big5')
df_104 =pd.read_csv('台北104.csv',encoding = 'big5')
df_109 =pd.read_csv('台北109.csv',encoding = 'big5')
df_930 =pd.read_csv('台東930.csv',encoding = 'big5')
df_512 =pd.read_csv('永靖512.csv',encoding = 'big5')
df_648 =pd.read_csv('西螺648.csv',encoding = 'big5')
df_260 =pd.read_csv('宜蘭260.csv',encoding = 'big5')
df_423 =pd.read_csv('東勢423.csv',encoding = 'big5')
df_220 =pd.read_csv('板橋220.csv',encoding = 'big5')
df_950 =pd.read_csv('花蓮950.csv',encoding = 'big5')
df_540 =pd.read_csv('南投540.csv',encoding = 'big5')
df_338 =pd.read_csv('桃農338.csv',encoding = 'big5')
df_800 =pd.read_csv('高雄800.csv',encoding = 'big5')
df_514 =pd.read_csv('溪湖514.csv',encoding = 'big5')
df_600 =pd.read_csv('嘉義600.csv',encoding = 'big5')
df_420 =pd.read_csv('豐原420.csv',encoding = 'big5')


df_a = pd.merge(df, df_241, on=['時間', '地區碼'])
df_b = pd.merge(df, df_400, on=['時間', '地區碼'])
df_c = pd.merge(df, df_104, on=['時間', '地區碼'])
df_d = pd.merge(df, df_109, on=['時間', '地區碼'])
df_e = pd.merge(df, df_930, on=['時間', '地區碼'])
df_f = pd.merge(df, df_512, on=['時間', '地區碼'])
df_g = pd.merge(df, df_648, on=['時間', '地區碼'])
df_h = pd.merge(df, df_260, on=['時間', '地區碼'])
df_i = pd.merge(df, df_423, on=['時間', '地區碼'])
df_j = pd.merge(df, df_220, on=['時間', '地區碼'])
df_k = pd.merge(df, df_950, on=['時間', '地區碼'])
df_l = pd.merge(df, df_540, on=['時間', '地區碼'])
df_m = pd.merge(df, df_338, on=['時間', '地區碼'])
df_n = pd.merge(df, df_800, on=['時間', '地區碼'])
df_o = pd.merge(df, df_514, on=['時間', '地區碼'])
df_p = pd.merge(df, df_600, on=['時間', '地區碼'])
df_q = pd.merge(df, df_420, on=['時間', '地區碼'])




res = pd.concat([df_a, df_b, df_c,df_d,df_e,df_f,df_g,df_h,df_i,df_j,df_k,df_l,df_m,df_n,df_o,df_p,df_q], axis=0)

res = res.sort_values('產品區域碼')

res.to_csv('final_day.csv',index= False,encoding='utf-8-sig')
