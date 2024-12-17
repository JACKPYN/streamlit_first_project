import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 로드 함수
@st.cache_data
def load_data(file):
    data = pd.read_csv(file)
    return data

# 연령대별 인구 시각화 함수
def plot_population_structure(region_data, region_name):
    ages = region_data.filter(like="2024년11월_계_").iloc[:, 2:].columns
    age_labels = [age.split("_")[2] for age in ages]
    populations = region_data.iloc[:, 3:].values.flatten()

    # 시각화
    plt.figure(figsize=(10, 6))
    plt.bar(age_labels, populations, color="skyblue")
    plt.xticks(rotation=90)
    plt.title(f"{region_name} 연령대별 인구 구조")
    plt.xlabel("연령대")
    plt.ylabel("인구 수")
    st.pyplot(plt)

# Streamlit 앱 UI
st.title("📊 원하는 지역의 인구 구조 시각화")
st.write("원하는 지역을 선택하면 연령대별 인구 구조를 확인할 수 있어요!")

# 파일 업로드
uploaded_file = st.file_uploader("CSV 파일을 업로드해주세요", type=["csv"])

if uploaded_file:
    # 데이터 로드
    data = load_data(uploaded_file)

    # 지역 선택
    st.subheader("🔍 지역 선택")
    regions = data["행정구역"].unique()
    selected_region = st.selectbox("원하는 지역을 선택하세요:", regions)

    # 선택된 지역 데이터 필터링
    region_data = data[data["행정구역"] == selected_region]

    if not region_data.empty:
        st.subheader(f"📈 {selected_region}의 인구 구조")
        plot_population_structure(region_data, selected_region)
    else:
        st.error("선택한 지역의 데이터가 없습니다. 다른 지역을 선택해주세요.")
