# 🚀 Antigravity기반 Obsidian 관리 스킬 8종(MD변환/분류) 
> **Version 1.2 업데이트**: 
> 1. **하네스(Harness) 무결성 확보**: Master Hub(`Antigravity_Agent.md`) 동기화 오류 전면 교정 (누락된 `/hotkey` 스킬 및 쟈니 데시멀 룰 복구, 파일명 매핑 오류 100% 수정).
> 2. **점진적 학습(Incremental Learning) 고도화**: 신규 태그 생성 시 에이전트가 단어장(`04_Tag_Vocabulary_Rule.md`)을 단순 조회하는 것을 넘어, 스스로 신규 단어를 사전에 영구 등록(업데이트)하도록 태그 생성 룰 보완.
> 3. **PPT 파싱 예외 처리 (UTF-8 Stream Error 대응)**: 복잡한 특수 기호/이모지로 인한 대규모 마크다운 치환 튕김 현상을 원천 차단하기 위해, 파이썬 기반 정밀 문자열 치환(Python Injection)을 통해 병목을 자율 우회하는 지침 하네스 신규 추가.
> 4. **슬라이드 정밀 렌더링 규정 고도화**: 서식 유실을 대비해 거버넌스 문장의 '위치(제목 직하단)' 기반 판별 기준 추가 및 `# [번호] Page - [제목]` 형태의 슬라이드 타이틀 구조 의무화.

## 1. 폴더 구조
📦내_옵시디언_폴더(Vault)
 ┣ 📂.agent
 ┃ ┣ 📜Antigravity_Agent.md (마스터 허브)
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
 " 내 옵시디언 최상위 폴더 하위의 `.agent` 폴더에 있는 마스터 허브 문서 `Antigravity_Agent.md`를 열고,  이 문서 안에 포함(@include)된 모든 skill, rule, hook 폴더의 하위 문서들까지 전부 스캔하고 향후 작업 시 KI에로 숙지해 줘.  `.agent/ki/ MD파일은 코어 시스템인 'Knowledge Item(KI)'에 영구적으로 등록해"



## 3. 공식 슬래시 명령어 (Slash Commands)
에이전트 연동이 완료되면, 채팅창에 아래 명령어를 입력해 빠르고 정확하게 자동화 스킬을 발동할 수 있습니다.
- `/route` : 문서들을 알맞은 폴더로 자동 라우팅
- `/tagging` : 문서의 메타데이터 빈칸 채우기 및 태그 부착
- `/md` : 이메일/웹 클리핑 등 HTML 원시 파일 마크다운 정제 및 자동 태깅
- `/MD-PPT` : PPT 문서의 10대 핵심 파싱, 표 병합 복원 및 Mermaid 변환 적용
- `/title` : 본문 내용(description) 기반으로 알맞은 타이틀 및 파일명 자동 변경
- `/link` : 볼트 내 고아 문서를 찾아 기존 문서들과 문맥 연결
- `/rollup` : 오늘 생성된 문서와 진행 중인 태스크를 모아 데일리 리포트 작성
- `/hotkey` : 태깅, 제목 변경, 링크 연결, MOC 갱신을 한 번에 실행하는 올인원 스킬
- `/harness [내용]` : 에이전트에게 새로운 룰/스킬/훅을 생성해서 영구 등록하라고 지시

Antigravity, Obsidian, MarkdownConverter


