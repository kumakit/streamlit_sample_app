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
  response = requests.post("https://api.tts.quest/v3/voicevox/synthesis?text=" + text + "&speaker=" + speaker_type[speaker])
  res_json = response.json()
  #print(json.dumps(response.json(), indent=4))

  # 音声合成のステータスを確認する
  res_status = requests.get(res_json["audioStatusUrl"]).json()

  # ステータスがTrueになるまで待機する
  while res_status["isAudioReady"] is not True:
      # 一定時間待つ
      time.sleep(0.5)
      # ステータスを再度確認する
      res_status = requests.post(res_json["audioStatusUrl"]).json()

  res_wav = requests.get(res_json["wavDownloadUrl"]).content

  return res_wav

st.title('音声出力アプリ（低速）')
url = "https://voicevox.su-shiki.com/su-shikiapis/ttsquest/"
st.write("このアプリは [WEB版VOICEVOX API（低速）](%s)を利用して音声合成をしています。" % url)

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

    st.audio(def_response)
    comment.write('完了しました')