mercekd
=======

ISC DHCP log analyzer

installation
======

    $ sudo apt-get install git
    $ git clone git://github.com/COMU/mercekd.git
    $ git checkout develop
    $ python bootstrap.py
    $ ./bin/buildout
    $ ./bin/django runserver
    $ ./bin/start_master.sh
    $ ./bin/mongoimport --db leases --collection leases --file db/leases.json
    
