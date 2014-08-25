#!/usr/bin/env python
import subprocess

peak = ['ln', '-s', '/home/tevatron/.willie/peak.db', '/home/tevatron/tevatron/willie/custom_modules/peak.db']
subprocess.Popen(peak)

