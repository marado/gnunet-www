<article>
  <h3>
    <a name="gnunet-0.11.1-release">2019-04-03: GNUnet 0.11.1 released</a>
  </h3>
  <p>
    We are pleased to announce the release of GNUnet 0.11.1.
  </p>
  <p>
    This is a bugfix release for 0.11.0, mostly fixing minor bugs,
    improving documentation and fixing various build issues.  In
    terms of usability, users should be aware that there are still a large
    number of known open issues in particular with respect to ease of use,
    but also some critical privacy issues especially for mobile users.
    Also, the nascent network is tiny (about 200 peers) and thus unlikely to
    provide good anonymity or extensive amounts of interesting
    information.  As a result, the 0.11.1 release is still only suitable
    for early adopters with some reasonable pain tolerance.
  </p>
  <h4>Download links</h4>
  <ul>
    <li><a href="http://ftpmirror.gnu.org/gnunet/gnunet-0.11.1.tar.gz">http://ftpmirror.gnu.org/gnunet/gnunet-0.11.1.tar.gz</a></li>
    <li><a href="http://ftpmirror.gnu.org/gnunet/gnunet-0.11.1.tar.gz.sig">http://ftpmirror.gnu.org/gnunet/gnunet-0.11.1.tar.gz.sig</a></li>
    <li><a href="http://ftpmirror.gnu.org/gnunet/gnunet-gtk-0.11.0.tar.gz">http://ftpmirror.gnu.org/gnunet/gnunet-gtk-0.11.0.tar.gz</a></li>
    <li><a href="http://ftpmirror.gnu.org/gnunet/gnunet-gtk-0.11.0.tar.gz.sig">http://ftpmirror.gnu.org/gnunet/gnunet-gtk-0.11.0.tar.gz.sig</a></li>
    <li><a href="http://ftpmirror.gnu.org/gnunet/gnunet-fuse-0.11.0.tar.gz">http://ftpmirror.gnu.org/gnunet/gnunet-fuse-0.11.0.tar.gz</a></li>
    <li><a href="http://ftpmirror.gnu.org/gnunet/gnunet-fuse-0.11.0.tar.gz.sig">http://ftpmirror.gnu.org/gnunet/gnunet-fuse-0.11.0.tar.gz.sig</a></li>
  </ul>
  <p>
    (gnunet-gtk and gnunet-fuse were not released again, as there were no
    changes and the 0.11.0 versions are expected to continue to work fine
    with gnunet-0.11.1.)
  </p>
  <p>
    Note that due to mirror synchronization, not all links might be functional
    early after the release. For direct access try <a href="http://ftp.gnu.org/gnu/gnunet/">http://ftp.gnu.org/gnu/gnunet/</a>
  </p>
  <p>
    Note that GNUnet is now started using <tt>gnunet-arm -s</tt>. GNUnet should be
    stopped using <tt>gnunet-arm -e</tt>.
  </p>
  <h4>Noteworthy changes in 0.11.1</h4>
  <ul>
    <li>
      gnunet-qr was rewritten in C, removing our last dependency on Python 2.x
    </li>
    <li>
      REST and GNS proxy configuration options for address binding were added
    </li>
    <li>
      gnunet-publish by default no longer includes creation time
    </li>
    <li>
      Unreliable message ordering logic in CADET was fixed
    </li>
    <li>
      Various improvements to build system and documentation
    </li>
  </ul>
  <p>
    The above is just the short list, our bugtracker lists
    <a href="https://bugs.gnunet.org/changelog_page.php?version_id=312">
      14 individual issues</a> that were resolved since 0.11.0.
  </p>
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
    ng0, Christian Grothoff, Hartmut Goebel, Martin Schanzenbach, Devan Carpenter, Naomi Phillips and Julius B&#xFC;nger.
  </p>
</article>
