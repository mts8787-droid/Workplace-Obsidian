---
title: "08_MD_PPT_Convert_Skill"
description: "원시 추출 문서(PPT/Excel)를 전용 파서 스크립트와 AI의 구조화 능력을 결합해 정보 손실 없이 정밀 파싱하고 리팩토링하는 가이드"
category: "skill"
tags:
  - PPT변환
  - 마크다운
  - 파싱
  - 리팩토링
---

# 🛠️ Skill: MD-PPT 파싱 및 정밀 구조화 스킬 (/MD-PPT)
**Precedence: 2**

## 1. 목적
단순 텍스트로 무작위 추출된 PPT, 엑셀 기반의 원시 마크다운 파일을 에이전트 자체의 맥락 추론 능력을 사용해 논리적으로 분리하고, 가독성이 극대화된 고급 마크다운(Mermaid, Table, Callout)으로 리팩토링 및 구조화(문장화) 합니다. 

## 2. 작동 조건 (Triggers)
- **대상 파일**: `00. Inbox` 등에 존재하는 PPTX 원본 파일 또는 파편화된 원시 마크다운 문서
- **사용자 명령어 규칙**: 
  - `/MD-PPT [파일명 또는 경로]`: 특정 대상 문서에 대해 4-Agent 파싱 가동 (예: `/MD-PPT FFFFFFFFFFF.pptx`)
  - `/MD-PPT --folder [경로]`: 대기열의 문서를 대상으로 순차적 파싱 시작
- **🚨 묻기 규칙 (Ask First)**: 만약 사용자가 경로 명시 없이 `/MD-PPT`만 입력할 경우, 에이전트는 절대 임의로 실행하지 말고 **반드시 변환할 타겟 파일명이나 경로를 되물어야** 합니다.

## 3. 참조 문서 (Rules & Hooks)
이 스킬 워크플로우를 가동할 때 에이전트는 반드시 아래의 세부 규칙과 절대 훅을 병합하여 준수해야 합니다.
- **세부 변환 규칙**: `@include rule/08_PPT_Parsing_Rule.md` (타이포그래피, 다이어그램, 시맨틱 컬러 매핑 룰 등)
- **절대 보호 훅**: `@include hook/03_PPT_Parsing_Hook.md` (세션당 2개 제한, 불완전 종료 금지)

## 4. 🤖 자율형 PPT 파싱 4-Agent 파이프라인 (Multi-Agent Architecture)
단순 Raw 마크다운 추출을 넘어, 완벽한 시각화 마크다운을 자동으로 생성하기 위해 **'4-Agent 워크플로우(Parser ➡️ Editor ➡️ Reviewer ➡️ Writer)'** 아키텍처를 스킬에 등록했습니다. 

### 4.1 4-Agent 워크플로우 구조 (Antigravity 1인 4역 직접 수행)
사용자는 별도의 API 키가 없으므로, 1단계 추출만 파이썬 스크립트가 담당하고 나머지 2~4단계는 **반드시 메인 세션(Antigravity LLM)이 지능적 추론을 통해 직접 수행**해야 합니다. (파이썬 정규식 스크립트로 덮어쓰는 꼼수 사용 절대 금지)

1. **Parser Agent (파서 에이전트 - 파이썬 스크립트)**: 백그라운드 터미널(`run_command`)로 파이썬 스크립트를 실행해 PPTX의 텍스트와 좌표를 Raw 마크다운으로 1차 추출 및 저장합니다.
2. **Editor Agent (편집 에이전트 - LLM 직접 추론)**: 파서가 만들어낸 파일이 방대하므로, 에이전트는 `view_file` 도구를 사용해 **500줄 단위로 끊어 읽으며(Chunking)** 내용의 문맥을 직접 파악합니다. 단순 정규식으로 처리 불가능한 복잡한 구조(예: AS-IS vs TO-BE 매트릭스)를 LLM 지능으로 추론하여 마크다운 표(Table)나 Mermaid 차트로 직접 재구성(Refining) 및 덮어쓰기(`multi_replace_file_content`) 합니다.
3. **Reviewer Agent (검수 에이전트 - LLM 직접 수행)**: 조립된 MD 파일 구간을 다시 검수하여, 렌더링 에러(Mermaid 따옴표 누락 등)나 누락된 표 제목이 있는지 최종 QC(Quality Control)를 진행합니다.
4. **Writer Agent (구조화 및 라이터 에이전트 - LLM 직접 수행)**: 에디터 작업과 병행하여, `![Slide Image]` 같은 시각 더미 데이터를 삭제하고, 표로 만들지 못한 파편화된 단어들을 앞뒤 문맥(Context)을 바탕으로 자연스러운 문장(Sentence)으로 구조화합니다.

### 4.2 실행 방법 (채팅 기반 자동 실행)
- 사용자가 채팅창에 **`/MD-PPT [파일명]`** 형태로 타겟을 명시하여 입력하면, 에이전트(LLM)가 알아서 지정된 파일의 절대 경로를 탐색하여 백그라운드 터미널(run_command)로 파이썬 스크립트를 자동 실행합니다.
- 만약 파일명이 생략되었다면, 에이전트는 사용자에게 타겟을 묻고 답변을 받은 후에만 파이프라인을 가동합니다.
- 추출 스크립트 실행 명령어 (UTF-8 강제 적용):
```bash
python -X utf8 "c:/Users/ts.moon/OneDrive - LG전자/obsidian/.agent/scripts/autonomous_ppt_agent.py" "전달받은_PPT경로"
```
- **🚨 절대 훅 (Hook)**: 스크립트 실행이 끝났다고 "완료되었습니다" 하고 넘어가면 안 됩니다. 에이전트는 반드시 결과 파일을 읽어들여 Editor ➡️ Reviewer ➡️ Writer 에이전트 단계를 연달아 수행한 후, 완벽히 문장화된 최종 결과물을 사용자에게 보고해야 합니다.
