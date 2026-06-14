# 🤖 AGENTS.md (Master Core)
**Precedence: 1 (최우선 마스터 허브)**

> 이 문서는 사용자의 옵시디언(Obsidian) 볼트를 효율적으로 관리하기 위한 AI 에이전트 전용 **'통제 허브(Hub)'**입니다.
> This file governs the vault root and all descendants unless a closer `AGENTS.md` overrides it.

## 0. Repository Instructions
When working in this repository:
- Treat this `AGENTS.md` as the master index for all repo-specific `ki`, skill, subagent, rule, and hook documents.
- Apply every skill, rule, and hook under `.agent/skill/`, `.agent/rule/`, and `.agent/hook/` that matches the task, file state, or workflow.
- Use the matching `ki/` or `subagent/` document when the task touches the corresponding workflow.
- Treat hooks as hard constraints.
- Keep the Obsidian vault structure, metadata, and note integrity intact unless the user explicitly asks for a change.
- Keep this file at the harness level: command-specific procedures, exceptions, and execution details belong in the relevant skill, rule, or hook document.
- When editing harness documents, classify the target layer first and keep the change inside that layer; split cross-layer content into separate files instead of blending it here.

---

## 1. 하네스 엔지니어링 3대 원칙 (Harness Engineering)
에이전트는 사용자의 모든 시스템/규칙 관련 명령을 다음 3가지 관점으로 엄격히 분류하여 `.agent` 폴더 하위에 마크다운(MD) 파일로 영구 저장하고 스스로 진화해 나갑니다.

1. **🛠️ SKILLS (자동화 워크플로우)**: 어떻게 실행하고 라우팅할 것인가? (How-to, Automated Process)
2. **📋 RULES (작업/참고 규칙)**: 작업을 할 때 무엇을 기준으로 삼을 것인가? (Guidelines, Standards)
3. **🚫 HOOKS (절대 금지 사항)**: 생태계 파괴를 막기 위해 에이전트가 '절대 하지 말아야 할 것'은 무엇인가? (Don'ts)

*(아래는 현재 활성화된 하네스 엔지니어링 파일 목록입니다)*

### 🧠 KI (내부 두뇌 영구 등록용 지침)
에이전트가 작업 전 반드시 숙지해야 할 최상위 행동 강령 및 메타 규칙입니다.
- `@include ki/KI_코어_시스템_지침.md` (하네스 시스템 및 폴더 보호 메타 원칙)
- `@include ki/KI_Karpathy_Guidelines.md` (안드레 카파시 행동 지침)
- `@include ki/KI_Harness_Engineering.md` (하네스 진화 및 점진적 학습 관리 원칙)

### 🛠️ SKILLS (에이전트 행동 엔진)
- `@include skill/01_Directory_Routing_Skill.md` (폴더 자동 라우팅 및 쟈니 데시멀 정밀 분류)
- `@include skill/02_Metadata_Tagging_Skill.md` (메타데이터 및 태그 자동 매핑, `/taggging`)
- `@include skill/04_Orphan_Linker_Skill.md` (고립된 고아 문서 문맥 연결)
- `@include skill/05_Daily_Rollup_Skill.md` (일일/주간 작업 요약 리포트 작성)
- `@include skill/06_Title_Change_Skill.md` (description 기반 파일명 및 타이틀 자동 변경)
- `@include skill/07_MD_HTML_Convert_Skill.md` (HTML 원시 파일 마크다운 정제 및 자동 태깅, `/md-html`)
- `@include skill/08_MD_PPT_Convert_Skill.md` (PPT 이미지/렌더링 포함 정밀 구조화, `/md-ppt-render`)
- `@include skill/13_MD_PPT_Text_Convert_Skill.md` (PPT 텍스트 기반 도식화 및 정제, 이미지 생략, `/md-ppt-text`)
- `@include skill/14_MD_Excel_Convert_Skill.md` (Excel 병합 셀 정제 및 시트 분리 구조화, `/md-xlsx`)
- `@include skill/12_MD_Dispatch_Skill.md` (선택된 파일 형식에 따라 `/md-html` 또는 `/md-ppt-text`를 자동 호출하는 `/md` 디스패처)
- `@include skill/09_All_in_One_Classification_Skill.md` (올인원 태깅/분류/라우팅 일괄 처리)

### 🤖 SUBAGENTS (서브에이전트 페르소나 및 롤 정의)
특정 스킬(특히 파싱/정제)을 수행하기 위해 메인 에이전트와 역할을 분담하는 전담 서브에이전트들의 페르소나와 워크플로우 정의입니다.
- `@include subagent/01_PPT_Parser_Agent.md` (1차 텍스트 및 좌표 원시 추출 파서)
- `@include subagent/02_PPT_Editor_Agent.md` (파편화된 원시 마크다운의 표/다이어그램 정제 조립)
- `@include subagent/03_PPT_Reviewer_Agent.md` (조립된 최종 파일의 렌더링 검수 및 무결성 확보)
- `@include subagent/04_PPT_Writer_Agent.md` (단어 파편의 문장화 및 시각 더미/페이지 번호 삭제 등 최종 구조화)

### 📋 RULES (작업 표준 및 규정)
- `@include rule/01_Directory_Structure_Rule.md` (폴더 분류 체계)
- `@include rule/02_Frontmatter_Standard_Rule.md` (15개 필수 속성 및 YAML 문법)
- `@include rule/03_Tag_Creation_Rule.md` (보수적 태그 생성 원칙)
- `@include rule/04_Tag_Taxonomy_Rule.md` (15개 네임스페이스 기반 태그 택소노미 및 허용 사전)
- `@include rule/06_Obsidian_Syntax_Rule.md` (옵시디언 특화 렌더링 및 참조 문법 규칙)
- `@include rule/07_Johnny_Decimal_Rule.md` (쟈니 데시멀 넘버링 정밀 규칙)
- `@include rule/08_PPT_Parsing_Rule.md` (PPT 타이포그래피, 다이어그램 등 정밀 변환 룰)
- `@include rule/09_HTML_Parsing_Rule.md` (HTML 태그 제거 및 마크다운 치환 정규화 룰)
- `@include rule/10_Mermaid_Rendering_Rule.md` (Obsidian Mermaid 렌더링 오류 방지 및 QC 룰)

### 🚫 HOOKS (절대 금지 사항 - Precedence 0)
- `@include hook/01_Data_Integrity_Hook.md` (태그 삭제 금지, 문법 파괴 금지, 파편화 금지, .agent 이동 금지)
- `@include hook/03_PPT_Parsing_Hook.md` (PPT 파싱 시 2개 문서 제한 및 불완전 종료 절대 금지)
- `@include hook/06_Harness_Layer_Fence_Hook.md` (하네스 레이어 경계 강제, Hub/Skill/Rule/Hook 분리)
- `@include hook/07_MD_Extraction_Routing_Hook.md` (모든 /md 변환 결과물을 00. Inbox로 강제 라우팅)

---

## 2. 공식 슬래시 명령어 (Slash Commands)
사용자는 에이전트에게 아래의 슬래시 명령어를 입력하여 빠르고 정확하게 자동화 스킬을 가동하거나 진화시킬 수 있습니다.
- `/skill-list` : 현재 에이전트가 가동할 수 있는 모든 스킬(명령어) 리스트와 간단한 설명을 출력
- `/route` : `01_Directory_Routing_Skill` 발동 (Inbox 문서의 1 Depth 분류 및 2~3 Depth 쟈니 데시멀 정밀 타겟팅 이동)
- `/taggging` : `02_Metadata_Tagging_Skill` 발동 (메타데이터 할당 및 200자 description 자동 생성)
- `/md` : 선택된 파일 형식에 따라 `/md-html` 또는 `/md-ppt-text`를 자동 호출하는 디스패처
- `/md-html` : `07_MD_HTML_Convert_Skill` 발동 (HTML 코드 텍스트 추출 후 마크다운 정제 + 자동 태깅)
- `/md-ppt-render` : `08_MD_PPT_Convert_Skill` 발동 (이미지 파싱 포함 정밀 구조화)
- `/md-ppt-text` : `13_MD_PPT_Text_Convert_Skill` 발동 (이미지 파싱 생략, 텍스트 기반 다이어그램 도식화)
- `/md-xlsx` : `14_MD_Excel_Convert_Skill` 발동 (Excel 시트별 표 및 타임라인 정제 구조화)
- `/title` : `06_Title_Change_Skill` 발동 (description 기반으로 알맞은 타이틀/파일명 변경)
- `/link` : `04_Orphan_Linker_Skill` 발동 (고립된 고아 문서를 찾아 문맥 연결)
- `/rollup` : `05_Daily_Rollup_Skill` 발동 (생성된 문서와 태스크 모아 데일리 요약)
- `/hotkey` : `09_All_in_One_Classification_Skill` 발동 (태깅, 제목 변경, 링크, 분류 일괄 적용)
- `/harness [내용]` : 새로운 규칙을 하네스 관점(Skill/Rule/Hook)으로 파악해 `.agent`에 MD로 저장
