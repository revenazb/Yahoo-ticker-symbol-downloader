#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
	name = 'Yahoo-ticker-downloader',
	version = '0.1.2',
	author = 'Benny',
	author_email = 'Benny@GMX.it',
	url='https://github.com/Benny-/Yahoo-ticker-symbol-downloader',
	license='LICENSE.txt',
	description='A python3 script to scrape ticker symbols from yahoo finance',
	packages = find_packages(),
	scripts = ['YahooTickerDownloader.py'],
    install_requires=[
        "beautifulsoup4 >= 4.2.1",
        "requests >= 2.2.1",
    ],
)

