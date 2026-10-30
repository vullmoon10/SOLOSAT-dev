# C# / Unity 핵심 개념

SOLO SAT 개발에 필요한 C# 및 Unity 핵심 개념을 단계적으로 학습하기 위한 실전 커리큘럼이다.

> 목표: **C# 문법 → 객체지향 → Unity 구조 → 2D 게임 개발 → 데이터 관리 → 게임 시스템 → 디버깅 → 최적화 → SOLO SAT 실전 구현**

---

# Part 1. C# 기초

## 1. 변수 (Variable)
- 변수의 개념
- 변수 선언과 초기화
- 변수에 값 대입
- 변수의 유효 범위

## 2. 자료형 (Data Type)
- int
- float
- double
- bool
- char
- string
- decimal

## 3. 상수 (const)
- const
- 상수와 변수의 차이

## 4. var
- var의 개념
- 컴파일러의 타입 추론
- 명시적 자료형과의 차이

## 5. 연산자
- 산술 연산자 + - * / %
- 대입 연산자 =
- 복합 대입 연산자 += -= *= /=
- 비교 연산자 == != > < >= <=
- 논리 연산자 && || !
- 증감 연산자 ++ --

## 6. 조건문
- if
- else if
- else
- 중첩 조건문
- switch

## 7. 반복문
- for
- foreach
- while
- do while
- break
- continue

## 8. 메서드 (Method)
- 메서드 선언
- 호출
- 매개변수 (Parameter)
- 반환값 (Return)
- void
- 메서드 오버로딩

## 9. 배열 (Array)
- 배열 선언
- 배열 초기화
- 인덱스
- 배열 순회
- 다차원 배열

## 10. List
- List<T>
- Add
- Remove
- Count
- 인덱스 접근
- 리스트 순회
- AddRange
- RemoveAt
- Clear
- Contains
- Find
- Sort

## 11. Dictionary
- Dictionary<TKey, TValue>
- Key / Value
- Add
- ContainsKey
- 값 검색 및 수정

## 12. null
- null의 의미
- null 검사
- NullReferenceException

## 13. 형 변환 (Type Casting)
- 암시적 형 변환
- 명시적 형 변환
- 캐스팅 `(int)`, `(float)`
- Convert
- Parse
- TryParse
- 형 변환 오류

## 14. 문자열 처리 (String)
- 문자열 연결
- 문자열 보간 `$""`
- Length
- Substring
- Contains
- Replace
- Split
- ToUpper / ToLower

## 15. 참조와 값
- Value Type
- Reference Type
- 값 복사
- 참조 복사
- ref
- out
- in

## 16. 배열과 컬렉션 선택
- 배열과 List 차이
- List와 Dictionary 선택 기준
- 컬렉션별 장단점
- 데이터 구조에 따른 선택

---

# Part 2. C# 객체지향 프로그래밍

## 17. Class
- 클래스 선언
- 필드 (Field)
- 메서드
- 객체 생성

## 18. Object
- 객체의 개념
- new
- 클래스와 객체의 관계

## 19. Constructor
- 생성자
- 기본 생성자
- 매개변수가 있는 생성자
- 생성자 오버로딩

## 20. 접근 제한자
- public
- private
- protected
- internal
- 접근 범위 비교

## 21. Property
- Property의 개념
- get
- set
- 자동 구현 Property

## 22. static
- static 변수
- static 메서드
- 인스턴스와 static의 차이

## 23. 캡슐화 (Encapsulation)
- 데이터 은닉
- private
- public
- Property
- 클래스 내부 상태 보호

## 24. 상속 (Inheritance)
- 부모 클래스
- 자식 클래스
- `:`
- base
- 코드 재사용
- 상속의 장단점

## 25. 다형성 (Polymorphism)
- 다형성의 개념
- virtual
- override
- 부모 타입으로 자식 객체 다루기

## 26. 추상 클래스
- abstract
- 추상 메서드
- 추상 클래스의 목적

## 27. Interface
- Interface 선언
- Interface 구현
- 다중 Interface

## 28. Struct
- struct
- Class와 Struct의 차이

## 29. Enum
- enum
- 열거형
- 상태와 종류 표현

## 30. Serializable
- [Serializable]
- 데이터 직렬화의 개념

## 31. Exception
- 예외의 개념
- try
- catch
- finally
- throw

## 32. Delegate
- Delegate의 개념
- 메서드를 변수처럼 전달

## 33. Event
- Event의 개념
- 이벤트 발생과 구독
- Observer 구조의 기초

## 34. Lambda
- Lambda Expression
- `=>`

## 35. Action / Func
- Action
- Func
- Delegate와의 관계

## 36. Generic
- Generic의 개념
- T
- List<T>
- Dictionary<TKey,TValue>
- 재사용 가능한 코드

## 37. Composition
- 상속 대신 조합
- 객체가 다른 객체를 포함하는 구조
- Unity Component 구조와의 관계

---

# Part 3. Unity 기본 구조

## 38. Unity Editor
- Scene View
- Game View
- Hierarchy
- Inspector
- Project
- Console

## 39. Project / Scene
- Unity Project
- Scene
- Scene 저장
- Scene 전환

## 40. GameObject
- GameObject의 개념
- GameObject 생성
- 활성화 / 비활성화

## 41. Component
- Component의 개념
- Component 추가
- Component 제거
- Component와 GameObject의 관계

## 42. Component 기반 설계
- GameObject
- Component
- Script
- Component 조합
- Unity의 Composition 구조

## 43. Transform
- Position
- Rotation
- Scale
- Local / World 좌표

## 44. MonoBehaviour
- MonoBehaviour
- Unity Component Script
- GameObject와 Script 연결

## 45. Unity Lifecycle
- Awake()
- Start()
- Update()
- FixedUpdate()
- LateUpdate()
- 실행 시점 차이

## 46. GetComponent
- Component 가져오기
- Component 참조
- GetComponent<T>()

## 47. Instantiate
- Prefab / Object 복제
- Instantiate()

## 48. Destroy
- GameObject 삭제
- Destroy()

## 49. Inspector / SerializeField
- Inspector의 역할
- public field
- [SerializeField]
- 에디터에서 값 수정
- 참조 연결
- Unity Serialization의 기본 원리

---

# Part 4. Unity 2D

## 50. Sprite
- Sprite
- Sprite Import
- SpriteRenderer

## 51. SpriteRenderer
- Sprite 표시
- Sorting Layer
- Order in Layer

## 52. Rigidbody2D
- 2D 물리
- Dynamic / Kinematic / Static
- Gravity Scale
- Mass
- Constraints
- Linear Velocity
- Angular Velocity
- Body Type

## 53. Collider2D
- Collider의 개념
- BoxCollider2D
- CircleCollider2D
- CapsuleCollider2D
- PolygonCollider2D
- Offset
- Composite Collider
- Collider 조합

## 54. Collision
- Collision 개념
- OnCollisionEnter2D
- OnCollisionStay2D
- OnCollisionExit2D

## 55. Trigger
- Trigger 개념
- OnTriggerEnter2D
- OnTriggerStay2D
- OnTriggerExit2D

## 56. Layer
- Layer
- LayerMask
- 충돌 대상 분리
- Layer Collision Matrix

## 57. Tag
- Tag
- 객체 분류
- CompareTag()

## 58. Physics Material 2D
- 마찰
- 탄성
- 물리 재질

## 59. Raycast
- Raycast 개념
- 방향성 충돌 검사
- Physics2D.Raycast()
- RaycastHit2D

## 60. Physics Query
- OverlapCircle
- OverlapBox
- 범위 내 객체 검색
- 공격 판정
- 적 탐지
- 바닥 감지

## 61. Vector2 / Vector3
- 벡터
- 방향
- 위치
- 이동량
- 좌표 계산

## 62. Mathf
- Unity 수학 함수
- Clamp
- Lerp
- Abs
- Min / Max
- Sin / Cos 등

## 63. Time
- Time.deltaTime
- Time.time
- 시간 기반 처리
- 프레임 독립적 이동

---

# Part 5. Unity 2D 맵 / 그래픽

## 64. Tilemap
- Tilemap
- Grid
- Tile Palette
- Tile
- Tilemap Collider
- Composite Collider 2D

## 65. Camera
- Camera
- Orthographic
- Perspective
- Camera Follow
- Camera Bounds

## 66. Prefab
- Prefab 생성
- Prefab 수정
- Prefab Instance
- Prefab Variant

## 67. Animation
- Animation Clip
- Animator
- Animator Controller
- Parameter
- Transition
- State

## 68. Sorting
- Sorting Layer
- Order in Layer
- 2D 오브젝트 표시 순서

## 69. Material / Shader
- Material
- Shader
- Sprite 효과
- 간단한 색상 변경
- 피격 효과

## 70. Particle System
- Particle System
- Spawn
- Lifetime
- Emission
- 피격 / 공격 / 레벨업 효과

---

# Part 6. Unity UI

## 71. Canvas
- Canvas
- Screen Space
- World Space

## 72. RectTransform
- Position
- Width / Height
- Anchor
- Pivot

## 73. TextMeshPro
- TMP Text
- 텍스트 변경
- 폰트 설정

## 74. Image
- Image Component
- Sprite 표시
- Fill

## 75. Button
- Button
- OnClick
- 버튼 이벤트
- UnityEvent

## 76. Slider
- Slider
- Value
- Min / Max
- HP / EXP Bar

## 77. Canvas Scaler
- UI 해상도 대응
- Scale With Screen Size

## 78. EventSystem
- UI 입력 처리
- Pointer / Button Event

## 79. UI 상태 관리
- Panel 활성화 / 비활성화
- Question Panel
- Result Panel
- Game Over Panel
- Pause Panel

## 80. UI 데이터 연결

```text
PlayerData
 ↓
Game System
 ↓
UIManager
 ↓
Text / Slider / Image
```

## 81. UI 갱신 구조
- Update 방식
- Event 방식
- 값 변경 시 UI 갱신
- 불필요한 UI 갱신 방지

---

# Part 7. 입력 / 시간 / 실행 제어

## 82. Input System
- Input System
- Input Action
- Action Map
- Player Input
- Binding

## 83. Input
- 키보드 입력
- 마우스 입력
- 컨트롤러 입력

## 84. Input과 게임 로직 분리

```text
Input
 ↓
PlayerController
 ↓
Game Logic
 ↓
Physics
```

## 85. Update / FixedUpdate / LateUpdate
- Update
- FixedUpdate
- LateUpdate
- 입력 처리
- 물리 처리
- 카메라 처리

## 86. Coroutine
- Coroutine
- IEnumerator
- StartCoroutine()
- StopCoroutine()

## 87. WaitForSeconds
- 일정 시간 대기
- Coroutine과 결합

---

# Part 8. Unity 데이터 관리

## 88. ScriptableObject
- ScriptableObject 개념
- 데이터 Asset
- Inspector에서 데이터 수정
- 코드와 데이터 분리
- 재사용 가능한 데이터

## 89. QuestionData

```text
QuestionData
├─ ID
├─ Subject
├─ Category
├─ Difficulty
├─ Question
├─ Choices
├─ Answer
├─ Explanation
├─ EXP
└─ Penalty
```

## 90. ItemData

```text
ItemData
├─ ID
├─ Name
├─ Subject
├─ Rarity
├─ Description
├─ Effect
└─ Value
```

## 91. EnemyData

```text
EnemyData
├─ ID
├─ Name
├─ HP
├─ Attack
├─ Defense
└─ Difficulty
```

## 92. StageData

```text
StageData
├─ StageID
├─ Name
├─ Difficulty
├─ EnemyList
├─ QuestionPool
├─ Reward
└─ TimeLimit
```

## 93. Serialization
- Unity Serialization
- [SerializeField]
- 데이터 저장 구조
- 직렬화 가능한 타입

## 94. JSON
- JSON 구조
- Serialize
- Deserialize
- JSON 파일 저장

## 95. PlayerPrefs
- 간단한 값 저장
- PlayerPrefs의 용도와 한계

## 96. SaveData
- 저장 전용 데이터 클래스
- 게임 오브젝트와 저장 데이터 분리

---

# Part 9. Unity Scene / 시스템 관리

## 97. SceneManager
- Scene Load
- Scene 전환
- Scene 관리
- Async Load
- Scene 간 데이터 전달

## 98. DontDestroyOnLoad
- Scene 전환
- 객체 유지
- Manager 유지
- 중복 생성 방지

## 99. GameManager
- 전체 게임 흐름 관리
- 전역 시스템 관리

## 100. Singleton
- Singleton 개념
- 전역 접근
- Singleton의 장단점과 주의점

## 101. Manager Architecture
- Manager 역할 분리
- 책임 분리
- 시스템 간 의존성 관리
- 초기화 순서

---

# Part 10. 게임 시스템 구조

## 102. Game State

```text
Title
 ↓
Stage
 ↓
Exploration
 ↓
Battle
 ↓
Question
 ↓
Result
 ↓
Stage Clear
```

- 현재 게임 상태
- 상태 전환
- 상태별 입력 제한
- 상태별 UI

## 103. State Machine / FSM
- State
- Transition
- State Machine
- AI 상태 관리

예:

```text
Idle
 ↓
Chase
 ↓
Attack
 ↓
Hit
 ↓
Dead
```

## 104. Event 기반 구조
- 시스템 간 이벤트 전달
- 결합도 감소
- Event / Delegate 활용
- Observer 구조

## 105. Data-Driven Design
- 데이터와 코드 분리
- ScriptableObject 활용
- 하드코딩 최소화
- 콘텐츠 확장 구조

## 106. Battle System

```text
Enemy
 ↓
Battle Start
 ↓
Question
 ↓
Answer
 ↓
Correct?
 ├─ YES → Damage
 └─ NO → Penalty
 ↓
Enemy HP
 ↓
Death
```

## 107. Question System
- 문제 선택
- 문제 표시
- 선택지 표시
- 답안 입력
- 정답 판정
- 해설 표시
- EXP 지급
- 오답 패널티

## 108. Reward System
- EXP
- Coins
- Item
- Skill
- Stage Reward
- Difficulty Bonus

## 109. Damage System
- Attack
- Defense
- Damage
- Critical
- Damage Clamp
- HP 감소
- Death

## 110. Cooldown System
- Skill Cooldown
- Item Cooldown
- Attack Cooldown
- Timer
- Coroutine 활용

## 111. Object Pooling
- Object Pool
- 생성/삭제 비용 감소
- 반복 객체 재사용
- Instantiate / Destroy 최소화

---

# Part 11. 디버깅

## 112. Console
- Error
- Warning
- Log

## 113. Debug.Log
- 변수 확인
- 실행 흐름 확인
- 상태 확인

## 114. NullReferenceException
- null 참조
- Inspector 참조 확인
- GetComponent 확인

## 115. 실행 흐름 분석

```text
Error
 ↓
발생 위치
 ↓
호출 흐름
 ↓
변수 값
 ↓
참조 상태
 ↓
수정
 ↓
재실행
```

## 116. Assertion
- Debug.Assert
- 예상 조건 검사
- 개발 중 오류 조기 발견

## 117. Defensive Programming
- null 검사
- 범위 검사
- 잘못된 입력 처리
- 예외 상황 대비

---

# Part 12. 성능 최적화

## 118. Profiler
- CPU Usage
- GPU
- Memory
- Rendering
- Garbage Collection

## 119. Garbage Collection
- GC의 개념
- 불필요한 Allocation
- GC Spike

## 120. Draw Call
- Draw Call의 개념
- 렌더링 비용

## 121. Batching
- Batching 개념
- Static Batching
- Dynamic Batching

## 122. Memory
- Heap
- Allocation
- Garbage Collection
- Memory 사용량

## 123. CPU / GPU
- CPU Bottleneck
- GPU Bottleneck
- Rendering Cost
- Physics Cost
- Script Cost

## 124. Optimization 원칙

```text
기능 구현
 ↓
플레이 테스트
 ↓
Profiler
 ↓
병목 확인
 ↓
필요한 부분만 최적화
 ↓
재측정
```

---

# Part 13. SOLO SAT 실전 시스템

## 125. Player System
- PlayerData
- HP
- MaxHP
- Defense
- EXP
- Level
- Coins
- CurrentStage

## 126. Question System
- QuestionData
- QuestionManager
- Question UI
- Answer Check
- Difficulty
- EXP
- Penalty

## 127. Battle System
- EnemyData
- EnemyManager
- BattleManager
- Attack
- Damage
- HP
- Death

## 128. EXP / Level System

```text
Question
 ↓
Correct
 ↓
EXP
 ↓
Level Threshold
 ↓
Level Up
```

## 129. Item System

```text
ItemData
 ↓
ItemManager
 ↓
Acquire
 ↓
Inventory
 ↓
Use
 ↓
Effect
```

## 130. Inventory System
- Item ID
- Count
- Rarity
- Upgrade
- Add
- Remove
- Use

## 131. Skill System
- SkillData
- SkillManager
- Skill Effect
- Cooldown
- Activation
- Subject-specific Skill

## 132. Attribute System

6개 학습 속성:

- 국어
- 수학
- 영어
- 한국사
- 통합사회
- 통합과학

- Attribute Level
- Attribute EXP
- Attribute Bonus
- Subject-specific Effect

## 133. Combination System

```text
Attribute A
+
Attribute B
↓
Combination Skill
```

총 **36개 조합 슬롯**을 관리한다.

## 134. Stage System
- StageData
- StageManager
- Stage Clear
- Stage Unlock
- Boss
- Reward

## 135. Roguelike System
- Random Route
- Event
- Combat
- Question
- Item
- Choice
- Reward
- Risk / Reward

## 136. Learning Record

```text
Question
 ↓
Answer
 ↓
Result
 ↓
LearningRecord
```

기록:

- 총 문제 수
- 정답률
- 오답 수
- 평균 풀이 시간
- 과목별 정답률
- 단원별 정답률

## 137. Save System

```text
Game State
 ↓
SaveData
 ↓
Serialization
 ↓
JSON
 ↓
File
```

## 138. 전체 시스템 통합

```text
QuestionData
      ↓
QuestionManager
      ↓
Question UI
      ↓
Answer Check
      ↓
BattleManager
      ↓
EXP / Penalty
      ↓
PlayerData
      ↓
Level / Item / Skill
      ↓
Attribute
      ↓
Combination
      ↓
Stage
      ↓
SaveData
```

---

# Part 14. SOLO SAT 구현 순서

1. Unity 프로젝트 생성
2. Player
3. Movement
4. Jump
5. Camera
6. Tilemap
7. Collider
8. Enemy
9. Enemy AI
10. Battle
11. HP
12. Question Object
13. Question UI
14. Question Data
15. Answer Checking
16. EXP
17. Level
18. Score
19. Game Over
20. Result
21. Item
22. Inventory
23. Hotbar
24. Skill
25. Save
26. Scene
27. Stage
28. Animation
29. Sound
30. Roguelike
31. Attribute
32. Combination
33. Learning Analytics
34. Optimization
35. Build

---

# Part 15. 최종 학습 방향

```text
C# 문법
 ↓
자료구조
 ↓
객체지향
 ↓
Unity 구조
 ↓
Unity Component
 ↓
2D Physics
 ↓
UI
 ↓
Animation
 ↓
Scene
 ↓
Coroutine
 ↓
Data
 ↓
Event / FSM
 ↓
Architecture
 ↓
Debugging
 ↓
Optimization
 ↓
SOLO SAT Systems
```

최종적으로는 **“C#으로 코드를 작성하고, Unity의 Component와 시스템을 이용해 실제 게임으로 연결하는 능력”**을 목표로 한다.

---

# 📌 핵심 원칙

1. 기능 구현을 먼저 한다.
2. 작은 단위로 테스트한다.
3. 데이터와 게임 로직을 분리한다.
4. Manager의 책임을 분리한다.
5. 문제·아이템·스킬·적·스테이지는 가능한 한 데이터 중심으로 관리한다.
6. 오류가 발생하면 첫 번째/root error부터 해결한다.
7. 최적화는 Profiler로 병목을 확인한 뒤 필요한 부분만 수행한다.
8. 최종 목표는 문법 암기가 아니라 **실제 SOLO SAT 시스템 구현**이다.
