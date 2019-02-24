<!--
<div id="header" class="">
       <ul class="skip">
         <li><a href="#nav">jump to main navigation</a></li> 
         <li><a href="#content">jump to main content</a></li>
         <li><a href="#footer">jump to footer</a></li>
       </ul>
</div>
-->
<nav class="navbar navbar-expand-md navbar-inverse navbar-dark fixed-top bg-dark">
  <a class="navbar-brand" href="index.html">
    <!-- 
	 TODO: imo this is bad in the navbar. a readable "gnunet" font-logo would
	 be better for orientation.
      -->
    <img src="{{ url('static/images/gnunet-icon.png') }}" alt="" />
    <!-- <img width="70%" height="70%" src="../static/images/gnunet-logo-dark-only-text.svg" alt="" /> -->
  </a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarMain" aria-controls="navbarMain" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarMain">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">{{ _("Community") }}</a>
        <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
          <li><a class="dropdown-item" href="engage.html">{{ _("Discussion") }} </a></li>
          <li><a class="dropdown-item" href="copyright.html">{{ _("Copyright for Contributors") }} </a></li>
          <li><a class="dropdown-item" href="ev.html">{{ _("GNUnet e.V.") }}</a></li>
	  <li><a class="dropdown-item" href="https://old.gnunet.org/bot/log/gnunet">{{ _("IRC Archive") }}</a></li>
        </ul>
      </li>
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">{{ _("Development") }}</a>
        <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
          <li><a class="dropdown-item" href="architecture.html">{{ _("System Architecture") }}</a></li>
          <li><a class="dropdown-item" href="https://bugs.gnunet.org/my_view_page.php">{{ _("Bugtracker") }}</a></li>
          <li><a class="dropdown-item" target="_blank" href="https://git.gnunet.org">{{ _("Source Code") }}</a></li>
          <li><a class="dropdown-item" target="_blank" href="https://old.gnunet.org/buildbot/">{{ _("Continuous Integration") }}</a></li>
	  <li><a class="dropdown-item" href="gnurl.html">{{ _("libgnurl") }}</a></li>
        </ul>
      </li>
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">{{ _("Documentation") }}</a>
        <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
          <li>
	    <a class="dropdown-item" href="tutorial.html">{{ _("Tutorials") }}<i class="icon-arrow-right"></i></a>
	    <ul class="dropdown-menu sub-menu">
	      <li><a class="dropdown-item" href="tutorial-ubuntu1804.html">{{ _("Tutorial Ubuntu 18.04") }}</a></li>
	      <li><a class="dropdown-item" href="tutorial-archpi.html">{{ _("Tutorial Archlinux Raspberry Pi 3") }}</a></li>
	      <li><a class="dropdown-item" href="tutorial-debian9.html">{{ _("Tutorial Debian 9") }}</a></li>
	      <li><a class="dropdown-item" href="tutorial-macos.html">{{ _("Tutorial macOS") }}</a></li>
	    </ul>
	  </li>
          <li><a class="dropdown-item" href="glossary.html">{{ _("Glossary") }}</a></li>
	  <li><a class="dropdown-item" target="_blank" href="https://docs.gnunet.org">{{ _("Handbook") }}</a></li>
          <li><a class="dropdown-item" target="_blank" href="https://tutorial.gnunet.org/">{{ _("C-Tutorial") }}</a></li>
          <li><a class="dropdown-item" href="faq.html">{{ _("FAQ") }}</a></li>
          <li><a class="dropdown-item" href="https://old.gnunet.org/bibliography">{{ _("Bibliography") }}</a></li>
	</ul>
      </li>
    </ul>
    <ul class="navbar-nav navbar-right">
      <li class="nav-item dropdown">
        <!--<button class="btn btn-dark dropdown-toggle" type="button" id="dropdownMenu1" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">
          <img src="{{ url('static/images/languageicon.svg') }}" height="15" alt="[{{lang}}]" /> {{ lang_full }} [{{ lang }}] 
        </button> -->
	<a class="nav-link dropdown-toggle" href="#" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">{{ lang_full }} [{{ lang }}]</a>
        <ul class="dropdown-menu dropdown-menu-right" aria-labelledby="navbarMain">
          <li><a class="dropdown-item" href="{{ self_localized('en') }}">English [en]</a></li>
          <li><a class="dropdown-item" href="{{ self_localized('de') }}">Deutsch [de]</a></li>
          <li><a class="dropdown-item" href="{{ self_localized('fr') }}">Fran&ccedil;ais [fr]</a></li>
          <li><a class="dropdown-item" href="{{ self_localized('it') }}">Italiano [it]</a></li>
          <li><a class="dropdown-item" href="{{ self_localized('es') }}">Espa&ntilde;ol [es]</a></li>
        </ul>
      </li>
    </ul>
  </div>
</nav>
