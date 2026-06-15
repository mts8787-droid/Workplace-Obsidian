---
title: "15_MD_PDF_Convert_Skill"
description: "PDF 문서의 OCR 텍스트를 분석하여 페이지 번호 등 불필요한 메타데이터를 제거하고 논리적 마크다운으로 변환하는 스킬"
category: "skill"
tags:
  - type/playbook
  - status/active
  - doc/data
  - topic/tech/agent
---

# Skill: MD-PDF 변환 및 정제 (/md-pdf)
**Precedence: 2**

## 1. 목적
`/md-pdf`은 PDF 형식의 문서(보고서, 논문, 아키텍처 다이어그램 등)에서 추출된 원시 텍스트(OCR 포함)를 정제하여, 의미 없는 페이지 헤더/푸터 및 파편화된 줄바꿈을 제거하고 완결성 있는 마크다운 문서로 구조화합니다.

## 2. 작동 조건
- **대상 파일**: `.pdf` 파일
- **명령어**
  - `/md-pdf [파일명 또는 경로]`
  - `/md-pdf`만 입력된 경우 현재 활성 파일을 확인하고, 없으면 경로를 요청합니다.

## 3. 참조 규칙
- `@include rule/02_Frontmatter_Standard_Rule.md`
- `@include rule/06_Obsidian_Syntax_Rule.md`
- `@include hook/07_MD_Extraction_Routing_Hook.md`

## 4. 처리 파이프라인
1. **텍스트 추출 (Parser 단계)**: PDF 문서에서 텍스트 및 OCR 데이터를 추출합니다.
2. **노이즈 제거 (Filter 단계)**: 모든 페이지 하단/상단에 반복되는 타임스탬프, 파일 경로, 페이지 번호(예: `4/30/26, 2:33 PM ... file:///... 1/12`) 등을 식별하여 완전히 삭제합니다.
3. **구조 복원 (Reassembly 단계)**: 단어 단위로 찢어진 문장이나 다이어그램 기호를 논리적인 마크다운 표, 리스트, 또는 문장으로 조립합니다.
4. **Inbox 정착 단계 (Routing)**: `07_MD_Extraction_Routing_Hook.md`에 따라 최종 결과물을 `00. Inbox` 폴더에 강제 저장하고, 즉각 `/taggging` 및 `/title` 스킬을 연쇄 가동합니다.

## 5. PDF 특화 정제 원칙 (LLM Self-Correction)
- **헤더/푸터(Header/Footer) 노이즈 차단**: 
  - PDF 특성상 모든 페이지마다 반복되는 파일명, 날짜, URL, 페이지 번호 등은 본문 컨텍스트를 방해하므로 정제 과정에서 최우선으로 필터링하여 삭제해야 합니다.
- **다단/다이어그램 텍스트의 선형화**: 
  - 시각적 다이어그램에서 추출된 파편화된 단어들(예: A -> B -> C 흐름)을 문장형 설명이나 계층형 리스트(`-`, `*`)로 재조립하여 읽기 편하게 선형화(Linearization)합니다.
- **문장 끊김 복원**: 
  - 페이지가 넘어가면서 강제로 줄바꿈된 문장을 문맥을 파악하여 하나의 자연스러운 문장으로 이어 붙입니다.
