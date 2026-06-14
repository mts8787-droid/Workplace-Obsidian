---
title: "12_MD_Dispatch_Skill"
description: "선택된 파일 형식에 따라 /md-html, /md-ppt-text 또는 /md-xlsx를 자동 호출하는 변환 디스패처"
category: "skill"
tags:
  - md
  - dispatch
  - html
  - ppt
---

# 🛠️ Skill: 파일 형식 자동 변환 디스패처 (/md)
**Precedence: 2**

## 1. 목적
사용자가 `/md`를 입력하면, 대상 파일의 형식과 컨텍스트를 판별해 적절한 변환 스킬을 자동 호출한다.

## 2. 작동 조건 (Triggers)
- **사용자 슬래시 명령어**: `/md [파일명 또는 경로]`
- **폴더 모드**: `/md --folder [경로]`
- **무경로 입력**: 경로가 없으면 IDE의 현재 활성 탭 또는 선택된 파일을 먼저 확인한다.

## 3. 자동 선택 규칙
- HTML, HTM, MHT, 이메일 원시본, 웹 클리핑 계열이면 `/md-html`을 호출한다.
- PPT, PPTX, 슬라이드 추출 문서 계열이면 토큰 절약을 위해 기본적으로 `/md-ppt-text`를 호출한다. (단, 사용자가 이미지 기반 렌더링을 원하면 `/md-ppt-render`를 호출)
- Excel 파일(XLSX, CSV, XLS) 계열이면 시트별 정제 및 구조화를 위해 `/md-xlsx`를 호출한다.
- 형식이 혼재하거나 판별이 불가능하면 사용자에게 다시 확인한다.

## 4. 참조 문서 (Rules & Hooks)
- `@include skill/07_MD_HTML_Convert_Skill.md`
- `@include skill/08_MD_PPT_Convert_Skill.md`
- `@include skill/13_MD_PPT_Text_Convert_Skill.md`
- `@include skill/14_MD_Excel_Convert_Skill.md`
- `@include rule/09_HTML_Parsing_Rule.md`
- `@include rule/08_PPT_Parsing_Rule.md`
- `@include hook/03_PPT_Parsing_Hook.md`
- `@include hook/01_Data_Integrity_Hook.md`

## 5. 워크플로우
1. 대상 파일 또는 폴더를 확인한다.
2. 확장자와 소스 유형을 판별한다.
3. HTML 계열이면 `/md-html`을, PPT 계열이면 `/md-ppt-text`를, Excel 계열이면 `/md-xlsx`를 자동 호출한다.
4. 대상이 명확하지 않으면 사용자에게 형식을 다시 묻는다.
5. 호출된 하위 스킬의 결과물(`.md`)은 `00. Inbox` (수집함) 폴더에 최종 저장(또는 이동)한다.
6. 이어서 해당 결과물에 대해 `/taggging` 스킬과 `/title` 스킬을 순차적으로 자동 실행하여 문서 정규화를 완료한다.

## 6. 완료 기준
- 사용자가 `/md` 하나만 입력해도 파일 형식에 맞는 변환 경로가 자동으로 선택된다.
- 변환 대상이 섞여 있으면 파일별로 적절한 하위 스킬로 분기된다.
- 판별 불가 파일은 잘못 추측하지 않고 확인 질문으로 중단한다.
