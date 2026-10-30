# 🎮 SOLO SAT C# / Unity 실전 교재

> **목표: C#과 Unity를 배우고, 배운 내용을 SOLO SAT의 실제 시스템으로 구현한다.**

---

## 0. 교재 사용법

각 단원은 같은 순서로 진행한다.

1. **개념** — 무엇인지 이해한다.
2. **코드 예제** — 최소 코드를 직접 작성한다.
3. **Unity 실습** — Unity에서 확인한다.
4. **SOLO SAT 적용** — 실제 프로젝트에 연결한다.
5. **연습문제** — 스스로 구현한다.
6. **완료 기준** — 다음 단원으로 넘어갈 수 있는지 확인한다.

> 이 교재는 문법 암기보다 **작은 기능을 직접 만들고 연결하는 것**을 우선한다.

---

# Part 1. C# 기초

## 1. 변수와 자료형

### 개념
변수는 값을 저장하는 이름이다. `int`, `float`, `bool`, `string` 등이 대표적인 자료형이다.

```csharp
int hp = 100;
float speed = 5.5f;
bool isAlive = true;
string playerName = "SOLO";
```

### Unity 실습
Player 오브젝트에 스크립트를 붙이고 HP와 이동 속도를 Inspector에서 확인한다.

### SOLO SAT 적용
`PlayerData`의 HP, MaxHP, EXP, Level 등의 기본 데이터에 사용한다.

### 연습문제
- HP를 150으로 설정해라.
- EXP를 35 증가시켜라.
- 플레이어가 살아 있는지 `bool`로 표현해라.

### 완료 기준
자료형을 보고 어떤 타입을 사용해야 하는지 판단할 수 있다.

---

## 2. 연산자와 조건문

```csharp
if (hp <= 0)
{
    Debug.Log("GAME OVER");
}
else if (hp < 30)
{
    Debug.Log("WARNING");
}
else
{
    Debug.Log("SAFE");
}
```

### SOLO SAT 적용
정답 여부, HP 0 판정, 레벨업 조건, 보상 조건 등에 사용한다.

### 연습문제
HP가 0 이하이면 `gameOver = true`가 되도록 만들어라.

---

## 3. 반복문

```csharp
for (int i = 0; i < 5; i++)
{
    Debug.Log(i);
}
```

### SOLO SAT 적용
문제 목록, 선택지, 인벤토리 슬롯 등을 반복 처리한다.

### 연습문제
5개의 선택지를 순서대로 출력해라.

---

## 4. 메서드

```csharp
void AddExp(int amount)
{
    exp += amount;
}
```

### 핵심
메서드는 특정 작업을 하나의 단위로 묶는다.

### SOLO SAT 적용
`AddExp()`, `TakeDamage()`, `CheckAnswer()`, `UseItem()` 등의 기능을 분리한다.

### 연습문제
`TakeDamage(int damage)`를 만들어 HP를 감소시켜라.

---

## 5. 배열 / List / Dictionary

```csharp
List<string> choices = new List<string>();
choices.Add("A");
choices.Add("B");
```

```csharp
Dictionary<int, string> questionNames = new Dictionary<int, string>();
questionNames[1] = "다항식 문제";
```

### SOLO SAT 적용
- `List` → 문제 목록, 인벤토리 목록
- `Dictionary` → ID 기반 데이터 검색

### 연습문제
5개의 선택지를 List에 저장하고 출력해라.

---

## 6. 타입 변환 / 문자열 / null

### 핵심
서로 다른 자료형을 사용할 때 명시적 변환이 필요할 수 있다.

```csharp
float value = 10.5f;
int number = (int)value;
```

문자열 보간:

```csharp
Debug.Log($"HP: {hp}");
```

`null`은 참조가 존재하지 않는 상태를 나타낸다.

### SOLO SAT 적용
UI에 수치 표시, 저장 데이터 변환, 참조 오류 방지 등에 사용한다.

### 연습문제
EXP와 Level을 한 줄의 문자열로 출력해라.

---

# Part 2. C# 객체지향

## 7. Class

```csharp
public class PlayerData
{
    public int hp;
    public int exp;
    public int level;
}
```

### SOLO SAT 적용
PlayerData, QuestionData, ItemData, EnemyData 등을 클래스로 모델링한다.

---

## 8. 접근 제한자와 캡슐화

```csharp
private int hp;

public void TakeDamage(int damage)
{
    hp -= damage;
}
```

외부에서 데이터를 무분별하게 변경하지 못하도록 책임을 제한한다.

### SOLO SAT 적용
HP 변경은 Player 객체가 담당하고, UI가 직접 HP를 변경하지 않도록 설계한다.

---

## 9. Property

```csharp
public int HP { get; private set; }
```

읽기는 허용하고 변경은 클래스 내부에서만 허용하는 구조를 만들 수 있다.

---

## 10. Enum

```csharp
public enum Difficulty
{
    Easy,
    Normal,
    Hard,
    VeryHard,
    Extreme
}
```

### SOLO SAT 적용
난이도, 게임 상태, 아이템 등급, 전투 상태 등을 표현한다.

---

## 11. Interface / 상속 / 다형성

공통 동작을 추상화할 때 사용한다.

```csharp
public interface IUsable
{
    void Use();
}
```

### 핵심 원칙
상속을 무조건 사용하는 것이 아니라 **공통 책임이 실제로 존재할 때** 사용한다. 서로 다른 시스템을 연결할 때는 조합(Composition)이 더 적절할 수도 있다.

### SOLO SAT 적용
사용 가능한 아이템, 스킬 효과 등의 공통 인터페이스를 설계할 수 있다.

---

## 12. Generic / 예외 처리

Generic은 타입을 재사용 가능한 형태로 만들 때 사용한다.

```csharp
List<int> numbers = new List<int>();
List<string> names = new List<string>();
```

예외 처리는 예상 가능한 런타임 문제를 다룰 때 사용한다.

```csharp
try
{
    // 위험할 수 있는 작업
}
catch (Exception e)
{
    Debug.LogError(e.Message);
}
```

---

# Part 3. Unity 기본 구조

## 13. GameObject / Component / Transform

Unity의 GameObject는 장면 속 객체이고 Component가 기능을 제공한다. Transform은 위치·회전·크기를 담당한다.

```csharp
transform.position = new Vector3(0, 1, 0);
```

### SOLO SAT 적용
Player, Enemy, QuestionObject, ItemObject 모두 GameObject와 Component의 조합으로 구성한다.

---

## 14. MonoBehaviour와 생명주기

```csharp
void Awake() { }
void Start() { }
void Update() { }
void FixedUpdate() { }
void LateUpdate() { }
```

- `Awake` → 초기화
- `Start` → 시작 시 준비
- `Update` → 프레임 기반 처리
- `FixedUpdate` → 물리 처리
- `LateUpdate` → 후처리

### SOLO SAT 적용
게임 초기화, 입력, 물리 이동, 카메라 추적 등을 적절한 생명주기에 배치한다.

---

## 15. GetComponent / Instantiate / Destroy

```csharp
Rigidbody2D rb = GetComponent<Rigidbody2D>();
```

```csharp
Instantiate(enemyPrefab, position, Quaternion.identity);
```

```csharp
Destroy(gameObject);
```

### 연습문제
Enemy Prefab을 생성하고 일정 조건에서 제거해라.

---

## 16. Inspector / Serialization

Unity에서 Inspector로 수정해야 하는 값은 직렬화 가능한 필드로 노출할 수 있다.

```csharp
[SerializeField] private float moveSpeed = 5f;
```

### SOLO SAT 적용
플레이어 속도, 적 HP, 제한시간 등을 코드 수정 없이 조정할 수 있도록 만든다.

---

# Part 4. Unity 2D / 물리

## 17. Rigidbody2D

2D 물리 시뮬레이션을 적용하는 Component다.

핵심 개념:
- Mass
- Gravity Scale
- Linear Velocity
- Collision Detection

---

## 18. Collider2D / Trigger

Collider는 충돌 영역을 정의한다. Trigger는 물리적으로 밀어내는 충돌 대신 이벤트 검출에 활용한다.

```csharp
void OnTriggerEnter2D(Collider2D other)
{
    Debug.Log(other.name);
}
```

### SOLO SAT 적용
맵의 문제 오브젝트, 아이템, 이벤트 영역을 Trigger로 만들 수 있다.

---

## 19. Layer / LayerMask / Physics Query

레이어를 이용해 어떤 객체끼리 상호작용할지 제한한다.

```csharp
RaycastHit2D hit = Physics2D.Raycast(transform.position, Vector2.right, 5f);
```

### SOLO SAT 적용
Enemy 탐색, 바닥 감지, 상호작용 대상 검색 등에 사용한다.

---

## 20. 이동과 점프

```csharp
float x = Input.GetAxisRaw("Horizontal");
rb.linearVelocity = new Vector2(x * speed, rb.linearVelocity.y);
```

> 실제 프로젝트에서는 사용 중인 Unity/Input System 버전에 맞춰 입력 API를 통일한다.

### 연습문제
좌우 이동과 점프가 가능한 Player를 구현해라.

---

# Part 5. 맵 / 그래픽 / 애니메이션

## 21. Tilemap / Grid

Tilemap은 2D 맵을 타일 단위로 구성한다.

구조 예시:

```text
Grid
├ Ground Tilemap
├ Wall Tilemap
├ Decoration Tilemap
└ Collision Tilemap
```

### SOLO SAT 적용
Stage 1~Boss Stage의 기본 맵 제작에 사용한다.

---

## 22. SpriteRenderer / Sorting Layer / Order in Layer

2D 객체가 어떤 순서로 렌더링될지 관리한다.

### 연습문제
Player가 배경보다 앞에 표시되도록 렌더 순서를 구성해라.

---

## 23. Animator

```text
Idle → Run
  ↓
Jump → Fall
```

전투에서는 Idle / Attack / Hit / Dead 등을 구성할 수 있다.

### SOLO SAT 적용
Player와 Enemy의 상태 변화가 시각적으로 전달되도록 한다.

---

## 24. Material / Shader / Particle System

Material은 렌더링 설정을, Shader는 화면에 그려지는 방식을 정의한다. Particle System은 효과를 반복적으로 생성하는 데 사용한다.

### SOLO SAT 적용
정답 공격 효과, 레벨업 효과, 보스 효과 등을 구현한다.

---

# Part 6. UI

## 25. Canvas / RectTransform / Anchor

UI는 Canvas 안에 배치하며 RectTransform으로 위치와 크기를 관리한다. Anchor를 이용하면 화면 크기 변화에 대응하기 쉽다.

---

## 26. TextMeshPro / Button / Slider / Image

### SOLO SAT UI
```text
LV 12    EXP ███████░░░
HP ██████░░

[ Question Panel ]
① 보기
② 보기
③ 보기
④ 보기
⑤ 보기

[1][2][3][4][5]
```

---

## 27. UI 이벤트와 상태 관리

버튼을 눌렀을 때 게임 로직을 직접 뒤섞기보다 UI 이벤트 → 시스템 호출 구조를 유지한다.

예:

```text
Button
 ↓
QuestionUI
 ↓
QuestionManager.CheckAnswer()
 ↓
Game Result
```

### 연습문제
정답 버튼을 누르면 정답 판정 함수가 실행되도록 연결해라.

---

## 28. UI 데이터 갱신

데이터가 바뀌면 UI가 그 결과를 표시한다.

```text
PlayerData
 ↓
EXPManager
 ↓
Player EXP 변경
 ↓
UI Refresh
 ↓
EXP Bar
```

UI가 게임 규칙을 직접 소유하지 않도록 한다.

---

# Part 7. 입력 / 시간 / Coroutine

## 29. Input과 게임 로직 분리

입력 코드는 "무엇을 눌렀는가"를 처리하고 게임 시스템은 "그 행동이 무엇을 의미하는가"를 처리한다.

예:

```text
Input Action
 ↓
PlayerController
 ↓
Player System
```

---

## 30. Time.deltaTime / Update / FixedUpdate

프레임 속도에 영향을 덜 받는 이동과 시간 계산을 위해 `Time.deltaTime`을 이해한다.

물리 기반 처리는 `FixedUpdate`와 연관된다.

---

## 31. Coroutine / WaitForSeconds

```csharp
IEnumerator AttackCooldown()
{
    yield return new WaitForSeconds(1f);
    canAttack = true;
}
```

### SOLO SAT 적용
- 공격 쿨다운
- 무적 시간
- 문제 제한시간 연출
- UI 순차 표시
- 스킬 쿨다운

---

# Part 8. 데이터 중심 설계

## 32. ScriptableObject

Unity에서 재사용 가능한 데이터를 Asset 형태로 관리할 수 있다.

예:

```csharp
[CreateAssetMenu]
public class ItemData : ScriptableObject
{
    public string id;
    public string itemName;
    public string description;
}
```

### SOLO SAT 적용
문제, 아이템, 적, 스테이지 데이터를 코드와 분리한다.

---

## 33. QuestionData

```text
QuestionData
├ ID
├ Subject
├ Category
├ Difficulty
├ Question
├ Choices
├ Answer
├ Explanation
├ EXP
└ Penalty
```

### 핵심 원칙
새 문제를 추가할 때 `QuestionManager`의 코드를 수정하지 않는 구조를 지향한다.

---

## 34. ItemData / EnemyData / StageData

각 시스템의 데이터와 실행 로직을 분리한다.

```text
ItemData → ItemManager
EnemyData → Enemy/Battle System
StageData → StageManager
```

### 연습문제
적의 HP와 공격력을 데이터로 분리해라.

---

# Part 9. Scene / Manager 구조

## 35. SceneManager

씬 전환을 중앙에서 관리한다.

```csharp
SceneManager.LoadScene("Battle");
```

### SOLO SAT
```text
Title
 ↓
CharacterSelect
 ↓
StageSelect
 ↓
Stage01
 ↓
Battle
 ↓
Result
```

---

## 36. DontDestroyOnLoad와 초기화 순서

씬이 바뀌어도 유지되어야 하는 전역 시스템은 별도 구조가 필요하다.

예:

```text
GameManager
PlayerManager
SaveManager
```

단, 전역 객체를 무분별하게 늘리지 않고 책임을 명확히 한다.

---

## 37. Manager 책임 분리

```text
GameManager
├ PlayerManager
├ QuestionManager
├ EXPManager
├ LevelManager
├ ItemManager
├ SkillManager
├ InventoryManager
├ BattleManager
├ StageManager
├ SaveManager
└ UIManager
```

### 핵심
Manager 하나에 모든 로직을 넣는 **God Object**를 피한다.

---

# Part 10. 게임 시스템

## 38. Game State

게임 전체의 상태를 명시적으로 관리한다.

```text
Title
 ↓
Stage
 ↓
Question
 ↓
Result
 ↓
Game Over
```

Enum으로 상태를 표현할 수 있다.

---

## 39. Question System

```text
Question Data
 ↓
QuestionManager
 ↓
Question UI
 ↓
Player Answer
 ↓
Answer Check
 ↓
Correct / Wrong
```

### SOLO SAT 적용
정답이면 공격 성공 및 EXP 획득, 오답이면 공격 실패와 패널티를 적용한다.

---

## 40. Battle System

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
 ├ YES → Damage → Enemy HP 감소
 └ NO → Penalty
```

전투 계산은 Question UI와 분리한다.

---

## 41. Damage / HP System

```csharp
public void TakeDamage(int damage)
{
    hp -= damage;
    if (hp <= 0)
        Die();
}
```

### 연습문제
Enemy가 HP 0이 되면 Dead 상태로 바뀌도록 만들어라.

---

## 42. EXP / Level System

```text
Question
 ↓
EXP
 ↓
EXP 누적
 ↓
Threshold 도달
 ↓
Level Up
```

기본 예시:
- 중하 10
- 중 20
- 중상 35
- 상 50
- 최상 80

실제 수치는 플레이 테스트로 조정한다.

---

## 43. Reward / Item / Inventory

```text
Reward
 ↓
Item 획득
 ↓
Inventory
 ↓
Hotbar
 ↓
Use
 ↓
Effect
```

### 핵심 데이터
```text
Item ID
Count
Rarity
Upgrade
```

---

## 44. Skill / Cooldown System

스킬은 효과와 사용 조건을 분리한다.

```text
Skill Input
 ↓
CanUse?
 ↓
Effect
 ↓
Cooldown
```

예: `속독`, `암산 가속`, `직독직해` 등.

---

# Part 11. 디버깅

## 45. Console / NullReferenceException

기본 순서:

```text
Error 발생
 ↓
Console 확인
 ↓
첫 번째 오류 확인
 ↓
코드 위치 확인
 ↓
변수/참조 확인
 ↓
Inspector 확인
 ↓
수정
 ↓
재실행
```

### 핵심
오류 메시지를 무시하고 코드를 무작정 수정하지 않는다. **첫 번째 근본 오류**부터 해결한다.

---

## 46. Debug.Log / Assert

```csharp
Debug.Log($"HP = {hp}");
Debug.Assert(hp >= 0);
```

### SOLO SAT 적용
문제 ID, 정답, EXP, HP 변화 등을 개발 중 로그로 검증한다.

---

## 47. Defensive Programming

외부 입력이나 데이터가 항상 정상이라고 가정하지 않는다.

예:
- null 검사
- 범위 검사
- 잘못된 ID 처리
- 빈 문제 목록 처리

---

# Part 12. 성능 최적화

## 48. CPU / GPU / Memory

성능 문제를 막연히 "최적화"하지 않는다.

먼저:

```text
기능 완성
 ↓
플레이 테스트
 ↓
Profiler
 ↓
병목 확인
 ↓
필요한 부분만 최적화
```

---

## 49. Garbage Collection / Allocation

런타임에서 객체를 반복 생성하면 메모리 할당과 GC 부담이 커질 수 있다.

특히 반복적으로 생성·삭제되는 탄환, 이펙트, 적 등을 확인한다.

---

## 50. Object Pooling

자주 생성하고 삭제하는 객체를 미리 만들어 재사용한다.

```text
Pool
 ↓
Object 활성화
 ↓
사용
 ↓
비활성화
 ↓
Pool 반환
```

### SOLO SAT 적용 후보
- 공격 이펙트
- 탄환
- 반복 생성되는 적
- 파티클

단, **Profiler로 병목이 확인된 경우** 우선 적용한다.

---

# Part 13. SOLO SAT 실전 시스템

## 51. Player System

### 목표
플레이어 이동, HP, EXP, Level, 상태를 관리한다.

```text
PlayerController
PlayerData
PlayerManager
```

### 실습
좌우 이동 → 점프 → HP → EXP → Level 순으로 연결한다.

---

## 52. Question System

### 목표
문제 데이터를 읽고 출제하고 정답을 판정한다.

```text
QuestionData
 ↓
QuestionManager
 ↓
QuestionUI
 ↓
Answer
 ↓
CheckAnswer
```

### 실습
5지선다 문제 5개를 만들어 무작위로 출제한다.

---

## 53. Battle System

### 목표
문제 정답을 전투 판정으로 연결한다.

```text
정답
 ↓
Attack Success
 ↓
Damage
 ↓
Enemy HP 감소
```

오답:

```text
오답
 ↓
Attack Fail
 ↓
Penalty
```

---

## 54. EXP / Level System

### 목표
학습 성과를 RPG 성장으로 변환한다.

```text
정답
 ↓
EXP
 ↓
Threshold
 ↓
Level Up
 ↓
Stat Increase
```

### 실습
레벨 1에서 시작해 일정 EXP마다 레벨업하도록 구현한다.

---

## 55. Item / Inventory / Hotbar

### 목표
문제 풀이 보조 효과를 가진 아이템을 관리한다.

```text
ItemData
 ↓
Inventory
 ↓
Hotbar
 ↓
Use Item
 ↓
Effect
```

핫바:

```text
[1][2][3][4][5]
```

---

## 56. Skill System

```text
Skill
├ ID
├ Name
├ Effect
├ Cooldown
└ Condition
```

### 실습
간단한 스킬 하나를 만들어 EXP 보너스 또는 제한시간 보너스를 적용한다.

---

## 57. Attribute / Combination System

6개 학습 영역을 속성으로 취급한다.

```text
국어
수학
영어
한국사
통합사회
통합과학
```

조합 시스템은 총 36개 슬롯을 설계한다.

예:
- 국어 + 수학 → 음운 인수분해
- 수학 + 영어 → 직독 미적분
- 통합사회 + 과학 → 데이터 생태론

### 실습
먼저 속성 2개를 저장하고 조합 결과를 반환하는 기능부터 만든다.

---

## 58. Stage System

```text
Stage 1
 ↓
Stage 2
 ↓
Stage 3
 ↓
Stage 4
 ↓
Boss
```

StageData에 문제 난이도, 적 정보, 제한시간, 이벤트 등을 저장한다.

---

## 59. Roguelike System

매 플레이마다 일부 요소가 달라지도록 한다.

```text
Stage
 ↓
Choice
 ↓
Next Area
 ↓
Combat / Event / Item
 ↓
Next Choice
```

문제와 아이템 선택이 다음 경로에 영향을 주도록 확장한다.

---

## 60. Learning Record

기록할 데이터:

- 총 문제 수
- 정답률
- 오답 수
- 평균 풀이 시간
- 과목별 정답률
- 단원별 정답률
- EXP
- Level
- 아이템 사용
- 스킬 사용

향후:

```text
오답 데이터
 ↓
약점 분석
 ↓
취약 단원
 ↓
관련 문제 우선 출제
```

---

## 61. Save System

저장 데이터:

```text
SaveData
├ Level
├ EXP
├ Coins
├ CurrentStage
├ Inventory
├ Skills
└ LearningRecord
```

원칙: 게임 오브젝트 자체가 아니라 **필요한 상태 데이터**를 저장한다.

---

## 62. 전체 시스템 통합

최종 데이터 흐름:

```text
Question Data
 ↓
QuestionManager
 ↓
Question UI
 ↓
Player Answer
 ↓
Answer Check
 ├─ Correct → EXP / Attack / Reward
 └─ Wrong → Penalty
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

### 최종 목표

> **문제를 풀면 실제 게임 플레이가 진행되고, 학습 성과가 RPG 성장 데이터로 이어지는 구조를 완성한다.**

---

# Part 14. 구현 순서

```text
01 Unity Project
02 Player
03 Movement
04 Jump
05 Camera
06 Tilemap
07 Collider
08 Enemy
09 Enemy AI
10 Battle
11 HP
12 Question Object
13 Question UI
14 Question Data
15 Answer Check
16 EXP
17 Level
18 Score
19 Game Over
20 Result
21 Item
22 Inventory
23 Hotbar
24 Skill
25 Save
26 Scene
27 Stage
28 Animation
29 Sound
30 Roguelike
31 Attribute
32 Combination
33 Learning Analytics
34 Optimization
35 Build
```

### MVP 우선순위

MVP에서는 다음만 먼저 완성한다.

```text
Start
 ↓
Subject Select
 ↓
Question
 ↓
5 Choices
 ↓
Answer
 ↓
EXP
 ↓
Level
 ↓
Result
```

전투와 대형 콘텐츠는 MVP 이후 단계적으로 추가한다.

---

# Part 15. 최종 학습 체크

## C#

- [ ] 변수 / 자료형
- [ ] 연산자
- [ ] 조건문
- [ ] 반복문
- [ ] 메서드
- [ ] 배열 / List / Dictionary
- [ ] Class
- [ ] Enum
- [ ] Interface
- [ ] Property
- [ ] null
- [ ] 예외 처리

## Unity

- [ ] GameObject
- [ ] Component
- [ ] Transform
- [ ] MonoBehaviour
- [ ] Unity 생명주기
- [ ] GetComponent
- [ ] Prefab
- [ ] Instantiate / Destroy
- [ ] Scene
- [ ] SceneManager

## 2D

- [ ] Rigidbody2D
- [ ] Collider2D
- [ ] Trigger
- [ ] Layer / LayerMask
- [ ] Raycast
- [ ] Tilemap
- [ ] Animator
- [ ] SpriteRenderer

## 게임 시스템

- [ ] Question System
- [ ] Answer Check
- [ ] EXP
- [ ] Level
- [ ] HP / Damage
- [ ] Battle
- [ ] Item
- [ ] Inventory
- [ ] Skill
- [ ] Save
- [ ] Stage
- [ ] Roguelike
- [ ] Learning Record

## 고급

- [ ] ScriptableObject
- [ ] FSM
- [ ] Coroutine
- [ ] Event / Delegate
- [ ] SaveData
- [ ] Serialization
- [ ] Debugging
- [ ] Profiler
- [ ] Object Pooling
- [ ] 책임 분리

---

# 🧭 최종 학습 방향

```text
C# 기초
 ↓
C# 객체지향
 ↓
Unity 기본
 ↓
Unity 2D
 ↓
UI / Input
 ↓
데이터 설계
 ↓
게임 시스템
 ↓
SOLO SAT MVP
 ↓
Battle
 ↓
Item / Skill
 ↓
Save
 ↓
Stage
 ↓
Roguelike
 ↓
Attribute / Combination
 ↓
Learning Analytics
 ↓
Optimization
 ↓
Release
```

**핵심 원칙:** 기능을 많이 배우는 것이 목표가 아니라, 배운 개념을 실제 SOLO SAT 시스템에 연결할 수 있는 것이 목표다.
