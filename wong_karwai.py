import time
import streamlit as st
from aitextgen import aitextgen

st.set_page_config(layout="centered")

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

st.title("Wong Kar-W'A.I.'")
st.subheader("Director Wong Kar-Wai Style Script Generator")

st.markdown("""---""")

col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image("wong_karwai_images.gif",'Images from DALL-E')

with col3:
    st.write(' ')


with st.expander("LIST OF TRAINED SCRIPTS & TOOL"):
    st.write("Days of Being wild (1990) [link](https://www.imdb.com/title/tt0101258/)")
    st.write("Chungking Express (1994) [link](https://www.imdb.com/title/tt0109424/)")
    st.write("Happy Together (1997) [link](https://www.imdb.com/title/tt0118845/)")
    st.write("In the Mood for Love (2000) [link](https://www.imdb.com/title/tt0118694/)")
    st.write("2046 (2004) [link](https://www.imdb.com/title/tt0212712/)")
    st.write("My Blueberry Nights (2007) [link](https://www.imdb.com/title/tt0765120/)")
    st.write("aitextgen [link](https://docs.aitextgen.io/)")

st.markdown("""---""")

st.subheader("TYPE ANYTHING")
st.write("Then it will automatically create a scene.")
input_prompt = st.text_input("")

@st.cache(persist=True, allow_output_mutation=True)
def load_model():
    ai_generate = aitextgen(model_folder='trained_model',
                        tokenizer_file='aitextgen.tokenizer.json')
    return ai_generate

makebtn = st.button("MAKE SCRIPT")

if makebtn : 
    tmp_aigenerate = load_model()
    generated_text = tmp_aigenerate.generate_one(prompt=input_prompt, max_length=64)
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.02)
        my_bar.progress(percent_complete + 1)
    st.success(generated_text + "...")
else : 
    st.write('')


