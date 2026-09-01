/* The Kissler Lab — interactions
   nav toggle · sticky header state · scroll reveal · publication filters
   · animated epidemic-curve hero motif */
(function () {
  "use strict";
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Progressive enhancement: only opt into hidden-until-revealed once JS is live,
  // so content is always visible if scripts fail to run.
  document.documentElement.classList.add("js");

  /* ---------- mobile nav ---------- */
  var toggle = document.querySelector("[data-nav-toggle]");
  var nav = document.querySelector("[data-nav]");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.hasAttribute("data-open");
      if (open) { nav.removeAttribute("data-open"); } else { nav.setAttribute("data-open", ""); }
      toggle.setAttribute("aria-expanded", String(!open));
    });
    nav.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        nav.removeAttribute("data-open");
        toggle.setAttribute("aria-expanded", "false");
      });
    });
  }

  /* ---------- sticky header shadow ---------- */
  var header = document.querySelector("[data-header]");
  if (header) {
    var onScroll = function () {
      if (window.scrollY > 8) { header.setAttribute("data-scrolled", ""); }
      else { header.removeAttribute("data-scrolled"); }
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* ---------- scroll reveal ---------- */
  var reveals = document.querySelectorAll(".reveal");
  if (reveals.length) {
    if (reduceMotion || !("IntersectionObserver" in window)) {
      reveals.forEach(function (el) { el.classList.add("is-in"); });
    } else {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) { e.target.classList.add("is-in"); io.unobserve(e.target); }
        });
      }, { threshold: 0.12, rootMargin: "0px 0px -8% 0px" });
      reveals.forEach(function (el) { io.observe(el); });
    }
  }

  /* ---------- publication filters ---------- */
  var chips = document.querySelectorAll("[data-filter]");
  var rows = document.querySelectorAll("[data-tags]");
  var empty = document.querySelector(".pub-empty");
  if (chips.length && rows.length) {
    chips.forEach(function (chip) {
      chip.addEventListener("click", function () {
        var tag = chip.getAttribute("data-filter");
        chips.forEach(function (c) { c.setAttribute("aria-pressed", String(c === chip)); });
        var shown = 0;
        rows.forEach(function (row) {
          var tags = row.getAttribute("data-tags").split(" ");
          var match = tag === "all" || tags.indexOf(tag) !== -1;
          row.classList.toggle("is-hidden", !match);
          if (match) shown++;
        });
        if (empty) empty.style.display = shown === 0 ? "block" : "none";
      });
    });
  }

})();
