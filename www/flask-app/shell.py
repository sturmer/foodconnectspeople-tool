#!/usr/bin/env python
# Get a console to enter flask commands (see 
# https://github.com/pallets/flask/wiki/Large-app-how-to)
import os
import readline
from pprint import pprint

from flask import *
from app import *

os.environ['PYTHONINSPECT'] = 'True'
