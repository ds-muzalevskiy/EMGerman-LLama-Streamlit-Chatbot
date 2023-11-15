# EMGerman-LLama-Streamlit-Chatbot
**Streamlit App for Chatbot creation using EMGerman LLama 2 model**

This repo is designed for the Streamlit Web application for EMGerman LLama 2 model. Using Streamlit, one can easily create a prototype to test different ideas/approaches and also use it for the showcase of these ideas to bigger audience. 

Most of contemporary custom LLMs were trained using mostly textual information in English and EMGerman is one of the few current custom models that was trained on German text corpus and therefore achieves really good results in different tasks such as Text Generation and named entity recognition (NER). 

Streamlit: https://streamlit.io/

EMGerman: https://github.com/jphme/EM_German

LLama2 Paper: https://arxiv.org/abs/2307.09288

**To run the app all you need is:**

1. Clone this repo to your local machine using git clone and change the directory:

```
git clone https://github.com/ds-muzalevskiy/EMGerman-LLama-Streamlit-Chatbot.git
cd EMGerman-LLama-Streamlit-Chatbot-main
```

2. Create a virtual env and start using it (optionally you can use conda as well):

```
python -m venv venv
source venv/bin/activate  
```

3. Install required Python packages:

```
pip install -r requirements.txt 
```

4. Run the app using Streamlit:
```
streamlit run app.py
```

If everything went fine, you should be able to see similar screen and have a chance to interact with the app :)


![streamlit](https://github.com/ds-muzalevskiy/EMGerman-LLama-Streamlit-Chatbot/assets/74115150/4721216e-8c6a-4b45-b6cd-73508e2d5efd)
