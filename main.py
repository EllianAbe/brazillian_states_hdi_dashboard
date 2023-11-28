import streamlit as st
import pandas as pd
from tabs import state_tab, comparision_tab


@st.cache_data
def get_data():
    df = pd.read_csv('data/report.csv', sep=',')

    return df

def main():
    state, comparision = st.tabs(['state', 'comparision'])

    df = get_data()

    state_tab.main(state, df)
    comparision_tab.main(comparision, df)

# Page setting
st.set_page_config(layout="wide", page_title="States HDI")
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

main()