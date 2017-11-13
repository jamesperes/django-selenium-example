## django-selenium-example

An example Django project for selenium test implementation.

Python 2 

### Test Case Scenarios
* Verifies user registration.
* Verifies user login.
* Creates active todo object with an authenticated user.
* Changes the status of todo objects from active to completed
* Changes the status of todo objects from completed to active.



###Demo in Firefox 
![selenium-demo](https://github.com/erdem/django-selenium-example/blob/master/demo.gif?raw=true)

###Demo in PhantomJS

![selenium-demo-phantom](https://github.com/jamesperes/django-selenium-example/blob/master/phantomjs.jpg?raw=true)

Take screenshots

    self.browser.save_screenshot('sc002.jpg')


###Install 

    pip install -r requirements.txt

###Install PhantomJS 

http://phantomjs.org/download.html

###Usage

    python manage.py test

