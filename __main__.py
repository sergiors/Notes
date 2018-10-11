#/usr/bin/env python3

import requests
import calendar
import datetime
import urwid

from xml.etree import ElementTree
from tabulate import tabulate
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

    def fmt(d):
        currency = d | filter(lambda c: c.attrib['currency'] == 'BRL') | first
        return (d.attrib['time'], 'BRL ' + currency.attrib['rate'])

    return envelope.findall('./eurofxref:Cube/eurofxref:Cube[@time]', ns) | map(fmt)


if __name__ == '__main__':
    now = datetime.datetime.now()

    rates = last_90_days_rates()[:7]

    calendar = urwid.Text(calendar.month(now.year, now.month))
    button = urwid.Button(u'Exit or Press q')
    table = urwid.Text(
        tabulate(rates, headers=['Date', 'Rate'], tablefmt='orgtbl'))
    div = urwid.Divider()
    columns = urwid.Columns([
        urwid.Pile([urwid.Text(now.isoformat()), div, calendar]),
        urwid.Pile([urwid.Text('Euro History'), div, table])
    ])
    view = urwid.Filler(urwid.Pile([columns, button]), valign='top')

    def on_exit_clicked(button):
        raise urwid.ExitMainLoop()

    def exit_on_q(key):
        if key in ('q', 'Q'):
            raise urwid.ExitMainLoop()

    urwid.connect_signal(button, 'click', on_exit_clicked)

    urwid.MainLoop(view, unhandled_input=exit_on_q).run()