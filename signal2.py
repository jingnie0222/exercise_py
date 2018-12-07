#!/usr/bin/python/

import os
import signal

os.kill(13810,signal.SIGTERM)

os.kill(13810, signal.SIGUSR1)
