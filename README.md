# 🚀 Antigravity 기반 Obsidian 관리 스킬 (MD변환/분류/태깅)
> **사용 팁**: 이 스킬 묶음은 Antigravity와 Codex를 함께 쓰는 통합 버전입니다. VS Code에서 열어 쓰면 더 편하게 다룰 수 있습니다.

## Version 1.3 Release Notes
- `AGENTS.md`의 공식 명령어 목록을 정리하고 `/skill-list`를 표준 진입점으로 맞췄습니다.
- `/md`를 디스패처로 재설계해 파일 형식에 따라 `/md-html` 또는 `/md-ppt`를 자동 호출하도록 바꿨습니다.
- HTML 변환 스킬은 `/md-html`로, PPT 변환 스킬은 `/md-ppt`로 명령어를 분리했습니다.
- `02_Metadata_Tagging_Skill.md`의 명령 표기를 `/taggging`으로 통일했습니다.
- README, AGENTS, 훅, 스킬 문서 전반의 슬래시 명령어 표기를 새 체계에 맞게 동기화했습니다.
- 새 스킬 `12_MD_Dispatch_Skill.md`를 추가해 `/md`의 분기 규칙과 호출 흐름을 정의했습니다.
- 옴니 에이전트(Omni-Agent) 아키텍처로 전환해 파싱 및 작업 처리 안정성을 강화했습니다.
- Mermaid 차트 렌더링 오류 방어 룰과 훅을 추가해 특수문자 기반 렌더링 깨짐을 줄였습니다.
- `/hotkey`와 태그 마이그레이션 흐름을 정리해 태그 및 핫키 스킬을 안정화했습니다.
- `/moc-set-user`, `/moc-set-ai` 로직을 보완해 MOC 스킬을 안정화했습니다.
- PPT 파싱 예외 룰과 레이아웃 복원 규칙을 강화해 복합 슬라이드 구조 인식을 개선했습니다.

## 1. 폴더 구조
📦내_옵시디언_폴더(Vault)
 ┣ 📜AGENTS.md (마스터 허브)
 ┣ 📜README.md (본 문서)
 ┣ 📂.agent
 ┃ ┣ 📂skill/
 ┃ ┣ 📂rule/
 ┃ ┗ 📂hook/
 ┣ 📂00. Inbox (수집함)
 ┣ 📂10. 프로젝트 (Projects)
 ┣ 📂20. 산출물 (Outputs)
 ┗ 📂30. 참고자료 (References)


## 2. 설치순서
1. 회사 시스템을 통해 배포된 `agent-d2c.zip` 파일을 다운로드하고 압축을 풉니다.
2. 압축을 푼 폴더의 이름을 `.agent`로 변경합니다.
3. 이름을 변경한 `.agent` 폴더를 본인의 옵시디언 볼트(Vault) 최상위(Root) 경로에 복사하여 넣습니다.
4. Antigravity 에이전트에서 'Open Folder'를 통해 방금 적용한 옵시디언 볼트를 작업 공간으로 엽니다.
5. 아래 텍스트를 복사해서 Antigravity 대화창에 전송하세요.
  "내 옵시디언 최상위 폴더에 있는 마스터 허브 문서 `AGENTS.md`를 열고, 이 문서 안에 포함(@include)된 모든 skill, rule, hook 폴더의 하위 문서들까지 전부 스캔하고 향후 작업 시 KI에 숙지해 줘. `.agent/` 폴더 하위의 MD파일은 코어 시스템인 'Knowledge Item(KI)'에 영구적으로 등록해"


## 3. 공식 슬래시 명령어 (Slash Commands)
에이전트 연동이 완료되면, 채팅창에 아래 명령어를 입력해 빠르고 정확하게 자동화 스킬을 발동할 수 있습니다.
- `/skill-list` : 현재 에이전트가 사용할 수 있는 모든 스킬 명령어와 간단한 설명을 출력
- `/route` : 문서들을 알맞은 폴더로 자동 라우팅
- `/taggging` : 문서의 메타데이터 빈칸 채우기 및 15개 택소노미 기반 다차원 태그 할당
- `/md` : 선택된 파일 형식에 따라 `/md-html` 또는 `/md-ppt`를 자동 호출하는 변환 디스패처
- `/md-html` : 이메일/웹 클리핑 등 HTML 원시 파일 마크다운 정제 및 자동 태깅
- `/md-ppt` : PPT 문서의 핵심 파싱, 보이지 않는 그리드(Invisible Grid) 표 병합, 부유 주석 귀속 및 복원
- `/title` : 본문 내용(description) 기반으로 알맞은 타이틀 및 파일명 자동 변경
- `/link` : 볼트 내 고아 문서를 찾아 기존 문서들과 문맥 연결 (위키링크)
- `/rollup` : 오늘 생성된 문서와 진행 중인 태스크를 모아 데일리 리포트 작성
- `/hotkey` : 태깅, 제목 변경, 링크 연결, MOC 갱신을 한 번에 실행하는 올인원 스킬
- `/moc-set-user` : 사용자의 기존 폴더 트리를 분석해 조니 데시멀 하위 트리로 재분배
- `/moc-set-ai` : 볼트 전체 분석 후 사용자 최적화 1-Depth 조니 데시멀 MOC 구조 재설계 및 제안
- `/harness [내용]` : 에이전트에게 새로운 룰/스킬/훅을 생성해서 영구 등록하라고 지시

## 4. Git Repo
- https://github.com/mts8787-droid/Workplace-Obsidian

Antigravity, Obsidian, MarkdownConverter
