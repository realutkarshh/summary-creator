import streamlit as st
import nltk
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')

def score_sentence(sentence):
    words = nltk.word_tokenize(sentence.lower())
    stop_words = set(stopwords.words('english'))
    content_words = [word for word in words if word not in stop_words]
    return len(content_words)

def create_summary(paragraph, num_sentences):
    sentences = nltk.sent_tokenize(paragraph)
    sentence_scores = {}
    for sentence in sentences:
        sentence_scores[sentence] = score_sentence(sentence)
    top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    summary = ' '.join(top_sentences)
    return summary

def wrap_text(text, line_length):
    words = text.split()
    lines = []
    current_line = ""
    for word in words:
        if len(current_line.split()) == line_length:
            lines.append(current_line.strip())
            current_line = ""
        current_line += word + " "
    if current_line:
        lines.append(current_line.strip())
    return "\n".join(lines)


st.title("Summary.com")
st.divider()
st.write("Write anything in the text area and then click Done. The program will create a short summary for you")
inp = st.text_area("")
btn = st.button("Done")
if btn:
     st.write("Please note that the summary creator tool is designed to automatically generate a condensed version of a given text. However, it is important to keep in mind that the accuracy of the summary may depend on the length and complexity of the original text. If the original text is too short or lacks sufficient detail, the summary may not provide an accurate representation of the content. Therefore, we recommend that you use the summary as a starting point and carefully review the original text to ensure that you have not missed any important details. Thank You")
     data = wrap_text(create_summary(inp, num_sentences=2),11)
     code_container = st.container()
     with code_container:
        st.code(data, language='None')
        code_container.markdown(
            f"""
            <style>
            .css-1aumxhk {{
                max-height: 300px;
                overflow-y: scroll;
            }}
            </style>
            """,
            unsafe_allow_html=True,
        )



