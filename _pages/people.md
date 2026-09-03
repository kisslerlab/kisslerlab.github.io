---
permalink: /people/
title: "People"
lead: "A small, interdisciplinary group of mathematicians, computer scientists, and epidemiologists, dedicated to improving public health."
wide: true
---

<section class="people-section">
  <h2>Current members</h2>
  <div class="people-cards">
    {% for m in site.data.people.current %}
      <a class="people-card" href="{{ m.page | relative_url }}">
        {% if m.photo %}
          <img src="{{ m.photo | relative_url }}" alt="{{ m.name }}" loading="lazy">
        {% else %}
          <span class="ph" aria-hidden="true">{{ m.name | slice: 0 }}</span>
        {% endif %}
        <span class="nm">{{ m.name }}</span>
        <span class="rl">{{ m.role }}</span>
      </a>
    {% endfor %}
  </div>
</section>

<section class="people-section" style="margin-top:3.5rem;">
  <h2>Lab alumni</h2>
  <ul class="alumni-list">
    {% for m in site.data.people.alumni %}
      {% if m.page %}
        <li><a href="{{ m.page | relative_url }}">{{ m.name }}</a></li>
      {% else %}
        <li><span>{{ m.name }}</span></li>
      {% endif %}
    {% endfor %}
  </ul>
</section>
