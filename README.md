# 🚀 Antigravity 기반 Obsidian 관리 스킬 (MD변환/분류/태깅)
> **Version 1.3 업데이트 릴리즈 노트**: 
> 1. **다차원 태그 택소노미(Tag Taxonomy) 전면 도입**: 단순 키워드(Vocabulary) 방식을 폐기하고 15개 중첩 네임스페이스(`type`, `market`, `product`, `topic` 등) 기반의 다차원 태그 택소노미(`04_Tag_Taxonomy_Rule.md`)를 구축하여 옵시디언 검색 해상도를 극대화했습니다.
> 2. **트라이앵글 태그 시스템 상호 동기화(Sync Hook)**: 메타데이터 스킬(`02`), 태그 생성 룰(`03`), 택소노미 사전(`04`) 세 문서 간의 강제 동기화 훅(`05_Tag_Sync_Hook`)을 신설하여, 에이전트가 문서를 읽고 ➡ 사전을 뒤지고 ➡ 없으면 만들어서 ➡ 사전에 영구 등재하는 완벽한 자율형 워크플로우를 완성했습니다.
> 3. **MOC 동적 재배치 자율/수동 스킬 추가**: 사용자의 기존 조니데시멀 트리를 분석 및 재배치하는 수동 결합 룰(`/moc-set-user`)과, AI 기반 Vault 전수 스캔으로 사용자 업무 성향에 맞춰 MOC 1-Depth를 자체 재설계하는 자율 제안 룰(`/moc-set-ai`)을 신설했습니다.
> 4. **PPT 정밀 파싱 한계 돌파 (Invisible Grid & Floating Annotations)**: 선이 보이지 않는 바둑판식 레이아웃 표(Invisible Grid Table) 인식 룰과, 표 밖으로 밀려난 말풍선/주석(Floating Annotations)을 표 내부에 강제 귀속시키는 룰을 장착해 표 파싱의 유실률을 0%에 가깝게 방어했습니다.
> 5. **Local Dependency 제거 (Workspace Agnostic)**: `robocopy` 및 Python 실행 환경에 하드코딩 되어있던 로컬 디렉토리 의존성(c:/Users/...)을 완벽히 제거하여 공유 배포의 유연성을 확보했습니다.

> **Version 1.2 업데이트 릴리즈 노트**: 
> 1. **하네스(Harness) 무결성 확보**: Master Hub(`Antigravity_Agent.md`) 동기화 오류 전면 교정 (누락된 `/hotkey` 스킬 및 쟈니 데시멀 룰 복구, 파일명 매핑 오류 100% 수정).
> 2. **점진적 학습(Incremental Learning) 고도화**: 신규 태그 생성 시 에이전트가 단어장(`04_Tag_Vocabulary_Rule.md`)을 단순 조회하는 것을 넘어, 스스로 신규 단어를 사전에 영구 등록(업데이트)하도록 태그 생성 룰 보완.
> 3. **PPT 파싱 예외 처리 (UTF-8 Stream Error 대응)**: 복잡한 특수 기호/이모지로 인한 대규모 마크다운 치환 튕김 현상을 원천 차단하기 위해, 파이썬 기반 정밀 문자열 치환(Python Injection)을 통해 병목을 자율 우회하는 지침 하네스 신규 추가.
> 4. **슬라이드 정밀 렌더링 규정 고도화**: 서식 유실을 대비해 거버넌스 문장의 '위치(제목 직하단)' 기반 판별 기준 추가 및 `# [번호] Page - [제목]` 형태의 슬라이드 타이틀 구조 의무화.

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
