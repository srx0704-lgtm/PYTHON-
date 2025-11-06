import streamlit as st
st.write("This is my first app in ISTM634")
st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

st.balloons()
st.progress(0.7)

st.checkbox("Check me out!")
st.button("Click me!")
st.radio("Choose one:", ["Option 1", "Option 2", "Option 3"])
st.selectbox("Select an option:", ["Choice A", "Choice B", "Choice C"])
st.multiselect("Select multiple options:", ["Item 1", "Item 2", "Item 3"])
st.select_slider("Select a range:", ["Low", "Medium", "High"])

st.slider("Select a value:", 0, 100, 50)


st.header("This is a header")
st.markdown("This is a markdown text.")
st.latex(r"E=mc^2")

import streamlit as st
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt

# Title
st.title("Histogram Example")

# Generate 5000 random numbers from N(1, 2)
data = np.random.normal(loc=1, scale=2, size=5000)

# Create the plot
#fig, ax = plt.subplots()
#ax.hist(data, bins=15, color="skyblue", edgecolor="black")
#ax.set_title("Histogram of Normal Distribution (mean=1, std=2)")

# Display in Streamlit
#st.pyplot(fig)

df = pd.DataFrame(np.random.randn(10, 2), columns=['product A', 'product B'])  
print(df)
st.line_chart(df)
st.bar_chart(df)    
st.area_chart(df)

df2 = pd.DataFrame(np.random.randn(500, 2)/[50, 50] + [37.76, -122.4], columns=['lat', 'lon'])
st.map(df2)
print(df2)
df = pd.DataFrame(np.random.randn(10, 2), columns=['product A', 'product B'])
print(df)

