import streamlit as st
import requests
import urllib.parse
import json
import io
import time

def synthsize_speech(input_text, speaker='ずんだもん（ノーマル）'):

  speaker_type = {
      'VOICEVOX：四国めたん（あまあま）':"0",
      'VOICEVOX：ずんだもん（あまあま）':"1",
      'VOICEVOX：四国めたん（ノーマル）':"2",
      'VOICEVOX：ずんだもん（ノーマル）':'3',
      'VOICEVOX：四国めたん（セクシー）':'4',
      'VOICEVOX：ずんだもん（セクシー）':'5',
      'VOICEVOX：四国めたん（ツンツン）':'6',
      'VOICEVOX：ずんだもん（ツンツン）':'7',
      'VOICEVOX：春日部つむぎ（ノーマル）':'8',
      'VOICEVOX：波音リツ（ノーマル）':'9',
      'VOICEVOX：雨晴はう（ノーマル）':'10',
      'VOICEVOX：玄野武宏（ノーマル）':'11'
  }

  # 音素データ生成
  text = urllib.parse.quote(input_text)
  response = requests.get("https://deprecatedapis.tts.quest/v2/voicevox/audio/?key=Y5R236H-n8r1934&speaker=" + speaker_type[speaker] + "&pitch=0&intonationScale=1&speed=1&text="+ text)

  return response

def point_balance():
  results = requests.get("https://deprecatedapis.tts.quest/v2/api/?key=Y5R236H-n8r1934")
  results_json = results.json()
  points = results_json['points']

  return points

st.title('音声出力アプリ(高速)')
url = "https://voicevox.su-shiki.com/su-shikiapis/#step3"
st.write("本サイトは [WEB版VOICEVOX API（高速）](%s)を利用して音声合成をしています。" % url)

st.markdown('### データ準備')

input_option = st.selectbox(
  '入力データの選択',
  ('直接入力', 'テキストファイル')
)
input_data = None

if input_option =='直接入力':
  input_data =st.text_area('こちらにテキストを入力してください','VOICEVOX用のサンプル文になります。')
else:
  uploaded_file = st.file_uploader('テキストファイルをアップロードしてください。',['txt'])
  if uploaded_file is not None:
    content = uploaded_file.read()
    input_data = content.decode()

if input_data is not None:
  st.write('入力データ')
  st.write(input_data)
  st.markdown('### パラメータ設定')

  speaker = st.selectbox(
    'VOICEの選択をしてください',
    ('VOICEVOX：ずんだもん（あまあま）',
    'VOICEVOX：四国めたん（あまあま）',
    'VOICEVOX：四国めたん（ノーマル）',
    'VOICEVOX：ずんだもん（ノーマル）',
    'VOICEVOX：四国めたん（セクシー）',
    'VOICEVOX：ずんだもん（セクシー）',
    'VOICEVOX：四国めたん（ツンツン）',
    'VOICEVOX：ずんだもん（ツンツン）',
    'VOICEVOX：春日部つむぎ（ノーマル）',
    'VOICEVOX：波音リツ（ノーマル）',
    'VOICEVOX：雨晴はう（ノーマル）',
    'VOICEVOX：玄野武宏（ノーマル）'
    )
  )

  st.markdown('### 音声合成')
  st.write('こちらの文章で音声ファイルの生成を行いますか？')
  if st.button('開始'):
    comment = st.empty()
    comment.write('音声出力を作成しています')
    def_response = synthsize_speech(input_data, speaker)

    st.audio(def_response.content)
    #points_balance = point_balance()
    st.write("Point Balance : " + f"{point_balance():,}" + " / 10,000,000")
    #st.write(str(point_balance['points'])+ "/10000000" + int(point_balance['points']/10000000*100 + "%") )
    comment.write('完了しました')