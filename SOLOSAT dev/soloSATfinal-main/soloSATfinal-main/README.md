# 🎮 SOLO SAT

## 나 혼자만 1등급

> **문제를 풀수록 강해지는 수능 RPG**

SOLO SAT는 학습 콘텐츠와 RPG 시스템을 결합한 **2D 사이드스크롤 RPG × 로그라이크 학습 게임**이다.

문제 풀이를 단순한 퀴즈가 아니라 게임의 핵심 플레이로 만들고,
**학습 → 성취 → 보상 → 성장 → 도전 → 재학습**의 순환 구조를 구현하는 것을 목표로 한다.

---

## 📌 프로젝트 정보

- 프로젝트명: **SOLO SAT**
- 부제: **나 혼자만 1등급**
- 프로젝트 계열: **VIAUS 프로젝트**
- 장르: **학습 연동형 2D 사이드스크롤 RPG × 로그라이크**
- 엔진: **Unity 2D**
- 플랫폼: **Windows PC**
- 화면비: **16:9**
- 개발 언어: **C#**
- 프로토타입: **Scratch**
- 시스템 검증: **Python**
- 본개발: **Unity + C#**
- 초기 문제 데이터: **120문제**
- 교육과정: **2022 개정 교육과정**
- 핵심 방향: **데이터 중심 · 모듈화 · 단계적 확장**

---

# 🎯 핵심 철학

### 공부 = 플레이

SOLO SAT에서는 공부와 게임을 분리하지 않는다.

> **공부 = 게임 플레이**

### 문제 = 전투

```text
문제 등장
  ↓
문제 해결
  ↓
정답
  ↓
공격 성공
  ↓
적 HP 감소
```

### 학습 성과 = 성장 자원

문제를 잘 풀수록 EXP, 레벨, 보상, 아이템, 스킬, 스테이지 진행으로 연결된다.

---

# 📚 초기 학습 영역

- 📚 국어
- ➗ 수학
- 🇬🇧 영어
- 🏺 한국사
- 🌏 통합사회
- 🧪 통합과학

---

# 📖 교육과정

## 📚 국어

- 듣기·말하기
- 읽기
- 쓰기
- 문법
- 문학
- 매체

게임 콘텐츠:

- 독해
- 문학 분석
- 문법
- 논증
- 토론
- 매체 분석
- 보고서 작성
- 주제 통합적 읽기

## ➗ 수학

### 공통수학1

- 다항식
- 방정식과 부등식
- 경우의 수
- 행렬

### 공통수학2

- 도형의 방정식
- 집합과 명제
- 함수와 그래프

### 향후 선택 과목

- 미적분
- 확률과 통계
- 기하

## 🇬🇧 영어

- 어휘
- 문법
- 구문
- 독해
- 듣기
- 문맥 분석
- 정보 해석

## 🏺 한국사

- 시대 흐름
- 사건
- 사료
- 문화
- 왕조
- 근현대사
- 역사적 맥락

## 🌏 통합사회

- 시간적 관점
- 공간적 관점
- 사회적 관점
- 윤리적 관점
- 인간과 사회
- 국가
- 세계
- 인권
- 헌법
- 경제
- 환경
- 시민 참여

향후 선택 과목:

- 생활과 윤리
- 윤리와 사상
- 한국지리
- 세계지리
- 동아시아사
- 세계사
- 경제
- 정치와 법
- 사회·문화

## 🧪 통합과학

### 초기 포함

**통합과학1**

- 물질과 규칙성
- 시스템과 상호작용

**통합과학2**

- 변화와 다양성
- 환경과 에너지

### 초기 제외

- 통합과학1 「과학의 기초」
- 통합과학2 「과학과 미래 사회」
- 과학탐구실험1·2

초기 콘텐츠에서는 선택 과목의 전문 내용을 무리하게 혼합하지 않는다.

향후 선택 과목:

- 물리학
- 화학
- 생명과학
- 지구과학

---

# 📝 문제 시스템

## 초기 문제 구성

총 **120문제**.

과목별 20문제:

- 국어 20
- 수학 20
- 영어 20
- 한국사 20
- 통합사회 20
- 통합과학 20

각 과목의 난이도 구성:

- 중하 4문제
- 중 4문제
- 중상 4문제
- 상 4문제
- 최상 4문제

기본 문제 형식은 **5지선다형**이다.

## Question 데이터

```text
Question
├─ id
├─ subject
├─ category
├─ difficulty
├─ question
├─ choices
├─ answer
├─ explanation
├─ exp
└─ penalty
```

문제 데이터와 게임 코드는 분리한다.

> **문제 추가를 위해 게임 로직을 수정하지 않는 구조를 지향한다.**

---

# 🎮 핵심 게임 루프

```text
START
  ↓
Stage Select
  ↓
Stage
  ↓
Exploration
  ↓
Combat / Event / Question
  ↓
Answer
  ↓
EXP / Reward / Penalty
  ↓
Growth
  ↓
Stage Clear
  ↓
Result
  ↓
Next Stage
```

---

# 🗺️ 스테이지

```text
Stage 1
  ↓
Stage 2
  ↓
Stage 3
  ↓
Stage 4
  ↓
Boss Stage
```

스테이지가 상승할수록 다음 요소가 상승한다.

- 문제 난이도
- 적 HP
- 전투 난이도
- 제한시간
- 이벤트 난이도

---

# ⚔️ 전투

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
 ├─ YES → Attack Success → Damage → Enemy HP 감소
 └─ NO  → Attack Fail → Penalty
```

전투 계산:

```text
공격 판정
 ↓
대상 탐색
 ↓
Damage 계산
 ↓
HP 감소
 ↓
사망 처리
```

### Player

- HP
- MaxHP
- Defense

### Enemy

- HP
- MaxHP
- Attack

플레이어 HP가 0이 되면 GAME OVER.

---

# ⭐ EXP & Level

기본 EXP 예시:

- 중하: 10
- 중: 20
- 중상: 35
- 상: 50
- 최상: 80

실제 수치는 플레이 테스트를 통해 조정한다.

```text
문제 풀이
 ↓
EXP 획득
 ↓
EXP 누적
 ↓
필요 EXP 도달
 ↓
LEVEL UP
 ↓
능력치 증가
 ↓
콘텐츠 해금
```

레벨은 플레이어의 전반적인 학습 성장도를 표현한다.

---

# 🎒 아이템

## 국어

비문학의 활 · 운율의 단검 · 고전시가 두루마리 · 문학 해석서 · 화법의 확성기 · 작문 수정펜 · 독해 증폭 렌즈 · 어휘 사전검 · 문장구조 큐브 · 현대시 수정구

## 수학

인수분해검 · 함수의 활 · 극한의 창 · 미분 단검 · 적분 대검 · 벡터 부메랑 · 로그 크리스탈 · 기하의 방패 · 정적분 캐논 · 가우스 연산핵

## 영어

구문해석 레이피어 · 청해 이어폰 · 문법 수정봉 · 숙어 단검 · 독해 라이플 · 빈칸추론 수정구 · 순서배열 카드 · 접속사 채찍 · 어휘 결정체

## 한국사

왕조의 검 · 연표 두루마리 · 문화재 방패 · 사료 분석서 · 조선 붓검 · 삼국의 창 · 근현대 권총 · 역사 기록석 · 유물 수정구 · 개혁의 도끼

## 통합사회

사회계약 검 · 경제 계산기 · 윤리 천칭 · 지리 나침반 · 정치 토론서 · 법률 사슬 · 문화 분석기 · 시장 그래프 활 · 인구통계 수정구 · 세계지도 망토

## 통합과학

원소 주기검 · 역학 추진기 · 생명 반응포 · 전자기 코어 · 화학 결합검 · 세포 증폭기 · 지질 해머 · 천체 망원창 · 유전 마도서 · 실험 플라스크

## 보조 아이템

- 집중 노트 → EXP 획득량 증가
- 암기 카드 → 오답 패널티 감소
- 에너지 드링크 → 제한 시간 보너스
- 계산기 조각 → 수학 관련 보너스

---

# 🎒 인벤토리 & 핫바

인벤토리 데이터:

- Item ID
- Count
- Rarity
- Upgrade

핫바:

```text
[1] [2] [3] [4] [5]
```

---

# 🧠 스킬

## 국어

속독 · 핵심문장 추출 · 문맥 추론 · 함정 선지 간파 · 시어 해석 · 고전어 해독 · 논리 연결 · 문단 압축 · 주제 관통 · 오답 제거

## 수학

암산 가속 · 공식 전개 · 그래프 분석 · 킬러 패턴 감지 · 계산 폭주 · 실수 보정 · 조건 정리 · 경우의 수 확장 · 함수 추적 · 시간 압축 풀이

## 영어

직독직해 · 문장 재배열 · 빈칸 예측 · 단어 연상 · 구문 분해 · 문맥 연결 · 듣기 집중 · 함정 보기 제거 · 속해석 · 지문 압축

## 한국사

연표 암기 · 시대 구분 · 사료 해석 · 사건 연결 · 왕 업적 분석 · 흐름 파악 · 근현대 압축 · 문화 구별 · 연상 암기 · 시간 역행 추적

## 통합사회

자료 해석 · 그래프 분석 · 사회 흐름 감지 · 경제 추론 · 법률 적용 · 윤리 판단 · 지도 판독 · 함정 통계 제거 · 사례 분석 · 개념 연결

## 통합과학

실험 분석 · 공식 적용 · 물리 계산 · 화학 반응 예측 · 생명 추론 · 그래프 판독 · 변수 통제 · 데이터 해석 · 개념 융합 · 현상 시뮬레이션

---

# 📊 속성 & 조합

6개 학습 영역을 게임의 핵심 속성으로 취급한다.

각 속성은 전용 아이템, 스킬, 효과, 스테이지, 시각적 정체성을 가진다.

총 **36개 조합 슬롯**을 설계한다.

예시:

- 국어 + 국어 → 언어폭주
- 국어 + 수학 → 음운 인수분해
- 국어 + 영어 → 문맥 번역
- 국어 + 과학 → 과학 독해
- 수학 + 수학 → 초월 계산
- 수학 + 영어 → 직독 미적분
- 수학 + 과학 → 벡터 역학
- 영어 + 영어 → 네이티브 영역
- 한국사 + 수학 → 역사 좌표화
- 통합사회 + 수학 → 확률 경제학
- 통합사회 + 과학 → 데이터 생태론
- 통합과학 + 통합과학 → 궁극 이론

---

# 🎲 로그라이크

플레이마다 일부 요소가 달라진다.

```text
Stage
 ↓
Combat / Question / Item / Event
 ↓
Choice
 ↓
Next Area
```

문제와 아이템 선택이 다음 루트에 영향을 줄 수 있도록 설계한다.

---

# ⏱️ 시간 시스템

일부 스테이지와 문제에는 제한 시간이 존재한다.

- 제한 시간 내 정답 → 보너스
- 오답 → 패널티
- 지나치게 늦은 풀이 → 패널티 가능

시간 압박이 학습 자체를 방해하지 않도록 밸런스를 조정한다.

---

# 💀 GAME OVER

조건:

- 플레이어 HP 0
- 특정 실패 조건 충족

```text
GAME OVER
 ↓
Result
 ↓
EXP 기록
 ↓
Learning Record
 ↓
Retry
```

게임 오버가 발생해도 학습 기록 전체를 삭제하지 않는다.

---

# 📈 학습 분석

기록 데이터:

- 총 문제 수
- 정답률
- 오답 수
- 평균 풀이 시간
- 과목별 정답률
- 단원별 정답률
- EXP
- 레벨
- 아이템 사용 기록
- 스킬 사용 기록

향후:

```text
오답 데이터
 ↓
약점 분석
 ↓
취약 단원 판별
 ↓
관련 문제 우선 출제
```

---

# 🖥️ UI / UX

## HUD

- LV
- EXP Bar
- Game World
- Player / Enemy
- HP
- Hotbar

## Question UI

- 문제 본문
- 5개 선택지
- 제출 버튼
- 해설 / 결과

UI는 별도의 학습 앱이 아니라 **게임 세계에 통합된 형태**를 지향한다.

---

# 🎨 아트 디렉션

**2D Pixel Art × Education × RPG × SF**

- 국어 → 문자 / 고전 / 언어
- 수학 → 기계 / 기하 / 계산
- 영어 → 데이터 / 정보
- 한국사 → 기록 / 유물
- 통합사회 → 지도 / 분석
- 통합과학 → 실험 / SF

---

# 🏗️ Unity 아키텍처

```text
GameManager
├─ PlayerManager
├─ QuestionManager
├─ EXPManager
├─ LevelManager
├─ ItemManager
├─ SkillManager
├─ InventoryManager
├─ BattleManager
├─ StageManager
├─ SaveManager
└─ UIManager
```

책임 분리:

- GameManager → 전체 게임 흐름
- PlayerManager → 플레이어 상태
- QuestionManager → 문제 선택 및 진행
- BattleManager → 전투 계산
- EXPManager → EXP 처리
- LevelManager → 레벨 및 성장
- ItemManager → 아이템 데이터 및 효과
- InventoryManager → 보유 아이템
- SkillManager → 스킬 및 쿨다운
- StageManager → 스테이지 진행
- SaveManager → 저장 및 불러오기
- UIManager → 화면 표시

---

# 🗂️ 프로젝트 구조

```text
Assets/
├─ Scenes/
├─ Scripts/
│  ├─ Player/
│  ├─ Enemy/
│  ├─ Combat/
│  ├─ Questions/
│  ├─ Items/
│  ├─ Skills/
│  ├─ Inventory/
│  ├─ UI/
│  ├─ Managers/
│  └─ Save/
├─ Data/
├─ ScriptableObjects/
├─ Prefabs/
├─ Art/
├─ Audio/
└─ Tilemaps/
```

---

# 🎬 Scene 구조

```text
Title
CharacterSelect
StageSelect
Stage01
Stage02
Stage03
Battle
Result
```

Scene 전환은 `SceneManager`를 중심으로 관리한다.

---

# 🧍 Player

기본 구성:

- Transform
- Rigidbody2D
- Collider2D
- SpriteRenderer
- Animator
- PlayerController

기능:

- 좌우 이동
- 점프
- 애니메이션
- 충돌 처리
- HP
- 공격
- 아이템 사용

---

# ⚙️ Unity 2D 핵심 기술

## Physics 2D

Rigidbody2D · Collider2D · Trigger · Collision · Raycast · Layer · LayerMask · Physics Material 2D · velocity / linearVelocity · Gravity

## Map

```text
Grid
├─ Ground Tilemap
├─ Wall Tilemap
├─ Decoration Tilemap
└─ Collision Tilemap
```

## Camera

Orthographic Camera · Player Follow · Stage Bounds

## Animation

```text
Idle → Run → Jump → Fall
```

전투:

```text
Idle → Attack → Hit → Idle
```

---

# 🖱️ Unity UI

- Canvas
- RectTransform
- TextMeshPro
- Button
- Slider
- Image
- Anchor
- Canvas Scaler
- EventSystem
- Input System
- Input Action

---

# 💾 Save System

게임 오브젝트 자체가 아니라 **데이터만 저장**한다.

```text
SaveData
├─ Level
├─ EXP
├─ Coins
├─ CurrentStage
├─ Inventory
├─ Skills
└─ LearningRecord
```

저장:

```text
Game State
 ↓
SaveData
 ↓
Serialization
 ↓
File
```

---

# 📦 ScriptableObject

아이템, 문제, 스킬, 스테이지 등의 편집 가능한 데이터를 코드와 분리하기 위해 사용한다.

```csharp
[CreateAssetMenu]
public class ItemData : ScriptableObject
{
    public string id;
    public string itemName;
    public string subject;
    public string rarity;
    public string description;
}
```

데이터 추가를 위해 C# 게임 로직을 계속 수정하지 않는 구조를 지향한다.

---

# 🧠 State Machine / FSM

적 AI:

```text
Idle → Chase → Attack → Hit → Dead
```

게임 상태:

```text
Title → Stage → Question → Result
```

---

# 🐞 Debugging

```text
Error
 ↓
Console
 ↓
첫 번째 Error 확인
 ↓
Source Code
 ↓
변수 값 확인
 ↓
Reference 상태 확인
 ↓
Inspector 확인
 ↓
수정
 ↓
재실행
```

특히 `NullReferenceException`은 참조가 제대로 연결되어 있는지 우선 확인한다.

> 여러 오류가 발생해도 먼저 **첫 번째/root error**를 해결한다.

---

# 🚀 Optimization

```text
기능 완성
 ↓
Playtest
 ↓
Profiler
 ↓
병목 확인
 ↓
필요한 부분만 최적화
```

확인 대상:

- FPS
- GC
- Allocation
- Draw Calls
- Overdraw
- Batching

반복적으로 생성·삭제되는 오브젝트에는 Object Pooling을 고려한다.

---

# 🛠️ 개발 단계

## Phase 0 — Planning

전체 시스템 설계 · 데이터 구조 설계 · MVP 범위 확정

## Phase 1 — Scratch Prototype

```text
Start → Subject → Question → Answer → EXP → Level → Result
```

## Phase 2 — Python System Verification

문제 데이터 · 정답 확인 · EXP · Level · Score · Penalty · Game Over · Result · Save · Learning Record

## Phase 3 — C# / Unity Learning

### C#

변수 · 자료형 · 연산자 · 조건문 · 반복문 · 메서드 · 클래스 / 객체 · 접근 제한자 · 배열 · List · Dictionary · Enum · Interface · Property · Exception

### Unity

MonoBehaviour · GameObject · Component · Transform · Lifecycle · Input · Physics · UI · Scene · Prefab · Coroutine

## Phase 4 — Unity Basics

Unity 프로젝트 → Player → 이동 → 점프 → Camera → Tilemap → Collider → Animation

## Phase 5 — Core System

Question Object → Question UI → Answer → EXP → Level → Game Over → Result

## Phase 6 — Battle

```text
Enemy → AI → Attack → Question → Answer → Damage → HP → Death
```

## Phase 7 — Item / Inventory

```text
ItemData → Acquire → Inventory → Hotbar → Use → Effect
```

## Phase 8 — Save

```text
State → SaveData → Serialization → File
```

## Phase 9 — Stage

Stage progression · Stage data · Stage transitions

## Phase 10 — Roguelike

Randomized routes · Events · Choices · Rewards

## Phase 11 — Attribute / Combination

6 attributes · 36 combination slots

## Phase 12 — Electives

선택 과목 확장 · 콘텐츠 확장

---

# 🧱 실제 구현 순서

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

# 🎯 MVP

## 포함

- 시작 화면
- 과목 선택
- 문제 출력
- 5지선다
- 정답 판정
- EXP
- Level
- Score
- Game Over
- Result
- 간단한 스테이지

## 제외

- 대규모 스토리
- 모든 선택 과목
- 대규모 아이템 시스템
- 36개 조합 전체 구현
- 복잡한 AI
- 온라인 기능

### 성공 기준

> **문제를 풀면 경험치를 얻고 레벨업한다.**

---

# 📋 개발 체크리스트

## C#

- [ ] HP / Score 변수
- [ ] Game Over 조건
- [ ] 반복문
- [ ] Method
- [ ] Parameter / Return
- [ ] Class
- [ ] List / Dictionary
- [ ] Enum

## Unity

- [ ] GameObject / Component 관계
- [ ] GetComponent
- [ ] Rigidbody2D
- [ ] Collider2D
- [ ] Player Movement
- [ ] Jump
- [ ] Prefab
- [ ] Instantiate
- [ ] Scene

## 2D

- [ ] Camera Follow
- [ ] Tilemap
- [ ] Animator
- [ ] Idle / Run / Jump
- [ ] HP UI
- [ ] EXP UI

## Game Systems

- [ ] Question System
- [ ] Answer System
- [ ] EXP
- [ ] Level
- [ ] Damage
- [ ] Enemy Death
- [ ] Item
- [ ] Inventory
- [ ] Skill Cooldown

## Advanced

- [ ] ScriptableObject
- [ ] FSM
- [ ] SaveData
- [ ] Save / Load
- [ ] Console Debugging
- [ ] NullReference 해결
- [ ] Profiler
- [ ] Object Pooling 판단
- [ ] Class 책임 분리

---

# 🔗 전체 데이터 흐름

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
 ├─ Correct → EXP
 └─ Wrong → Penalty
 ↓
PlayerData
 ↓
LevelManager
 ↓
Item / Skill / Stage
 ↓
SaveManager
 ↓
SaveData
```

---

# 🏛️ 최종 아키텍처

```text
SOLO SAT
│
├─ GameManager
│  ├─ PlayerManager
│  ├─ QuestionManager
│  └─ StageManager
│
├─ PlayerData
├─ QuestionData
├─ StageData
│
├─ BattleManager
├─ ItemManager
├─ SkillManager
├─ InventoryManager
├─ Ability System
└─ SaveManager
   └─ SaveData
```

---

# 📦 Data-Driven Design

다음 콘텐츠를 데이터와 코드로 분리한다.

- Questions
- Items
- Skills
- Enemies
- Stages
- Rewards

새 콘텐츠 추가 시 기존 C# 게임 로직을 수정하기보다 데이터 에셋을 추가하는 방향으로 설계한다.

---

# 📐 개발 전략

1. **작동하는가?**
2. **재미있는가?**
3. **확장 가능한가?**
4. **최적화가 필요한가?**

> **기능 완성 → 플레이 테스트 → 구조 개선 → 필요한 부분만 최적화**

---

# 🔮 장기 확장

- 약점 분석
- 적응형 난이도
- 문제 추천
- 통계 시스템
- Codex
- Achievement
- Boss
- Story
- 과목별 세계
- 선택 과목 세계
- 장비 강화
- Skill Tree
- Roguelike Event

핵심 게임 루프를 먼저 완성한 뒤 확장한다.

---

# 🆚 프로젝트 차별점

일반적인 학습 앱:

```text
문제 → 정답 → 점수
```

SOLO SAT:

```text
문제
 ↓
정답
 ↓
전투 결과
 ↓
EXP
 ↓
Level
 ↓
Item
 ↓
Skill
 ↓
Attribute
 ↓
Combination
 ↓
Stage
 ↓
더 어려운 문제
 ↓
다시 학습
```

학습 결과가 게임의 진행을 직접 결정한다.

---

# 🧭 최종 시스템 구조

```text
SOLO SAT
 ↓
STAGE
 ↓
GAMEPLAY
 ↓
Combat / Question / Event
 ↓
Problem Solving
 ↓
Correct / Incorrect
 ↓
EXP / Penalty
 ↓
PLAYER DATA
 ↓
LEVEL / ITEM / SKILL
 ↓
ATTRIBUTE
 ↓
COMBINATION
 ↓
NEXT STAGE
 ↓
REPEAT
```

---

# 🗺️ 최종 로드맵

```text
Planning
 ↓
Scratch
 ↓
Python
 ↓
C# Basics
 ↓
Unity Basics
 ↓
Player
 ↓
Map / Camera
 ↓
Question System
 ↓
EXP / Level
 ↓
Battle
 ↓
Item
 ↓
Inventory
 ↓
Skill
 ↓
Save
 ↓
Stage
 ↓
Animation / Sound
 ↓
Roguelike
 ↓
Attribute
 ↓
Combination
 ↓
Analytics
 ↓
Optimization
 ↓
Release
```

---

# 🏁 최종 선언

SOLO SAT은 단순한 **「수능 문제를 넣은 RPG」**가 아니다.

> **공부 자체를 게임 플레이로 만든다.**

```text
공부
 ↓
문제
 ↓
정답
 ↓
EXP
 ↓
성장
 ↓
아이템 / 스킬
 ↓
전투
 ↓
스테이지
 ↓
더 어려운 문제
 ↓
다시 공부
```

최종적으로 **교육과정 → 문제 데이터 → 문제 풀이 → RPG 성장 → 전투 → 아이템 → 스킬 → 속성 → 조합 → 로그라이크 → 학습 분석**을 하나의 데이터 흐름으로 연결하는 것을 목표로 한다.

---

# 📌 Project Status

**FINAL MASTER PLAN**

- [x] 프로젝트 콘셉트 확정
- [x] 초기 6개 영역 확정
- [x] 초기 문제 120문제 구조 확정
- [x] 핵심 게임 루프 설계
- [x] Unity / C# 개발 방향 확정
- [x] 데이터 중심 아키텍처 설계
- [x] MVP 범위 정의
- [ ] Scratch Prototype
- [ ] Python System Verification
- [ ] C# / Unity Core Implementation
- [ ] MVP
- [ ] Battle System
- [ ] Item / Skill System
- [ ] Save System
- [ ] Roguelike System
- [ ] Attribute / Combination
- [ ] Learning Analytics
- [ ] Release

---

## 🎮 SOLO SAT

### 나 혼자만 1등급

**문제를 풀수록 강해지는 수능 RPG.**

_VIAUS Project_

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