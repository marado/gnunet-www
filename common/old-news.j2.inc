{% macro oldnews(year) %}
  <div class="container-fluid">
    <div class="container">
      <article>
        <div class="row">
          <div class="container text-center">
            <h1>{{ _("News") + " " + (year|string) }}<a name="news"></a></h1>
            <section>
              <p>
                {% trans %}
                News posts about changes related to
                GNUnet such as releases and events
                {% endtrans %}
                &#8211;
                <a href="{{ url_localized('rss.xml') }}">{{ _("subscribe to our RSS feed") }}</a>
              </p>
            </section>
          </div>
        </div>
        <div class="row">
          <b>{{ year }}</b>
          <ul class="timeline">
          {% for item in newsdata|selectattr('date.year', 'eq', year) %}
          <li>
              <section class="item-preview">
               <header>
                  <h3>{{ item['title']|e }}</h3>
                  <p class="item-date">
                    {{ item['date'] }}
                  </p>
                </header>
                <p class="item-abstract">
                  {{ get_abstract('news/' + item['page'], 1000) }} <br/>
                  [<a href="{{ url_localized('news/' + item['page']) }}" title="{{ item['date']}}">{{ _("read more") }}</a>]
                </p>
              </section>
            </li>
          {% endfor %}
          </ul>
        </div>
      </article>
    </div>
  </div>
{% endmacro %}
