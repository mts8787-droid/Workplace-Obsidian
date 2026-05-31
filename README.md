# 🚀 Antigravity 기반 Obsidian 관리 스킬 (MD변환/분류/태깅)
> **Version 1.2 업데이트 릴리즈 노트 (스킬 고도화 중심)**: 
> 
> **1. 태깅 및 메타데이터 최적화 (`/tag`, `/hotkey`)**
> - **다차원 태그 택소노미 전면 도입**: 단순 키워드(Vocabulary) 방식을 폐기하고 15개 중첩 네임스페이스(`type`, `market`, `product` 등) 기반 체계를 구축해 옵시디언 검색 해상도 극대화.
> - **점진적 학습 및 동기화 훅(Sync Hook) 완성**: [문서 맥락 분석 ➡ 택소노미 탐색 ➡ 신규 태그 창조 ➡ 택소노미 영구 등재]로 이어지는 트라이앵글 자율형 워크플로우 달성.
> - **하네스 무결성 확보**: 누락되었던 `/hotkey` 스킬 및 쟈니 데시멀 룰을 복구하고 마스터 허브(`Antigravity_Agent.md`) 동기화 오류 전면 교정.
> 
> **2. 시각 매체 정밀 파싱 고도화 (`/MD-PPT`)**
> - **레이아웃 인식 한계 돌파 (Invisible Grid & Floating Annotations)**: 선이 보이지 않는 바둑판식 레이아웃 표 인식 및 표 밖으로 밀려난 말풍선/주석을 표 내부에 강제 귀속시켜 유실률 0% 달성.
> - **슬라이드 정밀 렌더링 규정 강화**: 거버넌스 문장의 위치(제목 직하단) 기반 판별 기준을 추가하고, `# [번호] Page - [제목]` 형태의 슬라이드 타이틀 구조를 의무화.
> - **UTF-8 Stream Error 원천 차단**: 특수 기호/이모지로 인한 대규모 마크다운 치환 튕김 현상을 파이썬 정밀 스크립트(Python Injection)로 우회하여 안전성 확보.
> 
> **3. MOC 및 폴더 트리 동적 관리 (`/moc-set-user`, `/moc-set-ai`)**
> - **조니 데시멀 재배치 스킬 신설**: 사용자의 기존 트리를 병합/재분배하는 수동 룰(`/moc-set-user`)과, AI 기반 전수 스캔으로 최적의 1-Depth 구조를 재설계하는 자율 제안 룰(`/moc-set-ai`) 장착.
> 
> **4. 배포 및 환경 제어 (System)**
> - **Local Dependency 완전 제거 (Workspace Agnostic)**: `robocopy` 및 Python 실행 환경에 하드코딩 되어있던 로컬 디렉토리 의존성(c:/Users/...)을 제거하여 공유 배포 유연성 확보.

## 1. 폴더 구조
📦내_옵시디언_폴더(Vault)
 ┣ 📂.agent
 ┃ ┣ 📜Antigravity_Agent.md (마스터 허브)
 ┃ ┣ 📜README.md (본 문서)
 ┃ ┣ 📂skill/
 ┃ ┣ 📂rule/
 ┃ ┗ 📂hook/
 ┣ 📂00. Inbox (수집함)
 ┣ 📂10. 프로젝트 (Projects)
 ┣ 📂20. 산출물 (Outputs)
 ┗ 📂30. 참고자료 (References)


## 2. 설치순서
1. 파일을 다운 받아 Obsidian vault에 압축 풀기
2. Antigravity 에서 Open Folder 에서 Onsidan Valut 열기
3. 아래 텍스트를 복사해서 Antigravity에게 전송하세요.
  " 내 옵시디언 최상위 폴더 하위의 `.agent` 폴더에 있는 마스터 허브 문서 `Antigravity_Agent.md`를 열고, 이 문서 안에 포함(@include)된 모든 skill, rule, hook 폴더의 하위 문서들까지 전부 스캔하고 향후 작업 시 KI에 숙지해 줘. `.agent/` 폴더 하위의 MD파일은 코어 시스템인 'Knowledge Item(KI)'에 영구적으로 등록해"


## 3. 공식 슬래시 명령어 (Slash Commands)
에이전트 연동이 완료되면, 채팅창에 아래 명령어를 입력해 빠르고 정확하게 자동화 스킬을 발동할 수 있습니다.
- `/route` : 문서들을 알맞은 폴더로 자동 라우팅
- `/tagging` : 문서의 메타데이터 빈칸 채우기 및 15개 택소노미 기반 다차원 태그 할당
- `/md` : 이메일/웹 클리핑 등 HTML 원시 파일 마크다운 정제 및 자동 태깅
- `/MD-PPT` : PPT 문서의 핵심 파싱, 보이지 않는 그리드(Invisible Grid) 표 병합, 부유 주석 귀속 및 복원
- `/title` : 본문 내용(description) 기반으로 알맞은 타이틀 및 파일명 자동 변경
- `/link` : 볼트 내 고아 문서를 찾아 기존 문서들과 문맥 연결 (위키링크)
- `/rollup` : 오늘 생성된 문서와 진행 중인 태스크를 모아 데일리 리포트 작성
- `/hotkey` : 태깅, 제목 변경, 링크 연결, MOC 갱신을 한 번에 실행하는 올인원 스킬
- `/moc-set-user` : 사용자의 기존 폴더 트리를 분석해 조니 데시멀 하위 트리로 재분배
- `/moc-set-ai` : 볼트 전체 분석 후 사용자 최적화 1-Depth 조니 데시멀 MOC 구조 재설계 및 제안
- `/harness [내용]` : 에이전트에게 새로운 룰/스킬/훅을 생성해서 영구 등록하라고 지시

Antigravity, Obsidian, MarkdownConverter
