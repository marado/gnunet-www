<footer id="footer" class="near-white bg-near-black">
  <div class="container-fluid">
    <div class="container">
      <div class="row">
        <div class="col-12 col-sm-4">
          <ul class="footer-list">
            <li><p><a href="team.html">{{ _("Developer Team") }}</a></p></li>
            <li><p><a href="contact.html">{{ _("Contact") }}</a></p></li>
            <li><p><a href="ev.html">{{ _("GNUnet e.V.") }}</a></p></li>
            <li><p><a href="about.html">{{ _("About GNUnet") }}</a></p></li>
          </ul>
        </div>
        <div class="col-12 col-sm-4">
          <ul class="footer-list">
            <li><p><a href="https://bugs.gnunet.org/">{{ _("Bug Tracker") }}</a></p></li>
            <!-- <li><p><a href="https://irc.gnunet.org/gnunet">{{ _("IRC archive") }}</a></p></li> -->
          </ul>
        </div>
        <div class="col-12 col-sm-4">
          <ul class="footer-list">
            <li><p><a href="copyright.html">{{ _("Copyright Assignment") }}</a></p></li>
            <!-- <li><p><a href="https://gitlab.gnunet.org/">{{ _("Continuous Integration") }}</a></p></li> -->
            <li><p><a href="https://bib.gnunet.org/">{{ _("Bibliography") }}</a></p></li>
          </ul>
        </div>
      </div>
    </div>
  </div>
  <div class="container text-center">
    <p>
    {% trans %}
      Copyright &copy; <a href="ev.html">GNUnet e.V.</a> 2015 &mdash; 2019.
      <!-- This just takes up space no one is interested in: -->
    <!-- This page was created using <a href='https://www.gnu.org/'>Free Software</a> only.<br> -->
    <a href='https://git.gnunet.org/www.git'>Source code of this site.</a>
    <a href='contact.html'>Report issues with this website</a>.
    {% endtrans %}
    </p>
  </div>
</footer>
