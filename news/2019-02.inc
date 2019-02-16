<h3>
<A NAME="gsoc2019"></A>2019-02: Topics for GSoC 2019
</h3>
<h4>Android Port</h4>
<p>
It is time for GNUnet to run properly on Android.  Note that
GNUnet is written in C, and this is not about rewriting
GNUnet in Java, but about getting the C code to run on Android.
<br>
Mentor: <a href="https://www.goebel-consult.de/">Hartmut Goebel</a>
</p>

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

<h4>Migrate gnunet-qr from Python 2.7 to C using libzbar</h4>
<p>
Python 2.7 is reaching its end-of-life, and we want to get rid
of the dependency on Python. The existing gnunet-qr tool is a
rather simple wrapper around python-zbar, which itself wraps
libzbar. The goal of this project is to directly use libzbar
to scan QR codes for GNUnet / the GNU Name System (see
also <a href="https://gnunet.org/bugs/view.php?id=5562">#5562</a>).
<br>
Mentor: Christian Grothoff
</p>


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
This project also includes two separate, smaller tasks:
<ul>
<li> Performance improvements to the out-of-band authorization flow (OpenID Connect)</li>
<li> A webextension which allows reclaimID to be used without the need of a GNS proxy.
</ul>
The two smaller tasks are optional and may be dropped in case the student
encounters any unforseen complications when implementing the main task.
<br>
Mentor: Martin Schanzenbach
</p>
