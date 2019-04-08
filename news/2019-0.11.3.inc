<article>
  <h3>
    <a name="gnunet-0.11.3-release">2019-04-07: GNUnet 0.11.3 released</a>
  </h3>
  <p>
    We are pleased to announce the release of GNUnet 0.11.3.
  </p>
  <p>
    This is a bugfix release for 0.11.2, mostly fixing a few
    build issues. In
    terms of usability, users should be aware that there are still a large
    number of known open issues in particular with respect to ease of use,
    but also some critical privacy issues especially for mobile users.
    Also, the nascent network is tiny (about 200 peers) and thus unlikely to
    provide good anonymity or extensive amounts of interesting
    information.  As a result, the 0.11.3 release is still only suitable
    for early adopters with some reasonable pain tolerance.
  </p>
  <h4>Download links</h4>
  <ul>
    <li><a href="http://ftpmirror.gnu.org/gnunet/gnunet-0.11.3.tar.gz">http://ftpmirror.gnu.org/gnunet/gnunet-0.11.3.tar.gz</a></li>
    <li><a href="http://ftpmirror.gnu.org/gnunet/gnunet-0.11.3.tar.gz.sig">http://ftpmirror.gnu.org/gnunet/gnunet-0.11.3.tar.gz.sig</a></li>
    <li><a href="http://ftpmirror.gnu.org/gnunet/gnunet-gtk-0.11.0.tar.gz">http://ftpmirror.gnu.org/gnunet/gnunet-gtk-0.11.0.tar.gz</a></li>
    <li><a href="http://ftpmirror.gnu.org/gnunet/gnunet-gtk-0.11.0.tar.gz.sig">http://ftpmirror.gnu.org/gnunet/gnunet-gtk-0.11.0.tar.gz.sig</a></li>
    <li><a href="http://ftpmirror.gnu.org/gnunet/gnunet-fuse-0.11.0.tar.gz">http://ftpmirror.gnu.org/gnunet/gnunet-fuse-0.11.0.tar.gz</a></li>
    <li><a href="http://ftpmirror.gnu.org/gnunet/gnunet-fuse-0.11.0.tar.gz.sig">http://ftpmirror.gnu.org/gnunet/gnunet-fuse-0.11.0.tar.gz.sig</a></li>
  </ul>
  <p>
    (gnunet-gtk and gnunet-fuse were not released again, as there were no
    changes and the 0.11.0 versions are expected to continue to work fine
    with gnunet-0.11.3.)
  </p>
  <p>
    Note that due to mirror synchronization, not all links might be functional
    early after the release. For direct access try <a href="http://ftp.gnu.org/gnu/gnunet/">http://ftp.gnu.org/gnu/gnunet/</a>
  </p>
  <p>
    Note that GNUnet is now started using <tt>gnunet-arm -s</tt>. GNUnet should be
    stopped using <tt>gnunet-arm -e</tt>.
  </p>
  <h4>Noteworthy changes in 0.11.3 (since 0.11.2)</h4>
  <ul>
    <li>
      gnunet-zoneimport now handles <tt>-h</tt> correctly
    </li>
    <li>
      <tt>iptables</tt> and other similar binaries are no longer
      hard-coded but detected at configure time (with hard-coded
      fallback locations).
    </li>
    <li>
      <tt>make uninstall</tt> now properly uninstalls all files
    </li>
    <li>
      Passing the no longer available <tt>--with-nssdir</tt>
      configuration option now results in a hard error.
    </li>
    <li>
      <tt>GNUNET_memcmp()</tt> and <tt>GNUNET_is_zero()</tt> macros
      introduced for improved type safety (but not yet used consistently).
    </li>
  </ul>
  <h4>Known Issues</h4>
  <ul>
    <li>
      There are known major design issues in the TRANSPORT, ATS and CORE subsystems
      which will need to be addressed in the future to achieve acceptable usability,
      performance and security.
    </li>
    <li>
      There are known moderate implementation limitations in CADET that
      negatively impact performance. Also CADET may unexpectedly deliver messages out-of-order.
    </li>
    <li>
      There are known moderate design issues in FS that also impact
      usability and performance.
    </li>
    <li>
      There are minor implementation limitations in SET that create
      unnecessary attack surface for availability.
    </li>
    <li>
      The RPS subsystem remains experimental.
    </li>
    <li>
      Some high-level tests in the test-suite fail non-deterministically due to
      the low-level TRANSPORT issues.
    </li>
  </ul>
  <p>
    In addition to this list, you may also want to consult our bug tracker
    at <a href="https://bugs.gnunet.org/">bugs.gnunet.org</a> which lists
    about 190 more specific issues.
  </p>

  <h4>Thanks</h4>
  <p>
    This release was the work of many people. The following people
    contributed code and were thus easily identified:
    ng0, Christian Grothoff, Daniel Golle, Martin Schanzenbach and Julius B&#xFC;nger.
  </p>
</article>
