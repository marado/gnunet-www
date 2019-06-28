{% extends 'base.html' %}
{% block content %}
  <div class="article-list">
    {% for post in current_posts %} 
      <div itemprop="blogPost">
        {% set teaser_only=true %}
        {% include 'post.html' %}
        <hr>
      </div>
    {% endfor %}  
  </div>
  <div class="bottom-nav">
    <p>
      <a href="/news/">{{ _("More news")}}</a>
    </p>
  </div>
{% endblock %}
