import streamlit as st

view = [100, 78, 4, 30]

st.write('# View List')

st.write('## raw data')
view

st.write('## bar chart')
st.bar_chart(view)

st.write('## line chart')
st.line_chart(view)


topics = [
    {'id':1, 'title':'html', 'view':100},
    {'id':2, 'title':'css', 'view':50},
    {'id':3, 'title':'js', 'view':140}
]

