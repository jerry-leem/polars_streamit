# Polars Streamlit DataFrame Viewer

Streamlit과 Polars를 활용한 **대용량 데이터프레임** 뷰어 애플리케이션입니다.

## 특징

- **Polars** 라이브러리를 사용한 고성능 데이터 처리
- **100만 개 레코드** 대용량 데이터셋 지원
- 다양한 데이터 타입 지원:
  - 숫자형 컬럼 (age, salary, years_experience)
  - 코드 컬럼 (code_snippet) - 14개 프로그래밍 언어
  - 문자열 컬럼 (name, department, country, job_title 등)
- 인터랙티브 데이터 필터링
- 통계 분석 및 시각화
- 코드 샘플 뷰어
- 자동 데이터셋 생성 기능

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

**참고**: 첫 실행 시 데이터셋이 자동으로 생성됩니다 (약 3-5초 소요).

### 수동 데이터 생성

필요시 데이터를 수동으로 생성할 수도 있습니다:

```bash
python generate_large_dataset.py
```

## 프로젝트 구조

```
polars_streamit/
├── app.py                          # Streamlit 메인 애플리케이션
├── generate_large_dataset.py       # 대용량 데이터셋 생성 스크립트
├── data/
│   └── programmers_dataset.csv     # 100만 개 레코드 데이터셋 (자동 생성)
├── requirements.txt                # 필요 패키지 목록
└── README.md                       # 프로젝트 문서
```

## 데이터셋 정보

프로그래머 정보를 담은 대용량 샘플 데이터셋 (**1,000,000 레코드**):

- **employee_id**: 직원 ID
- **name**: 이름 (한국어/영어 이름 혼합)
- **age**: 나이 (22-55세, 숫자)
- **department**: 부서 (Backend, Frontend, DevOps, Data Science 등 8개 부서)
- **country**: 국가 (15개국)
- **job_title**: 직급 (Junior ~ Principal 12개 직급)
- **years_experience**: 경력 연수 (0-25년, 숫자)
- **salary**: 연봉 (경력 연관, $50K-$200K, 숫자)
- **programming_language**: 주 사용 언어 (Python, JavaScript, Java 등 14개 언어)
- **code_snippet**: 실제 코드 샘플 (언어별 실제 코드)
- **skill_level**: 스킬 레벨 (Beginner, Intermediate, Advanced, Expert)

### 성능 특징

- **데이터 생성 시간**: ~3.5초 (100만 레코드)
- **CSV 파일 크기**: ~145MB
- **메모리 사용량**: ~148MB (Polars DataFrame)
- **데이터 로드 시간**: 1-2초 (Polars 고속 처리)

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
