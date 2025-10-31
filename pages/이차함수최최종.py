import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 🎨 배경색을 RGB(203,147,160)으로 지정
st.markdown(
    """
    <style>
    body {
        background-color: rgb(203, 147, 160);
    }
    .stApp {
        background-color: rgb(203, 147, 160);
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("💗 유리함수의 그래프와 평행이동 (디지털 교과서)")

st.markdown("""
이 단원에서는 **유리함수**의 그래프가 어떻게 변하는지를 학습합니다.  
공통수학 교과서의 내용을 토대로, 직접 그래프를 조작하면서 함수의 특징을 탐구해 봅시다.
""")

# ------------------------
# 1️⃣ y = a/x 그래프 학습
# ------------------------
st.header("1️⃣ 함수 y = a/x 의 그래프")

st.markdown("""
- 기본형 **y = a/x** 는 중심이 원점인 쌍곡선입니다.  
- **a**의 부호와 크기에 따라 그래프의 모양이 달라집니다.
""")

a = st.slider("a 값 조절", -5.0, 5.0, 1.0, 0.1)
x = np.linspace(-10, 10, 400)
y = np.where(x != 0, a/x, np.nan)

fig, ax = plt.subplots()
ax.plot(x, y, label=f"y = {a}/x")
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')  # ✅ 격자 크기 일정 유지
ax.grid(True)
ax.legend()
st.pyplot(fig)

st.markdown("""
👉 **관찰:**  
- a > 0이면 1, 3사분면에 그래프가 있습니다.  
- a < 0이면 2, 4사분면에 그래프가 있습니다.  
- |a|가 커질수록 그래프가 더 가파르게 나타납니다.
""")

# ------------------------
# 2️⃣ y = (ax + b)/(cx + d) 그래프
# ------------------------
st.header("2️⃣ 함수 y = (ax + b) / (cx + d)의 그래프")

st.markdown("""
이번에는 분모와 분자가 모두 1차식인 유리함수를 학습해 봅시다.  
단, **c ≠ 0**이어야 하며, 분모가 0이 되는 x값에서는 그래프가 끊어집니다.
""")

a2 = st.slider("a", -5.0, 5.0, 1.0, 0.1)
b2 = st.slider("b", -10.0, 10.0, 0.0, 0.5)
c2 = st.slider("c (0 제외)", -5.0, 5.0, 1.0, 0.1)
if c2 == 0:
    st.warning("⚠️ c의 값이 0이 될 수 없습니다. 자동으로 0.1로 설정됩니다.")
    c2 = 0.1
d2 = st.slider("d", -10.0, 10.0, 0.0, 0.5)

x2 = np.linspace(-10, 10, 400)
y2 = np.where((c2 * x2 + d2) != 0, (a2 * x2 + b2) / (c2 * x2 + d2), np.nan)

fig2, ax2 = plt.subplots()
ax2.plot(x2, y2, label=f"y = ({a2}x + {b2}) / ({c2}x + {d2})")
ax2.axhline(0, color='black', linewidth=1)
ax2.axvline(0, color='black', linewidth=1)
ax2.set_xlim(-10, 10)
ax2.set_ylim(-10, 10)
ax2.set_aspect('equal')
ax2.grid(True)
ax2.legend()
st.pyplot(fig2)

st.markdown("""
👉 **그래프 특징 정리**
- 수직점근선 : cx + d = 0 → x = -d/c  
- 수평점근선 : y = a/c  
- y = a/x 그래프를 **이동·변형한 형태**로 볼 수 있습니다.
""")

# ------------------------
# 3️⃣ 학습 확인 퀴즈
# ------------------------
st.header("3️⃣ 학습 확인 퀴즈")

st.markdown("그래프의 특징을 정확히 이해했는지 퀴즈로 확인해 봅시다.")

with st.form("quiz_form"):
    q1 = st.radio("① y = a/x 에서 a가 음수일 때 그래프는 어느 사분면에 있나요?",
                  ["1, 3사분면", "2, 4사분면", "x축 위"], index=None)

    q2 = st.radio("② y = (ax + b)/(cx + d) 에서 수직점근선은 어디에 있나요?",
                  ["x = -d/c", "y = a/c", "x = 0"], index=None)

    q3 = st.radio("③ y = (ax + b)/(cx + d) 의 수평점근선은?",
                  ["y = a/b", "y = a/c", "y = -d/c"], index=None)

    submit = st.form_submit_button("✅ 답안 제출")

if submit:
    score = 0
    if q1 == "2, 4사분면":
        score += 1
    if q2 == "x = -d/c":
        score += 1
    if q3 == "y = a/c":
        score += 1

    st.subheader(f"🎯 결과: {score}/3 점")

    if score == 3:
        st.success("완벽합니다! 유리함수의 평행이동과 점근선을 정확히 이해했습니다.")
    elif score == 2:
        st.info("좋아요! 한 문제만 더 복습해 봅시다.")
    else:
        st.warning("조금 더 복습이 필요해요. 그래프 변화를 다시 관찰해 보세요.")

# ------------------------
# 마무리
# ------------------------
st.markdown("""
---
✅ **정리**
- y = a/x 는 중심이 원점인 기본 유리함수입니다.  
- y = (ax + b)/(cx + d)는 점근선이 이동한 형태입니다.  
- 수직점근선과 수평점근선을 통해 그래프의 위치와 모양을 파악할 수 있습니다.

💡 **활동 제안:**  
a, b, c, d 값을 바꿔보며 점근선이 어떻게 변하는지 직접 확인해 보세요!
""")
