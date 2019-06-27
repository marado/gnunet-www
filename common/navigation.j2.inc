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
<!-- <nav class="navbar navbar-toggleable navbar-toggleable-md navbar-expand-md navbar-inverse navbar-dark fixed-top bg-dark"> -->
<!--<nav class="navbar navbar-expand-md navar-inverse navbar-dark bg-dark fixed-top"> -->
  <!-- <nav class="navbar navbar-expand-md fixed-top"> -->
<nav class="navbar navbar-expand-md bg-near-black">
  <a class="navbar-brand" href="index.html">
    <!-- 
      TODO: imo this is bad in the navbar.
      a readable "gnunet" font-logo would
      be better for orientation.
      -->
      <!-- <img src="{{ url('static/images/gnunet-icon.png') }}" alt="GNUnet Home Icon" /> -->
    <h1>GNUnet</h1>
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
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#" data-toggle="dropdown"
           role="button" aria-haspopup="true" aria-expanded="false">
           {{ _("Community") }}
        </a>
        <ul class="dropdown-menu" aria-labelledby="navbarMain">
          <li><a class="dropdown-item" href="engage.html">{{ _("Discussion") }} </a></li>
          <li><a class="dropdown-item" href="gsoc.html">{{ _("GSoC Projects") }}</a></li>
          <li><a class="dropdown-item" href="copyright.html">{{ _("Copyright for Contributors") }} </a></li>
          <li><a class="dropdown-item" href="ev.html">{{ _("GNUnet e.V.") }}</a></li>
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
          <li><a class="dropdown-item" href="https://bugs.gnunet.org/my_view_page.php">{{ _("Bug Tracker") }}</a></li>
          <li><a class="dropdown-item" target="_blank" href="https://git.gnunet.org">{{ _("Source Code") }}</a></li>
          <li><a class="dropdown-item" target="_blank" href="https://gitlab.gnunet.org/">{{ _("Continuous Integration") }}</a></li>
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
	  <li><a class="dropdown-item" href="tutorial.html">{{ _("Tutorials") }}</a></li>
	  <li><a class="dropdown-item" href="video.html">{{ _("Talks (videos)") }}</a></li>
          <li><a class="dropdown-item" href="glossary.html">{{ _("Glossary") }}</a></li>
	  <li><a class="dropdown-item" target="_blank" href="https://docs.gnunet.org">{{ _("Handbook") }}</a></li>
    <li><a class="dropdown-item" target="_blank" href="https://rest.gnunet.org">{{ _("REST API") }}</a></li>
          <li><a class="dropdown-item" target="_blank" href="https://tutorial.gnunet.org/">{{ _("C-Tutorial") }}</a></li>
          <li><a class="dropdown-item" href="faq.html">{{ _("FAQ") }}</a></li>
          <li><a class="dropdown-item" href="https://bib.gnunet.org/">{{ _("Bibliography") }}</a></li>
	</ul>
      </li>
    </ul>
    <ul class="navbar-nav navbar-right nav">
      <li class="nav-item dropdown">
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
      </li> <!-- /navbar-right dropdown -->
    </ul> <!-- /navbar-right -->
  </div> <!-- /navbar -->
</nav>
