<!--
  <div id="header" class="">
    <ul class="skip">
      <li><a href="#nav">jump to main navigation</a></li> 
      <li><a href="#content">jump to main content</a></li>
      <li><a href="#footer">jump to footer</a></li>
    </ul>
  </div>
-->
<noscript>
  <style>
    .collapse
    {
    display: block;
    }
  </style>
</noscript>
<nav class="navbar sticky-top navbar-expand-md bg-near-black">
  <a class="navbar-brand" href="index.html">
      <img src="{{ url('static/images/gnunet-logo-dark-only-text.png') }}" alt="GNUnet" height="25px" />
  </a>

  <!-- menu button -->
  <button class="navbar-toggler navbar-toggler-right custom-toggler"
          type="button"
          data-toggle="collapse"
          data-target="#navbarMain"
          aria-controls="navbarMain"
          aria-expanded="false"
          aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
  </button>
  <!-- /menu button -->

  <!-- navbar -->
  <div class="collapse navbar-collapse bg-near-black" id="navbarMain">
    <ul class="navbar-nav mr-auto nav">
      <li class="nav-link">
	<a href="about.html">{{ _("About") }}</a></li>
      </li>
      <li class="nav-link">
	<a href="index.html#news">{{ _("News") }}</a>
      </li>
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#" data-toggle="dropdown"
           role="button" aria-haspopup="true" aria-expanded="false">
           {{ _("Community") }}
        </a>
        <ul class="dropdown-menu" aria-labelledby="navbarMain">
          <li><a class="dropdown-item" href="engage.html">{{ _("Engage") }} </a></li>
          <li><a class="dropdown-item" href="gsoc.html">{{ _("GSoC Projects") }}</a></li>
          <li><a class="dropdown-item" href="ev.html">{{ _("GNUnet e.V.") }}</a></li>
          <li><a class="dropdown-item" href="copyright.html">{{ _("Copyright for Contributors") }} </a></li>
	  <!-- li><a class="dropdown-item" href="https://old.gnunet.org/bot/log/gnunet">{{ _("IRC Archive") }}</a></li -->
        </ul>
      </li>
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#" id="navbarMain"
           data-toggle="dropdown" role="button"
           aria-haspopup="true" aria-expanded="false">
           {{ _("Development") }}
        </a>
        <ul class="dropdown-menu" aria-labelledby="navbarMain">
          <li><a class="dropdown-item" href="architecture.html">{{ _("System Architecture") }}</a></li>
          <li><a class="dropdown-item" href="https://bugs.gnunet.org" target="_blank">{{ _("Bug Tracker") }}</a></li>
          <li><a class="dropdown-item" href="https://git.gnunet.org" target="_blank">{{ _("Source Code") }}</a></li>
          <li><a class="dropdown-item" href="https://gitlab.gnunet.org/" target="_blank">{{ _("Continuous Integration") }}</a></li>
          <li><a class="dropdown-item" target="_blank" href="https://tutorial.gnunet.org/">{{ _("Development Tutorial") }}</a></li>
	  <li><a class="dropdown-item" href="gnurl.html">libgnurl</a></li>
        </ul>
      </li>
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle"
	   href="#"
	   data-toggle="dropdown"
	   role="button"
	   aria-haspopup="true"
	   aria-expanded="false">
	   {{ _("Documentation") }}
	</a>
	<ul class="dropdown-menu" aria-labelledby="navbarMain">
	  <li><a class="dropdown-item" href="install.html">{{ _("Install") }}</a></li>
	  <li><a class="dropdown-item" href="use.html">{{ _("Use") }}</a></li>
	  <li><a class="dropdown-item" href="video.html">{{ _("Videos") }}</a></li>
          <li><a class="dropdown-item" href="glossary.html">{{ _("Glossary") }}</a></li>
	  <li><a class="dropdown-item" target="_blank" href="https://docs.gnunet.org">{{ _("Handbook") }}</a></li>
    <li><a class="dropdown-item" target="_blank" href="https://rest.gnunet.org">{{ _("REST API") }}</a></li>
          <li><a class="dropdown-item" href="faq.html">{{ _("FAQ") }}</a></li>
          <li><a class="dropdown-item" href="https://bib.gnunet.org/" target="_blank">{{ _("Bibliography") }}</a></li>
	</ul>
      </li>
    </ul>
    <ul class="navbar-nav navbar-right nav">
<!--      <li class="nav-item dropdown">
  <a class="nav-link dropdown-toggle" href="#"
           data-toggle="dropdown" role="button"
           aria-haspopup="true" aria-expanded="false">
           {{ lang_full }} [{{ lang }}]
        </a>
        <ul class="dropdown-menu dropdown-menu-right" aria-labelledby="navbarMain">
          <li><a class="dropdown-item" href="{{ self_localized('en') }}">English [en]</a></li>
          <li><a class="dropdown-item" href="{{ self_localized('de') }}">Deutsch [de]</a></li>
          <li><a class="dropdown-item" href="{{ self_localized('fr') }}">Fran&ccedil;ais [fr]</a></li>
          <li><a class="dropdown-item" href="{{ self_localized('it') }}">Italiano [it]</a></li>
          <li><a class="dropdown-item" href="{{ self_localized('es') }}">Espa&ntilde;ol [es]</a></li>
        </ul>
      </li> DISABLE FOR NOW FOR LACK OF EXISTING TRANSLATIONS -->
      <!-- /navbar-right dropdown -->
    </ul> <!-- /navbar-right -->
  </div> <!-- /navbar -->
</nav>
