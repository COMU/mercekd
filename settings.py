#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ConfigParser
import os

class ConfigClass:
    def __init__(self):
        self.config=ConfigParser.RawConfigParser()
        self.config.add_section("Sql Settings")
        self.config.set("Sql Settings","server","localhost")
        self.config.set("Sql Settings","user_name","mercekd_user")
        self.config.set("Sql Settings","passwd","")
        self.config.set("Sql Settings","database_name","mercekd_db")

    def read_config(self, path):
        settings_path = os.path.abspath(path)
        config_file=open(settings_path,'w')
        self.config.write(config_file)
        config_file.close()

if __name__=="__main__":
    config_class=ConfigClass()