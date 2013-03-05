![mercekd](http://i.imgur.com/IKDeu0I.png)
### ISC DHCP Log Analyzer

MercekDaemon is a free software tool for analysis of real-time ISC DHCP log data and interactive viewer that runs in browser.

## INSTALLATION

    $ sudo apt-get install git
    $ git clone git://github.com/COMU/mercekd.git
    $ cd mercekd
    $ python bootstrap.py
    $ ./bin/buildout
    $ ./bin/django runserver
    $ ./bin/start_master.sh
    $ python mercekd/daemon.py

That's it! Don't forget to check out 127.0.0.1:8000

## LICENCE

MercekDaemon is available under the [GPLv3](http://gplv3.fsf.org/)