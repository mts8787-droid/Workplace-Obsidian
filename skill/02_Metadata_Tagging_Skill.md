---
title: "02_Metadata_Tagging_Skill"
description: "문서 본문의 맥락을 분석하여 옵시디언 15개 표준 프론트매터 및 60+개의 풍성한 실무 기술 태그를 자동 할당하는 스킬"
category: "skill"
tags:
  - 스킬
  - 메타데이터
  - 태깅
---

# 🏷️ Skill: 메타데이터 및 풍성한 태그 할당 (/tag)
**Precedence: 2**

## 1. 목적 (Purpose)
문서의 빈 프론트매터(깡통 메타데이터)를 분석하여 상세 설명(Description), 도메인(Domain), 품질 점수 등을 정밀하게 채워 넣고, 단순 분류를 넘어 **60여 개의 고도화된 실무 키워드 기반 태그 풀(Tag Pool)**을 활용해 지식 검색의 해상도를 극대화합니다.

## 2. 작동 트리거 (Trigger)
- **명령어**: `/tag` (현재 문서 대상 정밀 태깅)
- **일괄 적용**: `/tag --folder` (대상 폴더 내 모든 문서의 메타데이터 및 태그 일괄 최적화)

## 3. 참조 문서 (Rules & Hooks)
이 스킬을 가동할 때 에이전트는 반드시 아래의 세부 규칙을 참조하여 메타데이터와 태그를 할당해야 합니다.
- **메타데이터 표준 규격**: `@include rule/02_Frontmatter_Standard_Rule.md` (15개 필수 속성 정의)
- **태그 생성 룰**: `@include rule/03_Tag_Creation_Rule.md` (보수적 태그 생성 원칙)
- **허용된 태그 단어장**: `@include rule/04_Tag_Vocabulary_Rule.md` (60여 개 실무 키워드 풀)

## 4. 라이프사이클 워크플로우 (Status)
- `draft` (초안) ➡️ `in_progress` (진행 중) ➡️ `reviewed` (검수 완료) ➡️ `완성` (최종)
