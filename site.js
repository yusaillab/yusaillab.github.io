/* SAIL 공통 스크립트: 메뉴, 공지 목록, 공지 상세, 구성원 목록 */
(function () {
  var CAT = { seminar: "세미나", event: "행사", recruit: "모집", news: "소식" };

  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  function fmtDate(iso) { return iso.replace(/-/g, "."); }
  function isNew(iso) {
    var d = new Date(iso), diff = (Date.now() - d.getTime()) / 86400000;
    return diff >= 0 && diff <= 14;
  }

  /* 모바일 메뉴 */
  var toggle = document.querySelector(".nav-toggle"), nav = document.querySelector(".nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  /* 공지 목록 */
  function noticeItem(n) {
    return '<li><a href="notice-detail.html?id=' + encodeURIComponent(n.id) + '">' +
      '<span class="cat ' + esc(n.category) + '">' + esc(CAT[n.category] || n.category) + '</span>' +
      '<span class="title">' + esc(n.title) + (isNew(n.date) ? '<span class="new">NEW</span>' : "") + '</span>' +
      '<time class="date" datetime="' + esc(n.date) + '">' + fmtDate(n.date) + '</time></a></li>';
  }
  function renderNotices(listEl, items) {
    if (!items.length) { listEl.innerHTML = '<li class="empty">아직 올라온 공지가 없습니다.</li>'; return; }
    listEl.innerHTML = items.map(noticeItem).join("");
  }
  var list = document.querySelector("[data-notices]");
  if (list && window.SAIL_NOTICES) {
    var all = window.SAIL_NOTICES.slice().sort(function (a, b) { return a.date < b.date ? 1 : -1; });
    var limit = parseInt(list.getAttribute("data-limit"), 10);
    if (limit) all = all.slice(0, limit);
    renderNotices(list, all);
    var filter = document.querySelector("[data-filter]");
    if (filter) {
      filter.addEventListener("click", function (e) {
        var b = e.target.closest("button"); if (!b) return;
        filter.querySelectorAll("button").forEach(function (x) { x.setAttribute("aria-pressed", "false"); });
        b.setAttribute("aria-pressed", "true");
        var c = b.getAttribute("data-cat");
        renderNotices(list, c === "all" ? all : all.filter(function (n) { return n.category === c; }));
      });
    }
  }

  /* 홈 소식 카드 */
  var cards = document.querySelector("[data-news-cards]");
  if (cards && window.SAIL_NOTICES) {
    var items = window.SAIL_NOTICES.slice().sort(function (a, b) { return a.date < b.date ? 1 : -1; });
    items = items.slice(0, parseInt(cards.getAttribute("data-limit"), 10) || 4);
    cards.innerHTML = items.map(function (n) {
      return '<li><a href="notice-detail.html?id=' + encodeURIComponent(n.id) + '">' +
        '<div class="card-meta"><span class="tag ' + esc(n.category) + '">' + esc(CAT[n.category] || n.category) + '</span>' +
        '<time datetime="' + esc(n.date) + '">' + fmtDate(n.date) + '</time></div>' +
        '<h3>' + esc(n.title) + '</h3>' +
        '<span class="read">자세히 보기</span></a></li>';
    }).join("");
  }

  /* 공지 상세 */
  var detail = document.querySelector("[data-notice-detail]");
  if (detail && window.SAIL_NOTICES) {
    var id = new URLSearchParams(location.search).get("id");
    var n = window.SAIL_NOTICES.filter(function (x) { return x.id === id; })[0];
    if (!n) {
      detail.innerHTML = '<p class="empty">해당 공지를 찾을 수 없습니다. <a href="notice.html">공지사항 목록으로</a></p>';
    } else {
      document.title = n.title + " — SAIL 영남대학교 AI안전연구소";
      var info = Object.keys(n.info || {}).map(function (k) {
        return "<dt>" + esc(k) + "</dt><dd>" + esc(n.info[k]) + "</dd>";
      }).join("");
      detail.innerHTML =
        '<p class="meta">' + esc(CAT[n.category] || n.category) + " · " + fmtDate(n.date) + "</p>" +
        "<h1>" + esc(n.title) + "</h1>" +
        (info ? '<dl class="info">' + info + "</dl>" : "") +
        '<div class="body">' + esc(n.body) + "</div>" +
        '<a class="back" href="notice.html">← 공지사항 목록</a>';
    }
  }

  /* 구성원 */
  var silhouette = '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><circle cx="32" cy="24" r="11"/><path d="M12 56c2-11 10-17 20-17s18 6 20 17"/></svg>';
  function memberCard(m) {
    var links = Object.keys(m.links || {}).map(function (k) {
      return '<a href="' + esc(m.links[k]) + '">' + esc(k) + "</a>";
    }).join("");
    var photo = m.photo ? '<img src="' + esc(m.photo) + '" alt="' + esc(m.name) + '">' : silhouette;
    return '<li class="member' + (m.feature ? " feature" : "") + '">' +
      '<div class="photo">' + photo + "</div>" +
      '<div class="text"><h4>' + esc(m.name) + (m.en ? "<small>" + esc(m.en) + "</small>" : "") + "</h4>" +
      '<div class="role">' + esc(m.role) + "</div>" +
      (m.about ? '<p class="about">' + esc(m.about) + "</p>" : "") +
      (links ? '<div class="links">' + links + "</div>" : "") + "</div></li>";
  }
  var mroot = document.querySelector("[data-members]");
  if (mroot && window.SAIL_MEMBERS) {
    mroot.innerHTML = window.SAIL_MEMBERS.map(function (g) {
      return '<section class="member-group"><h3>' + esc(g.group) + '</h3><ul class="members">' +
        g.members.map(memberCard).join("") + "</ul></section>";
    }).join("");
  }
})();
