# Polars Streamlit DataFrame Viewer

Streamlit과 Polars를 활용한 데이터프레임 뷰어 애플리케이션입니다.

## 특징

- **Polars** 라이브러리를 사용한 고성능 데이터 처리
- 다양한 데이터 타입 지원:
  - 숫자형 컬럼 (age, salary, years_experience)
  - 코드 컬럼 (code_snippet)
  - 문자열 컬럼 (name, department, country, job_title 등)
- 인터랙티브 데이터 필터링
- 통계 분석 및 시각화
- 코드 샘플 뷰어

## 설치 방법

```bash
# 의존성 패키지 설치
pip install -r requirements.txt
```

## 실행 방법

```bash
# Streamlit 앱 실행
streamlit run app.py
```

앱이 실행되면 브라우저에서 자동으로 `http://localhost:8501`이 열립니다.

## 프로젝트 구조

```
polars_streamit/
├── app.py                          # Streamlit 메인 애플리케이션
├── data/
│   └── programmers_dataset.csv     # 샘플 데이터셋
├── requirements.txt                # 필요 패키지 목록
└── README.md                       # 프로젝트 문서
```

## 데이터셋 정보

프로그래머 정보를 담은 샘플 데이터셋:

- **employee_id**: 직원 ID
- **name**: 이름
- **age**: 나이 (숫자)
- **department**: 부서 (문자열)
- **country**: 국가 (문자열)
- **job_title**: 직급 (문자열)
- **years_experience**: 경력 연수 (숫자)
- **salary**: 연봉 (숫자)
- **programming_language**: 주 사용 언어 (문자열)
- **code_snippet**: 코드 샘플 (코드)
- **skill_level**: 스킬 레벨 (문자열)

## 주요 기능

### 1. 데이터 탭
- Polars DataFrame 표시
- 컬럼 정보 및 데이터 타입 확인
- Null 값 확인

### 2. 통계 탭
- 숫자 컬럼 기술 통계
- 주요 지표 (평균 나이, 경력, 연봉)
- 부서별 통계

### 3. 코드 샘플 탭
- 프로그래밍 언어별 코드 샘플 확인
- 직원 정보와 함께 코드 표시

### 4. 시각화 탭
- 부서별 평균 연봉 바 차트
- 스킬 레벨 분포 파이 차트
- 경력 vs 연봉 산점도
- 프로그래밍 언어별 사용자 수

## 필터 기능

사이드바에서 다음 항목으로 필터링 가능:
- 부서
- 스킬 레벨
- 연봉 범위

## 기술 스택

- **Streamlit**: 웹 애플리케이션 프레임워크
- **Polars**: 고성능 DataFrame 라이브러리
- **Plotly**: 인터랙티브 차트 라이브러리
- **Pandas**: 데이터 변환 (Streamlit 호환성)
