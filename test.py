import most_active_cookie
import subprocess
import sys

def test_wrong_date_format():
    '''Wrong input format'''
    interpreter_location = sys.executable
    csv_file = "cookies.log"
    targetDay = "12/09/2020"
    output = subprocess.run([interpreter_location, "most_active_cookie.py", csv_file, "-d", targetDay], encoding='utf-8')
    assert(output.returncode != 1)

def test_wrong_date_len():
    '''Wrong input format'''
    interpreter_location = sys.executable
    logFile = "cookies.log"
    targetDay = "12-09-02020"
    output = subprocess.run([interpreter_location, "most_active_cookie.py", logFile, "-d", targetDay], encoding='utf-8')
    assert(output.returncode != 1)

def test_one_cookie():
    '''Only one matching cookie'''
    interpreter_location = sys.executable
    logFile = "cookies.log"
    targetDay = "2018-12-09"
    output = subprocess.run([interpreter_location, "most_active_cookie.py", logFile, "-d", targetDay], encoding='utf-8')
    assert(output.returncode == 1)

def test_multiple_cookies():
    '''Multiple matching cookies.'''
    interpreter_location = sys.executable
    logFile = "cookies.log"
    targetDay = "2018-12-07"
    output = subprocess.run([interpreter_location, "most_active_cookie.py", logFile, "-d", targetDay], capture_output=True, encoding='utf-8')
    targetOutput = "4sMM2LxV07bPJzwf\nfbcn5UAVanZf6UtG\n"
    assert(output.stdout == targetOutput)

def test_no_cookie():
    '''No matching cookie'''
    interpreter_location = sys.executable
    logFile = "cookies.log"
    targetDay = "2019-12-22"
    output = subprocess.run([interpreter_location, "most_active_cookie.py", logFile, "-d", targetDay], capture_output=True, encoding='utf-8')
    targetOutput = ""
    assert(output.stdout == targetOutput)