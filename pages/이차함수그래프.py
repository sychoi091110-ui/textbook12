import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("📈 유리함수 그래프 학습기")
st.markdown("### 두 가지 유리함수의 그래프를 시각적으로 학습해보세요!")

# 사이드바에서 함수 선택
func_type = st.sidebar.radio(
    "그래프 유형을 선택하세요:",
    ["y = a / (x - k)", "y = (a*x + b) / (c*x + d)"]
)

x = np.linspace(-10, 10, 1000)

# 함수 1: y = a / (x - k)
if func_type == "y = a / (x - k)":
    st.sidebar.subheader("매개변수 조정")
    a = st.sidebar.slider("a", -10.0, 10.0, 1.0, step=0.1)
    k = st.sidebar.slider("k", -5.0, 5.0, 0.0, step=0.1)
    
    y = a / (x - k)
    
    # 그래프
    fig, ax = plt.subplots(figsize=(8,5))
    ax.plot(x, y, label=f"y = {a}/(x - {k})", color='b')
    
    # 점근선 표시
    ax.axvline(k, color='r', linestyle='--', label=f"x = {k} (수직 점근선)")
    ax.axhline(0, color='g', linestyle='--', label="y = 0 (수평 점근선)")
    
    ax.set_ylim(-10, 10)
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)

# 함수 2: y = (a*x + b) / (c*x + d)
else:
    st.sidebar.subheader("매개변수 조정")
    a = st.sidebar.slider("a", -5.0, 5.0, 1.0, step=0.1)
    b = st.sidebar.slider("b", -5.0, 5.0, 0.0, step=0.1)
    c = st.sidebar.slider("c", -5.0, 5.0, 1.0, step=0.1)
    d = st.sidebar.slider("d", -5.0, 5.0, 0.0, step=0.1)

    denom = c * x + d
    y = (a * x + b) / denom

    fig, ax = plt.subplots(figsize=(8,5))
    ax.plot(x, y, label=f"y = ({a}x + {b}) / ({c}x + {d})", color='b')
    
    # 점근선 표시
    if c != 0:
        x_asym = -d / c
        ax.axvline(x_asym, color='r', linestyle='--', label=f"x = {x_asym:.2f} (수직 점근선)")
    if c != 0:
        y_asym = a / c
        ax.axhline(y_asym, color='g', linestyle='--', label=f"y = {y_asym:.2f} (수평 점근선)")
    
    ax.set_ylim(-10, 10)
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)

st.markdown("---")
st.markdown("💡 **Tip:** 슬라이더를 움직이며 점근선과 그래프의 위치 변화를 관찰해보세요!")
