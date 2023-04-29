import streamlit as st
import src.utils as utl
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="Self.Translate",
    page_icon="🦌",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)
html = """
<div class="container">
    <div class="static">self.</div>
        <ul class="dynamic">
            <li><span>translate</span></li>
            <li><span>traduire</span></li>
            <li><span>tradurre</span></li>
            <li><span>traducir</span></li>
        </ul>
</div>

<p>Translate text in any language!</p>
<p> or chat with a chatbot with any specified language :D </p>

"""

utl.read_markdown(html)

utl.read_css("frontend/streamlit.css")

col1, col2 = st.columns([0.4,3])

with col1:
    if st.button("translation"):
        switch_page("translate")

with col2:
    if st.button("about us"):
        switch_page("about")