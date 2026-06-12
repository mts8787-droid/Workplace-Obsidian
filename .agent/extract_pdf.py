import pypdf
reader = pypdf.PdfReader('c:\\Users\\ts.moon\\OneDrive - LG전자\\obsidian\\암묵지 변환 대상\\MAaMAS Proposal.pdf')
text = ''.join([page.extract_text() for page in reader.pages])
with open('c:\\Users\\ts.moon\\OneDrive - LG전자\\obsidian\\.agent\\pdf_text_proposal.txt', 'w', encoding='utf-8') as f:
    f.write(text)
