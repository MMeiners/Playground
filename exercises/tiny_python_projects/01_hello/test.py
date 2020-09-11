#! python
"""tests for hello.py"""

# edits: book's author was calling 'python3' but not found in venv... copied python.exe to python3.exe in venv dir.
# Windows generally doesn't have a python3 since it doesn't ship with Python 2 like Mac/Linux.
# Updated the shebang line but unsure if needed in Windows unless using py launcher for some reason.
# Updated prg string to use backslash instead of slash.
# Seriously considering installing WSL so I can use bash and avoid changing things to work in cmd

import os
from subprocess import getstatusoutput, getoutput

prg = '.\\hello.py'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_runnable():
    """Runs using python3"""

    out = getoutput(f'python3 {prg}')
    assert out.strip() == 'Hello, World!'


# --------------------------------------------------
def test_executable():
    """Says 'Hello, World!' by default"""

    out = getoutput(prg)
    assert out.strip() == 'Hello, World!'


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_input():
    """test for input"""

    for val in ['Universe', 'Multiverse']:
        for option in ['-n', '--name']:
            rv, out = getstatusoutput(f'{prg} {option} {val}')
            assert rv == 0
            assert out.strip() == f'Hello, {val}!'
