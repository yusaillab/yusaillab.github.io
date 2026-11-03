# 페이지 생성 스크립트: 공통 머리글/바닥글을 붙여 HTML 파일을 만듭니다.
# 사용법: python3 build.py   (sail-site 폴더에서 실행)
import pathlib

ROOT = pathlib.Path(__file__).parent

NAV = [("index.html", "홈"), ("about.html", "소개"), ("research.html", "연구"),
       ("notice.html", "소식"), ("members.html", "구성원"), ("contact.html", "오시는 길")]

def header(current):
    links = "".join(
        f'<a href="{href}"{" aria-current=\"page\"" if href == current else ""}>{label}</a>'
        for href, label in NAV)
    return f'''<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="SAIL 영남대학교 AI안전연구소 홈">
      <img class="brand-mark" src="assets/logo.png" alt="SAIL">
      <span class="brand-text"><span>영남대학교 AI안전연구소</span></span>
    </a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="nav">메뉴</button>
    <nav class="nav" id="nav" aria-label="주 메뉴">{links}</nav>
  </div>
</header>'''

FOOTER = '''<footer class="site-footer">
  <div class="wrap">
    <div>
      <a class="brand" href="index.html"><img class="brand-mark" src="assets/logo.png" alt="SAIL"></a>
      <p>영남대학교 AI안전연구소<br>Safety AI Lab (SAIL), Yeungnam University</p>
      <p>(38541) 경상북도 경산시 대학로 280 영남대학교 사회과학관 508호<br>전화 053-810-0000 · sail@yu.ac.kr</p>
    </div>
    <div>
      <h4>바로가기</h4>
      <ul>
        <li><a href="about.html">소개</a></li>
        <li><a href="research.html">연구</a></li>
        <li><a href="notice.html">소식</a></li>
        <li><a href="members.html">구성원</a></li>
      </ul>
    </div>
    <div>
      <h4>관련 사이트</h4>
      <ul>
        <li><a href="https://www.yu.ac.kr" target="_blank" rel="noopener">영남대학교</a></li>
        <li><a href="https://www.aisi.re.kr" target="_blank" rel="noopener">인공지능안전연구소(AISI)</a></li>
        <li><a href="https://www.data.go.kr" target="_blank" rel="noopener">공공데이터포털</a></li>
      </ul>
    </div>
    <p class="copy">© 2026 Safety AI Lab, Yeungnam University. All rights reserved.</p>
  </div>
</footer>
<script src="assets/notices.js"></script>
<script src="assets/members.js"></script>
<script src="assets/site.js"></script>
<script src="assets/sea.js"></script>'''

def page(filename, title, body, desc="영남대학교 AI안전연구소(SAIL)는 AI를 활용한 공공안전과 조직 위험관리 연구를 선도합니다."):
    html = f'''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" type="image/png" href="assets/favicon.png">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
{header(filename)}
<main>
{body}
</main>
{FOOTER}
</body>
</html>
'''
    (ROOT / filename).write_text(html, encoding="utf-8")
    print("wrote", filename)

# ---------------------------------------------------------------- 홈
HOME = """<section class="hero">
  <canvas id="sea" aria-hidden="true"></canvas>
  <div class="hero-inner">
    <h1>Safety AI Lab</h1>
    <p class="tagline">AI로 먼저 읽는 위험, 더 안전한 사회</p>
    <p class="sub">영남대학교 AI안전연구소 · 공공안전과 조직 위험관리 AI 연구</p>
  </div>
  <a class="hero-down" href="#news" aria-label="아래로"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M5 8l7 7 7-7M5 3l7 7 7-7"/></svg></a>
</section>

<section class="section center" id="news">
  <div class="wrap">
    <h2 class="tick">최근 소식</h2>
    <a class="pill" href="notice.html">전체 보기</a>
    <ul class="news-cards" data-news-cards data-limit="4"></ul>
  </div>
</section>

<section class="section center tinted">
  <div class="wrap">
    <h2 class="tick">연구</h2>
    <ul class="research-circles">
      <li><a href="research.html#r1"><span class="circle"><svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M6 36 L16 24 L24 30 L34 16 L42 22"/><circle cx="34" cy="16" r="3" fill="currentColor" stroke="none"/></svg></span><h3>공공안전 위기 대응</h3><p>데이터로 위험을 예측하고<br>실시간으로 이상징후를 탐지합니다</p></a></li>
      <li><a href="research.html#r2"><span class="circle"><svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="8" y="14" width="32" height="26" rx="3"/><path d="M18 14 V10 a6 6 0 0 1 12 0 v4 M8 26 h32"/></svg></span><h3>조직 위험관리</h3><p>기업·공공기관의 보안 위협과<br>리스크에 AI로 대응합니다</p></a></li>
      <li><a href="research.html#r3"><span class="circle"><svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M24 6 v36 M8 16 h32 M8 16 l-5 12 h10 z M40 16 l-5 12 h10 z"/><path d="M16 40 h16"/></svg></span><h3>AI 윤리·거버넌스</h3><p>공정하고 투명한 AI,<br>신뢰할 수 있는 공공 데이터</p></a></li>
      <li><a href="research.html#r4"><span class="circle"><svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="24" cy="12" rx="14" ry="5"/><path d="M10 12 v24 c0 2.8 6.3 5 14 5 s14-2.2 14-5 V12 M10 24 c0 2.8 6.3 5 14 5 s14-2.2 14-5"/></svg></span><h3>공공 데이터 플랫폼</h3><p>공공 데이터와 AI를 잇고<br>시민과 함께 다스립니다</p></a></li>
    </ul>
  </div>
</section>

<section class="section center">
  <div class="wrap">
    <h2 class="tick">연구소 소개</h2>
    <div class="intro">
      <p>SAIL은 영남대학교 AI안전연구소입니다.<br>AI를 활용한 공공안전과 조직 위험관리 연구를 선도하는 것을 목표로 합니다.</p>
      <div class="intro-links">
        <a class="outline" href="about.html">비전·목표</a>
        <a class="outline" href="members.html">구성원</a>
        <a class="outline" href="contact.html">오시는 길</a>
      </div>
    </div>
  </div>
</section>"""

# ---------------------------------------------------------------- 소개
ABOUT = """<section class="page-head center"><div class="wrap">
  <h1 class="tick">연구소 소개</h1>
  <p>AI로 사회와 조직의 위험을 미리 읽고, 안전하게 대응하는 방법을 연구합니다.</p>
</div></section>

<section class="section center"><div class="wrap">
  <p class="vision">AI를 활용한 공공안전 및<br>조직 위험관리 연구의 선도</p>
  <ol class="goal-grid">
    <li><strong>위험 예측·대응 시스템</strong><span>공공 부문을 위한 AI 기반 시스템 개발</span></li>
    <li><strong>조직 위험관리 솔루션</strong><span>기업·공공기관의 위기 대응 AI 연구</span></li>
    <li><strong>위협 예측 알고리즘</strong><span>이상 행동과 사회적 위협을 데이터로 예측</span></li>
    <li><strong>AI 거버넌스 정책</strong><span>공공 데이터의 신뢰성과 윤리를 고려한 정책 연구</span></li>
  </ol>
</div></section>

<section class="section center tinted"><div class="wrap">
  <h2 class="tick">함께하는 기관</h2>
  <ul class="partner-row">
    <li><strong>정부·공공</strong><span>행정안전부, 경찰청, 과학기술정보통신부, 공공 데이터 기관</span></li>
    <li><strong>국제 협력</strong><span>해외 공공안전 연구소, 대학 연구기관, AI 연구센터</span></li>
    <li><strong>산학 협력</strong><span>공공안전·AI 위험관리 기업</span></li>
  </ul>
</div></section>

<section class="section center"><div class="wrap">
  <h2 class="tick">나아갈 길</h2>
  <ul class="road">
    <li><time>1–2년</time><span>국제 학술지 논문 게재, 연구 기반 구축</span></li>
    <li><time>3–5년</time><span>국제 논문 5편 이상, 국가 연구과제 수주</span></li>
    <li><time>5년 이후</time><span>AI 공공안전 모델 상용화, 글로벌 연구소로 도약</span></li>
  </ul>
</div></section>"""

# ---------------------------------------------------------------- 연구 분야
RESEARCH = '''<section class="page-head center"><div class="wrap">
  <h1 class="tick">연구 분야</h1>
  <p>위험을 예측하는 기술과, 그 기술을 믿고 쓸 수 있게 하는 기반을 함께 연구합니다.</p>
</div></section>

<section class="section"><div class="wrap">
  <div class="kv">
    <div>
      <h3 id="r1">AI 기반 공공안전 및 위기 대응</h3>
      <div class="prose">
        
        <ul>
          <li>머신러닝·딥러닝 기반 공공안전 위험 예측 모델 구축</li>
          <li>실시간 이상징후 탐지 및 긴급 대응 알고리즘 연구</li>
          <li>대규모 재난·사회적 위험 상황에서의 AI 활용 방안 연구</li>
        </ul>
      </div>
    </div>
    <div>
      <h3 id="r2">AI를 활용한 조직 위험관리 및 대응</h3>
      <div class="prose">
        
        <ul>
          <li>조직 내 보안 위협·비즈니스 리스크 예측 모델 개발</li>
          <li>기업·공공기관을 위한 AI 기반 위험 대응 시스템 연구</li>
          <li>정책·법적 관점에서 본 조직 내 AI 활용 방안 연구</li>
        </ul>
      </div>
    </div>
    <div>
      <h3 id="r3">AI 윤리 및 공공 데이터 거버넌스</h3>
      <div class="prose">
        
        <ul>
          <li>AI 위험 예측 모델의 공정성·투명성 분석</li>
          <li>공공 데이터 보호 및 AI 윤리 규제 정책 연구</li>
          <li>공공·민간 부문에서 활용 가능한 AI 기반 위험관리 프레임워크 개발</li>
        </ul>
      </div>
    </div>
    <div>
      <h3 id="r4">공공 데이터 플랫폼과 AI의 융합</h3>
      <div class="prose">
        
        <ul>
          <li>정부·공공기관 데이터 플랫폼과 AI 기술의 연계 분석</li>
          <li>AI를 통한 공공 데이터 플랫폼의 효율성·신뢰성 강화 방안 연구</li>
          <li>시민 참여형 데이터 거버넌스와 공공 데이터 개방·활용 전략 연구</li>
        </ul>
      </div>
    </div>
  </div>
</div></section>'''

# ---------------------------------------------------------------- 공지
NOTICE = '''<section class="page-head center"><div class="wrap">
  <h1 class="tick">소식</h1>
  <p>세미나, 행사, 모집 소식을 안내합니다.</p>
</div></section>
<section class="section" style="padding-top:0"><div class="wrap">
  <div class="filter" data-filter role="group" aria-label="분류">
    <button data-cat="all" aria-pressed="true">전체</button>
    <button data-cat="seminar" aria-pressed="false">세미나</button>
    <button data-cat="event" aria-pressed="false">행사</button>
    <button data-cat="recruit" aria-pressed="false">모집</button>
    <button data-cat="news" aria-pressed="false">소식</button>
  </div>
  <ul class="notice-list" data-notices></ul>
</div></section>'''

NOTICE_DETAIL = '''<section class="section"><div class="wrap">
  <article class="notice-detail" data-notice-detail></article>
</div></section>'''

# ---------------------------------------------------------------- 구성원
MEMBERS = '''<section class="page-head center"><div class="wrap">
  <h1 class="tick">구성원</h1>
  <p>경찰행정학과 오경석 교수를 중심으로 학부 연구생들이 함께 연구합니다.</p>
</div></section>
<section class="section" style="padding-top:0"><div class="wrap" data-members></div></section>'''

# ---------------------------------------------------------------- 문의
CONTACT = '''<section class="page-head center"><div class="wrap">
  <h1 class="tick">오시는 길</h1>
  <p>연구 협력, 세미나, 연구생 지원 문의를 환영합니다.</p>
</div></section>
<section class="section" style="padding-top:0"><div class="wrap">
  <div class="contact">
    <div>
      <dl>
        <dt>주소</dt><dd>(38541) 경상북도 경산시 대학로 280<br>영남대학교 사회과학관 508호</dd>
        <dt>전화</dt><dd>053-810-0000</dd>
        <dt>이메일</dt><dd><a href="mailto:sail@yu.ac.kr">sail@yu.ac.kr</a></dd>
        <dt>운영 시간</dt><dd>평일 09:00–18:00</dd>
      </dl>
      <p style="margin-top:28px"><a class="btn" href="mailto:sail@yu.ac.kr">이메일 보내기</a></p>
    </div>
    <div class="map">
      <iframe title="영남대학교 위치" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
        src="https://www.google.com/maps?q=%EC%98%81%EB%82%A8%EB%8C%80%ED%95%99%EA%B5%90&output=embed"></iframe>
    </div>
  </div>
</div></section>'''

page("index.html", "SAIL — 영남대학교 AI안전연구소", HOME)
page("about.html", "연구소 소개 — SAIL 영남대학교 AI안전연구소", ABOUT)
page("research.html", "연구 분야 — SAIL 영남대학교 AI안전연구소", RESEARCH)
page("notice.html", "공지사항 — SAIL 영남대학교 AI안전연구소", NOTICE)
page("notice-detail.html", "공지사항 — SAIL 영남대학교 AI안전연구소", NOTICE_DETAIL)
page("members.html", "구성원 — SAIL 영남대학교 AI안전연구소", MEMBERS)
page("contact.html", "오시는 길·문의 — SAIL 영남대학교 AI안전연구소", CONTACT)
