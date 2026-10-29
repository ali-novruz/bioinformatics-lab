/* PhiX174 decks: deck engine, a JS port of biolab.orfs.find_orfs, and interactive SVG charts.
   Decks provide markup and CSS; colours come from CSS custom properties
   (--ink, --mute, --grid, --bg, --f0/--f1/--f2 frames, --minus, --good, --bad, --accent). */
(function () {
  const D = window.PHIX;
  const NOTES = window.NOTES || {};
  const SEQ = D.sequence, L = SEQ.length;
  const NS = "http://www.w3.org/2000/svg";
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const css = (n) => getComputedStyle(document.documentElement).getPropertyValue(n).trim();
  function s(tag, attrs = {}, parent) { const e = document.createElementNS(NS, tag); for (const k in attrs) e.setAttribute(k, attrs[k]); if (parent) parent.appendChild(e); return e; }
  function svg(el, w, h) { el.innerHTML = ""; const r = s("svg", { viewBox: `0 0 ${w} ${h}`, role: "img" }, el); r.style.width = "100%"; r.style.height = "auto"; r.style.overflow = "visible"; return r; }
  function t(p, x, y, str, a = {}) { const e = s("text", { x, y, fill: "var(--ink)", "font-family": "var(--font-data)", "font-size": 13, ...a }, p); e.textContent = str; return e; }

  /* ---------- ORF finder: same rules as biolab.orfs.find_orfs ---------- */
  const COMP = { A: "T", C: "G", G: "C", T: "A" };
  const revcomp = (x) => x.split("").reverse().map((c) => COMP[c]).join("");
  const STOPS = new Set(["TAA", "TAG", "TGA"]);
  function findOrfs(seq, minAa = 30, circular = true) {
    const n = seq.length, out = [];
    for (const [strand, oriented] of [["+", seq], ["-", revcomp(seq)]]) {
      const ext = circular ? oriented + oriented : oriented;
      for (let start = 0; start < n; start++) {
        if (ext.substr(start, 3) !== "ATG") continue;
        const limit = circular ? start + n : n;
        for (let stop = start + 3; stop < limit - 2; stop += 3) {
          if (!STOPS.has(ext.substr(stop, 3))) continue;
          const end = stop + 3, aa = (stop - start) / 3;
          if (aa >= minAa) {
            const os = [[start, Math.min(end, n)]].concat(end > n ? [[0, end - n]] : []);
            const seg = strand === "+" ? os : os.map(([a, b]) => [n - b, n - a]);
            out.push({ strand, start, segments: seg, aa, wraps: end > n, frame: start % 3 });
          }
          break;
        }
      }
    }
    return out;
  }
  const lociKey = (o) => o.strand + (o.strand === "+" ? o.segments[o.segments.length - 1][1] : o.segments[o.segments.length - 1][0]);
  function lociOf(orfs) {
    const m = new Map();
    for (const o of orfs) { const k = lociKey(o); const cur = m.get(k); if (!cur) m.set(k, { ...o, starts: 1, all: [o] }); else { cur.starts++; cur.all.push(o); if (o.aa > cur.aa) Object.assign(cur, { ...o, starts: cur.starts, all: cur.all }); } }
    return [...m.values()];
  }
  const GENE_BY_KEY = {};
  D.genes.forEach((g) => { if (g.gene !== "A*") GENE_BY_KEY["+" + g.segments0[g.segments0.length - 1][1]] = g; });

  /* genome frame (0,1,2) of each segment of a gene, for drawing frame tracks */
  function segFrames(segments) {
    let off = 0;
    return segments.map(([a, b]) => { const f = ((a - off) % 3 + 3) % 3; off += b - a; return f; });
  }

  /* ---------- circular genome ---------- */
  const TAU = Math.PI * 2;
  const ang = (x) => (x / L) * TAU - Math.PI / 2;
  function arc(cx, cy, r, a0, a1) {
    const p0 = [cx + r * Math.cos(ang(a0)), cy + r * Math.sin(ang(a0))], p1 = [cx + r * Math.cos(ang(a1)), cy + r * Math.sin(ang(a1))];
    const large = (a1 - a0) / L > 0.5 ? 1 : 0;
    return `M${p0[0].toFixed(2)},${p0[1].toFixed(2)} A${r},${r} 0 ${large} 1 ${p1[0].toFixed(2)},${p1[1].toFixed(2)}`;
  }
  function ring(el, opt = {}) {
    const W = 640, cx = W / 2, cy = W / 2, root = svg(el, W, W);
    const tip = el.closest(".slide")?.querySelector("[data-ring-info]");
    s("circle", { cx, cy, r: 300, fill: "none", stroke: "var(--grid)", "stroke-width": 1 }, root);
    for (let k = 0; k < L; k += 500) {
      const a = ang(k), r0 = 300, r1 = k % 1000 === 0 ? 312 : 306;
      s("line", { x1: cx + r0 * Math.cos(a), y1: cy + r0 * Math.sin(a), x2: cx + r1 * Math.cos(a), y2: cy + r1 * Math.sin(a), stroke: "var(--mute)" }, root);
      if (k % 1000 === 0) t(root, cx + 330 * Math.cos(a), cy + 330 * Math.sin(a) + 4, k ? `${k / 1000}k` : "0 · ori", { "text-anchor": "middle", "font-size": 12, fill: "var(--mute)" });
    }
    const groups = {};
    const layer = (name) => (groups[name] = s("g", { class: "layer layer-" + name }, root));
    // genes on three frame tracks
    const gl = layer("genes");
    D.genes.filter((g) => g.gene !== "A*").forEach((g, gi) => {
      const fr = segFrames(g.segments0);
      const grp = s("g", { class: "gene-arc", tabindex: 0 }, gl);
      g.segments0.forEach(([a, b], i) => {
        const r = 262 + fr[i] * 18;
        const p = s("path", { d: arc(cx, cy, r, a, b), stroke: `var(--f${fr[i]})`, "stroke-width": 14, fill: "none", "stroke-linecap": "butt", class: "draw" }, grp);
        p.style.setProperty("--len", ((b - a) / L) * TAU * r + 2);
        p.style.animationDelay = `${gi * 80}ms`;
      });
      const mid = g.segments0[0][0] + ((g.segments0.reduce((acc, [a, b]) => acc + b - a, 0)) / 2);
      const ma = ang(mid % L), lr = 222;
      t(grp, cx + lr * Math.cos(ma), cy + lr * Math.sin(ma) + 6, g.gene, { "text-anchor": "middle", "font-size": 20, "font-weight": 700, "font-family": "var(--font-display)", class: "gene-label" });
      const show = () => { root.querySelectorAll(".gene-arc").forEach((x) => x.classList.toggle("dim", x !== grp)); if (tip) tip.innerHTML = `<b>${g.gene}</b> · ${g.product}<br><span>${g.length_aa} aa · ${g.segments0.map(([a, b]) => `${a + 1}–${b}`).join(" + ")}${g.wraps_origin ? " · origin-i keçir" : ""}</span>`; };
      const hide = () => root.querySelectorAll(".gene-arc").forEach((x) => x.classList.remove("dim"));
      grp.addEventListener("mouseenter", show); grp.addEventListener("focus", show); grp.addEventListener("mouseleave", hide); grp.addEventListener("blur", hide);
    });
    // loci (+ outer inner ring, − innermost)
    const loci = lociOf(findOrfs(SEQ, opt.minAa || 30));
    const ll = layer("loci");
    loci.forEach((o, i) => {
      const g = GENE_BY_KEY[lociKey(o)];
      const r = o.strand === "+" ? 190 : 160;
      o.segments.forEach(([a, b]) => {
        const p = s("path", { d: arc(cx, cy, r, a, b), stroke: o.strand === "+" ? (g ? "var(--good)" : "var(--plus-false, var(--mute))") : "var(--minus)", "stroke-width": 10, fill: "none", opacity: g ? 1 : 0.55, class: "draw locus" + (g ? " is-gene" : " not-gene") }, ll);
        p.style.setProperty("--len", ((b - a) / L) * TAU * r + 2);
        p.style.animationDelay = `${600 + i * 25}ms`;
        p.dataset.aa = o.aa;
      });
    });
    t(root, cx, cy - 12, opt.center || "PhiX174", { "text-anchor": "middle", "font-size": 30, "font-family": "var(--font-display)", "font-weight": 700 });
    t(root, cx, cy + 18, "5386 nt · dairəvi ssDNA", { "text-anchor": "middle", "font-size": 13, fill: "var(--mute)" });
    el._groups = groups;
    el._setMin = (m) => root.querySelectorAll(".locus").forEach((p) => p.classList.toggle("off", +p.dataset.aa < m));
    return el;
  }

  /* ---------- reading-frame reader ---------- */
  function reader(el) {
    const slide = el.closest(".slide");
    const from = 560, n = 75; // region where E (frame +0 at 567) starts inside D
    function draw(strand, frame) {
      const plain = SEQ.slice(from, from + n);
      const seq = strand === "+" ? plain : revcomp(plain);
      let html = "";
      for (let i = 0; i < seq.length; i++) {
        const inFrame = (i - frame) >= 0 && (i - frame) % 3 === 0 && i + 3 <= seq.length;
        if (inFrame) {
          const c = seq.substr(i, 3);
          const cls = c === "ATG" ? "start" : STOPS.has(c) ? "stop" : "";
          html += `<span class="codon ${cls}" style="--i:${i}">${c}</span>`;
          i += 2;
        } else html += `<span class="nt">${seq[i]}</span>`;
      }
      el.innerHTML = html;
      slide.querySelectorAll("[data-frame]").forEach((b) => b.setAttribute("aria-pressed", b.dataset.frame === strand + frame));
      const label = slide.querySelector("[data-frame-label]");
      if (label) label.textContent = `${strand === "+" ? "plus" : "minus"} strand · çərçivə ${frame + 1} · mövqe ${from + 1}–${from + n}`;
    }
    slide.querySelectorAll("[data-frame]").forEach((b) => b.addEventListener("click", () => draw(b.dataset.frame[0], +b.dataset.frame[1])));
    draw("+", 1);
  }

  /* ---------- nested starts of locus A ---------- */
  function ladder(el) {
    const W = 760, H = 320, root = svg(el, W, H);
    const A = lociOf(findOrfs(SEQ)).find((o) => GENE_BY_KEY[lociKey(o)]?.gene === "A");
    const starts = A.all.slice().sort((a, b) => b.aa - a.aa);
    const total = 522, x0 = 20, x1 = W - 200, X = (aaFromStop) => x1 - (aaFromStop / total) * (x1 - x0);
    starts.forEach((o, i) => {
      const y = 20 + i * ((H - 70) / starts.length);
      const curated = o.aa === 513, longest = i === 0, astar = o.aa === 341;
      const r = s("rect", { x: X(o.aa), y, width: x1 - X(o.aa), height: Math.max(4, (H - 90) / starts.length - 2), fill: curated ? "var(--good)" : longest ? "var(--bad)" : astar ? "var(--accent)" : "var(--grid)", class: "grow-x" }, root);
      r.style.transitionDelay = `${i * 30}ms`;
      if (curated || longest || astar) t(root, x1 + 12, y + 9 + (curated ? 12 : 0), curated ? "A · 513 aa (GenBank)" : longest ? "ən uzun ATG · 522 aa" : "A* · 341 aa", { "text-anchor": "start", "font-size": 13, fill: curated ? "var(--good)" : longest ? "var(--bad)" : "var(--accent)", "font-weight": 600 });
    });
    s("line", { x1: x1, x2: x1, y1: 10, y2: H - 40, stroke: "var(--ink)", "stroke-width": 3 }, root);
    t(root, x1, H - 20, "eyni stop", { "text-anchor": "middle", "font-size": 13 });
    t(root, x0, H - 20, `${starts.length} ATG başlanğıcı → 1 lokus`, { "font-size": 13, fill: "var(--mute)" });
  }

  /* ---------- threshold curve with slider ---------- */
  function curve(el) {
    const slide = el.closest(".slide"), input = slide.querySelector("[data-threshold]");
    const W = 640, H = 300, pad = { l: 46, r: 16, t: 14, b: 40 }, root = svg(el, W, H);
    const xs = D.curve.map((c) => c.min_aa), X = (v) => pad.l + ((v - 30) / (530 - 30)) * (W - pad.l - pad.r), Y = (v) => H - pad.b - v * (H - pad.t - pad.b);
    [0, 0.25, 0.5, 0.75, 1].forEach((v) => { s("line", { x1: pad.l, x2: W - pad.r, y1: Y(v), y2: Y(v), stroke: "var(--grid)" }, root); t(root, pad.l - 8, Y(v) + 4, v.toFixed(2), { "text-anchor": "end", "font-size": 11 }); });
    [30, 100, 200, 300, 400, 500].forEach((v) => t(root, X(v), H - 18, v, { "text-anchor": "middle", "font-size": 11 }));
    t(root, (W + pad.l) / 2, H - 2, "minimum ORF uzunluğu (aa)", { "text-anchor": "middle", "font-size": 12, fill: "var(--mute)" });
    const line = (key, color) => s("path", { d: D.curve.filter((c) => c[key] !== null).map((c, i) => `${i ? "L" : "M"}${X(c.min_aa)},${Y(c[key])}`).join(""), fill: "none", stroke: color, "stroke-width": 3.5, class: "draw-line" }, root);
    line("recall", "var(--good)"); line("precision", "var(--accent)");
    const cursor = s("line", { y1: pad.t, y2: H - pad.b, stroke: "var(--ink)", "stroke-width": 1.5, "stroke-dasharray": "4 4" }, root);
    const dotR = s("circle", { r: 7, fill: "var(--good)" }, root), dotP = s("circle", { r: 7, fill: "var(--accent)" }, root);
    const ringEl = slide.querySelector('[data-chart="ring"]');
    function set(v) {
      const c = D.curve.reduce((a, b) => (Math.abs(b.min_aa - v) < Math.abs(a.min_aa - v) ? b : a));
      cursor.setAttribute("x1", X(c.min_aa)); cursor.setAttribute("x2", X(c.min_aa));
      dotR.setAttribute("cx", X(c.min_aa)); dotR.setAttribute("cy", Y(c.recall));
      dotP.setAttribute("cx", X(c.min_aa)); dotP.setAttribute("cy", Y(c.precision ?? 0));
      const lost = D.genes.filter((g) => g.gene !== "A*" && Math.max(g.length_aa, g.longest_candidate_aa || 0) < c.min_aa).map((g) => g.gene);
      const q = (k) => slide.querySelector(`[data-out="${k}"]`);
      q("t") && (q("t").textContent = c.min_aa);
      q("loci") && (q("loci").textContent = c.loci);
      q("p") && (q("p").textContent = (c.precision ?? 0).toFixed(2));
      q("r") && (q("r").textContent = c.recall.toFixed(2));
      q("lost") && (q("lost").textContent = lost.length ? lost.join(", ") : "heç biri");
      ringEl && ringEl._setMin && ringEl._setMin(c.min_aa);
    }
    input.addEventListener("input", () => set(+input.value));
    el._set = set;
    set(+input.value);
  }

  /* ---------- shuffle null ---------- */
  function nullHist(el, key = "loci_ge_100aa", real = D.summary.null.real_loci_ge_100aa, label = "≥100 aa lokus sayı") {
    const vals = D.null.map((r) => r[key]);
    const W = 640, H = 280, pad = { l: 40, r: 20, t: 20, b: 44 }, root = svg(el, W, H);
    const max = Math.max(real + 1, ...vals) + 1;
    const counts = new Array(max).fill(0); vals.forEach((v) => counts[v]++);
    const bw = (W - pad.l - pad.r) / max, ymax = Math.max(...counts);
    const X = (v) => pad.l + v * bw;
    counts.forEach((c, v) => {
      const h = (c / ymax) * (H - pad.t - pad.b);
      const r = s("rect", { x: X(v) + 2, y: H - pad.b - h, width: bw - 4, height: h, fill: "var(--mute)", opacity: 0.75, class: "grow" }, root);
      r.style.transformOrigin = `0 ${H - pad.b}px`; r.style.transitionDelay = `${v * 50}ms`;
      t(root, X(v) + bw / 2, H - pad.b + 18, v, { "text-anchor": "middle", "font-size": 12 });
    });
    const rx = X(real) + bw / 2;
    const ln = s("line", { x1: rx, x2: rx, y1: pad.t - 6, y2: H - pad.b, stroke: "var(--good)", "stroke-width": 6, class: "grow" }, root);
    ln.style.transformOrigin = `0 ${H - pad.b}px`; ln.style.transitionDelay = "700ms";
    t(root, rx - 10, pad.t + 8, `həqiqi genom: ${real}`, { "text-anchor": "end", fill: "var(--good)", "font-weight": 700 });
    t(root, (W + pad.l) / 2, H - 4, `${label} · 200 qarışdırılmış genom (boz)`, { "text-anchor": "middle", "font-size": 12, fill: "var(--mute)" });
  }

  /* ---------- overlapping genes ---------- */
  function overlaps(el) {
    const slide = el.closest(".slide"), list = slide.querySelector("[data-overlap-list]");
    const G = Object.fromEntries(D.genes.map((g) => [g.gene, g]));
    const pairs = D.overlaps.slice().sort((a, b) => b.overlap_nt - a.overlap_nt);
    function draw(p) {
      const [a, b] = p.genes.split("–").map((x) => G[x]);
      const W = 700, H = 230, root = svg(el, W, H);
      // linear window covering both genes (unwrap around origin for A/B/K)
      const unwrap = (g) => { const segs = g.segments0.map(([x, y]) => [x, y]); if (g.wraps_origin) segs[1] = [segs[1][0] + L, segs[1][1] + L]; return [segs[0][0], segs[segs.length - 1][1]]; };
      let ra = unwrap(a), rb = unwrap(b);
      if (ra[0] > rb[1] && ra[0] - L >= -L) { ra = [ra[0] - L, ra[1] - L]; }
      if (rb[0] > L && ra[1] < L) rb = [rb[0] - L, rb[1] - L];
      const lo = Math.min(ra[0], rb[0]), hi = Math.max(ra[1], rb[1]);
      const X = (v) => 30 + ((v - lo) / (hi - lo)) * (W - 60);
      const ovA = Math.max(ra[0], rb[0]), ovB = Math.min(ra[1], rb[1]);
      if (ovB > ovA) s("rect", { x: X(ovA), y: 20, width: Math.max(2, X(ovB) - X(ovA)), height: 150, fill: "var(--accent)", opacity: 0.16 }, root);
      [[a, ra, 55], [b, rb, 115]].forEach(([g, r, y]) => {
        const fr = segFrames(g.segments0)[0];
        const bar = s("rect", { x: X(r[0]), y, width: X(r[1]) - X(r[0]), height: 34, rx: 4, fill: `var(--f${fr})`, class: "grow-x" }, root);
        bar.style.transformOrigin = `${X(r[0])}px 0`;
        t(root, X(r[0]) + 10, y + 23, `${g.gene} · ${g.length_aa} aa`, { "font-weight": 700, fill: "var(--on-frame, #fff)" });
        // codon ticks inside overlap
        for (let x = r[0]; x < r[1]; x += 3) if (x >= ovA && x < ovB && (ovB - ovA) < 400) s("line", { x1: X(x), x2: X(x), y1: y + 34, y2: y + 42, stroke: `var(--f${fr})` }, root);
      });
      t(root, X((ovA + ovB) / 2), 200, `${p.overlap_nt} nt üst-üstə · çərçivə sürüşməsi +${p.frame_shift}`, { "text-anchor": "middle", "font-weight": 600 });
      list.querySelectorAll("button").forEach((x) => x.setAttribute("aria-pressed", x.dataset.pair === p.genes));
      const info = slide.querySelector("[data-overlap-info]");
      if (info) info.innerHTML = `<b>${a.gene}</b> ${a.product} · <b>${b.gene}</b> ${b.product}`;
    }
    pairs.forEach((p) => { const btn = document.createElement("button"); btn.type = "button"; btn.className = "chip"; btn.dataset.pair = p.genes; btn.textContent = `${p.genes} · ${p.overlap_nt} nt`; btn.onclick = () => draw(p); list.appendChild(btn); });
    draw(pairs.find((p) => p.genes === "D–E"));
  }

  /* ---------- deck engine (same contract as the Khan decks) ---------- */
  const Deck = { i: 0, step: 0, hooks: {}, start: Date.now() };
  window.Deck = Deck;
  Deck.on = (id, fn) => ((Deck.hooks[id] = Deck.hooks[id] || []).push(fn));
  const slides = () => [...document.querySelectorAll(".slide")];
  function render(dir = 1) {
    const list = slides();
    list.forEach((sl, k) => {
      sl.classList.toggle("is-active", k === Deck.i); sl.classList.toggle("is-past", k < Deck.i); sl.classList.toggle("is-future", k > Deck.i);
      if (k === Deck.i) sl.removeAttribute("inert"); else sl.setAttribute("inert", "");
    });
    document.documentElement.dataset.dir = dir > 0 ? "fwd" : "back";
    const sl = list[Deck.i];
    sl.querySelectorAll("[data-step]").forEach((e) => e.classList.toggle("shown", +e.dataset.step <= Deck.step));
    document.querySelectorAll("[data-progress]").forEach((p) => p.style.setProperty("--p", (Deck.i + 1) / list.length));
    document.querySelectorAll("[data-counter]").forEach((p) => (p.textContent = `${String(Deck.i + 1).padStart(2, "0")} / ${String(list.length).padStart(2, "0")}`));
    try { history.replaceState(null, "", "#s" + (Deck.i + 1)); } catch (e) {}
    notes();
  }
  function enter(dir) {
    const sl = slides()[Deck.i];
    Deck.step = dir > 0 ? 0 : +(sl.dataset.steps || 0);
    sl.classList.remove("played"); render(dir); void sl.offsetWidth;
    requestAnimationFrame(() => sl.classList.add("played"));
    (Deck.hooks[sl.dataset.id] || []).forEach((fn) => fn(sl));
    sl.querySelectorAll("[data-count]").forEach((e) => {
      const to = parseFloat(e.dataset.count), dec = +(e.dataset.dec || 0), dur = reduce ? 0 : 1200, t0 = performance.now();
      const tick = (now) => { const k = dur ? Math.min(1, (now - t0) / dur) : 1; e.textContent = (to * (1 - Math.pow(1 - k, 3))).toFixed(dec); if (k < 1) requestAnimationFrame(tick); };
      requestAnimationFrame(tick);
    });
  }
  Deck.go = (n, dir) => { const list = slides(); n = Math.max(0, Math.min(list.length - 1, n)); if (n === Deck.i && dir !== 0) return; const d = dir ?? (n > Deck.i ? 1 : -1); Deck.i = n; enter(d); };
  Deck.next = () => { const sl = slides()[Deck.i]; if (Deck.step < +(sl.dataset.steps || 0)) { Deck.step++; render(1); return; } Deck.go(Deck.i + 1, 1); };
  Deck.prev = () => { if (Deck.step > 0) { Deck.step--; render(-1); return; } Deck.go(Deck.i - 1, -1); };
  let notesOn = false;
  function notes() {
    const p = document.querySelector("[data-notes]"); if (!p) return;
    const n = NOTES[slides()[Deck.i].dataset.id]; p.hidden = !notesOn; if (!n) return;
    p.querySelector("[data-n-title]").textContent = `${Deck.i + 1}. ${n.t} · ~${n.min} dəq`;
    p.querySelector("[data-n-say]").textContent = n.say; p.querySelector("[data-n-tip]").textContent = n.tip;
  }
  setInterval(() => { const c = document.querySelector("[data-n-clock]"); if (!c) return; const sec = Math.floor((Date.now() - Deck.start) / 1000); c.textContent = `${String(Math.floor(sec / 60)).padStart(2, "0")}:${String(sec % 60).padStart(2, "0")}`; }, 1000);

  function wire() {
    if (!slides().length) return; // pages without slides only use the exported helpers
    document.querySelectorAll('[data-chart="ring"]').forEach((el) => ring(el, { center: el.dataset.center }));
    document.querySelectorAll('[data-chart="reader"]').forEach(reader);
    document.querySelectorAll('[data-chart="ladder"]').forEach(ladder);
    document.querySelectorAll('[data-chart="curve"]').forEach(curve);
    document.querySelectorAll('[data-chart="null"]').forEach((el) => nullHist(el));
    document.querySelectorAll('[data-chart="null-longest"]').forEach((el) => {
      const vals = D.null.map((r) => Math.floor(r.longest_aa / 20) * 20);
      const W = 640, H = 220, pad = 40, root = svg(el, W, H), X = (v) => pad + (v / 560) * (W - 2 * pad);
      const counts = {}; vals.forEach((v) => (counts[v] = (counts[v] || 0) + 1)); const ym = Math.max(...Object.values(counts));
      Object.entries(counts).forEach(([v, c]) => { const h = (c / ym) * (H - 70); const r = s("rect", { x: X(+v) + 1, y: H - 40 - h, width: X(20) - X(0) - 2, height: h, fill: "var(--mute)", opacity: .75, class: "grow" }, root); r.style.transformOrigin = `0 ${H - 40}px`; });
      [0, 100, 200, 300, 400, 500].forEach((v) => t(root, X(v), H - 20, v, { "text-anchor": "middle", "font-size": 11 }));
      const rx = X(D.summary.null.real_longest_aa);
      s("line", { x1: rx, x2: rx, y1: 10, y2: H - 40, stroke: "var(--good)", "stroke-width": 6 }, root);
      t(root, rx - 8, 24, `A geni: ${D.summary.null.real_longest_aa} aa`, { "text-anchor": "end", fill: "var(--good)", "font-weight": 700 });
      t(root, W / 2, H - 2, "ən uzun ORF (aa) · qarışdırılmış genomlarda maksimum 222", { "text-anchor": "middle", "font-size": 12, fill: "var(--mute)" });
    });
    document.querySelectorAll('[data-chart="overlaps"]').forEach(overlaps);
    document.querySelectorAll("[data-ring-layer]").forEach((b) => b.addEventListener("click", () => {
      const ringEl = b.closest(".slide").querySelector('[data-chart="ring"]'); const g = ringEl._groups[b.dataset.ringLayer];
      const on = g.style.display === "none"; g.style.display = on ? "" : "none"; b.setAttribute("aria-pressed", on);
    }));
    document.querySelectorAll("[data-credits]").forEach((el) => { el.innerHTML = Object.values(D.credits).map((c) => `<li><a href="${c.page}" target="_blank" rel="noopener">${c.title.replace("File:", "")}</a>${c.artist ? " · " + c.artist : ""} · ${c.license}</li>`).join(""); });

    document.addEventListener("keydown", (e) => {
      if (e.target.closest("input, textarea, select")) return;
      if (["ArrowRight", "PageDown", " "].includes(e.key)) { e.preventDefault(); Deck.next(); }
      else if (["ArrowLeft", "PageUp"].includes(e.key)) { e.preventDefault(); Deck.prev(); }
      else if (e.key === "Home") Deck.go(0, -1);
      else if (e.key === "End") Deck.go(slides().length - 1, 1);
      else if (e.key === "n" || e.key === "N") { notesOn = !notesOn; notes(); }
      else if (e.key === "f" || e.key === "F") { if (document.fullscreenElement) document.exitFullscreen(); else document.documentElement.requestFullscreen?.().catch(() => {}); }
    });
    document.querySelectorAll("[data-next]").forEach((b) => b.addEventListener("click", Deck.next));
    document.querySelectorAll("[data-prev]").forEach((b) => b.addEventListener("click", Deck.prev));
    document.querySelectorAll("[data-notes-toggle]").forEach((b) => b.addEventListener("click", () => { notesOn = !notesOn; notes(); }));
    let x0 = null;
    document.addEventListener("touchstart", (e) => (x0 = e.touches[0].clientX), { passive: true });
    document.addEventListener("touchend", (e) => { if (x0 === null) return; const dx = e.changedTouches[0].clientX - x0; if (Math.abs(dx) > 60) (dx < 0 ? Deck.next : Deck.prev)(); x0 = null; });
    const m = location.hash.match(/^#s(\d+)$/);
    Deck.i = m ? Math.min(slides().length - 1, +m[1] - 1) : 0;
    enter(1);
  }
  Object.assign(Deck, { findOrfs, lociOf, lociKey, revcomp, segFrames, GENE_BY_KEY });
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", wire); else wire();
})();
