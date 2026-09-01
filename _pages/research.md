---
permalink: /research/
title: "Research"
wide: true
---

<p class="mission-line" style="margin: .5rem 0 3rem;">
  We study <em>how pathogens interact</em>, <em>how our bodies, communities, and
  societies respond to infection</em>, and <em>how epidemics compound other threats
  to our well-being</em> — using the latest data, statistics, and computational methods.
</p>

<div class="research-themes">
{% for theme in site.data.research %}
  {% assign is_even = forloop.index | modulo: 2 %}
  <section class="theme-row{% if is_even == 0 %} theme-row--rev{% endif %}" id="{{ theme.id }}">
    <div class="theme-media">
      <img src="{{ theme.image | relative_url }}" alt="Animation illustrating {{ theme.title | downcase }}">
    </div>
    <div class="theme-text">
      <span class="theme-num">{{ theme.number }}</span>
      <h2>{{ theme.title }}</h2>
      <p class="theme-tagline">{{ theme.tagline }}</p>
      <p>{{ theme.summary }}</p>
    </div>
  </section>
{% endfor %}
</div>

<h2 id="publications" style="margin-top:3.5rem;">Selected publications</h2>

<p>A curated selection below — the complete, up-to-date list lives on <a href="{{ site.scholar_url }}" target="_blank" rel="noopener">Google Scholar</a>. Filter by topic:</p>

<div class="pub-toolbar" role="group" aria-label="Filter publications by topic">
  <button class="chip" data-filter="all" aria-pressed="true">All</button>
  {% for f in site.data.publications.filters %}
    <button class="chip" data-filter="{{ f.tag }}" aria-pressed="false">{{ f.label }}</button>
  {% endfor %}
</div>

<div class="pub-list">
  {% for pub in site.data.publications.items %}
    <div class="pub-row" data-tags="{{ pub.tags | join: ' ' }}">
      <span class="pub-year">{{ pub.year }}</span>
      <div class="pub-main">
        <a class="pub-title" href="{{ pub.url }}" target="_blank" rel="noopener">{{ pub.title }}</a>
        <p class="pub-authors">{% include authors.html authors=pub.authors %} · <span class="pub-venue">{{ pub.venue }}</span> ({{ pub.year }})</p>
      </div>
      {% if pub.type == 'preprint' %}<span class="pub-flag">Preprint</span>{% endif %}
    </div>
  {% endfor %}
  <p class="pub-empty">No publications match that filter yet.</p>
</div>
