"""
대용량 프로그래머 데이터셋 생성 스크립트 (100만 개 레코드)
Polars의 고속 연산 성능 테스트를 위한 데이터 생성
"""
import polars as pl
import random
from datetime import datetime

# 데이터 생성 설정
NUM_RECORDS = 1_000_000

print(f"Starting to generate {NUM_RECORDS:,} records...")
start_time = datetime.now()

# 샘플 데이터 풀
korean_names = [
    "김철수", "이영희", "박민수", "최지우", "정현우", "강민지", "오수진", "윤서연",
    "임동현", "한지민", "송중기", "전지현", "이민호", "김태희", "박보검", "수지"
]

international_names = [
    "John Smith", "Maria Garcia", "Anna Mueller", "Chen Wei", "Sarah Johnson",
    "Lucas Silva", "Emma Wilson", "Ahmed Hassan", "Sophie Martin", "Raj Kumar",
    "Hans Schmidt", "Yuki Tanaka", "Isabella Rossi", "Mohammed Ali", "Elena Petrova"
]

departments = ["Backend", "Frontend", "DevOps", "Data Science", "Full Stack", "Mobile", "QA", "Security"]
countries = ["South Korea", "USA", "Germany", "Spain", "China", "Brazil", "UK", "Egypt",
             "France", "India", "Japan", "Italy", "Canada", "Australia", "Singapore"]
job_titles = ["Junior Developer", "Developer", "Senior Developer", "Lead Developer",
              "Junior Engineer", "Engineer", "Senior Engineer", "Data Scientist",
              "Data Engineer", "DevOps Engineer", "Tech Lead", "Principal Engineer"]
programming_languages = ["Python", "JavaScript", "TypeScript", "Java", "Go", "Rust",
                        "Kotlin", "Swift", "PHP", "Ruby", "C++", "C#", "R", "Scala"]
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
        "import polars as pl\ndf = pl.read_csv('data.csv')\ndf.filter(pl.col('age') > 25)"
    ],
    "JavaScript": [
        "const fetchData = async () => {\n    return await api.get('/data');\n};",
        "function debounce(func, wait) {\n    let timeout;\n    return function() {\n        clearTimeout(timeout);\n        timeout = setTimeout(func, wait);\n    };\n}",
        "async function processData(data) {\n    try {\n        const result = await transform(data);\n        return result;\n    } catch(e) {\n        console.error(e);\n    }\n}",
        "const users = data.map(user => ({\n    id: user.id,\n    name: user.name\n}));",
        "class DataService {\n    async fetchAll() {\n        return await this.http.get('/api/data');\n    }\n}"
    ],
    "Java": [
        "public class Main {\n    public static void main(String[] args) {\n        System.out.println(\"Hello\");\n    }\n}",
        "public interface UserRepository extends JpaRepository<User, Long> {\n    List<User> findByAge(int age);\n}",
        "@RestController\npublic class UserController {\n    @GetMapping(\"/users\")\n    public List<User> getUsers() {\n        return userService.findAll();\n    }\n}"
    ],
    "Go": [
        "func main() {\n    fmt.Println(\"Hello, World!\")\n}",
        "func calculate(a, b int) int {\n    return a + b\n}",
        "type User struct {\n    ID   int\n    Name string\n}"
    ],
    "TypeScript": [
        "interface User {\n    id: number;\n    name: string;\n}",
        "class DataService {\n    async fetchData(): Promise<Data[]> {\n        return await this.http.get<Data[]>('/api/data');\n    }\n}",
        "type Result<T> = Success<T> | Error;"
    ],
    "Kotlin": [
        "fun greet(name: String) {\n    println(\"Hello, $name\")\n}",
        "data class User(val id: Int, val name: String)",
        "suspend fun fetchData(): List<Data> {\n    return api.getData()\n}"
    ],
    "R": [
        "library(dplyr)\ndata %>% filter(age > 25) %>% select(name, age)",
        "model <- lm(y ~ x, data = dataset)\nsummary(model)",
        "ggplot(data, aes(x=age, y=salary)) + geom_point()"
    ],
    "Swift": [
        "struct ContentView: View {\n    var body: some View {\n        Text(\"Hello\")\n    }\n}",
        "class DataManager {\n    func fetchData() async throws -> [Data] {\n        return try await api.get()\n    }\n}"
    ],
    "PHP": [
        "<?php\nclass Database {\n    private $conn;\n    public function connect() { }\n}",
        "<?php\n$users = array_filter($data, function($user) {\n    return $user['age'] > 25;\n});"
    ],
    "Rust": [
        "fn main() {\n    let numbers = vec![1, 2, 3];\n    println!(\"{:?}\", numbers);\n}",
        "struct User {\n    id: u32,\n    name: String,\n}"
    ],
    "C++": [
        "#include <iostream>\nint main() {\n    std::cout << \"Hello\" << std::endl;\n    return 0;\n}",
        "class User {\npublic:\n    int id;\n    std::string name;\n};"
    ],
    "C#": [
        "public class User {\n    public int Id { get; set; }\n    public string Name { get; set; }\n}",
        "var users = await _context.Users\n    .Where(u => u.Age > 25)\n    .ToListAsync();"
    ],
    "Ruby": [
        "def greet(name)\n  puts \"Hello, #{name}\"\nend",
        "class User\n  attr_accessor :id, :name\nend"
    ],
    "Scala": [
        "object Main extends App {\n  println(\"Hello, World!\")\n}",
        "case class User(id: Int, name: String)"
    ]
}

# 데이터 생성
print("Generating data...")

# 모든 이름 풀
all_names = korean_names + international_names

# 랜덤 데이터 생성
employee_ids = list(range(1, NUM_RECORDS + 1))
names = [random.choice(all_names) for _ in range(NUM_RECORDS)]
ages = [random.randint(22, 55) for _ in range(NUM_RECORDS)]
depts = [random.choice(departments) for _ in range(NUM_RECORDS)]
countries_list = [random.choice(countries) for _ in range(NUM_RECORDS)]
job_titles_list = [random.choice(job_titles) for _ in range(NUM_RECORDS)]
years_exp = [random.randint(0, 25) for _ in range(NUM_RECORDS)]
# 연봉은 경력과 연관성 있게 생성 (더 현실적)
salaries = [50000 + (exp * 5000) + random.randint(-10000, 10000) for exp in years_exp]
prog_langs = [random.choice(programming_languages) for _ in range(NUM_RECORDS)]
skill_levels_list = [random.choice(skill_levels) for _ in range(NUM_RECORDS)]

# 코드 스니펫 생성 (언어에 맞는 코드 선택)
code_snippets_list = []
for lang in prog_langs:
    if lang in code_snippets:
        code_snippets_list.append(random.choice(code_snippets[lang]))
    else:
        code_snippets_list.append(f"// {lang} code sample\nconsole.log('Hello');")

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

print(f"\n✅ Successfully generated {NUM_RECORDS:,} records!")
print(f"⏱️  Time taken: {elapsed:.2f} seconds")
print(f"📁 File saved to: {output_path}")
print(f"📊 DataFrame shape: {df.shape[0]:,} rows × {df.shape[1]} columns")
print(f"💾 Estimated memory: {df.estimated_size('mb'):.2f} MB")
