## Prerequisites

api_automation project requires Python 3 and pip installed. 
To verify if you have both packages installed run the following commands:

`python3 --version` <br>
`pip --version`

If pip and Python 3 are installed you should see version of each package. Otherwise you'll see an error message.

If you do not have Python 3 and pip installed, use your operating system package manager to install both tools.<br>

On Mac OS you could use brew:

`brew install python`


## Install Requirements

`pip install -r requirements.txt`

If there is a permissions error add a `--user` flag to the end of the command.

## To Run

### Run all tests
change your working directory to api_automation project

`pytest --html=report.html --self-contained-html tests/`


## Report

After all test execution is done, you will see report.html in Reports folder in python_api_automation