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
