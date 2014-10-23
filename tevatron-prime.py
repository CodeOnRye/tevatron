#!/usr/bin/env python
import subprocess
from sys import argv

script, job = argv

peak = ['ln', '-s', '/home/tevatron/.willie/peak.db', '/home/tevatron/tevatron/willie/custom_modules/peak.db']
karma = ['ln', '-s', '/home/tevatron/.willie/karma.db', '/home/tevatron/tevatron/willie/custom_modules/karma.db']
quotes = ['ln', '-s', '/home/tevatron/.willie/quote.db', '/home/tevatron/tevatron/willie/custom_modules/quote.db']

def SymLinks():
    subprocess.Popen(peak)
    subprocess.Popen(karma)
    subprocess.Popen(quotes)

if job == 'prime-db':
  SymLinks()
else:
    print "You need an argument..."
