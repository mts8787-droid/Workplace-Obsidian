import os
import re

inbox_dir = r"00. Inbox"

taxonomy_map = {
    # File 4: GMC/MCC/NC
    "d2c마케팅": "model/d2c",
    "gmc": "topic/tech/gmc",
    "mcc": "topic/tech/mcc",
    "mediagovernance": "topic/data/governance",
    "namingconvention": "topic/data/governance",
    "교육자료": "type/playbook",
    
    # File 5 & 6: 스윗/미국법인/MaMAS
    "mamas": "program/mamas",
    "swit": "topic/tech/swit",
    "tier3": "topic/tech/llm",
    "모델자가진화": "topic/tech/agent",
    "에이전틱mmm": "topic/tech/agent",
    "미국법인": "market/na/us",
    "scm": "topic/biz/scm",
    "미팅": "type/meeting",
    "스윗": "topic/tech/swit",
    "시맨틱레이어": "topic/tech/semantic-layer",
    
    # File 7: 크리테오/오픈AI
    "chatgpt": "topic/tech/llm",
    "광고": "topic/marketing/performance",
    "크리테오": "ad/criteo",
    "협의": "type/meeting",
    "ai커머스": "topic/tech/llm",
    "openai": "topic/tech/llm",
    "광고패키지": "topic/marketing/performance",
    
    # File 3: 마마스 도입조건
    "neuralworldmodel": "topic/tech/agent",
    "협상": "deal/negotiation",
    "poc": "topic/strategy/poc",
    "라이선스": "topic/biz/contract"
}

# Add standard topics to avoid duplicate tmp prefixes if they had tmp/old_ already
def clean_tag(t):
    t = t.lower()
    if t.startswith("tmp/old_"): t = t.replace("tmp/old_", "")
    return t

def map_tag(tag):
    tag = tag.strip(' "\'')
    cleaned = clean_tag(tag)
    
    if cleaned in taxonomy_map:
        return taxonomy_map[cleaned]
    
    # If it's already a valid taxonomy namespace, leave it
    if "/" in tag and not tag.startswith("tmp/"):
        return tag
        
    return tag

for f in os.listdir(inbox_dir):
    if not f.endswith('.md'): continue
    filepath = os.path.join(inbox_dir, f)
    
    with open(filepath, 'r', encoding='utf-8-sig') as file:
        content = file.read()
        
    match = re.match(r'^---\r?\n(.*?)\r?\n---\r?\n(.*)', content, re.DOTALL)
    if not match: continue
    
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
            if line.lstrip().startswith('-'):
                tag_val = line.split('-', 1)[1].strip()
                mapped = map_tag(tag_val)
                # handle multiple tags mapping to the same
                new_tags.add(mapped)
            elif not line.startswith(' ') and not line.startswith('-'):
                for t in sorted(new_tags):
                    new_lines.append(f'  - "{t}"')
                new_tags = set()
                in_tags = False
                new_lines.append(line)
        else:
            new_lines.append(line)
            
    if in_tags and new_tags:
        for t in sorted(new_tags):
            new_lines.append(f'  - "{t}"')
            
    new_frontmatter = '\n'.join(new_lines)
    
    if new_frontmatter != frontmatter:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(f"---\n{new_frontmatter}\n---\n{body}")
        print(f"Updated: {f}")
