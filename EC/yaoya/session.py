from enum import Enum

_ = '''
「SessionManger は Streamlit のセッションとデータをやり取りします。
YaEC では見通しの良いコードを目指し、st.session_stateのデータ読取・書込の責務を 
SessionManager で担うようにします。」
'''

class SessionKey(Enum):
    USER = auto()

class StreamlitSessionManager:
    def __init__(self) -> None:
        self._session_state = st.session_state

    def get_user(self) -> User:
        return self._session_state[SessionKey.USER.name]

    def set_user(self, user: User) -> None:
        self._session_state[SessionKey.USER.name] = user