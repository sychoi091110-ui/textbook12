import streamlit as st
import random

# 앱 제목
st.title("🎰 로또 번호 생성기")

# 게임 수 입력 (1~10 사이)
game_count = st.number_input("몇 게임을 생성할까요?", min_value=1, max_value=10, value=1, step=1)

# 버튼 클릭 시 번호 생성
if st.button("번호 생성 🎲"):
    st.write(f"총 {game_count}개의 로또 조합을 생성했습니다.\n")
    
    for i in range(game_count):
        # 1~45 중 중복 없이 6개 추첨
        numbers = random.sample(range(1, 46), 6)
        numbers.sort()
        st.write(f"게임 {i+1}: 🎟️ {numbers}")
