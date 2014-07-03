#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Alexandre Vicenzi'
__version__ = '0.3.2'
__license__ = 'MIT'

'''
The MIT License (MIT)

Copyright (c) 2014 Alexandre Vicenzi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import json
import sys

if sys.version_info[0] == 2:
    from urllib2 import Request, urlopen, HTTPError
elif sys.version_info[0] == 3:
    from urllib.request import Request, urlopen
    from urllib.error import HTTPError
else:
    raise ImportError('Module for urllib not found.')

if sys.version_info[0] < 3:
    from cStringIO import StringIO
else:
    from io import StringIO

TELIZE_BASE_URL = 'http://www.telize.com'
TELIZE_BASE_URL_IP = TELIZE_BASE_URL + '/jsonip'
TELIZE_BASE_URL_GEOIP = TELIZE_BASE_URL + '/geoip/'

class GeoIP:

    def __init__(self):
        self.ip = None             # (Visitor IP address, or IP address specified as parameter)
        self.country_code = None   # (Two-letter ISO 3166-1 alpha-2 country code)
        self.country_code3 = None  # (Three-letter ISO 3166-1 alpha-3 country code)
        self.country = None        # (Name of the country)
        self.region_code = None    # (Two-letter ISO-3166-2 state / region code)
        self.region = None         # (Name of the region)
        self.city = None           # (Name of the city)
        self.postal_code = None    # (Postal code / Zip code)
        self.continent_code = None # (Two-letter continent code)
        self.latitude = None       # (Latitude)
        self.longitude = None      # (Longitude)
        self.dma_code = None       # (DMA Code)
        self.area_code = None      # (Area Code)
        self.asn = None            # (Autonomous System Number)
        self.isp = None            # (Internet service provider)
        self.timezone = None       # (Time Zone)

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)

    def __getitem__(self, key):
        return self.__dict__.get(key)

def __json(value):
    try:
        return json.loads(value)
    except ValueError:
        return None

def __get(url):

    req = Request(url, headers={ 'Accept': 'application/json' })

    try:
        response = urlopen(req)
    except HTTPError as e:
        response = e

    if response.headers.get('Content-Encoding') == 'gzip':
        buf = StringIO(response.read())
        f = gzip.GzipFile(fileobj=buf)
        body = f.read()
    else:
        body = response.read()

    return {'code' : response.code, 'body' : __json(body.decode('utf-8'))}

def get_ip():
    '''
        Returns the visitor IP address (IPv4 or IPv6).
        :return The visitor IP address.
        :rtype str, unicode or None
    '''
    response = __get(TELIZE_BASE_URL_IP)

    if response['code'] == 200:
        return response['body'].get('ip')
    else:
        return None

def get_geoip(ip=None):
    '''
        Return the visitor GeoIP data or the data for the given IP.
        :return GeoIP data for the visitor IP or the giver IP.
        :rtype GeoIP or None
    '''
    url = TELIZE_BASE_URL_GEOIP

    if ip:
        assert(type(ip) == str)
        url = url + ip

    response = __get(url)

    if response['code'] == 200:

        b = response['body']
        g = GeoIP()

        g.ip = b.get('ip')
        g.country_code = b.get('country_code')
        g.country_code3 = b.get('country_code3')
        g.country = b.get('country')
        g.region_code = b.get('region_code')
        g.region = b.get('region')
        g.city = b.get('city')
        g.postal_code = b.get('postal_code')
        g.continent_code = b.get('continent_code')
        g.latitude = b.get('latitude')
        g.longitude = b.get('longitude')
        g.dma_code = b.get('dma_code')
        g.area_code = b.get('area_code')
        g.asn = b.get('asn')
        g.isp = b.get('isp')
        g.timezone = b.get('timezone')

        return g
    else:
        return None

if __name__ == '__main__':
    print(get_ip())
    print(get_geoip())