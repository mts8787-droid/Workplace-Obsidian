---
title: "11_MOC_Set_AI_Skill"
description: "AI가 볼트 전체의 파일, 태그, 링크 체계를 스캔/분석하여 최적의 Johnny Decimal 1 Depth 구조를 새롭게 제안하고 룰 문서를 재설계하는 스킬"
category: "skill"
tags:
  - MOC
  - AI추천
  - 조니데시멀설계
---

# 🛠️ Skill: AI 주도 MOC 및 조니 데시멀 설계 (/moc-set-ai)
**Precedence: 2**

## 1. 목적
에이전트가 사용자의 전체 Obsidian Vault 환경(파일군, 태그 클러스터, 양방향 링크 네트워크)을 지능적으로 스캔하고 분석하여, 현재 사용자 업무 패턴에 가장 최적화된 새로운 Johnny Decimal 1 Depth(10~30) MOC 구조를 추천하고 `07_Johnny_Decimal_Rule.md` 문서를 재설계합니다.

## 2. 작동 조건 (Triggers)
- **명령어**: `/moc-set-ai`

## 3. 참조 문서 (Rules & Hooks)
- `@include rule/07_Johnny_Decimal_Rule.md`: 이 문서가 재설계 및 업데이트 타겟이 됩니다.
- `@include hook/01_Destructive_Action_Hook.md`: 구조적 룰 변경 사항이므로 최종 적용 전 사용자 승인이 필요합니다.

## 4. 🤖 워크플로우 (Workflow)
1. **메타데이터 및 네트워크 스캔**:
   - Vault 내 파일들의 메타데이터(Frontmatter properties), 자주 사용되는 태그(Tags 클러스터), 파일 간의 연결망(Links) 등을 수집 및 분석합니다.
2. **패턴 추론 및 1 Depth 재설계**:
   - 분석된 데이터 패턴을 바탕으로 기존의 일률적인 "10. 프로젝트, 20. 산출물, 30. 참고자료" 구조가 아닌, 사용자의 실제 업무 도메인과 데이터 성격에 가장 밀착된 새로운 1 Depth (10~90) 분류 체계를 제안합니다.
3. **07_Johnny_Decimal_Rule.md 업데이트 제안**:
   - AI가 새롭게 설계한 조니 데시멀 룰셋과, 그 구조가 왜 타당한지에 대한 분석 논리(Rationale)를 Artifact 문서로 정리하여 사용자에게 보고합니다.
4. **사용자 승인 및 룰 덮어쓰기**:
   - 사용자가 새 구조를 승인할 경우, 파일 편집 도구를 사용하여 `07_Johnny_Decimal_Rule.md` 파일의 기존 분류 내용을 새 디자인으로 덮어씁니다.
