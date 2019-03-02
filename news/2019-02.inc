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
Currently, we piggyback a small authorization ticket in an OpenID authorization
code.
This ticket is used by a relying party (e.g. website) to retrieve a decryption
key and user attributes.
However, the lookups can timeout and fail in GNS due to adverse network conditions or
empty caches.
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
<h4>reclaimID alternative GNS-based encryption</h4>
<p>
reclaimID is a decentralized identity system build on top of the GNU
Name System.
Currently, it uses an encryption scheme called attribute-based encryption.
However, through the clever use of GNS's built in record encryption,
it is possible to...
<ol>
<li> ... improve performance by reducing encryption overhead.</li>
<li> ... reduce dependencies.</li>
</ol>
<br/>
Mentor: Martin Schanzenbach
</p>
</section>
</article>
