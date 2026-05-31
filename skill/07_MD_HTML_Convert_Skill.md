# 🛠️ Skill: 이메일 정제 스킬 (Email_MD-HTML Convert Skill)
**Precedence: 3**

## 1. 목적
`Email_Raw` 등 외부에서 수집되어 HTML 코드가 뒤섞인 원시(Raw) 마크다운 파일에서, 지저분한 태그를 걷어내고 순수한 텍스트와 링크만 추출하여 깔끔한 옵시디언 표준 Markdown 문법으로 재구성합니다. 변환 후 메타데이터 할당까지 원스톱으로 처리합니다.

## 2. 작동 트리거 (Trigger)
- **사용자 슬래시 명령어**: `/md-mail` (또는 `/md-mail --folder`로 현재 폴더 전체 일괄 적용)

## 3. 참조 문서 (Rules & Hooks)
이 스킬 워크플로우를 가동할 때 에이전트는 반드시 아래의 세부 규칙을 준수해야 합니다.
- **HTML 파싱 세부 규칙**: `@include rule/09_HTML_Parsing_Rule.md` (태그 제거 및 치환 방식)

## 4. 자동 태깅 (Auto-Tagging) 연계 워크플로우
- 마크다운 정제가 완료되면, 즉시 내부적으로 `/tagging` 스킬을 자동 호출합니다.
- 정제된 본문을 바탕으로 200자 요약(`description`)을 생성하고, 16개의 표준 Frontmatter(메타데이터)를 최상단에 삽입하여 문서를 완성합니다.
