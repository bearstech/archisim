Archi-Sim
=========


Test it
-------

Build :

    vagrant up

Enter :

    vagrant ssh

Go to source folder :

    cd /vagrant/archisim

Spawn some VM :

    ./spawn.py alpha beta gamma

List them :

    lxc list

Test them

    ssh root@beta

Install ping (the Debian is naked) :

    apt-get install iputils-ping

Ping some friends :

    ping alpha

Licence
-------

3 Terms BSD Licence © 2015 Mathieu Lecarme
