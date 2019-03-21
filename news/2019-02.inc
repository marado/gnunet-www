<article>
<h3>
<a NAME="gsoc2019"></a>2019-02: Topics for GSoC 2019
</h3>
<section>
<h4>Android Port</h4>
<p>
It is time for GNUnet to run properly on Android.  Note that
GNUnet is written in C, and this is not about rewriting
GNUnet in Java, but about getting the C code to run on Android.
<br>
Mentor: <a href="https://www.goebel-consult.de/">Hartmut Goebel</a>
</p>
</section>

<section>
<h4>Help with Continuous Integration setup</h4>
<p>
There is a push for migrating our CI to Gitlab.  The CI should
eventually not just run "make check" on various platforms, but also
perform tests with multiple peers running in different VMs with
specific network topologies (i.e. NAT) between them being simulated.
The CI should also be integrated with Gauger for performance
regression analysis.  Running jobs only when dependencies have changed
and scripting more granular triggers or ideally automatic dependency
discovery (as done by the autotools) is also important.
<br>
Mentor: TBD
</p>
</section>

<section>
<h4>Migrate gnunet-qr from Python 2.7 to C using libzbar</h4>
<p>
Python 2.7 is reaching its end-of-life, and we want to get rid
of the dependency on Python. The existing gnunet-qr tool is a
rather simple wrapper around python-zbar, which itself wraps
libzbar. The goal of this project is to directly use libzbar
to scan QR codes for GNUnet / the GNU Name System (see
also <a href="https://bugs.gnunet.org/view.php?id=5562">#5562</a>).
<br>
Mentor: Christian Grothoff
</p>
</section>

<section>
<h4>re:claimID OpenID Connect performance improvements</h4>
<p>
reclaimID is a decentralized identity system build on top of the GNU
Name System.
Upon authorization, the user provides a requesting party (RP) such as a website
with an authorization ticket (e.g. piggybacked in an OpenID authorization code).
The RP uses information contained in this ticket to
<ol>
<li> Retrieve the decryption key from GNS</li>
<li> Retrieve the user attributes from GNS</li>
</ol>
The GNS lookups ensure that the RP receives up-to-date attributes and functional
decryption keys. However, in particular the RP-specific encryption key
resolution can be slow and even fail depending on the network topology.
We propose that in an initial exchange, in particular OpenID authorization code
flows, we try to incorporate key and maybe even an attribute set in the ticket
exchange.

In order to mitigate this issue, this project is meant to investigate and implement how...
<ol>
<li> ... decryption keys can be added to an initial exchange in OpenID.</li>
<li> ... initial set(s) of attributes can be piggybacked in OpenID.</li>
</ol>
<br/>
Mentor: Martin Schanzenbach
</p>
</section>

<section>
<h4>re:claimID alternative GNS-based encryption</h4>
<p>
re:claimID is a decentralized identity system build on top of the GNU
Name System.
The initial design and implementation of re:claimID includes an attribute-based
encryption module in order to prevent unauthorized access to attributes in the
name system.
Our motivation for re:claimID was for it to be name system agnostic, which
means the design theoretically also works for other name systems such as
namecoin.
Other name systems often do not have built-in mechanisms in order to do this.
Hence, we implemented an ABE access control layer. Our ABE implementation
requires two third party libraries: libpbc and libgabe. While we could merge
libgabe into the gnunet service implementation of re:claimID, libpbc is a
rather large, third party library which lacks packaging in distributions and
for platforms.
On the other hand, GNS supports record data encryption using symmetric keys as
labels.
If we make the access control layer of re:claimID more generic in order to
support both ABE and GNS encryption, we could reduce the required depenencies.
This would result in gnunet packages to include re:claimID by default.

In short, the goals are to...
<ol>
<li> ... improve performance by reducing encryption overhead.</li>
<li> ... reduce dependencies.</li>
</ol>
<br/>
Mentor: Martin Schanzenbach
</p>
</section>

<section>
<h4>Enable all networking applications to run over GNUnet out of the box</h4>
<p>
One great problem of the current Internet is the lack of disintermediation. When people want to talk they need a chat service. When they want to share files they need a file transfer service. Although GNUnet already possesses quite advanced integration into Linux networking, a little extra work is needed for existing applications like irc, www, ftp, rsh, nntpd to run over it in a peer-to-peer way, simply by using a GNS hostname like friend.gnu. Once people have added a person to their GNS they can immediately message, exchange files and suchlike directly, with nothing but the GNUnet in the middle, using applications that have been distributed with unix systems ever since the 1980's. We can produce an OS distribution where these things work out of the box with the nicknames of people instead of cloud services. For more information and context, read <a href="https://bugs.gnunet.org/view.php?id=4625">bug id 4625</a>.
</p>
<p>
Mentors: lynX &amp; dvn
</p>
</section>
</article>
