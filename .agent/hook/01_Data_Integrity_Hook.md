---
title: "Data Integrity Hook"
author: "Antigravity Agent"
author_email: ""
team: ""
access_level: "system"
category: "guide"
tags:
  - 시스템_규칙
domain: ""
status: "done"
created_at: "2026-05-22"
updated_at: "2026-05-22"
source_filename: ""
version: "1.0"
converter_version: ""
quality_score: ""
---
# 🚫 Hook: 데이터 무결성 보존 (Data Integrity Hook)
**Precedence: 0 (가장 먼저 평가됨, 절대적)**

## 1. 절대 금지 사항 (Don'ts)
이 Hook에 명시된 사항은 어떠한 Skill이나 Rule보다 우선하며, 절대 위반해서는 안 됩니다.

1. **스킬 제어 및 구조 변경 강제 차단 구역 (Skill Denial Zones)**
   - 볼트의 무결성 및 시스템 보호를 위해, 폴더별로 다음 수준의 제어를 강제 차단(Deny)해야 합니다.
     - **[수준 1: 전면 차단 구역]** **`.`으로 시작하는 모든 시스템 폴더** (예: `.agent/`, `.obsidian/` 등) 및 **볼트 최상위 루트**
       - **적용 규칙**: 사용자가 `/moc`, `/md`, `/tagging`, `/route` 등 **어떠한 슬래시 명령어(Skill)를 입력하더라도 절대 실행해서는 안 됩니다.** 실수로 명령어를 입력한 경우에도 "해당 폴더는 시스템 폴더로 스킬 발동이 금지되어 있습니다"라고 안내하며 강제 차단해야 합니다.
     - **[수준 2: 구조 변경 차단 구역]** **특수 목적 폴더 4종** (`Email_Raw/`, `Clippings/`, `암묵지 변환 결과/`, `암묵지 변환 대상/`)
       - **적용 규칙**: `/route`, `/title` 등 파일명을 변경하거나 폴더를 이동(구조 파괴)시키는 스킬은 절대 금지됩니다. (단, 사용자가 명시적으로 지시한 데이터 정제용 스킬(`/md`, `/tagging`, `/link` 등)은 허용됩니다.)
2. **태그 및 메타데이터 삭제 금지 (No Deletion)**
   - 한 번 문서에 부여된 `tags`나 메타데이터 속성은 시스템의 지식망을 구성하므로 임의로 삭제해서는 안 됩니다. (추가만 가능)
3. **YAML 문법 붕괴 금지 (No Malformed YAML)**
   - 따옴표로 감싸지 않은 특수문자나 닫히지 않은 괄호(`[[ ]]`)를 YAML에 삽입하여 메타데이터 인식을 고장 내지 마십시오.
4. **동의어 파편화 금지 (No Synonyms Splitting)**
   - `#인공지능`과 `#AI`를 섞어 쓰지 마십시오.
5. **문장형 태그 금지 (No Sentence Tags)**
   - 서술형이나 문장이 담긴 태그 생성을 절대 금지합니다.
