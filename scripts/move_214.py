import os, re, shutil

folder = r"20. 산출물 (Outputs)\21. 정기보고\214. 해영본 KPI 정기 보고"

# New sub-directories to map to
dest_map = {
    '10. 프로젝트 (Projects)\\11. GEO\\114. WBS 및 진행현황': [],
    '20. 산출물 (Outputs)\\23. 전략회의': [],
    '30. 참고자료 (References)\\31. 가이드': [],
    '30. 참고자료 (References)\\32. 매체 제안서': [],
    '20. 산출물 (Outputs)\\21. 정기보고\\214. 해영본 KPI 정기 보고': [] # Keep remaining here
}

for f in os.listdir(folder):
    if not f.endswith('.md'): continue
    filepath = os.path.join(folder, f)
    with open(filepath, encoding='utf-8-sig', errors='ignore') as file:
        content = file.read()
    
    match = re.match(r'^---\r?\n(.*?)\r?\n---', content, re.DOTALL)
    tags_str = ""
    if match:
        tags = []
        for line in match.group(1).splitlines():
            if line.strip().startswith('- '):
                tags.append(line.split('-', 1)[1].strip(' "\''))
        tags_str = str(tags).lower()
        
    name_lower = f.lower()
    
    # 1. 가이드라인
    if '가이드' in name_lower or 'guide' in name_lower or '매뉴얼' in name_lower or 'manual' in name_lower:
        dest_map['30. 참고자료 (References)\\31. 가이드'].append(f)
    # 2. 제안서 및 계약 (외부 매체)
    elif '제안' in name_lower or 'proposal' in name_lower or '견적' in name_lower or 'doc/proposal' in tags_str:
        dest_map['30. 참고자료 (References)\\32. 매체 제안서'].append(f)
    # 3. 전략/회의/보고 (20. 산출물\23. 전략회의) -> prior over projects
    elif '회의록' in name_lower or '미팅' in name_lower or 'type/meeting' in tags_str or '전략' in name_lower or '결과보고' in name_lower or '현황분석' in name_lower or 'doc/strategy' in tags_str or '선정' in name_lower or '혁신' in name_lower:
        dest_map['20. 산출물 (Outputs)\\23. 전략회의'].append(f)
    # 4. WBS / 진행현황 / 운영안 (10. 프로젝트)
    elif 'wbs' in name_lower or '진행현황' in name_lower or 'roadmap' in name_lower or '운영안' in name_lower or '수행계획' in name_lower or '대응 현황' in name_lower or '과제' in name_lower:
        dest_map['10. 프로젝트 (Projects)\\11. GEO\\114. WBS 및 진행현황'].append(f)
    else:
        # Remaining items keep in original folder
        dest_map['20. 산출물 (Outputs)\\21. 정기보고\\214. 해영본 KPI 정기 보고'].append(f)

for dest, files in dest_map.items():
    if not files: continue
    os.makedirs(dest, exist_ok=True)
    for f in files:
        src = os.path.join(folder, f)
        if os.path.exists(src) and dest != folder:
            shutil.move(src, os.path.join(dest, f))
            print(f"Moved: {f} -> {dest}")
