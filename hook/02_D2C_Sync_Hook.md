# 🚫 HOOK: D2C 사본 동기화 강제 규정 (D2C Sync Hook)
**Precedence: 0 (절대적 준수 사항)**

## 1. 목적 (Purpose)
D2C 팀원들과 에이전트 환경(스킬/룰/훅)을 안전하게 공유하기 위해, 메인 통제 허브인 `.agent/` 폴더의 모든 변경 사항을 즉시 사본 폴더인 `.agent -D2C/` 로 동기화(Mirroring)합니다. 단, 사용자 개인의 폴더 구조 룰이 담긴 특정 파일은 덮어쓰지 않고 보호합니다.

## 2. 금지 및 강제 조항 (Absolute Rules)
1. **변경 시 즉각 동기화**: 에이전트는 `/harness` 명령어나 자체적인 판단으로 `.agent/` 하위의 파일(스킬, 룰, 훅 등)을 생성, 수정, 삭제한 직후에 **반드시 아래의 Robocopy 명령어를 터미널에서 실행하여 사본을 갱신**해야 합니다. (동기화를 빼먹는 행위 엄격히 금지)
2. **특정 룰 파일 덮어쓰기 금지**: 개인화된 폴더 트리 룰인 `01_Directory_Structure_Rule.md` 파일은 절대 D2C 사본 쪽으로 덮어쓰거나 동기화하면 안 됩니다. (아래 명령어의 `/XF` 옵션 필수 유지)

## 3. 실행 명령어 (Execution Command)
동기화가 필요할 때마다 터미널(PowerShell)에서 아래 명령어를 정확히 실행하십시오:
```powershell
robocopy "c:\Users\ts.moon\OneDrive - LG전자\obsidian\.agent" "c:\Users\ts.moon\OneDrive - LG전자\obsidian\.agent -D2C" /MIR /XF "01_Directory_Structure_Rule.md"
```
(Robocopy의 특성상 정상적으로 완료되어도 exit code가 1~3으로 반환될 수 있으므로 에러로 간주하지 마십시오.)
