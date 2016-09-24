#!/usr/bin/env python
# -*- coding: utf-8 -*-
# project = https://github.com/Xyntax/POC-T
# author = i@cdxy.me

import ConfigParser
from lib.core.data import paths, logger


class ConfigFileParser:
    def _get_option(self, section, option):
        try:
            cf = ConfigParser.ConfigParser()
            cf.read(paths.CONFIG_PATH)
            return cf.get(section=section, option=option)
        except ConfigParser.NoOptionError:
            logger.error('Lack of essential options, please check your config-file.')
            return ''

    def ZoomEyeEmail(self):
        return self._get_option('zoomeye', 'email')

    def ZoomEyePassword(self):
        return self._get_option('zoomeye', 'password')

    def ShodanApikey(self):
        return self._get_option('shodan', 'api_key')

    def BingApikey(self):
        return self._get_option('bing', 'api_key')

    def CloudEyeApikey(self):
        return self._get_option('cloudeye', 'api_key')

    def ColudEyePersonaldomain(self):
        return self._get_option('cloudeye', 'personal_domain')

    def GoogleProxy(self):
        return self._get_option('google', 'proxy')

    def GoogleDeveloperKey(self):
        return self._get_option('google', 'developer_key')

    def GoogleEngine(self):
        return self._get_option('google', 'search_engine')
