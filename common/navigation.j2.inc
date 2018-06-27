<nav class="navbar navbar-inverse">
  <div class="{{ 'active' if filename == 'index.html' else '' }}">
    <div class="index-logo">
      <img src="../images/gnunet-logo.svg" />
    </div>
  </div>
  <div class="container-fluid">
    <ul class="nav navbar-nav">
      </a>
      </li>
      <li class="{{ 'active' if filename != 'index.html' else '' }}">
        <a href="index.html"><img src="../images/gnunet-logo_notext.svg" width="35" /></a>
      </li>
      <li class="dropdown">
        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">{{ _("Community") }} <span class="caret"></span></a>
        <ul class="dropdown-menu">
          <li><a href="copyright.html">{{ _("Copyright for Contributors") }} </a></li>
          <li><a href="ev.html">{{ _("GNUnet e.V.") }}</a></li>
	  <li><a href="https://gnunet.org/bot/log/gnunet">{{ _("IRC Archive") }}</a></li>
        </ul>
      </li>
      <li class="dropdown">
        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">{{ _("Development") }} <span class="caret"></span></a>
        <ul class="dropdown-menu">
          <li><a href="architecture.html">{{ _("System Architecture") }}</a></li>
          <li><a href="https://gnunet.org/bugs/my_view_page.php">{{ _("Bugtracker") }}</a></li>
          <li><a href="https://gnunet.org/git">{{ _("Source Code") }}</a></li>
          <li><a href="https://gnunet.org/buildbot/">{{ _("Continuous Integration") }}</a></li>
        </ul>
      </li>
      <li class="dropdown">
        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">{{ _("Documentation") }} <span class="caret"></span></a>
        <ul class="dropdown-menu">
          <li><a href="glossary.html">{{ _("Glossary") }}</a></li>
	  <li><a href="https://gnunet.org/handbooks">{{ _("Handbook") }}</a></li>
          <li><a href="faq.html">{{ _("FAQ") }}</a></li>
          <li><a href="https://gnunet.org/bibliography">{{ _("Bibliography") }}</a></li>
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
</div>

</nav>
