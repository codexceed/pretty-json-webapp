# Pretty-Json Webapp
[![codecov.io](https://codecov.io/github/codexceed/pretty-json-webapp/coverage.svg?branch=master)](https://codecov.io/gh/codexceed/pretty-json-webapp/branch/master)
![Code Quality & Build](https://github.com/codexceed/pretty-json-webapp/workflows/Code%20Quality%20&%20Build/badge.svg?branch=master)  
A flask based web app project for playing with json strings.

## Setup
Clone the project and install the requirements using
```bash
pip install -r requirements.txt
```
Modify the `run.py` script by changing the `host` and `port` arguments in the following line:
```python
app.run(host="127.0.0.1", port="5001", debug=True)
```