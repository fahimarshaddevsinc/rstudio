# Rstudio

## Selenium-Pytest-Automation-Framework Demo
### Objective:
RStudio https://rstudio.cloud/ is a service designed to make it easy for professionals, hobbyists, trainers, teachers, and students to do, share, teach, and learn data science using R. Our main objective is:

1. Creating a Space

2. Creating a Project within the Space

3. Verifying that the RStudio IDE loads

Selenium automation with python is used to create/login user on RStudio, Add New Workspace, Create new RStudio project within that space and verify RStudio IDE loads  in browser.

### Installation:
You can use any IDE to implement and run automated script using python. VSCode and PyCharm are recommended.
#### First install python 

* For Windows: 
Download python from this link https://www.python.org/ description of how to install python is mention in this page https://www.tutorialspoint.com/how-to-install-python-in-windows 

* For Linux: 
Run this command into your terminal `sudo apt-get install python3`
#### IDE: 
You can use any IDE to implement and run automated script using python. 
Download Pycharm https://www.jetbrains.com/pycharm/download/ or VSCode https://code.visualstudio.com/download 

#### Install Dependencies:
In the terminal of source code install requirement.txt file by running this command:

 `$ pip install -r requirement.txt`
 
 ### Run
 Run project using this command into project terminal
`python -m pytest --browser=chrome --html=reports/report.html`
* The --browser flag tells which browser to run on. The three option are chrome, firefox and edge at the moment.
* The --html flag directs to the folder in which the report is to be saved and the report name.

