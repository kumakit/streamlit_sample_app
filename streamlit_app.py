import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title('kuma data')
st.caption('Pythonアプリの置き場所')

st.subheader('サブヘッダーのテスト')
st.text('本文のテストです。本文はここです')

st.link_button("Netlify page", "https://kumadata.netlify.app/")

st.text('ネイピア数を底とする指数関数')
fig, ax = plt.subplots()

# xの値（-2～5で0.1刻みで配列生成）
x=np.arange(-2, 5, 0.1)

#　ネイピア数を底とする関数
y = np.exp(x)

# グラフの設定
ax.plot(x, y) # プロット
ax.set_title('exponential function', fontsize = 12)
ax.set_xlabel('x', fontsize = 12)
ax.set_ylabel('f(x)', fontsize = 12)
ax.grid() # グリッド描画
st.pyplot(fig)

st.text('シグモイド関数')
fig, ax = plt.subplots()

# xの値（-8～8で0.1刻みで配列生成）
x = np.arange(-8, 8, 0.1)

#　シグモイド関数
y = 1 / (1 + np.exp(-x) )

# グラフの設定
ax.plot(x, y) # プロット
ax.set_title('Sigmoid function', fontsize = 12)
ax.set_xlabel('x', fontsize = 12)
ax.set_ylabel('f(x)', fontsize = 12)
ax.grid() # グリッド描画
st.pyplot(fig)

st.text('底を２とする対数関数　y=log2(x)')
fig, ax = plt.subplots()

# xの値（-8～8で0.1刻みで配列生成）
x = np.arange(0, 8, 0.1)

#　y=log2(x)
y = np.log2(x)

# グラフの設定
ax.plot(x, y) # プロット
ax.set_title('Logarithmic function', fontsize = 12)
ax.set_xlabel('x', fontsize = 12)
ax.set_ylabel('f(x)', fontsize = 12)
ax.grid() # グリッド描画
st.pyplot(fig)

st.text('底をe(ネイピア数=2.71828183…)とする対数(自然対数)')
fig, ax = plt.subplots()

# xの値（-8～8で0.1刻みで配列生成）
x = np.arange(-1, 100, 0.1)

#　シグモイド関数
y = np.log(x)

# グラフの設定
ax.plot(x, y) # プロット
ax.set_title('natural logarithm function', fontsize = 12)
ax.set_xlabel('x', fontsize = 12)
ax.set_ylabel('f(x)', fontsize = 12)
ax.grid() # グリッド描画
st.pyplot(fig)
