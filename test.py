#!/usr/bin/env python3
import dbm

with dbm.open('test', 'c') as db:
	db[b'counter'] = b'0'
