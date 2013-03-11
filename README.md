![mercekd](http://i.imgur.com/IKDeu0I.png)
### ISC DHCP Log Analyzer

MercekDaemon is a free software tool for analysis of real-time ISC DHCP log data and interactive viewer that runs in browser.

## INSTALLATION

    $ sudo apt-get install git
    $ git clone git://github.com/COMU/mercekd.git
    $ cd mercekd
    $ python bootstrap.py
    $ ./bin/buildout

## STARTING MERCEKDAEMON

    $ ./bin/start_master.sh
    $ ./bin/django runserver

Now you can access mercekd via web. [http://127.0.0.1:8000]
That's it! Don't forget to start mercekdaemon from options page.

## LICENCE

MercekDaemon is available under the [GPLv3](http://gplv3.fsf.org/)
