import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import seaborn as sns

def load_data():
    return pd.read_csv('data/most_followed_ig.csv')

df = load_data()
cat1 = df.groupby('CATEGORIES 1').agg(np.mean)
cat2 = df.groupby('CATEGORIES 2').agg(np.mean)

#st.sidebar.image('')

def home(title):
    st.title(title)
    #st.image('')
    #st.write('')

def page1(title):
    st.title(title)
    if st.checkbox('show raw data'):
        x = st.sidebar.slider('choose the number of rows', min_value=10, value=10, max_value=df.shape[0])
        st.write(df.head(x))
    st.plotly_chart(px.scatter(df, 'FOLLOWERS', 'MEDIA POSTED'))
    st.info("here we can see number of posted media doesn't have a strong affect on  followers")
    st.plotly_chart(px.scatter(df, 'FOLLOWERS', 'ER'))
    st.info("Even engagement rate of all media doesn't seem to have a strong relationship with followers")
    st.plotly_chart(px.line(df, 'RANK', 'MEDIA POSTED'))
    st.info("we can see in this graph the rank doesn't have to do anything with the number of media posted")
    st.plotly_chart(px.line(df, 'RANK', 'FOLLOWERS'))
    st.info("The dataset is ranked by number of followers.")
    st.plotly_chart(px.line(df, 'RANK', 'ER'))
    st.plotly_chart(px.scatter(df, 'FOLLOWERS', 'iPOSTS ON HASHTAG'))
    st.plotly_chart(px.scatter(df, 'ER', 'MEDIA POSTED'))
    st.plotly_chart(px.scatter(df, 'RANK', 'iPOSTS ON HASHTAG'))
    
def page2(title):
    st.title(title)
    if st.checkbox('show raw data'):
        st.write(cat1)
    st.plotly_chart(px.pie(df, names='CATEGORIES 1'))
    st.info('our dataset has mostly celebrities.')
    st.plotly_chart(px.bar(cat1, 'FOLLOWERS', cat1.index))
    st.info('On average, Entertainment category has most followers.')
    st.plotly_chart(px.bar(cat1, 'MEDIA POSTED', cat1.index))
    st.info('On average, Entertainment has most posts as well.')
    st.plotly_chart(px.bar(cat1, 'iPOSTS ON HASHTAG', cat1.index))
    st.info('Although, beverages have most posts on Hashtags.')

def page3(title):
    st.title(title)
    if st.checkbox('show raw data'):
        st.write(cat2)
    st.plotly_chart(px.pie(df, names='CATEGORIES 2'))
    st.info('our dataset has mostly musician celebrities.')
    st.plotly_chart(px.bar(cat2, 'FOLLOWERS', cat2.index))
    st.info('On Average, models have most followers.')
    st.plotly_chart(px.bar(cat2, 'MEDIA POSTED', cat2.index))
    st.info('On average, basketball has more posts then any other category.')
    st.plotly_chart(px.bar(cat2, 'iPOSTS ON HASHTAG', cat2.index))
    st.info('On average, luxury posts have most numbers in hashtags.')

pages = {
    'Introduction': home,
    'Analysis': page1,
    'Category 1 Analysis': page2,
    'Category 2 Analysis': page3,
    }

page = st.sidebar.selectbox('choose a page', list(pages.keys()))
pages[page](page)
