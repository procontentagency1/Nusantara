"""Run legacy and current browser checks against local HTTP, with installed Chromium."""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from threading import Thread
from pathlib import Path
import subprocess, tempfile, shutil, sys
class Quiet(SimpleHTTPRequestHandler):
    def log_message(self, *args): pass
server=ThreadingHTTPServer(('127.0.0.1',0),Quiet)
Thread(target=server.serve_forever,daemon=True).start()
browser=shutil.which('google-chrome') or shutil.which('chromium')
if not browser: raise RuntimeError('Install Chromium or Chrome first')
try:
    for path in sorted(Path('tests').glob('t[0-9]*.py')):
        source=path.read_text().replace('/usr/bin/google-chrome',browser).replace('/usr/bin/chromium',browser)
        source=source.replace("'file://' + __import__('os').path.abspath('index.html')",repr(f'http://127.0.0.1:{server.server_port}/'))
        source+='\nif globals().get("errs"): raise AssertionError(errs)\n'
        with tempfile.NamedTemporaryFile('w',suffix='.py') as file:
            file.write(source);file.flush()
            run=subprocess.run([sys.executable,file.name],text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        print(f'{path.name}: '+('PASS' if run.returncode==0 else 'FAIL'),flush=True)
        if run.returncode:
            print(run.stdout,flush=True);raise SystemExit(run.returncode)
finally: server.shutdown()
