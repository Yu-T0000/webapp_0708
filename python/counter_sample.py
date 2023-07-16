import streamlit as st

_ = ''' # なんか変数化しないとコメントアウトされないっぽい
st.title("Counter Example")
if "count" not in st.session_state: # session_stateがcountを保持してない時(初期化対策)
    st.session_state.count = 0 # countに0代入

increment = st.button("Increment") # 「Increment」ボタン 押されたタイミングでincrementにTrue
if increment:
    st.session_state.count += 1 # countに+1

st.write("Count = ", st.session_state.count) # 書き込み

'''

st.title("Counter Example using Callbacks") # コールバック関数を使うパターン
if "count" not in st.session_state:
    st.session_state.count = 0

def increment_counter():    # 足し算するよ
    st.session_state.count += 1

st.button("Increment", on_click=increment_counter) # 押されたらincrement_counter()実行してね

st.write("Count = ", st.session_state.count)

_ = ''' 

increment = st.button("Increment")
if increment:
    st.session_state.count += 1
st.write("Count = ", st.session_state.count)
と、
def increment_counter():
    st.session_state.count += 1
st.button("Increment", on_click=increment_counter)
st.write("Count = ", st.session_state.count)
の違いって何？
↓
if条件分岐だと押されたか押されてないかをチェックしてそれぞれの処理をする
(=押されなかった際の処理が存在する。elseがなくても「何もしないを実行する」みたいな...)

コールバックだと押された時だけ紐づけられた処理を実行する
(=押されなかった際の処理ってやつがない)

'''