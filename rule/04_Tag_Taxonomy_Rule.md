# 📖 Rule: 태그 택소노미 (Tag Taxonomy Rule)
**Precedence: 2**

**대상**: LG전자 해외사업부 — 가전 (TV·모니터·오디오·냉장고·세탁기·식기세척기·에어컨·공기청정기·가습기·제습기)
**모든 분류를 중첩 태그로 표현한다. 네임스페이스(`#type`, `#market`…)가 분류 축, 그 아래가 값이다.**

---
## 1. 설계 원칙
- `/`로 중첩, 모든 세그먼트는 소문자 `kebab-case`. 표기는 하나로 통일한다.
- 상위 태그로 묶음 검색이 된다 — `#market/eu` 하나로 EU 전체, `#product/air` 하나로 공조 전체가 잡힌다 (Obsidian은 중첩 태그를 계층으로 인식).
- 한 노트에 축마다 하나씩 단다 (type 1개, status 1개…). 단, 시장·제품처럼 복수가 맞으면 여러 개 가능.
- 고유 개체(특정 거래처·인물·제품 모델)는 태그가 아니라 **위키링크**(`[[ ]]`)로 연결한다. 태그는 "분류", 링크는 "개체".
- 새 값은 이 문서에 등록한 뒤 사용한다. (택소노미 드리프트 방지)

---
## 2. 네임스페이스 한눈에
| 네임스페이스 | 분류 축 | 예시 |
|---|---|---|
| `#type/` | 노트 종류 | `#type/campaign` |
| `#status/` | 진행 상태 | `#status/active` |
| `#model/` | 거래 형태 (B2B/B2C/D2C) | `#model/d2c` |
| `#market/` | 시장 (권역/국가) | `#market/eu/de` |
| `#product/` | 제품 (기능군/제품군) | `#product/air/air-purifier` |
| `#channel/` | 채널 (판매/마케팅) | `#channel/sales/amazon` |
| `#funnel/` | 퍼널 단계 | `#funnel/conversion` |
| `#deal/` | 거래 단계 | `#deal/negotiation` |
| `#priority/` | 우선순위 | `#priority/high` |
| `#ad/` | 광고 상품 | `#ad/google/pmax` |
| `#program/` | 업무·프로그램 | `#program/member-day` |
| `#doc/` | 보고·문서 성격 | `#doc/strategy` |
| `#period/` | 보고 주기 | `#period/monthly` |
| `#report-to/` | 보고 대상 | `#report-to/ceo` |
| `#topic/` | (통합) 업무 주제 및 기술 | `#topic/seo/geo` |

---
## 3. 세부 네임스페이스 사전

### 1) `#type/` — 노트 종류
```text
#type/account        거래처 (유통사·양판점·바이어)
#type/contact        인물
#type/deal           영업 건 / 파이프라인
#type/campaign       마케팅 캠페인
#type/content        콘텐츠 자산
#type/product        제품 / 모델 / 라인업
#type/research       시장·국가 리서치
#type/competitor     경쟁사 분석
#type/channel        채널 운영 노트
#type/meeting        회의록
#type/playbook       SOP·프로세스
#type/report         성과 분석·리포트
#type/idea           아이디어·메모
#type/moc            허브·인덱스
```

### 2) `#status/` — 진행 상태
```text
#status/inbox        미분류 수집
#status/draft        작성 중
#status/active       진행 중
#status/on-hold      보류
#status/done         완료
#status/archived     보관
#status/evergreen    상시 참조
```

### 3) `#model/` — 거래 형태
```text
#model/d2c           자사몰 직접 판매 (LG.com)
#model/b2c           일반 소비자 (마켓플레이스·양판점 경유)
#model/b2b           기업·바이어 대상
#model/b2b2c         유통사·양판점 거쳐 소비자 도달
#model/b2b-project   프로젝트성 대량 납품 (호텔·건설·기업)
```

### 4) `#market/` — 시장 (권역/국가 중첩)
*권역만 달아도 되고, 국가까지 좁혀도 된다.*
```text
#market/kr                      본사·국내
#market/na/us    #market/na/ca  북미
#market/eu/de  #market/eu/fr  #market/eu/uk  #market/eu/es  #market/eu/nl  유럽
#market/latam/br  #market/latam/mx  #market/latam/pe  #market/latam/cl     중남미
#market/mena/ae   #market/mena/sa                                          중동
#market/cis/ru                                                             러시아·CIS
#market/in                                                                 인도
#market/sea/id  #market/sea/th  #market/sea/vn  #market/sea/sg             동남아
#market/jp   #market/cn                                                    일본·중국
#market/oceania/au                                                         오세아니아
#market/global                                                             전 지역 공통
```

### 5) `#product/` — 제품 (기능군/제품군 중첩)
*중간 세그먼트가 기능군.*
```text
#product/he/tv      #product/he/monitor   #product/he/audio      홈엔터테인먼트
#product/living/refrigerator  #product/living/washer  #product/living/dishwasher  리빙가전
#product/air/air-conditioner  #product/air/air-purifier  #product/air/humidifier  #product/air/dehumidifier  공조
```

### 6) `#channel/` — 채널 (판매/마케팅 분리)
```text
# 판매 채널
#channel/sales/lg-com               자사몰
#channel/sales/amazon               아마존
#channel/sales/local-marketplace    현지 마켓플레이스
#channel/sales/electronics-retailer 가전 양판점
#channel/sales/distributor          유통사·총판
#channel/sales/dealer               대리점
#channel/sales/b2b-project          B2B 프로젝트
#channel/sales/offline-retail       오프라인 매장

# 마케팅 채널
#channel/mkt/seo                    검색 최적화
#channel/mkt/paid-search            검색광고
#channel/mkt/paid-social            유료 소셜
#channel/mkt/organic-social         오가닉 소셜
#channel/mkt/email                  이메일
#channel/mkt/crm                    자사 채널(앱푸시·문자)
#channel/mkt/influencer             인플루언서
#channel/mkt/affiliate              제휴
#channel/mkt/marketplace-ads        마켓플레이스 광고
#channel/mkt/pr                     홍보
#channel/mkt/content                콘텐츠 마케팅
#channel/mkt/event                  박람회·전시회
```

### 7) `#funnel/` — 퍼널 단계
```text
#funnel/awareness  #funnel/consideration  #funnel/conversion
#funnel/retention  #funnel/advocacy
```

### 8) `#deal/` — 거래 단계 (영업 건 전용)
```text
#deal/lead          발굴
#deal/qualified     검증
#deal/sample        샘플·데모 발송
#deal/quote         견적·조건 협의
#deal/negotiation   계약 협상
#deal/won           수주
#deal/lost          실패
```

### 9) `#priority/` — 우선순위
```text
#priority/high   #priority/medium   #priority/low
```

### 10) `#ad/` — 광고 상품 (플랫폼/상품)
```text
#ad/google/pmax        Google Performance Max
#ad/google/search      검색 광고
#ad/google/shopping    쇼핑 광고(PLA)
#ad/google/demand-gen  Demand Gen
#ad/google/youtube     유튜브
#ad/meta/asc           Advantage+ Shopping
#ad/meta/awareness     인지 캠페인
#ad/meta/retargeting   리타게팅
#ad/criteo             Criteo
#ad/tiktok             TikTok Ads
#ad/amazon             Amazon Ads
#ad/dv360              Display & Video 360
#ad/rtbhouse           RTB House
```

### 11) `#program/` — 업무·프로그램
```text
#program/monthly-lg    먼슬리 LG
#program/member-day    멤버데이
#program/tiktok-shop   틱톡샵 운영
#program/black-friday  블랙프라이데이
#program/npi           신제품 도입 (New Product Introduction)
#program/clearance     재고 소진
#program/trade-show    박람회(IFA·CES 등)
```

### 12) `#doc/` — 보고·문서 성격
*`#type/report` 또는 `#type/meeting` 노트에 무슨 문서인지를 붙인다.*
```text
#doc/strategy      전략보고
#doc/performance   성과보고 (실적)
#doc/plan          계획·로드맵
#doc/minutes       회의록
#doc/proposal      품의·제안
```
> 회의록은 `#type/meeting` + `#doc/minutes`로 단다. 보고 문서 성격이 중심이면 `#doc/`를 기준으로 검색한다.

### 13) `#period/` — 보고 주기
```text
#period/daily      일일
#period/weekly     주간
#period/monthly    월간
#period/quarterly  분기
#period/half       반기
#period/annual     연간
```

### 14) `#report-to/` — 보고 대상 (수신자)
```text
#report-to/ceo          CEO
#report-to/div-head     본부장
#report-to/group-head   그룹장
#report-to/office-head  실장
```
> 상위 보고일수록 묶음 점검이 쉽다 — `#report-to/ceo`로 CEO 보고 라인 전체를 한 번에 모은다.

### 15) `#topic/` — 핵심 키워드 사전 (기존 사전 통합)
*특정 기능군, 마케팅 용어, 기술 키워드는 아래 `topic` 네임스페이스 산하로 관리한다.*
```text
#topic/seo/geo                 GEO, 검색가시성 등
#topic/seo/aeo                 AEO
#topic/seo/tech                기술SEO
#topic/marketing/performance   퍼포먼스마케팅, 그로스해킹, ROAS, 전환율(CVR)
#topic/marketing/data          데이터분석, GA4, A_B_Test
#topic/marketing/social        소셜미디어, 콘텐츠마케팅, 이메일마케팅
#topic/brand/lg                LG전자, LG_COM
#topic/brand/competitor        경쟁사 분석
#topic/strategy/poc            PoC, 경쟁PT
#topic/tech/llm                ChatGPT, Gemini 등 LLM 전반
#topic/tech/akamai             Akamai, EdgeWorker, CDN
#topic/tech/schema             Schema, VideoObject
#topic/tech/rag                RAG
#topic/tech/api                API
```

---
## 4. 노트 태그 예시
**독일 멤버데이 시즌, 공기청정기 신제품 Meta 캠페인 노트:**
```text
#type/campaign #status/active #model/b2c #market/eu/de
#product/air/air-purifier #channel/mkt/paid-social #funnel/awareness
#ad/meta/asc #program/npi #priority/high
```
> 이 캠페인이 미는 특정 제품 모델이나 담당자는 본문에서 `[[OLED... ]]`, `[[홍길동]]` 위키링크로 연결한다.

**CEO에게 올리는 미주 월간 성과보고 노트:**
```text
#type/report #doc/performance #period/monthly #report-to/ceo
#market/na/us #status/done
```

---
## 5. 검색 예시 (Obsidian 기본 검색)
```text
독일 진행 중 캠페인       →  tag:#type/campaign tag:#status/active tag:#market/eu/de
공조 제품 전체            →  tag:#product/air
EU 거래처 전체            →  tag:#type/account tag:#market/eu
멤버데이 관련 모든 노트    →  tag:#program/member-day
진행 중 B2B 협상          →  tag:#deal/negotiation tag:#model/b2b
CEO 보고 라인 전체        →  tag:#report-to/ceo
이번 분기 전략보고        →  tag:#doc/strategy tag:#period/quarterly
```

---
## 6. 국가별 대표 리테일 (account 시드)
`#type/account` 노트를 만들 때 시작점. 로컬 기반 대표 가전·전자 리테일러 2곳씩.

| 시장 태그 | 국가 | 대표 ① | 대표 ② |
|---|---|---|---|
| `#market/na/us` | 미국 | Best Buy | Costco (백색가전은 Home Depot·Lowe's) |
| `#market/na/ca` | 캐나다 | Best Buy Canada | The Brick |
| `#market/eu/de` | 독일 | MediaMarkt | Otto (Saturn은 MediaMarkt 자매 브랜드) |
| `#market/eu/fr` | 프랑스 | Fnac-Darty | Boulanger |
| `#market/eu/uk` | 영국 | Currys | AO.com (+ John Lewis) |
| `#market/eu/es` | 스페인 | El Corte Inglés | MediaMarkt (로컬 온라인은 PcComponentes) |
| `#market/eu/nl` | 네덜란드 | Coolblue | Bol.com |
| `#market/latam/br` | 브라질 | Magazine Luiza | Casas Bahia |
| `#market/latam/mx` | 멕시코 | Liverpool | Coppel |
| `#market/latam/pe` | 페루 | Hiraoka | Saga Falabella |
| `#market/latam/cl` | 칠레 | Falabella | Ripley |
| `#market/mena/ae` | UAE | Sharaf DG | Jumbo Electronics |
| `#market/mena/sa` | 사우디 | eXtra | Jarir |
| `#market/cis/ru` | 러시아 | M.Video | DNS |
| `#market/in` | 인도 | Croma | Reliance Digital |
| `#market/sea/id` | 인도네시아 | Electronic City | Erafone |
| `#market/sea/th` | 태국 | Power Buy | BaNANA |
| `#market/sea/vn` | 베트남 | Điện Máy Xanh | Nguyễn Kim |
| `#market/sea/sg` | 싱가포르 | Courts | Harvey Norman |
| `#market/jp` | 일본 | Yodobashi Camera | Bic Camera (최대 체인 Yamada Denki) |
| `#market/cn` | 중국 | JD.com | Suning |
| `#market/oceania/au` | 호주 | JB Hi-Fi | Harvey Norman |

---
## 7. 운영 규칙
1. 태그는 위 정의된 네임스페이스만 쓴다. 일회성은 `#tmp/...`로 격리하고 주기적으로 비운다.
2. 새 값 추가 시 이 문서에 먼저 등록 — 택소노미 드리프트 방지.
3. 고유 개체(거래처·인물·특정 모델)는 태그로 만들지 말고 위키링크로 연결한다.
4. 축마다 값 하나가 원칙. `#market`·`#product`만 복수 허용.
