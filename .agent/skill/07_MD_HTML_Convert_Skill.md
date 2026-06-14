---
title: "07_MD_HTML_Convert_Skill"
description: "HTML 원시 문서와 이메일 클리핑을 Markdown으로 정제하고, /taggging을 통해 표준 frontmatter와 택소노미 태그를 완성하는 스킬"
category: "skill"
tags:
  - type/playbook
  - status/active
  - topic/marketing/content
---

# Skill: HTML 원시 파일 Markdown 변환 및 택소노미 태깅 (/md-html)
**Precedence: 3**

## 1. 목적
`/md-html`은 HTML 원시 코드, 이메일 원문, 웹 클리핑 문서를 Obsidian에서 읽기 쉬운 Markdown으로 정제하고, 변환 직후 `/taggging`을 적용해 표준 frontmatter와 태그 택소노미를 완성합니다.

이 스킬은 HTML 태그 제거만으로 완료되지 않습니다. 변환 결과는 반드시 `description`과 15개 네임스페이스 기반 `tags`를 포함해야 합니다.

## 2. 작동 트리거
- **명령어**: `/md-html`
- **일괄 적용**: `/md-html --folder [경로]`
- **디스패처 경유**: `/md`가 HTML, HTM, MHT, 이메일 원시본, 웹 클리핑 계열로 판단한 경우 자동 호출합니다.

## 3. 참조 문서
이 스킬을 수행할 때 에이전트는 아래 문서를 함께 적용합니다.

- `@include rule/09_HTML_Parsing_Rule.md` (HTML 태그 제거 및 Markdown 치환 방식)
- `@include rule/02_Frontmatter_Standard_Rule.md` (16개 필수 속성, YAML 문법, `tags` 세로 리스트)
- `@include skill/02_Metadata_Tagging_Skill.md` (`/taggging` 메타데이터 생성 및 태깅)
- `@include rule/04_Tag_Taxonomy_Rule.md` (15개 네임스페이스 기반 태그 사전)
- `@include rule/03_Tag_Creation_Rule.md` (신규 태그 생성 전 기존 택소노미 우선 조회)
- `@include hook/05_Tag_Sync_Hook.md` (태그 스킬, 생성 룰, 택소노미 룰 동기화 강제)

## 4. 변환 워크플로우
1. 원문에서 HTML 구조, 스타일, 불필요한 wrapper 태그를 제거합니다.
2. 본문 의미가 있는 제목, 문단, 목록, 링크, 인용, 첨부 정보를 Markdown 문법으로 보존합니다.
3. 이메일 헤더의 보낸 사람, 받은 사람, 제목, 발신 일시는 본문 상단의 읽기 쉬운 메타 블록으로 정리합니다.
4. 정제된 본문을 `00. Inbox` 폴더로 이동(저장)합니다.
5. 저장된 파일을 대상으로 즉시 `/taggging`과 `/title` 스킬을 순차적으로 수행합니다.
6. `/taggging`과 `/title` 처리 결과가 완료 조건을 통과한 경우에만 `/md-html` 완료로 간주합니다.

## 5. 메타데이터 완료 조건
`/md-html` 결과물은 아래 조건을 모두 만족해야 합니다.

1. `description` 필드는 반드시 존재해야 하며, 본문 맥락을 요약한 1~3문장 또는 약 200자 내외의 설명이어야 합니다.
2. frontmatter에는 `02_Frontmatter_Standard_Rule.md`의 16개 필수 속성이 모두 있어야 합니다.
3. `tags`는 세로 리스트로 작성합니다.
4. 모든 태그는 `04_Tag_Taxonomy_Rule.md`의 15개 네임스페이스 중 하나로 시작해야 합니다.
   - 허용 예: `type/report`, `status/inbox`, `model/d2c`, `market/global`, `topic/seo/geo`
   - 금지 예: `KI`, `GEO`, `D2C`, `마케팅`, `자동화` 같은 평면 태그
5. 조직명, 인물명, 특정 프로젝트명, 파일명, 제품 모델명 같은 고유명사는 태그로 만들지 않고 본문 또는 wikilink로 유지합니다.
6. 기존 택소노미에 맞는 태그가 없을 때만 `03_Tag_Creation_Rule.md`에 따라 신규 태그를 만들고, 즉시 `04_Tag_Taxonomy_Rule.md`에 등록합니다.

## 6. 실패로 간주하는 상태
아래 중 하나라도 발견되면 `/md-html` 결과물을 완료본으로 보지 말고 `/taggging` 보정 단계를 다시 수행합니다.

- `description` 누락 또는 빈 문자열
- `tags` 누락 또는 빈 리스트
- `/` 없는 평면 태그 포함
- 택소노미 네임스페이스가 아닌 임의 태그 포함
- YAML 따옴표, 리스트 들여쓰기, frontmatter 구분자(`---`) 파손
- `category`, `domain`, `status`가 문서 맥락과 무관한 자유 입력값으로 채워짐
