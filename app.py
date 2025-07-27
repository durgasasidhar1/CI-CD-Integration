import streamlit as st
st.title("Power calculator")
st.write("Enter a number to calculat its square, cube, and fifth power.")
number = st.number_input("Enter a number:", value=1.0)

# calculate powers
square = number ** 2
cube = number ** 3
fifth_power = number ** 5

# display results
st.write(f"Square: {square}")
st.write(f"Cube: {cube}")
st.write(f"Fifth Power: {fifth_power}")
# display the results in a table
st.write("### Results Table")
st.table({
    "Power": ["Square", "Cube", "Fifth Power"],
    "Value": [square, cube, fifth_power]
})