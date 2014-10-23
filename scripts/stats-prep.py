#!/usr/bin/env python
import subprocess

inLOG = "/home/tevatron/.willie/logs/raw.log"
outLOG = "/home/tevatron/.willie/logs/chat.log"

pushChat = "grep PRIVMSG %s > %s" % (inLOG, outLOG)

def GenChat():
  subprocess.call(pushChat, shell=True)

GenChat()

