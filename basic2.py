#streamlitの基本的な使い方 2カラム
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

left_column, right_column = st.columns(2)

btn = left_column.button('右カラムにテキストを表示')
if btn:
  right_column.write('テキストを表示')

#expander
expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせを書く')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせを書く')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせを書く')


