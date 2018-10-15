#/usr/bin/env python3


import click

from mechanicalsoup import StatefulBrowser
from pyf import map


@click.command()
@click.argument('word')
def examples(word):
    browser = StatefulBrowser()
    browser.open(f'https://skell.sketchengine.co.uk/run.cgi/concordance?lpos=&query={word}')
    fmt = lambda x: ''.join(x.findAll('td')[1].text.strip().splitlines())
    hits = browser.get_current_page().select('#conc_content tbody tr') | map(fmt)

    print('\n'.join(hits))


if __name__ == '__main__':
    examples()