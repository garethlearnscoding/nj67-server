#!/usr/bin/env python
"""
Script to be run on the server
"""

from pathlib import Path
from zipfile import ZipFile
from datetime import datetime
from flask import Flask, request, send_from_directory

app = Flask(__name__)

cwd = Path(__file__).parent

@app.route('/')
def index():
    return send_from_directory(Path(__file__).parent / 'static', 'index.html')

@app.route('/upload', methods=['POST'])
def get_ans():
    p = cwd / f'output/{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_{request.remote_addr}.zip'
    out_dir = p.with_suffix('')
    print(request.files.keys())
    request.files['file'].save(p)
    with ZipFile(p) as zip_ref:
        zip_ref.extractall(out_dir)
    contents = tuple(out_dir.iterdir())
    if len(contents) == 1 and contents[0].is_dir():
        try:
            for child in contents[0].iterdir():
                child.rename(out_dir / child.name)
                contents[0].rmdir()
        except OSError: 
            return "Error: invalid zip file", 500
    p.unlink()
    return 'ok', 200

if __name__ == '__main__':
    app.run(debug=True)