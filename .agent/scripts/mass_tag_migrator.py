import os
import re

# Taxonomy mapping rules based on 04_Tag_Taxonomy_Rule.md
raw_taxonomy_map = {
    # Types
    "회의록": "type/meeting",
    "보고서": "type/report",
    "기획안": "type/report",
    "제안서": "type/report",
    "가이드": "type/playbook",
    "메모": "type/idea",
    "캠페인": "type/campaign",
    "전략": "doc/strategy",
    "성과": "doc/performance",
    
    # Status
    "draft": "status/draft",
    "in-progress": "status/active",
    "진행중": "status/active",
    "완료": "status/done",
    "보류": "status/on-hold",
    "converted": "status/done",
    "inbox": "status/inbox",
    
    # Market
    "글로벌": "market/global",
    "미국법인": "market/na/us",
    "미국": "market/na/us",
    "유럽": "market/eu",
    "유럽전략": "market/eu",
    "독일": "market/eu/de",
    "영국": "market/eu/uk",
    "스페인": "market/eu/es",
    
    # Channels & Ads
    "PMax": "ad/google/pmax",
    "Criteo": "ad/criteo",
    "크리테오": "ad/criteo",
    "DV360": "ad/dv360",
    
    # Topics
    "GEO": "topic/seo/geo",
    "SEO": "topic/seo/geo",
    "검색최적화": "topic/seo/geo",
    "AI가시성": "topic/seo/geo",
    "기술SEO": "topic/seo/tech",
    "AEO": "topic/seo/aeo",
    "퍼포먼스마케팅": "topic/marketing/performance",
    "마케팅": "topic/marketing/performance",
    "데이터분석": "topic/marketing/data",
    "LLM": "topic/tech/llm",
    "ChatGPT": "topic/tech/llm",
    "Gemini": "topic/tech/llm",
    "생성형AI": "topic/tech/llm",
    "RAG": "topic/tech/rag",
    "거버넌스": "topic/seo/geo",
    "LG전자": "topic/brand/lg",
    "POC": "topic/strategy/poc",
    
    # Programs & Models
    "D2C": "model/d2c",
    "B2B": "model/b2b",
    "B2C": "model/b2c",
    "MaMAS": "tmp/mamas",
    "에이전틱MMM": "tmp/mamas",
    "모델자가진화": "topic/tech/llm",
}

taxonomy_map = {k.lower(): v for k, v in raw_taxonomy_map.items()}

# Valid taxonomy namespaces defined in the rule
valid_namespaces = [
    "type/", "status/", "model/", "market/", "product/", 
    "channel/", "funnel/", "deal/", "priority/", "ad/", 
    "program/", "doc/", "period/", "report-to/", "topic/", "tmp/"
]

def is_valid_tag(tag):
    return any(tag.startswith(ns) for ns in valid_namespaces)

def map_tag(tag):
    tag = tag.strip(' "\'')
    if is_valid_tag(tag):
        return tag
    
    lower_tag = tag.lower()
    if lower_tag in taxonomy_map:
        return taxonomy_map[lower_tag]
    
    # Basic fallbacks for remaining flat tags
    if "seo" in lower_tag or "geo" in lower_tag: return f"topic/seo/{lower_tag}"
    if "마케팅" in tag: return f"topic/marketing/{lower_tag}"
    if "ai" in lower_tag: return f"topic/tech/llm"
    
    # Isolate unknowns into tmp/ as per rule: "일회성은 #tmp/...로 격리하고 주기적으로 비운다"
    return f"tmp/old_{tag}"

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8-sig') as f:
            content = f.read()
    except Exception as e:
        return False
        
    # extract YAML frontmatter
    match = re.match(r'^---\r?\n(.*?)\r?\n---\r?\n(.*)', content, re.DOTALL)
    if not match:
        return False
        
    frontmatter = match.group(1)
    body = match.group(2)
    
    lines = frontmatter.splitlines()
    new_lines = []
    in_tags = False
    new_tags = set()
    
    for line in lines:
        if line.startswith('tags:'):
            in_tags = True
            new_lines.append(line)
            continue
        
        if in_tags:
            # Match list item: - "tag" or - tag
            if line.lstrip().startswith('-'):
                tag_val = line.split('-', 1)[1].strip()
                mapped = map_tag(tag_val)
                new_tags.add(mapped)
            elif not line.startswith(' ') and not line.startswith('-'):
                # Exited tags block
                for t in sorted(new_tags):
                    new_lines.append(f'  - "{t}"')
                new_tags = set()
                in_tags = False
                new_lines.append(line)
        else:
            new_lines.append(line)
            
    # Handle case where tags block is at the very end of frontmatter
    if in_tags and new_tags:
        for t in sorted(new_tags):
            new_lines.append(f'  - "{t}"')
            
    new_frontmatter = '\n'.join(new_lines)
    
    if new_frontmatter == frontmatter:
        return False
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f"---\n{new_frontmatter}\n---\n{body}")
    return True

base_dirs = [f"{i}0" for i in range(1, 10)] # '10' ~ '90' prefixes
count = 0
for d in os.listdir('.'):
    if os.path.isdir(d) and d[:2] in base_dirs:
        for root, dirs, files in os.walk(d):
            for file in files:
                if file.endswith('.md'):
                    if process_file(os.path.join(root, file)):
                        count += 1

print(f"Migration Complete: Updated {count} files.")
