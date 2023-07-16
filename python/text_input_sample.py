import streamlit as st

st.title("InputText using Callbacks")

st.text_input("Message", key="text_input") # 入力欄の名前(ラベル),多分ここでst.session_state["text_input"]に"無"が作られてる

def change_value():
    st.session_state["text_input"] = "Hello, World" # st.session_state["text_input"]をHello Worldに設定


st.button("Click", on_click=change_value) # ボタン押されたら真っ先にchange_valueを実行してね


_ = '''
#StreamlitAPIExceptionエラーが起きる

st.text_input("Message", key="text_input")


if st.button("Click"):
    st.session_state["text_input"] = "Hello, World"

ボタンが押される/入力されると上から処理をし直すので、
まず最初にst.text_input("Message", key="text_input")でst.session_state["text_input"]がウィジェットを取得
設定後の値変更はできない(st.session_state.text_input cannot be modified after 
the widget with key text_input is instantiated.)のでエラーが起きる。

コールバック使ってる方は
ボタン押されてない：
st.text_input("Message", key="text_input")でst.session_state["text_input"]が設定される

ボタン押された：
最初にst.session_state["text_input"] = "Hello, World"でst.session_state["text_input"]の値が設定される
↓
st.text_input("Message", key="text_input")でst.session_stateのtext_inputから値を持ってくる

'''