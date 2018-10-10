#/usr/bin/env python3

import requests

from xml.etree import ElementTree
from tableprint import table
from pipe import Pipe
from pipe import as_list, first

LAST_90_DAYS_RATES_URL = 'https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist-90d.xml'


@Pipe
def map(xs: list, f) -> list:
    return [f(x) for x in xs]


@Pipe
def filter(xs: list, f) -> list:
    return [x for x in xs if f(x)]


def last_90_days_rates():
    r = requests.get(LAST_90_DAYS_RATES_URL)
    envelope = ElementTree.fromstring(r.content)

    ns = {
        'gesmes': 'http://www.gesmes.org/xml/2002-08-01',
        'eurofxref': 'http://www.ecb.int/vocabulary/2002-08-01/eurofxref',
    }

    data = envelope.findall('./eurofxref:Cube/eurofxref:Cube[@time]', ns)

    def fmt(d):
        currency = d | filter(lambda c: c.attrib['currency'] == 'BRL') | first
        return (d.attrib['time'], currency.attrib['rate'])

    return data | map(fmt)


if __name__ == '__main__':
    rates = last_90_days_rates()
    headers = ['Date', 'Rate']

    table(rates, headers)