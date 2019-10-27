<article>
  <h3>
    <a name="gnunet-0.11.7-release">2019-XX-XX: GNUnet 0.11.7 released</a>
  </h3>
  <p>
    We are pleased to announce the release of GNUnet 0.11.7.
  </p>
  <p>
    This is a bugfix release for 0.11.6, fixing a lot of
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
    information.  As a result, the 0.11.7 release is still <b>only suitable
    for early adopters with some reasonable pain tolerance</b>.
  </p>
  <h4>Download links</h4>
  <ul>
    <li><a href="http://ftpmirror.gnu.org/gnunet/gnunet-0.11.7.tar.gz">http://ftpmirror.gnu.org/gnunet/gnunet-0.11.7.tar.gz</a></li>
    <li><a href="http://ftpmirror.gnu.org/gnunet/gnunet-0.11.7.tar.gz.sig">http://ftpmirror.gnu.org/gnunet/gnunet-0.11.7.tar.gz.sig</a></li>
    <li><a href="http://ftpmirror.gnu.org/gnunet/gnunet-gtk-0.11.7.tar.gz">http://ftpmirror.gnu.org/gnunet/gnunet-gtk-0.11.7.tar.gz</a></li>
    <li><a href="http://ftpmirror.gnu.org/gnunet/gnunet-gtk-0.11.7.tar.gz.sig">http://ftpmirror.gnu.org/gnunet/gnunet-gtk-0.11.7.tar.gz.sig</a></li>
    <li><a href="http://ftpmirror.gnu.org/gnunet/gnunet-fuse-0.11.0.tar.gz">http://ftpmirror.gnu.org/gnunet/gnunet-fuse-0.11.0.tar.gz</a></li>
    <li><a href="http://ftpmirror.gnu.org/gnunet/gnunet-fuse-0.11.0.tar.gz.sig">http://ftpmirror.gnu.org/gnunet/gnunet-fuse-0.11.0.tar.gz.sig</a></li>
  </ul>
  <p>
    gnunet-fuse was not released again, as there were no
    changes and the 0.11.0 versions are expected to continue to work fine
    with gnunet-0.11.7.
  </p>
  <p>
    Note that due to mirror synchronization, not all links might be functional
    early after the release. For direct access try <a href="http://ftp.gnu.org/gnu/gnunet/">http://ftp.gnu.org/gnu/gnunet/</a>
  </p>
  <h4>Noteworthy changes in 0.11.7 (since 0.11.6)</h4>
  <ul>
    <li>
     <tt>ARM</tt>: GNUnet CLI tools are now able to detect if gnunet(-arm) is
     not running and will exit with a warning (before the command would just
       hang and wait for GNUnet to be started). #5906
    </li>
    <li>
      win32 and mingw support were dropped, which resulted in a significant number of lines of
      code to be gone. The code has been unmaintained in our code base
      for many years and there are no known users. For details and further reasons refer to the discussion
      <a href="https://lists.gnu.org/archive/html/gnunet-developers/2019-09/msg00002.html">in our archives</a>.
    </li>
    <li>
      Removal of plibc, win32 and mingw support means you can now compile gnunet without requiring a Cxx compiler
      (you just need a C compiler). #5877
    </li>
    <li>
    <tt>REST</tt>: The new config endpoints can now be used to read and write
    the GNUnet config. #5808
    </li>
    <li>
    <tt>REST</tt>: The service is not started per user in multiuser setups.
    </li>
    <li>
      <tt>REST</tt>: Added tests for namestore and GNS. #5638
    </li>
    <li>
      <tt>re:claimID / OIDC</tt>: Now supports <a href="https://tools.ietf.org/html/rfc7636">PKCE</a>. #5807
    </li>
    <li>
      SUID binary detection mechanisms implemented to improve compatiblity with
      some distributions.
    </li>
    <li>
      <tt>CREDENTIAL</tt> subsystem reworked and renamed to <tt>ABD</tt>
      (attribute-based delegation).
    </li>
    <li>
      <a href="https://lists.gnu.org/archive/html/gnunet-developers/2019-10/msg00023.html">Minor TRANSPORT fixes</a> and <a href="https://lists.gnu.org/archive/html/gnunet-developers/2019-10/msg00022.html">NAT changes</a>.
    </li>
    <li>
      <tt>GNS</tt> prepared code for <a href="https://git.gnunet.org/lsd0001.git/tree/draft-schanzen-gns.txt">LSD001 changes</a>. #5920
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
    Martin Schanzenbach, Julius B&uuml;nger, ng0, Christian Grothoff, Alexia Pagkopoulou, rexxnor, xrs, lurchi and t3sserakt.
  </p>
</article>
