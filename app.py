import streamlit as st
import os
from transformers import LlamaForCausalLM, LlamaTokenizer
import torch

st.set_page_config(page_title="🦙💬 EMGerman Llama2 Chatbot")

@st.cache_resource()
def ChatModel():
    path = 'jphme/em_german_7b_v01'
    tokenizer = LlamaTokenizer.from_pretrained(path)
    model = LlamaForCausalLM.from_pretrained(
            path,
            torch_dtype=torch.float32,
            device_map='auto')
    return model

with st.sidebar:
    st.title('🦙💬 EMGerman Llama2 Chatbot')

    chat_model = ChatModel()

if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "Wie kann Ich heute Ihnen helfen?"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "Wie kann Ich heute Ihnen helfen?"}]
st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

def ask_model(instruct, system='Du bist ein hilfreicher Assistent.'):
    prompt=f"{system} USER: {instruct} ASSISTANT:"
    path = 'jphme/em_german_7b_v01'
    tokenizer = LlamaTokenizer.from_pretrained(path)
    input = tokenizer(prompt, return_tensors="pt").to(chat_model.device)
    output = chat_model.generate(**input,  max_new_tokens=5)[0]
    answer = tokenizer.decode(output, skip_special_tokens=True)
    return answer

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Ich denke. Bleiben Sie bitte geduldig..."):
            response = ask_model(prompt)
            placeholder = st.empty()
            full_response = ''
            for item in response:
                full_response += item
                placeholder.markdown(full_response)
            placeholder.markdown(full_response)
    message = {"role": "assistant", "content": full_response}
    st.session_state.messages.append(message)
