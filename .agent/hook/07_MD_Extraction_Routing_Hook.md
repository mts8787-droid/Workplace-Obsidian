---
title: "07_MD_Extraction_Routing_Hook"
description: "모든 /md 계열 변환 스킬의 결과물을 무조건 00. Inbox 폴더로 강제 라우팅하는 규칙"
category: "hook"
tags:
  - hook
  - routing
  - inbox
---

# 🚫 Hook: MD 변환 결과물 강제 수집 (MD Extraction Routing Hook)
**Precedence: 0 (절대적 강제 사항)**

## 1. 목적
`/md` 계열의 스킬(HTML, PPT, Excel 등 원시 문서의 마크다운 변환)을 수행한 뒤, 생성된 결과물이 작업 폴더나 임시 폴더(`암묵지 변환 결과` 등)에 방치되어 볼트의 구조가 파편화되는 것을 원천 차단합니다. 

## 2. 절대 금지 및 강제 사항 (Don'ts & Musts)

1. **결과물 방치 금지**
   - 어떠한 상황에서도 `/md`, `/md-html`, `/md-ppt-text`, `/md-ppt-render`, `/md-xlsx` 스킬이 생성한 마크다운 파일(`.md`)을 원래 있던 소스 폴더나 임시 추출 폴더에 그대로 남겨두어서는 안 됩니다.

2. **강제 라우팅 (Inbox Routing)**
   - 모든 변환 작업이 완료된 마크다운 파일은 생성 즉시 **`00. Inbox`** (수집함) 폴더로 무조건 저장되거나 이동되어야 합니다.
   - 이는 후속 정규화 작업(`/taggging`, `/title`, `/route`)이 파이프라인으로 매끄럽게 이어지기 위한 절대적 전제 조건입니다.

3. **자동 파이프라인 연계**
   - 파일이 `00. Inbox`로 이동한 직후, 시스템은 파일에 대한 누락 없이 즉각적으로 메타데이터 부여 및 제목 정제 스킬을 가동해야 합니다. 
