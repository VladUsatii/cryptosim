#!/usr/bin/env python3
from flask import Flask, render_template
import sys, os, dbm
app = Flask(__name__)

def file_exists(rel_path):
	return os.path.exists(rel_path)

def read(path, key):
	with dbm.open(path, 'r') as db:
		return db.get(key, b'')

def write(path, key, value):
	with dbm.open(path, 'c') as db:
		db[key] = value

def append(path, key, new):
	with dbm.open(path, 'c') as db:
		curr = db.get(key, b'').decode('utf-8')
		values_set = set(curr.split(',')) if curr else set()
		values_set.add(new)
		db[key] = ','.join(values_set).encode('utf-8')

def remove(path, key, value):
	with dbm.open(path, 'c') as db:
		curr = db.get(key, b'').decode('utf-8')
		values_set = set(curr.split(',')) if curr else set()
		values_set.discard(value)
		db[key] = ','.join(values_set).encode('utf-8')

@app.route('/')
def main():
	with dbm.open('test', 'c') as db:
		"""
		db[b'counter'] = str(int(db.get(b'counter', b'0')) + 1).encode('utf-8')
		return f'This page has been visited {db[b"counter"].decode("utf-8")} times.'
		"""
		return render_template('main.html', posts=[(k, db[k]) for k in db.keys()])

if __name__ == '__main__':
	app.run(debug=True)
