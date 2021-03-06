# IMPORTANT INFORMATION
The public API of [Telize](http://www.telize.com/) will permanently shut down on November 15th, 2015. More information can be found [here](http://www.cambus.net/adventures-in-running-a-free-public-api/).

This project is no longer useful.

# LizePy [![Build Status](https://travis-ci.org/alexandrevicenzi/lizepy.svg)](https://travis-ci.org/alexandrevicenzi/lizepy) [![Coverage Status](https://coveralls.io/repos/alexandrevicenzi/lizepy/badge.png)](https://coveralls.io/r/alexandrevicenzi/lizepy)

Python lib for Telize JSON IP and GeoIP REST API

### Requirements

Python 2.6 or later

### Install

`pip install lizepy`

### Usage

```python
import lizepy
```

#### Getting your IP

```python
ip = lizepy.get_ip()
print(ip)
>>> '0.0.0.0'
```


#### Getting GeoIP data

```python
geoip = lizepy.get_geoip('8.8.8.8') or lizepy.get_geoip()

# Return None if the field is not present.

geoip.ip or geoip['ip']
geoip.country_code or geoip['country_code']
geoip.country_code3 or geoip['country_code3']
geoip.country or geoip['country']
geoip.region_code or geoip['region_code']
geoip.region or geoip['region']
geoip.city or geoip['city']
geoip.postal_code or geoip['postal_code']
geoip.continent_code or geoip['continent_code']
geoip.latitude or geoip['latitude']
geoip.longitude or geoip['longitude']
geoip.dma_code or geoip['dma_code']
geoip.area_code or geoip['area_code']
geoip.asn or geoip['asn']
geoip.isp or geoip['isp']
geoip.timezone or geoip['timezone']
```
