import streamlit as st

with st.container():
    st.subheader("사용자 정보 입력")
    name=st.text_input('과목명을 입력해 주세요')
    page=st.text_input(f'{name}의 시험범위를 입력해주세요')
 
a=[]
st.button('저장하기')

