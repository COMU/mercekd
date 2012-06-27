#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ConfigParser
import os

class ConfigClass:
    def __init__(self):
        config=ConfigParser.RawConfigParser()
        config.add_section("Sql Settings")
        config.set("Sql Settings","server","localhost")
        config.set("Sql Settings","user_name","mercekd_user")
        config.set("Sql Settings","passwd","")
        config.set("Sql Settings","database_name","mercekd_db")

        config_path=os.path.abspath("settings.config")
        config_file=open(config_path,'w')
        config.write(config_file)
        config_file.close()

if __name__=="__main__":
    config_class=ConfigClass()
