/* 홈 배너의 입자 물결 애니메이션 (파도 위를 항해하는 느낌) */
(function () {
  var c = document.getElementById("sea"); if (!c) return;
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var ctx = c.getContext("2d"), W, H, dpr, t = 0, raf;
  var COLS = 110, ROWS = 42;

  function resize() {
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    W = c.clientWidth; H = c.clientHeight;
    c.width = W * dpr; c.height = H * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }
  function draw() {
    ctx.clearRect(0, 0, W, H);
    var horizon = H * 0.5, cols = Math.round(COLS * Math.max(0.5, W / 1400));
    for (var r = 0; r < ROWS; r++) {
      var z = r / (ROWS - 1);                 // 0 = 먼 곳, 1 = 가까운 곳
      var depth = 0.25 + z * z * 0.75;
      var y0 = horizon + Math.pow(z, 1.6) * (H - horizon) * 1.05;
      for (var i = 0; i <= cols; i++) {
        var u = i / cols;
        var x = W * 0.5 + (u - 0.5) * W * (0.6 + depth * 1.2);
        var wave = Math.sin(u * 9 + t * 0.9 + z * 4) * 14 * depth
                 + Math.sin(u * 3.3 - t * 0.6 + z * 2) * 24 * depth
                 + Math.cos((u + z) * 14 + t * 1.3) * 7 * depth;
        var y = y0 + wave;
        var a = (0.18 + depth * 0.7) * (1 - Math.abs(u - 0.5) * 1.1);
        if (a <= 0) continue;
        var size = 0.6 + depth * 1.6;
        ctx.fillStyle = "rgba(" + (z > 0.55 ? "110,150,200" : "96,132,173") + "," + a.toFixed(3) + ")";
        ctx.beginPath(); ctx.arc(x, y, size, 0, 6.283); ctx.fill();
      }
    }
    if (!reduce) { t += 0.012; raf = requestAnimationFrame(draw); }
  }
  resize(); window.addEventListener("resize", function () { resize(); if (reduce) draw(); });
  draw();
  document.addEventListener("visibilitychange", function () {
    if (document.hidden) cancelAnimationFrame(raf); else if (!reduce) draw();
  });
})();
