          <h3>10-9-2014: PayPal accounts hacked with a click</h3>
          <p>Yasser Ali reports a now patched vulnerability in PayPal that would
             have allowed him to reset other user's passwords and take over their
             accounts. This is unlikely to be the last vulnerability found in
             account-based payment systems.<br>
             In Taler, customers do not have accounts with usernames, passwords
             or associated e-mail addresses.  Instead, Taler uses reserves which
             are represented by a private key on the owner's computer.  Users
             create a reserve by depositing currency at a Taler exchange, and can then
             withdraw digital coins from that reserve using the respective private
             key.  There is no limit on the number of reserves a user can have, and
             even hacking the Taler exchange would not provide an adversary with access to
             user's reserves (as the Taler exchange does not have the private keys).
             Stealing in Taler requires breaking into each customer's computer to
             extract the reserve keys or the coins from the digital wallet.
          </p>
          <p><a class="btn btn-info" href="http://yasserali.com/hacking-paypal-accounts-with-one-click/" role="button">Source</a></p>
