#streamlitの基本的な使い方
#起動時のコマンド streamlit run ファイル名
'''
★詳しくはAPIリファレンスをチェック
https://docs.streamlit.io/library/api-reference
'''

import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time



#プログレスバー
st.write('Display of progras bar')
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f'Iteration{i+1}')
  bar.progress(i+1)
  time.sleep(0.001)

#タイトルを設定
st.title('Fundamentals of streamlit')


#テキスト追加
st.write('DataFrame')

#表を作成
df = pd.DataFrame({
  '1列目':[1,2,3,4],
  '2列目':[10,20,30,40]
})
#表を表示
st.write(df)
#動的な表の表示最大値にマーカーしてサイズ指定 列の場合axis=0　行の場合axis=1
st.dataframe(df.style.highlight_max(axis=0), width=100, height=100)

#静的な表
st.table(df.style.highlight_max(axis=0))

#テキストの表示
"""
# 章
## 節
### 項

```python

import streamlit as st
import numpy as np
import pandas as pd

```

"""

#正規分布の情報から縦20横3つのランダムな数値を取得し、abcの列名を入れる。
df2 = pd.DataFrame(
  np.random.rand(20,3),
  columns=['a','b','c']
)
#動的な折れ線グラフを作る
st.line_chart(df2)
#面折れ線グラフ
st.area_chart(df2)
#棒グラフ
st.bar_chart(df2)

#マップを描画(東京近辺の情報をmapping)
df3 = pd.DataFrame(
  np.random.rand(100,2)/[50,50]+[35.69, 139.70],
  columns=['lat','lon']
)
st.map(df3)

#画像の描画
st.write("DisPlay Image")
img = Image.open('material/img/sample.jpg')
#use_column_width=True　レイアウト横幅に合わせてレイアウトしてくれる。
st.image(img, caption="キャプション",use_column_width=True)


st.write('Interactive Widgets')

#チェックボックスを使って、画像を表示したり非表示にしたりする。
if st.checkbox('Show Image'):
  img = Image.open('material/img/sample.jpg')
  st.image(img, caption="キャプション",use_column_width=True)

#セレクトボックス 1～10までの数字を選ぶ
option = st.selectbox(
  'あなたが好きな数字を教えて下さい',
  list(range(1,11))
)
'あなたの好きな数字は',option,'です。'

#text_inputうまく起動しない
title = st.text_input('好きな映画は？', '入力名')
st.write('好きな映画は', title)

#slider#サイドバーに表示
st.sidebar.write("Sidebar")
condi = st.sidebar.slider('あなたの調子は?',0,100,50)
'あなたの調子は',condi


