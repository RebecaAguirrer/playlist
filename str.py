from pytube import Playlist
import streamlit as st
final = ''
st.title('Gerador de Urls de Videos de playList Youtube')
try:
    
    with st.form(key='form'):
        playlist = st.text_input('Url da Playlist')
        enviar = st.form_submit_button('Gerar')
        p = Playlist(playlist)
        if enviar:
            for v in p.video_urls:
                final = final + v+"\n"
                
    st.text_area('Urls da Playlist',final,300)
except:
    st.error('Url Inválida, a Url necessita ser uma playlist do YouTube')