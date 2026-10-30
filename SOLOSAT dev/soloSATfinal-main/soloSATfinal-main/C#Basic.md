C# / Unity 핵심 개념

Part 1. C# 기초

1. 변수 (Variable)

* 변수의 개념
* 변수 선언과 초기화
* 변수에 값 대입
* 변수의 유효 범위

2. 자료형 (Data Type)

* int
* float
* double
* bool
* char
* string
* decimal

3. 상수 (const)

* const
* 상수와 변수의 차이

4. var

* var의 개념
* 컴파일러의 타입 추론
* 명시적 자료형과의 차이

5. 연산자

* 산술 연산자 + - * / %
* 대입 연산자 =
* 복합 대입 연산자 += -= *= /=
* 비교 연산자 == != > < >= <=
* 논리 연산자 && || !
* 증감 연산자 ++ --

6. 조건문

* if
* else if
* else
* 중첩 조건문
* switch

7. 반복문

* for
* foreach
* while
* do while
* break
* continue

8. 메서드 (Method)

* 메서드 선언
* 호출
* 매개변수 (Parameter)
* 반환값 (Return)
* void
* 메서드 오버로딩

9. 배열 (Array)

* 배열 선언
* 배열 초기화
* 인덱스
* 배열 순회
* 다차원 배열

10. List

* List<T>
* Add
* Remove
* Count
* 인덱스 접근
* 리스트 순회

11. Dictionary

* Dictionary<TKey, TValue>
* Key / Value
* Add
* ContainsKey
* 값 검색 및 수정

12. null

* null의 의미
* null 검사
* NullReferenceException

⸻

Part 2. C# 객체지향 프로그래밍

13. Class

* 클래스 선언
* 필드 (Field)
* 메서드
* 객체 생성

14. Object

* 객체의 개념
* new
* 클래스와 객체의 관계

15. Constructor

* 생성자
* 기본 생성자
* 매개변수가 있는 생성자

16. 접근 제한자

* public
* private
* protected
* internal

17. Property

* Property의 개념
* get
* set
* 자동 구현 Property

18. static

* static 변수
* static 메서드
* 인스턴스와 static의 차이

19. 상속 (Inheritance)

* 부모 클래스
* 자식 클래스
* :
* 코드 재사용

20. 다형성 (Polymorphism)

* 다형성의 개념
* virtual
* override

21. 추상 클래스

* abstract
* 추상 메서드
* 추상 클래스의 목적

22. Interface

* Interface 선언
* Interface 구현
* 다중 Interface

23. Struct

* struct
* Class와 Struct의 차이

24. Enum

* enum
* 열거형
* 상태와 종류 표현

25. Serializable

* [Serializable]
* 데이터 직렬화의 개념

26. Exception

* 예외의 개념
* try
* catch
* finally
* throw

27. Delegate

* Delegate의 개념
* 메서드를 변수처럼 전달

28. Event

* Event의 개념
* 이벤트 발생과 구독

29. Lambda

* Lambda Expression
* =>

30. Action / Func

* Action
* Func
* Delegate와의 관계

⸻

Part 3. Unity 기본 구조

31. Unity Editor

* Scene View
* Game View
* Hierarchy
* Inspector
* Project
* Console

32. Project / Scene

* Unity Project
* Scene
* Scene 저장
* Scene 전환

33. GameObject

* GameObject의 개념
* GameObject 생성
* 활성화 / 비활성화

34. Component

* Component의 개념
* Component 추가
* Component 제거
* Component와 GameObject의 관계

35. Transform

* Position
* Rotation
* Scale
* Local / World 좌표

36. MonoBehaviour

* MonoBehaviour
* Unity Component Script
* GameObject와 Script 연결

37. Unity Lifecycle

* Awake()
* Start()
* Update()
* FixedUpdate()
* LateUpdate()

38. GetComponent

* Component 가져오기
* Component 참조
* GetComponent<T>()

39. Instantiate

* Prefab / Object 복제
* Instantiate()

40. Destroy

* GameObject 삭제
* Destroy()

⸻

Part 4. Unity 2D

41. Sprite

* Sprite
* Sprite Import
* SpriteRenderer

42. SpriteRenderer

* Sprite 표시
* Sorting Layer
* Order in Layer

43. Rigidbody2D

* 2D 물리
* Gravity Scale
* Mass
* Constraints
* Linear Velocity

44. Collider2D

* Collider의 개념
* BoxCollider2D
* CircleCollider2D
* CapsuleCollider2D
* PolygonCollider2D

45. Collision

* Collision 개념
* OnCollisionEnter2D
* OnCollisionStay2D
* OnCollisionExit2D

46. Trigger

* Trigger 개념
* OnTriggerEnter2D
* OnTriggerStay2D
* OnTriggerExit2D

47. Layer

* Layer
* LayerMask
* 충돌 대상 분리

48. Tag

* Tag
* 객체 분류
* CompareTag()

49. Physics Material 2D

* 마찰
* 탄성
* 물리 재질

50. Raycast

* Raycast 개념
* 방향성 충돌 검사
* Physics2D.Raycast()

51. Vector2 / Vector3

* 벡터
* 방향
* 위치
* 이동량

52. Mathf

* Unity 수학 함수
* Clamp
* Lerp
* Abs
* Min / Max
* Sin / Cos 등

53. Time

* Time.deltaTime
* Time.time
* 시간 기반 처리

⸻

Part 5. Unity 2D 맵 / 그래픽

54. Tilemap

* Tilemap
* Grid
* Tile Palette
* Tile
* Tilemap Collider

55. Camera

* Camera
* Orthographic
* Perspective
* Camera Follow
* Camera Bounds

56. Prefab

* Prefab 생성
* Prefab 수정
* Prefab Instance
* Prefab Variant

57. Animation

* Animation Clip
* Animator
* Animator Controller
* Parameter
* Transition
* State

58. Sorting

* Sorting Layer
* Order in Layer
* 2D 오브젝트 표시 순서

⸻

Part 6. Unity UI

59. Canvas

* Canvas
* Screen Space
* World Space

60. RectTransform

* Position
* Width / Height
* Anchor
* Pivot

61. TextMeshPro

* TMP Text
* 텍스트 변경
* 폰트 설정

62. Image

* Image Component
* Sprite 표시
* Fill

63. Button

* Button
* OnClick
* 버튼 이벤트

64. Slider

* Slider
* Value
* Min / Max
* HP / EXP Bar

65. Canvas Scaler

* UI 해상도 대응
* Scale With Screen Size

66. EventSystem

* UI 입력 처리
* Pointer / Button Event

⸻

Part 7. 입력 / 시간 / 실행 제어

67. Input System

* Input System
* Input Action
* Action Map
* Player Input

68. Input

* 키보드 입력
* 마우스 입력
* 컨트롤러 입력

69. Coroutine

* Coroutine
* IEnumerator
* StartCoroutine()
* StopCoroutine()

70. WaitForSeconds

* 일정 시간 대기
* Coroutine과 결합

⸻

Part 8. Unity 데이터 관리

71. ScriptableObject

* ScriptableObject 개념
* 데이터 Asset
* Inspector에서 데이터 수정
* 코드와 데이터 분리

72. Serialization

* Unity Serialization
* [SerializeField]
* 데이터 저장 구조

73. JSON

* JSON 구조
* Serialize
* Deserialize
* JSON 파일 저장

74. PlayerPrefs

* 간단한 값 저장
* PlayerPrefs의 용도와 한계

75. SaveData

* 저장 전용 데이터 클래스
* 게임 오브젝트와 저장 데이터 분리

⸻

Part 9. Unity Scene / 시스템 관리

76. SceneManager

* Scene Load
* Scene 전환
* Scene 관리

77. GameManager

* 전체 게임 흐름 관리
* 전역 시스템 관리

78. Singleton

* Singleton 개념
* 전역 접근
* Singleton의 장단점과 주의점

79. Manager Architecture

* Manager 역할 분리
* 책임 분리
* 시스템 간 의존성 관리

⸻

Part 10. 게임 시스템 구조

80. State Machine / FSM

* State
* Transition
* State Machine
* AI 상태 관리

예:

Idle
 ↓
Chase
 ↓
Attack
 ↓
Hit
 ↓
Dead

81. Event 기반 구조

* 시스템 간 이벤트 전달
* 결합도 감소
* Event / Delegate 활용

82. Data-Driven Design

* 데이터와 코드 분리
* ScriptableObject 활용
* 하드코딩 최소화

83. Object Pooling

* Object Pool
* 생성/삭제 비용 감소
* 반복 객체 재사용

⸻

Part 11. 디버깅

84. Console

* Error
* Warning
* Log

85. Debug.Log

* 변수 확인
* 실행 흐름 확인
* 상태 확인

86. NullReferenceException

* null 참조
* Inspector 참조 확인
* GetComponent 확인

87. 실행 흐름 분석

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

⸻

Part 12. 성능 최적화

88. Profiler

* CPU Usage
* GPU
* Memory
* Rendering
* Garbage Collection

89. Garbage Collection

* GC의 개념
* 불필요한 Allocation
* GC Spike

90. Draw Call

* Draw Call의 개념
* 렌더링 비용

91. Batching

* Batching 개념
* Static / Dynamic Batching

92. Object Pooling

* 반복적인 Instantiate / Destroy 최소화
* Pool 재사용

93. 최적화 원칙

기능 구현
 ↓
플레이 테스트
 ↓
Profiler
 ↓
병목 확인
 ↓
필요한 부분만 최적화

⸻

13. C# / Unity 핵심 100개

C# 기초

1. Variable
2. Data Type
3. int
4. float
5. bool
6. string
7. const
8. var
9. Operator
10. Comparison
11. Logical Operator
12. if
13. else if
14. else
15. switch
16. for
17. foreach
18. while
19. break
20. continue
21. Method
22. Parameter
23. Return
24. Array
25. List
26. Dictionary
27. Class
28. Struct
29. Enum
30. Interface
31. Property
32. Serializable
33. null
34. try / catch
35. Debug.Log

Unity 기본

36. MonoBehaviour
37. GameObject
38. Component
39. Transform
40. Vector2
41. Vector3
42. Time.deltaTime
43. Awake
44. Start
45. Update
46. FixedUpdate
47. LateUpdate
48. GetComponent
49. Instantiate
50. Destroy
51. Prefab
52. Scene
53. SceneManager

Unity 2D / Physics

54. Rigidbody2D
55. Linear Velocity
56. Gravity Scale
57. Collider2D
58. OnCollisionEnter2D
59. OnTriggerEnter2D
60. Trigger
61. Collision
62. Layer
63. LayerMask
64. Tag
65. Physics Material 2D
66. Raycast
67. Tilemap
68. Grid

Graphics / Animation

69. SpriteRenderer
70. Material
71. Shader
72. Sorting Layer
73. Order in Layer
74. Animation Clip
75. Animator
76. Animator Controller
77. Transition
78. Animator Parameter

UI / Input

79. Canvas
80. RectTransform
81. TextMeshPro
82. Button
83. Slider
84. Image
85. Anchor
86. Canvas Scaler
87. EventSystem
88. Input System
89. Input Action

시스템 / 아키텍처

90. Coroutine
91. WaitForSeconds
92. ScriptableObject
93. Delegate
94. Event
95. Lambda
96. Singleton
97. GameManager
98. State Machine / FSM
99. Object Pooling
100. Save System / Serialization / SaveData / Profiler / 책임 분리

⸻

14. 최종 학습 방향

C#은 단순히 문법을 외우는 것보다 다음 순서로 이해한다.

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

최종적으로는 **“C#으로 코드를 작성하고, Unity의 Component와 시스템을 이용해 실제 게임으로 연결하는 능력”**을 목표로 한다.