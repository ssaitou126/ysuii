import pandas as pd
import plotly
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st

st.subheader('年間水位推移グラフ')
t1 = '2021'

# 作図関数
def funcDraw(s,titl):
    # データフレーム作成
    dfs = pd.read_csv(f'{t1}suiidata/{t1}{s}.csv')
    xaxs = dfs['date']
    ygrf = dfs['suii']
    # 代表値設定
    dfmx = ygrf.max()
    dfme = round(ygrf.mean(),2)
    dfmd = ygrf.quantile(0.5)
    dfmo = ygrf.mode()[0]
    dfqt = ygrf.quantile(0.25)
    dfmn = round(ygrf.min(),2)
    # グラフ描画
    fig = make_subplots(rows=1, cols=2,column_widths=[0.9,0.1],shared_yaxes=True, horizontal_spacing=0.01)
    fig.update_layout(showlegend=False,title=f'{t1}{titl}水位推移図                  最大値={dfmx}    平均値={dfme}    中間値={dfmd}    最頻値={dfmo}    1stQ={dfqt}    最小値={dfmn}')
    fig.add_trace(go.Scatter(x=xaxs,y=ygrf,name=f'{titl}'),row=1,col=1)
    fig.add_trace(go.Violin(y=ygrf, box_visible=True, line_color='blue',meanline_visible=True, fillcolor='deepskyblue', opacity=0.6,name=f'{titl}'),row=1,col=2)
    fig.update_xaxes(rangeslider={"visible":True})
    fig.show()

# ラジオボタン設定
mysel = st.radio(' ',(
    '[河川選択]▼',
    '米代川扇田',
    '米代川二ツ井',
    '阿仁川米内沢',
    '長良川稲荷',
    '板取川洞戸',
    '飛騨川上呂',
    '神通川大沢野',
    '庄川大門',
    '九頭竜川五松橋',
    '仁淀川不動',
    '四万十川大正',
    '物部川戸板島',
    ))
if mysel == '米代川扇田':
   funcDraw('ougida',mysel)
elif mysel == '米代川二ツ井':
   funcDraw('futatui',mysel)
elif mysel == '阿仁川米内沢':
   funcDraw('yonai',mysel)
elif mysel == '長良川稲荷':
   funcDraw('inari',mysel)
elif mysel == '板取川洞戸':
   funcDraw('horado',mysel)
elif mysel == '飛騨川上呂':
   funcDraw('jouro',mysel)
elif mysel == '神通川大沢野':
   funcDraw('oosawano',mysel)
elif mysel == '庄川大門':
   funcDraw('daimon',mysel)
elif mysel == '九頭竜川五松橋':
   funcDraw('gom',mysel)
elif mysel == '仁淀川不動':
   funcDraw('fudou',mysel)
elif mysel == '四万十川大正':
   funcDraw('taisyou',mysel)
elif mysel == '物部川戸板島':
   funcDraw('toitajima',mysel)
else:
    pass

# 外部リンク設定
link1 = '[Link to　→　AyuZy](https://sites.google.com/view/ayuzy)'
st.markdown(link1,unsafe_allow_html=True)