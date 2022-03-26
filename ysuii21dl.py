import streamlit as st

st.subheader('2021年間水位推移グラフ')

# フォルダーのパス
fdir = '2021ysuii'
# 河川リストをタプルで
files = ('米代川扇田',
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
        '物部川戸板島')

# ダウンロード関数
def main(n):
    with open (f'{fdir}/2021{files[n]}.html') as f:
        st.download_button(label='HTMLダウンロード',
                            data= f,
                            file_name=f'2021{files[n]}.html',
                            mime='text/html',
                            )

# ラジオボタン
select = st.radio('川選択',files)
if select == files[0]:
    main(0)
elif select == files[1]:
    main(1)
elif select == files[2]:
    main(2)
elif select == files[3]:
    main(3)
elif select == files[4]:
    main(4)
elif select == files[5]:
    main(5)
elif select == files[6]:
    main(6)
elif select == files[7]:
    main(7)
elif select == files[8]:
    main(8)
elif select == files[9]:
    main(9)
elif select == files[10]:
    main(10)
elif select == files[11]:
    main(11)
else:
    pass

st.text('※国土交通省水文水質データベースのデータを利用して表示しています')
st.write('')
st.write('')
st.write('')
# 外部リンク設定
link1 = '[AyuZyのホームページ](https://sites.google.com/view/ayuzy)'
st.markdown(link1,unsafe_allow_html=True)








