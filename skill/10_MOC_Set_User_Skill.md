---
title: "10_MOC_Set_User_Skill"
description: "기존 사용자의 폴더 트리를 분석하여 Johnny Decimal 1 Depth(10~30) 구조는 유지하되, 2 Depth 이하의 하위 구조를 규칙에 맞게 재배치 및 생성하는 스킬"
category: "skill"
tags:
  - MOC
  - 폴더정리
  - 조니데시멀
---

# 🛠️ Skill: 사용자 지정 MOC 기반 폴더 재분배 (/moc-set-user)
**Precedence: 2**

## 1. 목적
사용자가 기존에 사용하던 폴더 트리(루트 경로)를 분석하여, `07_Johnny_Decimal_Rule.md`에서 정의된 핵심 1 Depth 분류(10~90 등 최상위 폴더)는 훼손하지 않고, 그 하위의 2 Depth ~ 3 Depth 폴더 트리를 MOC 논리에 따라 재설계하고 파일을 재분배(Redistribution)합니다.

## 2. 작동 조건 (Triggers)
- **대상 폴더**: 사용자가 지정한 기존 폴더 루트 경로
- **명령어**: `/moc-set-user [기존_폴더_루트경로]`
- **실행 원칙**: 
  - 사용자가 경로를 입력하지 않은 경우, 에이전트는 절대 임의의 경로를 타겟으로 삼지 말고 사용자에게 기존 폴더 경로를 물어야 합니다.

## 3. 참조 문서 (Rules & Hooks)
- `@include rule/07_Johnny_Decimal_Rule.md`: 1 Depth 유지 및 하위 폴더 배치의 절대 기준.
- `@include hook/01_Destructive_Action_Hook.md`: 기존 폴더 구조 변경 전 백업 및 확인 절차 의무.

## 4. 🤖 워크플로우 (Workflow)
1. **기존 디렉토리 스캔**:
   - 지정된 `[기존_폴더_루트경로]` 하위의 폴더 구조와 파일 목록을 `list_dir`을 통해 스캔합니다.
2. **2 Depth 매핑 및 재설계**:
   - `07_Johnny_Decimal_Rule.md`의 `10~30`번대 1 Depth(최상위 폴더) 구조는 절대 건드리지 않습니다.
   - 기존 폴더 트리의 목적과 파일 성격(프로젝트, 산출물, 레퍼런스 등)을 분석하여, 적합한 1 Depth 산하의 2 Depth 구조로 매핑하는 계획(Migration Plan)을 세웁니다.
3. **MOC 룰 적용 및 폴더 생성 제안**:
   - 기존 폴더 이름과 태그, 파일 속성을 기반으로 조니 데시멀 넘버링(`11. XX`, `21. YY` 등)을 부여하여 새로운 하위 폴더 트리를 구성합니다.
4. **리뷰 및 승인 요청**:
   - 파일을 실제로 이동시키거나 폴더를 삭제하기 전에, **반드시 사용자에게 변경될 Before/After 폴더 트리 매핑 계획을 표나 트리 형태로 보여주고 컨펌을 요청**해야 합니다.
