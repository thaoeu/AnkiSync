# -*- coding: utf-8 -*-
# Copyright: Ankitects Pty Ltd and contributors
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html

import html
import re, sys, threading, time, subprocess, os, atexit
import  random
from anki.hooks import addHook, runHook
from anki.utils import  tmpdir, isWin, isMac, isLin
from anki.lang import _

# Shared utils
##########################################################################

_soundReg = r"\[sound:(.*?)\]"

def playFromText(text):
    for match in allSounds(text):
        # filename is html encoded
        match = html.unescape(match)
        play(match)

def allSounds(text):
    return re.findall(_soundReg, text)

def stripSounds(text):
    return re.sub(_soundReg, "", text)

def hasSound(text):
    return re.search(_soundReg, text) is not None

