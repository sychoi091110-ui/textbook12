import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="이차함수의 그래프 이동 학습", layout="centered")

st.title("📈 이차함수 y = a(x - p)² + q 그래프의 특징 학습 앱")
st.write("이 앱은 이차함수의 **표준형 그래프**가 `p`와 `q` 값에 따라 어떻게 이동하는지를 시각적으로 학습하도록 설계되었습니다.")

st.divider()

# 1️⃣ Step 1: y = a(x - p)² 그래프에서 p의 변화 관찰
st.header("1️⃣ p 값이 변할 때 그래프의 이동")
st.write("아래 슬라이더로 **p** 값을 바꾸며 그래프가 x축 방향으로 어떻게 이동하는지 관찰하세요.")

a1 = st.slider("a 값 (기울기/폭 조절)", -2.0, 2.0, 1.0, 0.1)
p1 = st.slider("p 값 (x축 이동)", -5.0, 5.0, 0.0, 0.5)

x = np.linspace(-10, 10, 400)
y1 = a1 * (x - p1)**2

fig1, ax1 = plt.subplots()
ax1.plot(x, y1, label=f"y = {a1}(x - {p1})²")
ax1.plot(x, a1 * x**2, "--", label="기준 y = a·x²", color="gray")
ax1.legend()
ax1.grid(True)
ax1.set_xlabel("x")
ax1.set_ylabel("y")
st.pyplot(fig1)

st.info("👉 p가 양수일 때는 **오른쪽으로**, 음수일 때는 **왼쪽으로** 그래프가 이동합니다.")

st.divider()

# 2️⃣ Step 2: y = a·x² + q 그래프에서 q의 변화 관찰
st.header("2️⃣ q 값이 변할 때 그래프의 이동")
st.write("이번에는 **q** 값을 바꾸며 y축 방향 이동을 확인해 봅시다.")

a2 = st.slider("a 값 (기울기/폭 조절, q 이동용)", -2.0, 2.0, 1.0, 0.1, key="a2")
q2 = st.slider("q 값 (y축 이동)", -5.0, 5.0, 0.0, 0.5)

y2 = a2 * x**2 + q2

fig2, ax2 = plt.subplots()
ax2.plot(x, y2, label=f"y = {a2}x² + {q2}")
ax2.plot(x, a2 * x**2, "--", label="기준 y = a·x²", color="gray")
ax2.legend()
ax2.grid(True)
ax2.set_xlabel("x")
ax2.set_ylabel("y")
st.pyplot(fig2)

st.info("👉 q가 양수일 때는 **위로**, 음수일 때는 **아래로** 그래프가 이동합니다.")

st.divider()

# 3️⃣ Step 3: y = a(x - p)² + q 에서 p와 q 동시 조작
st.header("3️⃣ p와 q를 동시에 바꿔보며 전체 이동 확인")
st.write("이제 p와 q를 함께 조절해, 그래프가 어떻게 평행이동하는지 살펴봅시다.")

a3 = st.slider("a 값", -2.0, 2.0, 1.0, 0.1, key="a3")
p3 = st.slider("p 값", -5.0, 5.0, 0.0, 0.5, key="p3")
q3 = st.slider("q 값", -5.0, 5.0, 0.0, 0.5, key="q3")

y3 = a3 * (x - p3)**2 + q3

fig3, ax3 = plt.subplots()
ax3.plot(x, y3, label=f"y = {a3}(x - {p3})² + {q3}")
ax3.plot(x, a3 * x**2, "--", label="기준 y = a·x²", color="gray")
ax3.legend()
ax3.grid(True)
ax3.set_xlabel("x")
ax3.set_ylabel("y")
st.pyplot(fig3)

st.info(f"👉 꼭짓점은 ({p3}, {q3})에 위치합니다.")

st.divider()

# 4️⃣ Step 4: 개념 확인 퀴즈
st.header("4️⃣ 퀴즈로 개념 확인하기 🎯")

st.write("다음 중 옳은 설명을 모두 고르세요.")
quiz_options = st.multiselect(
    "이차함수의 그래프 이동에 대한 설명:",
    [
        "p가 커질수록 그래프는 오른쪽으로 이동한다.",
        "q가 커질수록 그래프는 아래로 이동한다.",
        "p가 음수이면 그래프는 왼쪽으로 이동한다.",
        "q가 음수이면 그래프는 위로 이동한다.",
        "꼭짓점의 좌표는 (p, q)이다."
    ]
)

if st.button("정답 확인"):
    correct = {"p가 커질수록 그래프는 오른쪽으로 이동한다.",
               "p가 음수이면 그래프는 왼쪽으로 이동한다.",
               "꼭짓점의 좌표는 (p, q)이다."}
    if set(quiz_options) == correct:
        st.success("정답입니다! 🎉 그래프 이동 개념을 완벽히 이해하셨군요.")
    else:
        st.error("아쉽습니다. 다시 한 번 그래프 이동을 관찰하며 복습해보세요.")
