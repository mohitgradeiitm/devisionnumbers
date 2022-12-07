import numpy as np
import pandas as pd
import streamlit as st


def main():
  
  if(num1==0 or num2==0):
    result = 0
  else:
    result=num1/num2
  
  st.success('The output is {}'.format(result))
  
st.title("Division of Two Numbers")
 
num1 = st.number_input("Number 1")
num2 = st.number_input("Number 2")  
  
if st.button("Calculate result"):
    main()
    
    
    
    
