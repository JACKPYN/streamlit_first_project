import streamlit as st

# MBTI에 따른 직업과 궁합 추천 데이터
mbti_data = {
    "INTJ": {
        "description": "전략적인 사고를 가진 🧠 **'전략가'**입니다. 문제 해결에 능숙하며 독립적이죠.",
        "jobs": "🔬 과학자, 📊 데이터 분석가, 🏢 경영 컨설턴트",
        "compatibility": "잘 맞는 사람: ENFP 😊 - 에너지 넘치는 성격이 서로를 보완해요!"
    },
    "INFP": {
        "description": "이상적인 꿈을 꾸는 🌸 **'중재자'**입니다. 감수성이 풍부하고 창의적이에요.",
        "jobs": "🎨 작가, 🎭 예술가, 🧑‍🎓 상담사",
        "compatibility": "잘 맞는 사람: ENTJ 👔 - 구조적인 사고가 INFP의 꿈을 현실로 이끌어줘요!"
    },
    "ENTP": {
        "description": "끊임없이 아이디어를 내는 💡 **'발명가'**입니다. 호기심이 많고 토론을 즐깁니다.",
        "jobs": "👨‍💻 스타트업 창업자, 📰 저널리스트, 💼 마케팅 전략가",
        "compatibility": "잘 맞는 사람: INFJ 🌟 - 깊이 있는 대화가 서로에게 영감을 줍니다!"
    },
    "ESFJ": {
        "description": "다정한 리더 💕 **'사교형 리더'**입니다. 타인의 감정을 잘 이해하고 돕고 싶어합니다.",
        "jobs": "🩺 의료계 종사자, 👨‍🏫 교사, 🧑‍🍳 이벤트 플래너",
        "compatibility": "잘 맞는 사람: ISFP 🎶 - 조용하고 세심한 성격이 ESFJ의 온기를 받쳐줘요!"
    }
    # 필요한 경우 다른 MBTI 유형도 추가 가능
}

# Streamlit UI 구성
st.title("📊 MBTI 맞춤 직업 & 궁합 추천")
st.write("당신의 MBTI를 선택하고 어떤 직업과 사람과 잘 맞는지 알아보세요! 🎉")

# 드롭다운 메뉴에서 MBTI 선택
mbti_types = list(mbti_data.keys())
selected_mbti = st.selectbox("🔍 **당신의 MBTI를 선택해주세요:**", mbti_types)

# 선택된 MBTI에 대한 결과 출력
if selected_mbti:
    st.subheader(f"📝 {selected_mbti} 유형의 분석 결과")
    st.write(mbti_data[selected_mbti]["description"])
    st.write(f"**💼 추천 직업:** {mbti_data[selected_mbti]['jobs']}")
    st.write(f"**❤️ 잘 맞는 사람:** {mbti_data[selected_mbti]['compatibility']}")
