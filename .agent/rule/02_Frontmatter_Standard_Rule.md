# 📝 Rule: 프론트매터 표준 및 문법 (Frontmatter Standard Rule)
**Precedence: 1**

## 1. YAML Frontmatter 필수 속성 16개
모든 문서는 최상단에 반드시 아래의 16개 속성을 포함해야 합니다. (값을 모를 경우 `null` 또는 `""` 처리)
`title`, `description`, `author`, `author_email`, `team`, `access_level`, `category`, `tags`, `domain`, `status`, `created_at`, `updated_at`, `source_filename`, `version`, `converter_version`, `quality_score`

## 2. 엄격한 문법 규칙 (Syntax Rules)

1. **들여쓰기 (Indentation)**
   - YAML 내의 모든 리스트(예: `tags` 하위 항목)는 반드시 **2-space (스페이스 2칸)** 들여쓰기를 사용합니다. (Tab 사용 절대 금지)
2. **양방향 링크 따옴표 (Wikilink Quoting)**
   - YAML Frontmatter 내부에서 옵시디언의 양방향 링크(`[[ ]]`)를 사용할 경우, 파싱 에러를 방지하기 위해 **반드시 큰따옴표(`" "`)로 전체를 감싸야 합니다.**
   - ❌ 잘못된 예: `source_filename: [[원본 회의록]]`
   - ✅ 올바른 예: `source_filename: "[[원본 회의록]]"`
3. **배열 포맷 (Array Format)**
   - `tags`는 하위 `-` 리스트 형태로 세로 작성하는 것을 표준으로 합니다.
