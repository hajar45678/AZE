import streamlit as st 
import pandas as pd
with st.sidebar:
    x=st.radio('pick your henger ',["page 1","page 2","page 3"])
table=pd.DataFrame({"column 1":[1,2,3,4,5,6,7],"column 2":[11,12,13,14,15,16,17]})
if (x=="page 1"):
    st.image("WhatsApp Image 2024-03-03 at 11.28.49_8dd3b47c.jpg",caption="this my image")
    st.audio("WhatsApp Audio 2024-03-03 at 11.17.10_fc26d21b.opus")
    st.video("stock-footage-nature-river-waterfall-forest-sun-morning-magical.webm")
elif(x=="page 2"):
    st.write("## H2")
    st.metric(label="wind spead",value="120mS",delta="1.4ms")
    st.table(table)
    st.dataframe(table)
else:
    st.title("hi I'm streamlit web app!!")
    st.markdown("""
    <style>
    .
               </style> 
    """,unsafe_allow_html=True)
    st.subheader("hi I'm your subheader ")
    st.header("i'm header")
    st.text("hi i'm text")
    st.markdown("---")
    st.markdown("[google](https://www.google.com)")
    st.caption("hi i'm caption")
    st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")
    json={"a":"1,2,3","b":"4,5,6"}
    st.json(json)
    code="""print("hello world)
    def funct():
    return 0;"""
    st.code(code,language="python")
   
