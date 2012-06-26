#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ConfigParser
config=ConfigParser.RawConfigParser()
config.add_section("Sql Settings")
config.set("Sql Settings","server","localhost")
config.set("Sql Settings","user_name","mercekd_user")
config.set("Sql Settings","passwd","")
config.set("Sql Settings","database_name","mercekd_db")

config_file=open("settings.config",'w')
config.write(config_file)
config_file.close()