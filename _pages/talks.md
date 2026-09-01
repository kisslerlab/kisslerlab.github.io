---
permalink: /talks/
title: "Talks"
lead: "Slides from selected lectures and invited talks. Click a thumbnail to open the deck."
wide: true
gallery:
  - url: /talks/Kissler_KineticsECDC/index.html
    image_path: /assets/images/Kissler_ECDC_titlepage.png
    title: "Viral kinetics for outbreak response"
    venue: "ECDC Modelling Perspectives · 2025"
  - url: /talks/Kissler_CCSS/index.html
    image_path: /assets/images/Kissler_CCSS_titlepage.png
    title: "Linking viral kinetics with disease transmission and control"
    venue: "Contagion on Complex Social Systems · 2022"
  - url: /talks/Kissler_EPI208/index.html
    image_path: /assets/images/Kissler_EPI208_titlepage.png
    title: "Introduction to epidemiological modeling"
    venue: "EPI 208 · 2022"
  - url: /talks/Kissler_BS825/index.html
    image_path: /assets/images/Kissler_BS825_titlepage.png
    title: "Understanding SARS-CoV-2 using simple models"
    venue: "BS825, Boston University · 2022"
---

<div class="talk-grid">
{% for talk in page.gallery %}
  <a class="talk-card" href="{{ talk.url | relative_url }}">
    <img src="{{ talk.image_path | relative_url }}" alt="Title slide: {{ talk.title }}" loading="lazy">
    <div class="talk-title">{{ talk.title }}<br><small style="font-weight:400;color:var(--muted);">{{ talk.venue }}</small></div>
  </a>
{% endfor %}
</div>
