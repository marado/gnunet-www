<article>
  <h3>
    <a name="gnunet-0.11.8-release">2019-10-27: GNUnet 0.11.8 released</a>
  </h3>
  <p>
    We are pleased to announce the release of GNUnet 0.11.8.
  </p>
  <p>
    This is a bugfix release for 0.11.7, fixing a lot of
    minor bugs, improving stability and code quality. Further, win32 support
    was removed for reasons you may read below.
    In this release, we again improved the webpage in general and updated our
    documentation.

    <i>As always:</i>
    In terms of usability, users should be aware that there are still <b>a large
    number of known open issues</b> in particular with respect to ease of use,
    but also some critical privacy issues especially for mobile users.
    Also, the nascent network is tiny (about 200 peers) and thus unlikely to
    provide good anonymity or extensive amounts of interesting
    information.  As a result, the 0.11.8 release is still <b>only suitable
    for early adopters with some reasonable pain tolerance</b>.
  </p>
  <h4>Download links</h4>
  <ul>
    <li><a href="http://ftpmirror.gnu.org/gnunet/gnunet-0.11.8.tar.gz">http://ftpmirror.gnu.org/gnunet/gnunet-0.11.8.tar.gz</a></li>
    <li><a href="http://ftpmirror.gnu.org/gnunet/gnunet-0.11.8.tar.gz.sig">http://ftpmirror.gnu.org/gnunet/gnunet-0.11.8.tar.gz.sig</a></li>
    <li><a href="http://ftpmirror.gnu.org/gnunet/gnunet-gtk-0.11.7.tar.gz">http://ftpmirror.gnu.org/gnunet/gnunet-gtk-0.11.7.tar.gz</a></li>
    <li><a href="http://ftpmirror.gnu.org/gnunet/gnunet-gtk-0.11.7.tar.gz.sig">http://ftpmirror.gnu.org/gnunet/gnunet-gtk-0.11.7.tar.gz.sig</a></li>
    <li><a href="http://ftpmirror.gnu.org/gnunet/gnunet-fuse-0.11.0.tar.gz">http://ftpmirror.gnu.org/gnunet/gnunet-fuse-0.11.0.tar.gz</a></li>
    <li><a href="http://ftpmirror.gnu.org/gnunet/gnunet-fuse-0.11.0.tar.gz.sig">http://ftpmirror.gnu.org/gnunet/gnunet-fuse-0.11.0.tar.gz.sig</a></li>
  </ul>
  <p>
    gnunet-fuse and gnunet-gtk were not released again, as there were no
    changes and the 0.11.0/0.11.7 versions are expected to continue to work fine
    with gnunet-0.11.8.
    The GPG key used to sign is: <tt>A88C8ADD129828D7EAC02E52E22F9BBFEE348588</tt>
  </p>
  <p>
    Note that due to mirror synchronization, not all links might be functional
    early after the release. For direct access try <a href="http://ftp.gnu.org/gnu/gnunet/">http://ftp.gnu.org/gnu/gnunet/</a>
  </p>
  <h4>Noteworthy changes in 0.11.8 (since 0.11.7)</h4>
  <ul>
    <li>
      <tt>GNS</tt> Portability fixes.
    </li>
    <li>
     <tt>PQ</tt>: Fixed build with postgresql plugin. (Regression introduces
       as part of #5733)
    </li>
    <li>
      Documentation, comments and code quality was improved.
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
      negatively impact performance.
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
    ng0, Daniel Golle.
  </p>
</article>
