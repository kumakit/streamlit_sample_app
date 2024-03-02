import streamlit as st
from bs4 import BeautifulSoup
import requests
from os import replace
import urllib.parse
import json
import io

import streamlit.components.v1 as stc
import base64
import time

def todays_wether():
    url= 'https://weathernews.jp/onebox/tenki/tokyo/13201/'
    res=requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    title = soup.find('div',{'class': 'comment no-ja pc'}).find_all('p')[0].text
    comment = soup.find('div',{'class': 'comment no-ja pc'}).find_all('p')[1].text
    to_day = soup.find('div',{'class':'wTable__day'}).find('p',{'class':'wTable__item'}).text
    temp_h = soup.find('p',{'class':'temp__h'}).find('span',{'class':'text wTable__item'}).text
    temp_l = soup.find('p',{'class':'temp__l'}).find('span',{'class':'text wTable__item'}).text
    am_raynyp = soup.find_all('span',{'class':'text wTable__item'})[2].text
    pm_raynyp = soup.find_all('span',{'class':'text wTable__item'})[3].text
    to_day = to_day.replace("(","").replace(")","")
    temp_h = temp_h.replace("℃","").replace("-","マイナス")
    temp_l = temp_l.replace("℃","").replace("-","マイナス")
    am_raynyp = am_raynyp.replace("%","％")
    pm_raynyp= pm_raynyp.replace("%","％")

    wether_text = f'{to_day}曜日、八王子市の天気をお知らせします。 {title}。 {comment} 最高気温は{temp_h}度、最低気温は{temp_l}度です。降水確率は午前{am_raynyp}、午後{pm_raynyp}になります。'
    return wether_text

def synthsize_speech(input_text):

    # 音素データ生成
    text = urllib.parse.quote(input_text)
    response = requests.get("https://deprecatedapis.tts.quest/v2/voicevox/audio/?key=Y5R236H-n8r1934&speaker=3&pitch=0&intonationScale=1&speed=1&text="+ text)

    return response

def point_balance():
    results = requests.get("https://deprecatedapis.tts.quest/v2/api/?key=Y5R236H-n8r1934")
    results_json = results.json()
    points = results_json['points']

    return points

st.title('ずんだもんの八王子天気予報')
url = "https://voicevox.su-shiki.com/su-shikiapis/#step3"
st.write("このアプリは [WEB版VOICEVOX API（高速）](%s)を利用して音声合成をしています。" % url)
st.markdown('### 天気予報の音声出力')

wether_data = None
if st.button('VOICEVOX：ずんだもん（ノーマル）で八王子の天気予報を音声出力すする！'):
    wether_data = todays_wether()
    st.info(wether_data)
    comment = st.empty()
    comment.write('音声出力を作成しています')

    audio_placeholder = st.empty()
    contents = synthsize_speech(wether_data).content #入力する音声ファイル

    audio_str = "data:audio/ogg;base64,%s" % (base64.b64encode(contents).decode())
    audio_html = """
                    <audio autoplay=True>
                    <source src="%s" type="audio/ogg" autoplay=True>
                    Your browser does not support the audio element.
                    </audio>
                """ %audio_str

    audio_placeholder.empty()
    time.sleep(0.5) #これがないと上手く再生されません
    audio_placeholder.markdown(audio_html, unsafe_allow_html=True)


    #points_balance = point_balance()
    st.write("Point Balance : " + f"{point_balance():,}" + " / 10,000,000")
    #st.write(str(point_balance['points'])+ "/10000000" + int(point_balance['points']/10000000*100 + "%") )
    comment.write('完了しました')