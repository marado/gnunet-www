      <div class="navbar navbar-default navbar-fixed-top" role="navigation">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#main-navbar">
            <span class="sr-only">Toggle navigation</span>
      	    <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
        </div>
        <div class="collapse navbar-collapse" id="main-navbar">
          <ul class="nav nav-justified">
            <li class="m_index"><a href=".">{{ _("Home") }}</a></li>
            <li class="m_demo btn btn-outline-success"><a href="https://demo.taler.net/" target="_blank">{{ _("Demo") }}</a></li>
	    <li class="m_citizens"><a href='citizens'>{{ _("Citizens") }}</a></li>
            <li class="m_merchants"><a href='merchants'>{{ _("Merchants") }}</a></li>
            <li class="m_governments"><a href='governments'>{{ _("Governments") }}</a></li>
            <li class="m_investors"><a href='investors'>{{ _("Operators") }}</a></li>
            <li class="m_developers"><a href='developers'>{{ _("Developers") }}</a></li>
            <li class="m_about"><a href='about'>{{ _("About&nbsp;us") }}</a></li>
          </ul>
        </div>
      </div>
       <div class="navbar navbar-default navbar-fixed-bottom" role="navigation">
         <div class="container lang-slector">
           <a href="#" onclick="location.pathname=location.pathname.replace(/^.../, '/en')"><img src="/images/gb.png" height="15" width="23" alt="English"></a>
           <a href="#" onclick="location.pathname=location.pathname.replace(/^.../, '/de')"><img src="/images/de.png" height="15" width="25" alt="Deutsch"></a>
           <a href="#" onclick="location.pathname=location.pathname.replace(/^.../, '/fr')"><img src="/images/fr.png" height="15" width="22" alt="Français"></a>
           <a href="#" onclick="location.pathname=location.pathname.replace(/^.../, '/it')"><img src="/images/it.png" height="15" width="22" alt="Italiano"></a>
           <a href="#" onclick="location.pathname=location.pathname.replace(/^.../, '/es')"><img src="/images/es.png" height="15" width="23" alt="Español"></a>
         </div>
       </div>
