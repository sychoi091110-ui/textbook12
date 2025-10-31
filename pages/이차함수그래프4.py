import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="유리함수의 그래프 학습", layout="centered")

# -------------------------------
# 🏫 교과서형 제목 및 개념 도입
# -------------------------------
st.title("📘 유리함수의 그래프 이해하기")
st.markdown("""
### 1️⃣ y = a/x 의 그래프  
이 함수는 **y = 1/x** 의 그래프를 기준으로, **a의 값**에 따라 그래프의 모양이 달라집니다.

- a > 0 : 1, 3사분면에 위치  
- a < 0 : 2, 4사분면에 위치  
- |a|가 커질수록 그래프가 **가늘어짐**  
- |a|가 작을수록 그래프가 **넓어짐**
""")

# -------------------------------
# 🎚️ a 값 조절 (y = a/x)
# -------------------------------
a = st.slider("a 값 선택", -5.0, 5.0, 1.0, 0.1)

x = np.linspace(-10, 10, 500)
y = a / x

# -------------------------------
# 📊 그래프 출력 (격자 고정)
# -------------------------------
fig, ax = plt.subplots(figsize=(6, 6))
ax.plot(x, y, color='royalblue', label=f"y = {a}/x")
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend()

# 격자 크기 고정
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal', adjustable='box')

st.pyplot(fig)

st.markdown("""
### 📖 관찰 포인트
- a값이 커질수록 그래프는 x축에 가까워지며 가늘어짐  
- a값이 작아질수록 그래프는 퍼짐  
- 부호에 따라 그래프의 위치가 바뀜
""")

# -------------------------------
# 2️⃣ y = (a x + b) / (c x + d)
# -------------------------------
st.markdown("""
---
### 2️⃣ y = (a x + b) / (c x + d) 의 그래프

이 함수는 일반적인 유리함수로, **x = -d/c**에서 정의되지 않으며,  
**수평·수직 점근선**이 나타납니다.

- 수직 점근선: x = -d/c  
- 수평 점근선: y = a/c  
""")

# 슬라이더로 계수 조절
a2 = st.slider("a 값", -5.0, 5.0, 1.0, 0.1, key="a2")
b2 = st.slider("b 값", -10.0, 10.0, 0.0, 0.5, key="b2")
c2 = st.slider("c 값", -5.0, 5.0, 1.0, 0.1, key="c2")
d2 = st.slider("d 값", -10.0, 10.0, 0.0, 0.5, key="d2")

x2 = np.linspace(-10, 10, 1000)

fig2, ax2 = plt.subplots(figsize=(6, 6))

if c2 != 0:
    # 일반적인 유리함수
    y2 = (a2 * x2 + b2) / (c2 * x2 + d2)
    ax2.plot(x2, y2, color='tomato', label=f"y = ({a2}x + {b2}) / ({c2}x + {d2})")

    # 점근선 표시
    ax2.axvline(-d2 / c2, color='gray', linestyle='--', label='수직 점근선')
    ax2.axhline(a2 / c2, color='purple', linestyle='--', label='수평 점근선')

else:
    # c = 0일 때 → 일차함수 y = (a/d)x + (b/d)
    if d2 != 0:
        y2 = (a2 / d2) * x2 + (b2 / d2)
        ax2.plot(x2, y2, color='green', label=f"y = ({a2/d2:.2f})x + ({b2/d2:.2f})")
        st.info("✅ c = 0일 때, 유리함수는 일차함수 y = (a/d)x + (b/d) 형태가 됩니다.")
    else:
        st.error("⚠️ a, b, c, d가 모두 0이 되면 함수가 정의되지 않습니다.")

ax2.axhline(0, color='black', linewidth=1)
ax2.axvline(0, color='black', linewidth=1)
ax2.grid(True, linestyle='--', alpha=0.5)
ax2.legend()

# 격자 고정
ax2.set_xlim(-10, 10)
ax2.set_ylim(-10, 10)
ax2.set_aspect('equal', adjustable='box')

st.pyplot(fig2)

# -------------------------------
# ✏️ 학습 확인 퀴즈
# -------------------------------
st.markdown("""
---
### 3️⃣ 학습 확인 퀴즈

다음 중 y = a/x의 그래프 변화에 대한 설명으로 **옳지 않은 것**은 무엇일까요?

A. a가 커질수록 그래프는 y축에 가까워진다  
B. a < 0일 때 그래프는 2,4사분면에 위치한다  
C. |a|가 작아질수록 그래프가 퍼진다  
D. a = 0이면 그래프는 x축 위의 직선이 된다
""")

quiz = st.radio("정답 선택", ["A", "B", "C", "D"])

if quiz:
    if quiz == "A":
        st.error("❌ 틀렸습니다. a가 커질수록 그래프는 **x축에 가까워집니다.**")
    elif quiz == "B":
        st.success("✅ 정답입니다!")
    elif quiz == "C":
        st.error("❌ 틀렸습니다. |a|가 작아질수록 그래프가 퍼집니다.")
    else:
        st.info("🟡 a = 0이면 유리함수가 정의되지 않습니다.")
