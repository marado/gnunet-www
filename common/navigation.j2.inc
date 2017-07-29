<nav class="navbar navbar-inverse">
  <div class="container-fluid">
    <ul class="nav navbar-nav">
      <li class="{{ 'active' if filename == 'index.html' else '' }}"><a class="taler_home" href="index.html">Taler</a></li>
      <li class="{{ 'active' if filename == 'citizens.html' else '' }}"><a href="citizens.html">{{ _("Citizens") }}</a></li>
      <li class="{{ 'active' if filename == 'merchants.html' else '' }}"><a href="merchants.html">{{ _("Merchants") }}</a></li>
      <li class="{{ 'active' if filename == 'governments.html' else '' }}"><a href="governments.html">{{ _("Governments") }}</a></li>
      <li class="dropdown">
        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">{{ _("Resources") }} <span class="caret"></span></a>
        <ul class="dropdown-menu">
          <li><a href="architecture.html">{{ _("System Architecture") }} </a></li>
          <li><a href="faq.html">{{ _("FAQ") }}</a></li>
          <li><a href="glossary.html">{{ _("Glossary") }}</a></li>
          <li><a href="developers.html">{{ _("Developer Introduction") }}</a></li>
          <li><a href="copyright.html">{{ _("Copyright for Contributors") }}</a></li>
          <li><a href="bibliography.html">{{ _("Bibliography") }}</a></li>
        </ul>
      </li>
    </ul>
    <ul class="nav navbar-right navbar-form">
      <li>
        <button class="btn btn-dark dropdown-toggle" type="button" id="dropdownMenu1" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">
          <img src="{{ url('images/'+lang+'.png') }}" alt="{{lang}}" />
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
      </li>
    </ul>
  </div>
</nav>
