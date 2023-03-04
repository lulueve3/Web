import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
import time



def Du_Doan():
    # Tạo Listbox cho phép người dùng chọn trang
    st.header("Dự đoán Output từ tập Input")
    page = st.selectbox("Chọn số lượng input", ["1 Input", "2 Input", "3 Input"])
    # Nếu người dùng chọn Trang chủ, cập nhật URL và chuyển đến trang tương ứng
    if page == "1 Input":
        st.experimental_set_query_params(page="1 Input")
        Input_1()
    elif page == "2 Input":
        st.experimental_set_query_params(page="2 Input")
        Input_2()
    else:
        st.experimental_set_query_params(page="3 Input")
        Input_3()

def Input_1():
    try:
        # Chờ nguoiw dùng nhập dữ liệu
        st.write("Vui lòng nhập đủ số lượng input và output (Bằng nhau)")
        input_str = st.text_input("Nhập dữ liệu cho input (cách nhau bằng dấu .):")
        if input_str != '':
            x = np.array(input_str.split(",")).astype(float)
        output_str = st.text_input("Nhập dữ liệu cho output (cách nhau bằng dấu .):")
        if output_str != '':
            y = np.array(output_str.split(",")).astype(float)

        # while x.size != y.size or x.size == 0:
        #     if input_str != '':
        #         x = np.array(input_str.split(",")).astype(float)
        #     if output_str != '':
        #         y = np.array(output_str.split(",")).astype(float)
        df = pd.DataFrame({"Input": x, "Output": y})
        st.write(df)
        regr = LinearRegression()
        regr.fit(x.reshape(-1, 1),y)
        fig = plt.figure()
        plt.xlabel("Input")
        plt.ylabel("Output")
        plt.scatter(x,y,color ='red')
        plt.plot(x,regr.predict(x.reshape(-1, 1)),color ='blue')
        st.pyplot(fig)
        input_str = st.text_input("Nhập dữ liệu để dự đoán (cách nhau bằng dấu ,):")
        if input_str != '':
            z = np.array(input_str.split(",")).astype(float)
        st.write("Kết quả dự đoán là: ")
        for i in z:
            st.write(str(regr.predict([[i]])))
    except:
        pass

def Input_2():
    st.write("3 input")
def Input_3():
    st.write("4 input")
    
def about():
    st.write("Đây là trang giới thiệu")

def contact():
    st.write("Đây là trang liên hệ")



# Tạo navigation cho trang web
menu = ["Trang chủ", "Giới thiệu", "Liên hệ"]
choice = st.sidebar.selectbox("Chọn trang", menu)

# Hiển thị trang tương ứng với lựa chọn
if choice == "Trang chủ":
    Du_Doan()
elif choice == "Giới thiệu":
    about()
else:
    contact()
