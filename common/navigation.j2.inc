      <div class="navbar navbar-fixed-top navbar-taler" role="navigation">
        <div class="navbar-header">
                <button class="navbar-toggle btn btn-default dropdown-toggle mobile-lang" type="button" id="dropdownMenu1" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">
                  <img src="{{ url('images/'+lang+'.png') }}"/></img>
                  <span class="caret"></span>
                </button>
                <ul class="dropdown-menu" aria-labelledby="dropdownMenu1">
                  <li>
                   <a href="{{ self_localized('en') }}"><img src="{{ url('images/gb.png') }}" height="15" width="23" alt="English">English</a>
                  </li>
                  <li>
                   <a href="{{ self_localized('de') }}"><img src="{{ url('images/de.png') }}" height="15" width="25" alt="Deutsch">Deutsch</a>
                  </li>
                  <li>
                   <a href="{{ self_localized('fr') }}"><img src="{{ url('images/fr.png') }}" height="15" width="22" alt="Français">Français</a>
                  </li>
                  <li>
                   <a href="{{ self_localized('it') }}"><img src="{{ url('images/it.png') }}" height="15" width="22" alt="Italiano">Italiano</a>
                  </li>
                  <li>
                   <a href="{{ self_localized('es') }}"><img src="{{ url('images/es.png') }}" height="15" width="23" alt="Español">Español</a>
                  </li>
                </ul>
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#main-navbar">
            <span class="sr-only">Toggle navigation</span>
      	    <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
        </div>
        <div class="collapse navbar-collapse" id="main-navbar">
          <ul class="nav nav-justified">
            <li class="m_index"><a href="{{ url_localized('index.html') }}">{{ _("Home") }}</a></li>
            <li class="m_demo"><a href="https://demo.taler.net/" target="_blank">{{ _("Demo") }}</a></li>
	    <li class="m_citizens"><a href="{{ url_localized('citizens.html') }}">{{ _("Citizens") }}</a></li>
            <li class="m_merchants"><a href="{{ url_localized('merchants.html') }}">{{ _("Merchants") }}</a></li>
            <li class="m_governments"><a href="{{ url_localized('governments.html') }}">{{ _("Governments") }}</a></li>
            <li class="m_investors"><a href="{{ url_localized('investors.html') }}">{{ _("Investors") }}</a></li>
            <li class="m_developers"><a href="{{ url_localized('developers.html') }}">{{ _("Developers") }}</a></li>
            <li class="m_about"><a href="{{ url_localized('about.html') }}">{{ _("About&nbsp;us") }}</a></li>
            <li>
              <div class="dropdown nav-lang">
                <button class="btn btn-default dropdown-toggle" type="button" id="dropdownMenu1" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">
                  <img src="{{ url('images/'+lang+'.png') }}"/></img>
                  <span class="caret"></span>
                </button>
                <ul class="dropdown-menu" aria-labelledby="dropdownMenu1">
                  <li>
                   <a href="{{ self_localized('en') }}"><img src="{{ url('images/gb.png') }}" height="15" width="23" alt="English">English</a>
                  </li>
                  <li>
                   <a href="{{ self_localized('de') }}"><img src="{{ url('images/de.png') }}" height="15" width="25" alt="Deutsch">Deutsch</a>
                  </li>
                  <li>
                   <a href="{{ self_localized('fr') }}"><img src="{{ url('images/fr.png') }}" height="15" width="22" alt="Français">Français</a>
                  </li>
                  <li>
                   <a href="{{ self_localized('it') }}"><img src="{{ url('images/it.png') }}" height="15" width="22" alt="Italiano">Italiano</a>
                  </li>
                  <li>
                   <a href="{{ self_localized('es') }}"><img src="{{ url('images/es.png') }}" height="15" width="23" alt="Español">Español</a>
                  </li>
                </ul>
              </div>
            </li>
          </ul>
        </div>
      </div>
