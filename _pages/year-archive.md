---
layout: page
permalink: /people/StephenKissler/posts/
title: "Essays"
eyebrow: "Stephen Kissler"
lead: "Rough-hewn essays on epidemiological modeling — thinking out loud about the craft."
---

{% assign essays = site.posts %}
{% if essays.size > 0 %}
<ul class="essay-list">
{% for post in essays %}
  <li>
    <a href="{{ post.url | relative_url }}"><strong>{{ post.title }}</strong></a>
    {% if post.date %}<span style="color:var(--muted); font-size:.9rem;"> · {{ post.date | date: "%B %-d, %Y" }}</span>{% endif %}
    {% if post.excerpt %}<div style="color:var(--muted); margin:.2rem 0 0;">{{ post.excerpt | strip_html | truncate: 160 }}</div>{% endif %}
  </li>
{% endfor %}
</ul>
{% else %}
<p>No essays yet — check back soon.</p>
{% endif %}
