<!--
<div id="header" class="">
       <ul class="skip">
         <!-- <li><a href="#nav">jump to main navigation</a></li> -->
         <li><a href="#content">jump to main content</a></li>
         <li><a href="#footer">jump to footer</a></li>
       </ul>
</div>
-->
<nav class="navbar navbar-inverse navbar-default">
  <div class="container-fluid">
    <ul class="nav navbar-nav">
       <li class="nav navbar-left">
         <a class="navbar-brand mr-0 mr-md-2" href="index.html">
           <img src="../images/gnunet-icon.png" alt="" />
         </a>
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
	  <li><a href="gnurl.html">{{ _("libgnurl") }}</a></li>
        </ul>
      </li>
      <li class="dropdown">
        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">{{ _("Documentation") }} <span class="caret"></span></a>
        <ul class="dropdown-menu">
          <li><a href="tutorial.html">{{ _("Tutorial") }}</a></li>
          <li><a href="glossary.html">{{ _("Glossary") }}</a></li>
	  <li><a href="https://docs.gnunet.org">{{ _("Handbook") }}</a></li>
          <li><a href="faq.html">{{ _("FAQ") }}</a></li>
          <li><a href="https://gnunet.org/bibliography">{{ _("Bibliography") }}</a></li>
	</ul>
      </li>
    </ul>
    <ul class="nav navbar-right">
      <li>
        <button class="btn btn-dark dropdown-toggle" type="button" id="dropdownMenu1" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">
          <img  src="{{ url('images/languageicon.svg') }}" height="15" alt="[{{lang}}]" /> {{ lang_full }} [{{ lang }}]
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
           <a href="{{ self_localized('fr') }}">Fran&ccedil;ais [fr]</a>
          </li>
          <li>
           <a href="{{ self_localized('it') }}">Italiano [it]</a>
          </li>
          <li>
           <a href="{{ self_localized('es') }}">Espa&ntilde;ol [es]</a>
          </li>
        </ul>
      </li>
      </ul>
  </div>
</nav>
