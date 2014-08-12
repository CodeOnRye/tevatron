#!/usr/bin/env python
import subprocess

peak = ['ln', '-s', '/home/tevatron/.willie/peak.db', '/home/tevatron/tevatron/willie/custom_modules/peak.db']
karma = ['ln', '-s', '/home/tevatron/.willie/karma.db', '/home/tevatron/tevatron/willie/custom_modules/karma.db']
subprocess.Popen(peak)
subprocess.Popen(karma)

