import yaml
import streamlit as st
import streamlit_authenticator as stauth
from env_settings import EnvSettings

env_settings = EnvSettings()

with open('./credentials.yaml') as file:
    config = yaml.load(file, Loader=yaml.SafeLoader)
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    with st.sidebar:
        st.write(f'Welcome *{name}*')
        authenticator.logout('Logout', 'main')

    st.title('Some content')
    with st.expander("See explanation"):
        st.write(
            """
        The chart above shows some numbers I picked for you.
            I rolled actual dice for these, so they're *guaranteed* to
            be random."""
        )
        st.image("https://static.streamlit.io/examples/dice.jpg")

    with st.expander("See explanation"):
        st.write(
            """
        The chart above shows some numbers I picked for you.
            I rolled actual dice for these, so they're *guaranteed* to
            be random."""
        )
        st.image("https://static.streamlit.io/examples/dice.jpg")

elif authentication_status is False:
    st.error('Username/password is incorrect')
elif authentication_status is None:
    st.warning('Please enter your username and password')
