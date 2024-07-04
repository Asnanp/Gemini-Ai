import os
from PIL import Image
from streamlit_option_menu import option_menu
import streamlit as st
from gemini_utility import (load_gemini_pro_model, gemini_pro_vision_response)

working_directory = os.path.dirname(os.path.abspath(__file__))

st.set_page_config(page_title="Gemini AI by Asnan", page_icon="🔬", layout="centered")

with st.sidebar:
    selected = option_menu("Gemini AI by Asnan",
                           ['ChatBox', 'Image Caption', 'Enhanced Text', 'Ask me anything'],
                           menu_icon='robot',
                           icons=['chat-dots-fill', 'card-image', 'question-circle-fill', 'question-circle-fill'],
                           default_index=0)

def translate_role_for_streamlit(user_role):
    if user_role == 'model':
        return 'assistant'
    else:
        return user_role

if selected == 'ChatBox':

    model = load_gemini_pro_model()

    if "chat_session" not in st.session_state:
        st.session_state.chat_session = model.start_chat(history=[])

    st.title('🤖 ChatBox by Asnan')

    # display the history by the user
    for message in st.session_state.chat_session.history:
        with st.chat_message(translate_role_for_streamlit(message.role)):
            st.markdown(message.parts[0].text)

    # input field for user's message
    user_prompt = st.chat_input('Ask Gemini-pro prompt by Asnan...')

    if user_prompt:
        st.chat_message("user").markdown(user_prompt)

        gemini_response = st.session_state.chat_session.send_message(user_prompt)

        # display gemini-pro response
        with st.chat_message('assistant'):
            st.markdown(gemini_response.text)

elif selected == 'Image Caption':
    st.title('📸 Snap Narrate')

    upload = st.file_uploader('Upload an image', type=['jpg', 'jpeg', 'png'])

    if upload is not None:
        image = Image.open(upload)

        col1, col2 = st.columns(2)

        with col1:
            resized_image = image.resize((800, 500))
            st.image(resized_image)

        default_prompt = "Write a short caption for the image"
        caption = gemini_pro_vision_response(default_prompt, image)

        with col2:
            st.info(caption)
    else:
        st.warning("Please upload an image before generating a caption.")

elif selected == 'Enhanced Text':
    st.title('📝 Enhanced Text')
    st.write("This feature is under development. Please check back later!")
