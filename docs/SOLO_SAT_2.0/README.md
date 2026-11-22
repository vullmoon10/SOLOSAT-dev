# SOLO SAT

Pygame으로 만든 수학 학습·전투 게임입니다. 네트워크나 서버 없이 한 컴퓨터에서 실행하며, 초등학교 후반부터 중학교 1학년 수준의 수학 문제를 플레이 중 생성합니다.

## 실행

Python 3.10 이상과 `pygame-ce`가 필요합니다. `pygame-ce`는 코드에서 기존 `pygame` 모듈 이름으로 가져오므로 게임 코드는 그대로 사용할 수 있습니다.

```bash
python -m pip install -r requirements.txt
python main.py
```

- `python -m pip install -r requirements.txt`: 현재 Python 환경에 프로젝트 의존성을 설치합니다. 주요 게임 라이브러리는 `pygame-ce`입니다.
- `python main.py`: 프로그램 진입점인 `main.py`를 실행해 Pygame 초기화와 메인 메뉴 표시를 시작합니다.
- Windows에서는 `SOLO_SAT_SETUP.bat`을 실행해도 됩니다.

## 플레이

- 새 게임에서 닉네임과 월드 시드를 입력합니다. 닉네임을 비우면 자동으로 지정되고, 시드를 비우면 무작위 월드가 생성됩니다. 같은 숫자 시드를 입력하면 같은 월드가 생성됩니다.
- 이동 속도·중력·점프력은 월드 시드와 별도로 새 게임마다 무작위로 정해집니다. 시작 카운트다운에서 이번 판의 값을 확인할 수 있으며, 이어 하기에서도 그대로 유지됩니다.
- 게임 진행은 `runtime/local/save.json`에 자동 저장되며, 메뉴에서 이어 할 수 있습니다.
- 게임 기록과 랭킹은 `runtime/local/`에 보관됩니다.
- 도전과제는 코인·아이템 수집, 몬스터 처치, 점수, 이동 거리, 코스 완주로 달성하며 진행도와 해금 상태는 로컬 프로필에 저장됩니다. 메인 메뉴의 `도전과제`에서 확인할 수 있습니다.
- 월드는 구간별로 다양한 지형을 생성합니다. 문제 몹은 문제 하나를 내며, 정답을 맞히면 처치됩니다. 구멍에 빠지면 시작 지점으로 돌아옵니다.
- 코스에서 아이템을 자동 획득합니다. 코인은 점수 +50, 하트는 체력 +20, 파란 S는 8초 속도 강화, 보라 J는 8초 점프 강화입니다.
- 게임 화면 오른쪽 아래 슬라이더를 드래그해 잡몹 생성 밀도를 조절합니다. 설정은 저장·불러오기에 유지됩니다.
- 일부 발판은 좌우로 움직입니다. 잡몹은 투사체를 쏘며, 막대기 공격으로 처치할 수 있습니다. 수학 문제를 내는 몹은 막대기에 피해를 받지 않습니다.
- 문제 몹은 각자 문제 하나를 내며, 정답을 맞히면 처치됩니다. 오답이면 같은 문제에 다시 도전할 수 있습니다.
- 플레이어의 Ek가 100 이상일 때 문제 몹과 부딪히면 문제 화면을 건너뛰고, Ek에 비례한 충돌 피해를 줍니다.
- 몹은 난이도와 문제 영역에 따라 외형·이름·보상·체력이 달라집니다. 산술·분수·측정/도형 몹은 쉬움, 수와 연산·문자와 식·좌표 몹은 보통과 도전 난이도로 출현합니다. `mob.jpg`를 2×2로 나눈 `mob_1.png`~`mob_4.png`를 몹 스프라이트로 사용합니다.
- 문항은 쉬움·보통·도전·최상 4단계입니다. 쉬움은 초등 연산·분수·측정, 보통은 중1 정수·유리수·문자식·좌표, 도전은 같은 범위의 괄호와 계산 순서, 최상은 중1 1학기 범위 안에서 여러 계산 단계를 결합합니다. 진행 거리에 따라 몹 난이도도 네 단계로 상승합니다.

## 조작

- A/D 또는 ←/→: 이동. 길게 누르면 가속하고 놓으면 감속
- Space: 점프
- W/S 또는 ↑/↓: 사다리 오르내리기
- E: 근처 몬스터와 상호작용
- 마우스 왼쪽 클릭: 바라보는 방향으로 막대기 휘두르기
- K 길게 누르기: 현재 이동 속도에 비례하는 막대기 공격. 누르는 동안 쿨다운 없이 적용
- P 길게 누르기: 지면에서 높이(위치 에너지)에 비례하는 범위 공격. 누르는 동안 쿨다운 없이 적용
- 문제 창: ↑/↓ 선택, Enter 제출, 1~4 즉시 선택, 마우스 클릭
- F9: 치트 선택 메뉴 열기. 메뉴에서 1~5로 치트 적용, 0으로 치트 해제; F9 또는 ESC로 닫기
- F11: 메뉴, 이름·시드 입력 화면, 게임에서 전체 화면 전환
- ESC: 게임 일시정지 또는 메뉴로 이동

새 게임을 선택하면 이름 입력 후 월드 시드 입력 화면이 나옵니다. 각 화면에서 Enter로 확정하고, 시드를 비우면 무작위 월드 시드를 사용합니다. ESC로 입력을 취소하고 메뉴로 돌아갑니다.

## 프로젝트 구조

- `main.py`: 게임 메뉴와 로컬 세션 실행
- `settings.py`: 화면 크기, 프레임 속도, 물리값, 색상 등 공통 설정
- `core/`: 게임 상태와 이벤트·디스플레이 처리
- `entities/`: 플레이어, 적, 잡몹, 투사체, 이동 발판
- `systems/`: 문항 생성, 퀴즈, 전투, 진행, 저장, 도전과제, 오디오
- `world/`: 지형 및 시드 기반 월드 생성
- `ui/`: 메뉴, 입력 화면, HUD, 렌더러

## 코드 선언 및 주요 구성 설명

이 절은 프로그램을 이해하는 데 중요한 모듈 최상위 설정값, 함수, 클래스 및 코드 블록의 역할을 설명합니다. 함수 내부의 임시 변수는 개별 목록 대신 해당 함수의 처리 목적에 포함해 설명합니다.

### 1. 주요 변수·상수 선언

| 파일 | 선언 | 설명 |
|---|---|---|
| `settings.py` | `WIDTH`, `HEIGHT`, `FPS` | 화면 크기와 목표 프레임 속도 |
| `settings.py` | `TITLE` | 게임 창 제목 |
| `settings.py` | `MOVE_SPEED`, `GRAVITY`, `JUMP_POWER` | 기본 이동·중력·점프 물리값 |
| `settings.py` | `PLAYER_WIDTH`, `PLAYER_HEIGHT` | 플레이어 기본 크기 |
| `settings.py` | `MAX_HP`, `CORRECT_SCORE`, `WRONG_DAMAGE`, `QUESTION_TIME` | 체력·점수·오답 피해·문제 제한 시간 |
| `settings.py` | 색상 상수 및 `GROUND_Y`, `SPAWN_SAFE_END` | 배경·지형 색상, 지면 높이, 시작 안전 구간 |
| `settings.py` | `FONT`, `SMALL`, `TITLE_FONT`, `BIG` | 공용 글꼴 객체 |
| `entities/enemies.py` | `ENEMY_TYPES`, `ENEMY_TYPES_BY_DIFFICULTY` | 몬스터 유형과 난이도별 출현 데이터 |
| `entities/enemies.py` | `DIFFICULTY_SPRITE_INDEX` | 난이도와 몬스터 스프라이트 대응 정보 |
| `systems/question_generator.py` | `QUESTION_KINDS` | 문항 생성 대상 영역 분류 |
| `systems/achievements.py` | `ACHIEVEMENTS` | 도전과제 이름·설명·달성 기준 |
| `systems/local_storage.py` | `DATA_DIR`, `DEFAULT_PROFILE` | 로컬 저장 위치와 기본 프로필 구조 |
| `systems/audio.py` | `SOUND_DIR`, `MUSIC_END_EVENT` | 사운드 경로와 음악 종료 이벤트 |

### 2. 주요 함수 선언

- `main.py`: `_new_session()`은 새 게임 세션을 구성하고, `_load_session()`은 저장 데이터를 이용해 이어 하기 세션을 구성하며, `main()`은 초기화·메뉴·게임 실행·종료를 연결합니다.
- `settings.py`: `random_physics()`는 새 게임에 적용할 물리값을 무작위로 선택하고, `choose_cheat()`는 치트 선택 입력을 내부 설정으로 변환합니다.
- `core/display.py`: `toggle_fullscreen()`은 전체 화면 상태를 전환합니다.
- `core/events.py`: `handle_quiz_event()`는 퀴즈 화면의 키보드·마우스 입력과 답안 제출 처리를 연결합니다.
- `systems/question_generator.py`: `_format()`은 수식 표시를 정리하고, `_multiple_choice()`는 정답·오답 선택지를 구성합니다. `_easy_question()`, `_medium_question()`, `_challenge_question()`, `_expert_question()`은 난이도별 문항을 생성하며, `generate_math_question()`은 난이도와 영역에 맞는 생성 함수를 선택합니다.
- `systems/quiz.py`: `get_random_question()`은 문항 생성기를 호출해 퀴즈에 사용할 문제를 가져옵니다.
- `systems/combat.py`: `apply_damage()`는 피해량과 무피해 조건을 반영해 체력을 계산합니다.
- `systems/progression.py`: `add_score()`는 획득 점수를 현재 점수에 반영합니다.
- `systems/local_storage.py`: 저장·읽기 함수들은 프로필, 자동 저장, 도전과제, 랭킹 데이터를 로컬 JSON 파일로 관리합니다.
- `ui/name_entry.py`, `ui/seed_entry.py`: 각각 닉네임과 월드 시드 입력 화면을 처리합니다.
- `ui/hud.py`: `draw_hud()`는 체력·점수·안내 메시지를 화면에 표시합니다.

### 3. 주요 클래스 선언

| 파일 | 클래스 | 역할 |
|---|---|---|
| `core/game.py` | `Game` | 게임 상태, 이벤트, 업데이트, 충돌, 저장 및 렌더링 흐름 통합 |
| `entities/player.py` | `Player` | 플레이어 위치·속도·점프·입력·물리 상태 관리 |
| `entities/enemies.py` | `Enemy` | 문제 몬스터의 상태와 처치 처리 |
| `entities/trash_mob.py` | `TrashMob` | 일반 잡몹의 이동·공격·피해 상태 |
| `entities/trash_mob.py` | `Projectile` | 잡몹 투사체의 위치와 이동 |
| `entities/moving_platform.py` | `MovingPlatform` | 좌우 이동 발판 |
| `world/terrain.py` | `Terrain` | 월드 지형 요소와 기반 데이터 |
| `world/generator.py` | `World` | 시드 기반 구간·지형·적·아이템 생성 |
| `systems/quiz.py` | `Quiz` | 문항·선택·제출·제한 시간·정답 결과 관리 |
| `systems/achievements.py` | `AchievementTracker` | 통계 갱신과 도전과제 달성 판정 |
| `systems/local_storage.py` | `LocalStorage` | 프로필·자동 저장·도전과제·랭킹 JSON 입출력 |
| `systems/save_manager.py` | `SaveManager` | 진행 데이터 JSON 저장 및 불러오기 |
| `systems/audio.py` | `AudioManager` | 효과음과 배경 음악 재생·전환 |
| `ui/menu.py` | `Menu` | 메인 메뉴와 메뉴 선택 흐름 |
| `ui/renderer.py` | `Renderer` | 배경·월드·플레이어·HUD·문제 화면 렌더링 |

### 4. 핵심 메서드와 코드 블록 흐름

- `Game`: `__init__()`에서 게임 구성 요소를 초기화합니다. `handle_event()`는 입력, `update()`는 게임 상태 갱신, `draw()`는 화면 출력을 담당합니다. `run()`은 이 과정을 반복하는 플레이 루프이며, `save_state()`는 진행 상태를 저장합니다.
- `Player`: `update()`에서 입력과 월드 충돌을 반영하고, `jump()`에서 점프를 시작하며, `reset_position()`에서 위치를 초기화합니다.
- `World`: `generate_chunk()` 계열 메서드가 구간을 만들고, `update_generation()`이 플레이어 위치에 따라 필요한 구간을 추가합니다.
- `Quiz`: `open()`은 문제를 열고, `submit()`은 선택한 답을 판정하며, 제한 시간 관련 메서드는 남은 시간과 시간 초과 여부를 관리합니다.
- `LocalStorage`: 읽기·쓰기 메서드는 JSON 파일을 처리하고, 초기화·정리 메서드는 데이터 구조와 랭킹을 검증·정리합니다.
- 설치 코드 블록은 의존성을 준비하는 단계, 실행 코드 블록은 프로그램 진입점을 호출하는 단계입니다. 이 순서로 실행해야 합니다.

### 5. 프로그램 데이터 흐름

1. `main.py`가 Pygame, 로컬 저장소, 오디오 관리자와 메뉴를 초기화합니다.
2. 새 게임을 선택하면 닉네임과 시드 입력을 거쳐 세션 정보를 구성합니다.
3. `Game`이 `Player`, `World`, `Quiz`, `Renderer` 및 진행 시스템을 연결합니다.
4. 게임 루프에서 입력 처리 → 상태 갱신 → 화면 출력을 반복합니다.
5. 문항 생성기가 난이도·영역에 맞는 문제를 만들고, `Quiz`가 답안을 판정해 게임 상태에 반영합니다.
6. 진행 상태·프로필·도전과제·랭킹은 로컬 JSON 파일에 기록됩니다.

> 참고: 선언 목록은 핵심 구조를 이해하기 위한 안내입니다. 모든 지역 변수와 모든 보조 함수의 세부 구현을 빠짐없이 열거한 API 명세서는 아닙니다.

## 범위 및 주의사항

게임은 프로토타입이며, 실제 공개 서비스 수준의 보안이나 접근성 검증을 제공하지 않습니다.


---

## 전체 코드 정적 분석

프로젝트의 전체 Python 소스 파일을 대상으로 생성한 정적 분석 명세서를 별도로 관리한다.

분석 범위:
- 모듈 수준 변수 및 상수, 함수 내부의 지역·대입 변수
- 함수와 메서드 선언 및 매개변수
- 클래스, 상속 관계, 메서드
- 조건 분기(`if / elif / else`, `match / case`)
- 반복문(`for / while`)
- 예외 처리(`try / except / finally`)
- 각 선언 및 제어 구조의 소스 파일 경로와 줄 번호

분석 문서는 소스 코드의 AST(추상 구문 트리)를 기준으로 추출한 정적 명세다. 실행 시점에 동적으로 생성되는 속성, 런타임 값, 실제 게임 동작은 정적 추출만으로 확정할 수 없으므로 별도 실행 검증이 필요하다.

현재 분석 기준은 `SOLO_SAT_FINAL_PLZ_2.0`의 Python 소스 29개 파일이다. 원본 게임 코드는 이 문서화 작업에서 변경하지 않았다.


### 전체 코드 정적 분석 명세서

전체 Python 소스의 파일별 변수·함수·클래스·조건 분기·반복문·예외 처리와 코드 위치를 정리한 상세 문서:

- [SOLO SAT 2.0 전체 코드 정적 분석 명세서](./전체_코드_정적_분석.md)
