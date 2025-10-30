import streamlit as st
import random
import pandas as pd

# 🚀 페이지 설정
st.set_page_config(
    page_title="로또 번호 생성기 🎰",
    layout="wide"
)

st.title('🇰🇷 로또 번호 생성기 (1~45 중 6개)')
st.write("원하는 게임 수를 입력하고 버튼을 눌러 로또 번호 조합을 생성하세요.")

# ---

### 🔢 게임 수 입력
# Streamlit의 slider를 사용하여 1부터 10까지의 게임 수를 입력받습니다.
game_count = st.slider(
    '생성할 게임 수를 선택하세요 (1~10)',
    min_value=1,
    max_value=10,
    value=5,  # 기본값
    step=1
)

# ---

### ✨ 로또 번호 생성 함수
def generate_lotto_numbers():
    """1부터 45까지의 숫자 중 중복 없이 6개의 숫자를 생성하고 정렬합니다."""
    # random.sample() 함수를 사용하여 중복 없이 6개의 숫자를 선택
    numbers = random.sample(range(1, 46), 6) 
    numbers.sort() # 숫자를 오름차순으로 정렬
    return numbers

# ---

### 🎯 번호 생성 및 결과 표시
if st.button('🎲 생성'):
    # 버튼 클릭 시 작동
    st.subheader(f"✨ 선택하신 **{game_count} 게임**의 로또 번호 추천입니다.")
    
    # 생성된 로또 번호를 저장할 리스트
    lotto_results = []
    
    # 게임 수만큼 반복하여 번호 조합을 생성합니다.
    for i in range(game_count):
        numbers = generate_lotto_numbers()
        lotto_results.append({
            '게임': f"Game {i+1}",
            '번호': numbers,
            '번호_문자열': " - ".join(map(str, numbers)) # 보기 좋게 문자열로 변환
        })

    # 결과를 데이터프레임으로 만들어 깔끔하게 표시
    # '번호_문자열' 컬럼만 사용
    df = pd.DataFrame(lotto_results)
    df_display = df[['게임', '번호_문자열']].rename(columns={'번호_문자열': '추천 번호'})
    
    # Streamlit의 dataframe으로 출력
    st.dataframe(
        df_display,
        hide_index=True,
        use_container_width=True
    )
    
    st.balloons() # 번호 생성 후 축하 효과 추가

# ---

### 📌 앱 실행 방법
st.sidebar.header("앱 실행 방법")
st.sidebar.markdown(
    """
    1. 위 코드를 `lotto_generator.py` 파일로 저장합니다.
    2. 터미널/명령 프롬프트에서 다음 명령어를 실행합니다.
    ```bash
    streamlit run lotto_generator.py
    ```
    """
)
