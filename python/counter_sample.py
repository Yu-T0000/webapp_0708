import streamlit as st

st.title("Counter Example")
if "count" not in st.session_state: # session_stateがcountを保持してない時
    st.session_state.count = 0 # countに0代入

increment = st.button("Increment") # 「Increment」ボタン
if increment:
    st.session_state.count += 1 # countに+1

st.write("Count = ", st.session_state.count) # 書き込み