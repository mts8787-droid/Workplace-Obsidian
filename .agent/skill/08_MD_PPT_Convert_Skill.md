---
title: "08_MD_PPT_Convert_Skill"
description: "PPT/Excel 추출 문서를 원본 구조에 맞춰 Markdown, 표, 안전한 Mermaid, callout으로 정리하는 변환 스킬"
category: "skill"
tags:
  - type/playbook
  - status/active
  - doc/strategy
  - topic/tech/agent
---

# Skill: MD-PPT 렌더링 파싱 및 정밀 구조화 (/md-ppt-render)
**Precedence: 2**

## 1. 목적
`/md-ppt-render`는 PPTX/PPT 기반 문서를 읽어 슬라이드의 의미, 구조, 표, 차트, 다이어그램, 강조 요소를 Obsidian에서 안정적으로 렌더링되는 Markdown 문서로 복원합니다. 이미지 및 복합 시각 요소의 파싱이 포함됩니다.

Mermaid는 필요한 경우에만 사용하며, Obsidian 렌더링 오류가 발생하지 않도록 `10_Mermaid_Rendering_Rule.md`의 생성/정제/QC 조건을 반드시 통과해야 합니다.

## 2. 작동 조건
- **대상 파일**: PPTX, PPT, 또는 사용자가 명시한 PPT 변환 대상 문서
- **명령어**
  - `/md-ppt-render [파일명 또는 경로]`
  - `/md-ppt-render --folder [경로]`
  - `/md-ppt-render`만 입력된 경우 현재 IDE 활성 파일을 우선 확인하고, 변환 대상이 아니면 경로를 다시 요청합니다.

## 3. 참조 규칙
아래 문서는 `/md-ppt-render` 수행 시 항상 함께 적용합니다.

- `@include rule/08_PPT_Parsing_Rule.md`
- `@include rule/10_Mermaid_Rendering_Rule.md`
- `@include rule/06_Obsidian_Syntax_Rule.md`
- `@include hook/03_PPT_Parsing_Hook.md`

## 4. 처리 파이프라인 (AI Agent 강제 수행 단계)
사용자가 `/md-ppt-render`를 호출하면 AI 에이전트는 다음 파이프라인을 **끝까지** 직접 수행해야 합니다.

1. **Parser 추출 단계**: `.agent/scripts/autonomous_ppt_agent.py`를 실행하여 텍스트와 슬라이드 이미지(`assets/` 폴더)를 1차 추출하고 `[파일명].md`를 생성합니다. (※ 이미 추출된 `.md` 파일이 활성화된 상태라면 이 단계는 생략합니다.)
2. **Vision 기반 분석 단계 (LLM 직접 수행)**: 에이전트는 추출된 `.md` 파일의 내용을 읽고, 각 슬라이드 상단에 링크된 이미지(`![Slide N Image](...)`)를 렌더링 및 참조하여 슬라이드의 실제 시각적 레이아웃과 도식 구조를 완벽히 파악합니다.
3. **Markdown 전면 재구성 단계 (LLM 지능적 개입 강제)**: 에이전트는 파이썬 스크립트가 1차적으로 추출하여 기계적으로 나열한 원시 마크다운(단순 화살표 나열, 고립된 단어 조각 등)을 그대로 방치해서는 안 됩니다. 파일 편집 도구를 사용하여 **보고서를 사람이 직접 쓴 것처럼 자연스럽고 완벽하게 전면 재작성(Rewrite)**해야 합니다.
   - **자연스러운 서술형 보고서화(말로 설명 최우선)**: `> [!info] 🧩 **[도식 공간 분석]**` 블록이나 복잡한 데이터는 무조건 Mermaid 다이어그램으로 그리지 마십시오. 기계적인 단어 나열 대신, 전체 문맥을 추론하여 읽기 편한 "자연스러운 서술형 문단(Paragraph)"이나 "완성된 문장 형태의 리스트"로 상세하게 풀어 써야 합니다.
   - **의미론적 맥락 및 흐름 완벽 복원 (Vision 기반)**: 파편화되고 끊어진 단어나 문장 조각(예: `- Search`, `- Retail` 등)은 단순 병합하지 말고, 슬라이드 원본 이미지(Vision)의 시각적 흐름을 대조 확인하여 원래 의도된 논리적 맥락에 맞게 **완벽한 문장과 논리 덩어리로 완전히 조립(Synthesize)**해야 합니다.
4. **Mermaid 방어 및 리뷰어 단계 (LLM 직접 수행)**: 에이전트는 치환된 결과물에 깨진 표 구조, 미변환된 Raw Dump 잔여물, 닫히지 않은 따옴표 등 Mermaid 렌더링 실패 조건이 있는지 전수 검사하고 보완합니다.
5. **Inbox 정착 단계**: 최종 생성된 마크다운 문서 최적화를 위해 `/taggging`과 `/title` 스킬을 연이어 호출합니다.

## 5. Mermaid 사용 기준
Mermaid는 아래 조건을 모두 만족할 때만 사용합니다.

- 방향성이 명확한 흐름 또는 간단한 프로세스임
- 노드 수가 과도하지 않고, 라벨이 짧게 정리 가능함
- 표나 WBS로 표현하는 것보다 흐름 이해에 분명히 유리함
- 모든 노드/subgraph 라벨을 닫힌 쌍따옴표로 감쌀 수 있음

아래 경우에는 Mermaid를 사용하지 않고 Markdown Table 또는 중첩 리스트로 변환합니다.

- 로드맵, WBS, 일정표, KPI 비교표
- 행/열 구조가 핵심인 매트릭스
- 좌우/상하 영역 비교 레이아웃
- 긴 문장 라벨이 많은 개념도
- `<br>` 같은 HTML 줄바꿈이 필요할 정도로 라벨이 긴 구조

## 6. Mermaid QC 게이트
최종 완료 전 모든 `.md` 결과물에서 아래 조건을 검사합니다.

- `> ```mermaid` 금지
- Mermaid 블록 내부 `>` 접두어 금지
- Mermaid 라벨 내부 `<br>`, `<b>` 등 HTML 태그 금지
- `A["라벨]`처럼 닫는 따옴표가 빠진 라벨 금지
- `subgraph ID["라벨]`처럼 닫는 따옴표가 빠진 subgraph 금지
- 단일 backtick 또는 미닫힌 fence 금지

하나라도 발견되면 완료를 선언하지 말고 즉시 정제하거나, 안정적인 Markdown Table/리스트로 대체합니다.

## 7. 실행 제약
- 한 번에 처리하는 대상은 최대 2개 문서로 제한합니다.
- 중간 추출 결과만 남기고 완료를 선언하지 않습니다.
- 이미지 추출이 실패해도 텍스트 구조화는 계속 진행할 수 있습니다.
- 최종 Markdown은 Obsidian에서 바로 열어 읽을 수 있는 상태여야 합니다.
