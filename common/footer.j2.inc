<footer id="footer" class="near-white bg-near-black">
  <div class="container-fluid">
    <div class="container">
      <div class="row">
        <div class="col-12 col-sm-4">
          <ul class="footer-list">
            <li><a href="{{ url_localized('contact.html') }}">{{ _("Contact") }}</a></li>
            <li><a href="{{ url_localized('ev.html') }}">{{ _("GNUnet e.V.") }}</a></li>
            <li><a href="{{ url_localized('about.html') }}">{{ _("About GNUnet") }}</a></li>
          </ul>
        </div>
        <div class="col-12 col-sm-4">
          <ul class="footer-list">
            <li><a href="https://bugs.gnunet.org/">{{ _("Bug Tracker") }}</a></li>
          </ul>
        </div>
        <div class="col-12 col-sm-4">
          <ul class="footer-list">
            <li><a href="{{ url_localized('copyright.html') }}">{{ _("Copyright Assignment") }}</a></li>
            <li><a href="https://bib.gnunet.org/">{{ _("Bibliography") }}</a></li>
          </ul>
        </div>
      </div>
    </div>
  </div>
  <div class="container text-center">
    <p>
      Copyright &copy;
      <a href="{{ url_localized('ev.html') }}">GNUnet e.V.</a>
      2001 &mdash; 2021.
      <a href="https://git.gnunet.org/www.git">{{ _("Source code of this site.") }}</a>
      <a href="{{ url_localized('contact.html') }}">{{ _("Report issues with this website.") }}</a>
    </p>
    <noscript>
      <p>
        <a href="#">back to top</a>
      </p>
    </noscript>
  </div>
</footer>
