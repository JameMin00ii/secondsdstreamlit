import streamlit as st
import pandas as pd

with st.echo():
    st.title("Get streamlit")
    st.write("This is introduction to stramlit")

    st.write("## code")
    st.markdown("*Streamlit* is **really** ***cool***.")
    st.markdown('''
        :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
        :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')

    code = '''def hello():
        print("Hello, Streamlit!")'''

    Showcode_btn = st.button("Run!")
    if Showcode_btn:
        st.code(code, language="python")    


    cols = st.columns(2)
    with cols[0]:
        age_input = st.number_input("Input your age")
        st.markdown(f"This is your age{age_input}")

    # st.markdown("#NLP Task")
    with cols[1]:
        text_input = st.text_input("Input your text")
        word_tokenize = " | ".join(text_input.split())
        st.markdown(f"{word_tokenize}")

    df = pd.DataFrame({
        'first column':[1,2,3,4],
        'second column':[10,20,60,90]
    })
    st.dataframe(df)
    show_chart_btn = st.button("Show Chart")
    if show_chart_btn:
        st.line_chart(df, x='first column',y='second column')