view_all_bug_page.php?refresh=true<nav class="navbar navbar-inverse">
  <div class="container-fluid">
    <ul class="nav navbar-nav">
      <li class="{{ 'active' if filename == 'index.html' else '' }}"><a class="smalllogo" href="index.html">
	<img src="images/gnunet-smaller-logo.png" />
	<img src="images/gnunet-anonymous-schriftzug.png" />
      </a></li>
      <li class="dropdown">
        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">{{ _("Resources") }} <span class="caret"></span></a>
        <ul class="dropdown-menu">
          <li><a href="architecture.html">{{ _("System Architecture") }}</a></li>
          <li><a href="faq.html">{{ _("FAQ") }}</a></li>
          <li><a href="glossary.html">{{ _("Glossary") }}</a></li>
	  <li><a href="https://old.gnunet.org/handbooks">{{ _("Documentation") }}</a></li>
          <li><a href="copyright.html">{{ _("Copyright for Contributors") }} </a></li>
          <li><a href="https://old.gnunet.org/bibliography">{{ _("Bibliography") }}</a></li>
	  <li><a href="ev.html">{{ _("GNUnet e.V.") }}</a></li>
	  <li><a href="https://old.gnunet.org/bot/log/gnunet">{{ _("IRC") }}</a></li>
	  <li><a href="https://old.gnunet.org/bugs">{{ _("Bugtracker") }}</a></li>
        </ul>
      </li>
    </ul>
    <ul class="nav navbar-right">
      <li>
        <button class="btn btn-dark dropdown-toggle" type="button" id="dropdownMenu1" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">
          <img  src="{{ url('images/languageicon.svg') }}" height="35" alt="[{{lang}}]" /> {{ lang_full }} [{{ lang }}]
          <span class="caret"></span>
        </button>
        <ul class="dropdown-menu" aria-labelledby="dropdownMenu1">
          <li>
           <a href="{{ self_localized('en') }}">English [en]</a>
          </li>
          <li>
           <a href="{{ self_localized('de') }}">Deutsch [de]</a>
          </li>
          <li>
           <a href="{{ self_localized('fr') }}">Français [fr]</a>
          </li>
          <li>
           <a href="{{ self_localized('it') }}">Italiano [it]</a>
          </li>
          <li>
           <a href="{{ self_localized('es') }}">Español [es]</a>
          </li>
        </ul>
      </li>
    </ul>
  </div>
</nav>
