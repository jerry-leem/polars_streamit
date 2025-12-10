import streamlit as st
import polars as pl
import plotly.express as px
from pathlib import Path
import subprocess
import sys
import time

# 페이지 설정
st.set_page_config(
    page_title="Polars DataFrame Viewer",
    page_icon="📊",
    layout="wide"
)

# 타이틀
st.title("📊 Polars DataFrame Viewer")
st.markdown("### 프로그래머 데이터셋 분석 (100만 레코드)")

# 데이터 생성 함수
def generate_dataset():
    """데이터셋이 없을 경우 자동 생성"""
    st.warning("⚠️ 데이터셋이 없습니다. 100만 개 레코드를 생성하는 중...")
    progress_bar = st.progress(0)
    status_text = st.empty()

    try:
        status_text.text("데이터 생성 스크립트 실행 중...")
        progress_bar.progress(20)

        # 스크립트 실행
        result = subprocess.run(
            [sys.executable, "generate_large_dataset.py"],
            capture_output=True,
            text=True,
            timeout=600
        )

        progress_bar.progress(80)

        if result.returncode == 0:
            progress_bar.progress(100)
            status_text.text("✅ 데이터 생성 완료!")
            time.sleep(1)
            st.success(result.stdout)
            return True
        else:
            st.error(f"❌ 데이터 생성 실패:\n{result.stderr}")
            return False
    except Exception as e:
        st.error(f"❌ 오류 발생: {e}")
        return False

# 데이터 로드 함수
@st.cache_data
def load_data():
    """Polars를 사용하여 CSV 데이터 로드"""
    data_path = Path(__file__).parent / "data" / "programmers_dataset.csv"

    # 데이터 파일이 없으면 생성
    if not data_path.exists():
        if generate_dataset():
            st.rerun()
        else:
            st.stop()

    # 데이터 로드 시작 시간 측정
    start_time = time.time()
    df = pl.read_csv(data_path)
    load_time = time.time() - start_time

    st.success(f"✅ 데이터 로드 성공: {df.shape[0]:,}개 행, {df.shape[1]}개 열 (로드 시간: {load_time:.2f}초)")

    return df

# 데이터 로드
try:
    df = load_data()
except Exception as e:
    st.error(f"❌ 데이터 로드 실패: {e}")
    st.stop()

# 사이드바 - 필터 옵션
st.sidebar.header("🔍 필터 옵션")

# 부서 필터
departments = ["All"] + df["department"].unique().sort().to_list()
selected_dept = st.sidebar.selectbox("부서 선택", departments)

# 스킬 레벨 필터
skill_levels = ["All"] + df["skill_level"].unique().sort().to_list()
selected_skill = st.sidebar.selectbox("스킬 레벨 선택", skill_levels)

# 연봉 범위 필터
min_salary = int(df["salary"].min())
max_salary = int(df["salary"].max())
salary_range = st.sidebar.slider(
    "연봉 범위 (USD)",
    min_salary,
    max_salary,
    (min_salary, max_salary)
)

# 데이터 필터링
filtered_df = df
if selected_dept != "All":
    filtered_df = filtered_df.filter(pl.col("department") == selected_dept)
if selected_skill != "All":
    filtered_df = filtered_df.filter(pl.col("skill_level") == selected_skill)
filtered_df = filtered_df.filter(
    (pl.col("salary") >= salary_range[0]) & (pl.col("salary") <= salary_range[1])
)

# 탭 생성
tab1, tab2, tab3, tab4 = st.tabs(["📋 데이터", "📈 통계", "💻 코드 샘플", "📊 시각화"])

# 탭 1: 데이터 테이블
with tab1:
    st.subheader("데이터프레임")
    st.info(f"필터 적용 후: {filtered_df.shape[0]}개 행")

    # Polars DataFrame을 Pandas로 변환하여 표시 (Streamlit 호환성)
    st.dataframe(
        filtered_df.to_pandas(),
        use_container_width=True,
        height=400,
        column_config={
            "salary": st.column_config.NumberColumn(
                "salary",
                format="$%,.0f"
            )
        }
    )

    # 컬럼 정보
    st.subheader("컬럼 정보")
    col_info = pl.DataFrame({
        "컬럼명": df.columns,
        "데이터 타입": [str(df[col].dtype) for col in df.columns],
        "Null 개수": [df[col].null_count() for col in df.columns]
    })
    st.dataframe(col_info.to_pandas(), use_container_width=True)

# 탭 2: 통계 정보
with tab2:
    st.subheader("숫자 컬럼 통계")

    # 숫자 컬럼 선택
    numeric_cols = ["age", "years_experience", "salary"]

    # 기술 통계
    stats_df = filtered_df.select(numeric_cols).describe()
    st.dataframe(
        stats_df.to_pandas(),
        use_container_width=True,
        column_config={
            "salary": st.column_config.NumberColumn(
                "salary",
                format="$%,.0f"
            )
        }
    )

    # 컬럼별 통계 카드
    st.subheader("주요 지표")
    col1, col2, col3 = st.columns(3)

    with col1:
        avg_age = filtered_df["age"].mean()
        st.metric("평균 나이", f"{avg_age:.1f}세")

    with col2:
        avg_exp = filtered_df["years_experience"].mean()
        st.metric("평균 경력", f"{avg_exp:.1f}년")

    with col3:
        avg_salary = filtered_df["salary"].mean()
        st.metric("평균 연봉", f"${avg_salary:,.0f}")

    # 부서별 통계
    st.subheader("부서별 통계")
    dept_stats = filtered_df.group_by("department").agg([
        pl.col("employee_id").count().alias("직원 수"),
        pl.col("salary").mean().alias("평균 연봉"),
        pl.col("years_experience").mean().alias("평균 경력")
    ]).sort("평균 연봉", descending=True)

    st.dataframe(
        dept_stats.to_pandas(),
        use_container_width=True,
        column_config={
            "평균 연봉": st.column_config.NumberColumn(
                "평균 연봉",
                format="$%,.0f"
            ),
            "평균 경력": st.column_config.NumberColumn(
                "평균 경력",
                format="%.1f년"
            )
        }
    )

# 탭 3: 코드 샘플
with tab3:
    st.subheader("프로그래머 코드 샘플")

    # 프로그래밍 언어별 필터
    languages = ["All"] + filtered_df["programming_language"].unique().sort().to_list()
    selected_lang = st.selectbox("프로그래밍 언어 선택", languages)

    code_df = filtered_df
    if selected_lang != "All":
        code_df = code_df.filter(pl.col("programming_language") == selected_lang)

    # 코드 샘플 표시
    for row in code_df.iter_rows(named=True):
        with st.expander(f"{row['name']} - {row['job_title']} ({row['programming_language']})"):
            st.write(f"**부서:** {row['department']}")
            st.write(f"**스킬 레벨:** {row['skill_level']}")
            st.write(f"**경력:** {row['years_experience']}년")
            st.write(f"**연봉:** ${row['salary']:,}")
            st.code(row['code_snippet'], language=row['programming_language'].lower())

# 탭 4: 시각화
with tab4:
    st.subheader("데이터 시각화")

    # 차트 1: 부서별 평균 연봉
    col1, col2 = st.columns(2)

    with col1:
        dept_salary = filtered_df.group_by("department").agg(
            pl.col("salary").mean().alias("평균 연봉")
        ).sort("평균 연봉", descending=True)

        fig1 = px.bar(
            dept_salary.to_pandas(),
            x="department",
            y="평균 연봉",
            title="부서별 평균 연봉",
            labels={"department": "부서", "평균 연봉": "평균 연봉 (USD)"}
        )
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        skill_count = filtered_df.group_by("skill_level").agg(
            pl.col("employee_id").count().alias("count")
        )

        fig2 = px.pie(
            skill_count.to_pandas(),
            values="count",
            names="skill_level",
            title="스킬 레벨 분포"
        )
        st.plotly_chart(fig2, use_container_width=True)

    # 차트 2: 경력 vs 연봉 산점도
    fig3 = px.scatter(
        filtered_df.to_pandas(),
        x="years_experience",
        y="salary",
        color="skill_level",
        size="age",
        hover_data=["name", "department", "programming_language"],
        title="경력 vs 연봉",
        labels={
            "years_experience": "경력 (년)",
            "salary": "연봉 (USD)",
            "skill_level": "스킬 레벨"
        }
    )
    st.plotly_chart(fig3, use_container_width=True)

    # 차트 3: 프로그래밍 언어별 분포
    lang_count = filtered_df.group_by("programming_language").agg(
        pl.col("employee_id").count().alias("count")
    ).sort("count", descending=True)

    fig4 = px.bar(
        lang_count.to_pandas(),
        x="programming_language",
        y="count",
        title="프로그래밍 언어별 사용자 수",
        labels={"programming_language": "프로그래밍 언어", "count": "사용자 수"}
    )
    st.plotly_chart(fig4, use_container_width=True)

# 푸터
st.markdown("---")
st.markdown("**Powered by Polars & Streamlit** | 데이터 분석 대시보드")
