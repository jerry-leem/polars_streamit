"""
대용량 프로그래머 데이터셋 생성 스크립트 (100만 개 레코드)
Polars의 고속 연산 성능 테스트를 위한 데이터 생성
Faker를 사용한 현실적인 랜덤 데이터 생성
"""
import polars as pl
import random
from datetime import datetime
from faker import Faker

# 데이터 생성 설정
NUM_RECORDS = 1_000_000

print(f"Starting to generate {NUM_RECORDS:,} records using Faker...")
start_time = datetime.now()

# Faker 인스턴스 생성 (다양한 로케일)
fake_en = Faker('en_US')
fake_ko = Faker('ko_KR')
fake_de = Faker('de_DE')
fake_es = Faker('es_ES')
fake_fr = Faker('fr_FR')
fake_ja = Faker('ja_JP')
fake_zh = Faker('zh_CN')
fake_pt = Faker('pt_BR')
fake_in = Faker('en_IN')
fake_it = Faker('it_IT')

# 로케일별 Faker 매핑
locale_fakers = {
    'USA': fake_en,
    'UK': fake_en,
    'Canada': fake_en,
    'Australia': fake_en,
    'South Korea': fake_ko,
    'Germany': fake_de,
    'Spain': fake_es,
    'France': fake_fr,
    'Japan': fake_ja,
    'China': fake_zh,
    'Brazil': fake_pt,
    'India': fake_in,
    'Italy': fake_it,
    'Egypt': fake_en,
    'Singapore': fake_en
}

departments = ["Backend", "Frontend", "DevOps", "Data Science", "Full Stack", "Mobile", "QA", "Security", "Cloud", "AI/ML"]
countries = list(locale_fakers.keys())
job_titles = [
    "Junior Developer", "Developer", "Senior Developer", "Lead Developer",
    "Junior Engineer", "Engineer", "Senior Engineer", "Staff Engineer",
    "Data Scientist", "Senior Data Scientist", "Data Engineer",
    "DevOps Engineer", "Tech Lead", "Principal Engineer", "Architect"
]
programming_languages = [
    "Python", "JavaScript", "TypeScript", "Java", "Go", "Rust",
    "Kotlin", "Swift", "PHP", "Ruby", "C++", "C#", "R", "Scala", "Elixir"
]
skill_levels = ["Beginner", "Intermediate", "Advanced", "Expert"]

# 코드 샘플 템플릿
code_snippets = {
    "Python": [
        "def calculate_sum(a, b):\n    return a + b",
        "import pandas as pd\ndf = pd.read_csv('data.csv')\ndf.head()",
        "class User:\n    def __init__(self, name):\n        self.name = name",
        "import tensorflow as tf\nmodel = tf.keras.Sequential([\n    tf.keras.layers.Dense(128, activation='relu')\n])",
        "from sklearn.model_selection import train_test_split\nX_train, X_test = train_test_split(X, y, test_size=0.2)",
        "import numpy as np\narr = np.array([1, 2, 3, 4, 5])\nprint(arr.mean())",
        "async def fetch_data():\n    async with aiohttp.ClientSession() as session:\n        return await session.get(url)",
        "import polars as pl\ndf = pl.read_csv('data.csv')\ndf.filter(pl.col('age') > 25)",
        "from fastapi import FastAPI\napp = FastAPI()\n@app.get('/')\ndef read_root():\n    return {'Hello': 'World'}",
        "with open('file.txt', 'r') as f:\n    data = f.read()\n    print(data)"
    ],
    "JavaScript": [
        "const fetchData = async () => {\n    return await api.get('/data');\n};",
        "function debounce(func, wait) {\n    let timeout;\n    return function() {\n        clearTimeout(timeout);\n        timeout = setTimeout(func, wait);\n    };\n}",
        "async function processData(data) {\n    try {\n        const result = await transform(data);\n        return result;\n    } catch(e) {\n        console.error(e);\n    }\n}",
        "const users = data.map(user => ({\n    id: user.id,\n    name: user.name\n}));",
        "class DataService {\n    async fetchAll() {\n        return await this.http.get('/api/data');\n    }\n}",
        "const sum = arr.reduce((acc, val) => acc + val, 0);",
        "export default function Component() {\n    return <div>Hello World</div>;\n}"
    ],
    "TypeScript": [
        "interface User {\n    id: number;\n    name: string;\n}",
        "class DataService {\n    async fetchData(): Promise<Data[]> {\n        return await this.http.get<Data[]>('/api/data');\n    }\n}",
        "type Result<T> = Success<T> | Error;",
        "const greet = (name: string): string => {\n    return `Hello, ${name}`;\n};",
        "enum Status { Active, Inactive, Pending }"
    ],
    "Java": [
        "public class Main {\n    public static void main(String[] args) {\n        System.out.println(\"Hello\");\n    }\n}",
        "public interface UserRepository extends JpaRepository<User, Long> {\n    List<User> findByAge(int age);\n}",
        "@RestController\npublic class UserController {\n    @GetMapping(\"/users\")\n    public List<User> getUsers() {\n        return userService.findAll();\n    }\n}",
        "Stream<String> stream = list.stream()\n    .filter(s -> s.length() > 5)\n    .map(String::toUpperCase);",
        "Optional<User> user = userRepository.findById(id);"
    ],
    "Go": [
        "func main() {\n    fmt.Println(\"Hello, World!\")\n}",
        "func calculate(a, b int) int {\n    return a + b\n}",
        "type User struct {\n    ID   int\n    Name string\n}",
        "go func() {\n    fmt.Println(\"Goroutine\")\n}()",
        "ch := make(chan int)\nch <- 42"
    ],
    "Kotlin": [
        "fun greet(name: String) {\n    println(\"Hello, $name\")\n}",
        "data class User(val id: Int, val name: String)",
        "suspend fun fetchData(): List<Data> {\n    return api.getData()\n}",
        "val numbers = listOf(1, 2, 3, 4, 5)\nval doubled = numbers.map { it * 2 }",
        "sealed class Result<out T>"
    ],
    "R": [
        "library(dplyr)\ndata %>% filter(age > 25) %>% select(name, age)",
        "model <- lm(y ~ x, data = dataset)\nsummary(model)",
        "ggplot(data, aes(x=age, y=salary)) + geom_point()",
        "sapply(1:10, function(x) x^2)",
        "df <- read.csv('data.csv')"
    ],
    "Swift": [
        "struct ContentView: View {\n    var body: some View {\n        Text(\"Hello\")\n    }\n}",
        "class DataManager {\n    func fetchData() async throws -> [Data] {\n        return try await api.get()\n    }\n}",
        "let numbers = [1, 2, 3, 4, 5]\nlet doubled = numbers.map { $0 * 2 }",
        "guard let url = URL(string: urlString) else { return }"
    ],
    "PHP": [
        "<?php\nclass Database {\n    private $conn;\n    public function connect() { }\n}",
        "<?php\n$users = array_filter($data, function($user) {\n    return $user['age'] > 25;\n});",
        "<?php\nforeach ($items as $item) {\n    echo $item;\n}"
    ],
    "Rust": [
        "fn main() {\n    let numbers = vec![1, 2, 3];\n    println!(\"{:?}\", numbers);\n}",
        "struct User {\n    id: u32,\n    name: String,\n}",
        "impl User {\n    fn new(id: u32, name: String) -> Self {\n        User { id, name }\n    }\n}",
        "let result = match value {\n    Some(x) => x,\n    None => 0,\n};"
    ],
    "C++": [
        "#include <iostream>\nint main() {\n    std::cout << \"Hello\" << std::endl;\n    return 0;\n}",
        "class User {\npublic:\n    int id;\n    std::string name;\n};",
        "std::vector<int> vec = {1, 2, 3, 4, 5};",
        "auto lambda = [](int x) { return x * 2; };"
    ],
    "C#": [
        "public class User {\n    public int Id { get; set; }\n    public string Name { get; set; }\n}",
        "var users = await _context.Users\n    .Where(u => u.Age > 25)\n    .ToListAsync();",
        "var result = numbers.Select(x => x * 2).ToList();",
        "public async Task<List<User>> GetUsersAsync() {\n    return await _repository.GetAllAsync();\n}"
    ],
    "Ruby": [
        "def greet(name)\n  puts \"Hello, #{name}\"\nend",
        "class User\n  attr_accessor :id, :name\nend",
        "users.select { |u| u.age > 25 }",
        "[1, 2, 3, 4, 5].map { |n| n * 2 }"
    ],
    "Scala": [
        "object Main extends App {\n  println(\"Hello, World!\")\n}",
        "case class User(id: Int, name: String)",
        "val doubled = numbers.map(_ * 2)",
        "def factorial(n: Int): Int = if (n <= 1) 1 else n * factorial(n - 1)"
    ],
    "Elixir": [
        "defmodule User do\n  defstruct [:id, :name]\nend",
        "Enum.map([1, 2, 3], fn x -> x * 2 end)",
        "def greet(name) do\n  \"Hello, #{name}\"\nend"
    ]
}

# 데이터 생성
print("Generating data with Faker...")

employee_ids = list(range(1, NUM_RECORDS + 1))
names = []
ages = []
depts = []
countries_list = []
job_titles_list = []
years_exp = []
salaries = []
prog_langs = []
skill_levels_list = []
code_snippets_list = []

# 배치 단위로 생성 (메모리 효율)
batch_size = 10000
print(f"Generating in batches of {batch_size:,}...")

for i in range(0, NUM_RECORDS, batch_size):
    batch_end = min(i + batch_size, NUM_RECORDS)
    batch_count = batch_end - i

    # 진행 상황 출력
    if (i // batch_size) % 10 == 0:
        progress = (i / NUM_RECORDS) * 100
        print(f"  Progress: {progress:.1f}% ({i:,}/{NUM_RECORDS:,})")

    for _ in range(batch_count):
        # 국가 선택
        country = random.choice(countries)
        faker_instance = locale_fakers[country]

        # Faker로 이름 생성
        names.append(faker_instance.name())

        # 나이 생성 (정규분포 사용하여 더 현실적)
        age = int(random.gauss(35, 8))  # 평균 35세, 표준편차 8
        age = max(22, min(60, age))  # 22-60세로 제한
        ages.append(age)

        # 부서 및 직급
        dept = random.choice(departments)
        depts.append(dept)

        countries_list.append(country)

        # 경력 연수 (나이와 연관성)
        min_exp = max(0, age - 24)  # 최소 24세부터 일 시작
        max_exp = min(25, age - 22)
        exp = random.randint(0, max_exp)
        years_exp.append(exp)

        # 직급 (경력에 따라)
        if exp <= 2:
            job_title = random.choice([t for t in job_titles if "Junior" in t])
        elif exp <= 5:
            job_title = random.choice([t for t in job_titles if "Junior" not in t and "Senior" not in t and "Lead" not in t and "Principal" not in t])
        elif exp <= 8:
            job_title = random.choice([t for t in job_titles if "Senior" in t or "Lead" in t])
        else:
            job_title = random.choice([t for t in job_titles if "Senior" in t or "Lead" in t or "Principal" in t or "Architect" in t])
        job_titles_list.append(job_title)

        # 연봉 (경력, 직급, 부서에 따라 달라짐)
        base_salary = 50000
        exp_bonus = exp * random.randint(4000, 6000)

        # 부서별 보너스
        dept_multiplier = {
            "AI/ML": 1.3,
            "Data Science": 1.25,
            "Cloud": 1.2,
            "Security": 1.2,
            "Backend": 1.1,
            "Full Stack": 1.1,
            "DevOps": 1.15,
            "Frontend": 1.0,
            "Mobile": 1.05,
            "QA": 0.95
        }

        salary = int((base_salary + exp_bonus) * dept_multiplier.get(dept, 1.0))
        salary += random.randint(-5000, 15000)  # 랜덤 변동
        salary = max(45000, salary)  # 최소 연봉
        salaries.append(salary)

        # 프로그래밍 언어
        lang = random.choice(programming_languages)
        prog_langs.append(lang)

        # 스킬 레벨 (경력에 따라)
        if exp <= 2:
            skill = random.choice(["Beginner", "Intermediate"])
        elif exp <= 5:
            skill = random.choice(["Intermediate", "Advanced"])
        else:
            skill = random.choice(["Advanced", "Expert"])
        skill_levels_list.append(skill)

        # 코드 스니펫
        if lang in code_snippets:
            code_snippets_list.append(random.choice(code_snippets[lang]))
        else:
            code_snippets_list.append(f"// {lang} code sample\nconsole.log('Hello');")

print("  Progress: 100.0% - Data generation complete!")
print("Creating Polars DataFrame...")

# Polars DataFrame 생성
df = pl.DataFrame({
    "employee_id": employee_ids,
    "name": names,
    "age": ages,
    "department": depts,
    "country": countries_list,
    "job_title": job_titles_list,
    "years_experience": years_exp,
    "salary": salaries,
    "programming_language": prog_langs,
    "code_snippet": code_snippets_list,
    "skill_level": skill_levels_list
})

print(f"DataFrame created with shape: {df.shape}")
print(f"Memory usage: {df.estimated_size('mb'):.2f} MB")

# CSV로 저장
output_path = "data/programmers_dataset.csv"
print(f"Writing to {output_path}...")
df.write_csv(output_path)

end_time = datetime.now()
elapsed = (end_time - start_time).total_seconds()

print(f"\n✅ Successfully generated {NUM_RECORDS:,} records using Faker!")
print(f"⏱️  Time taken: {elapsed:.2f} seconds")
print(f"📁 File saved to: {output_path}")
print(f"📊 DataFrame shape: {df.shape[0]:,} rows × {df.shape[1]} columns")
print(f"💾 Estimated memory: {df.estimated_size('mb'):.2f} MB")
print(f"\n📋 Data statistics:")
print(f"   - Age range: {df['age'].min()} - {df['age'].max()}")
print(f"   - Salary range: ${df['salary'].min():,} - ${df['salary'].max():,}")
print(f"   - Average experience: {df['years_experience'].mean():.1f} years")
print(f"   - Countries represented: {df['country'].n_unique()}")
print(f"   - Departments: {df['department'].n_unique()}")
print(f"   - Programming languages: {df['programming_language'].n_unique()}")
