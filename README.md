# flask_screenshooter

Flask api screenshoting provided URL

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them:


```
Python
Selenium
Firefox version 56 or above
Chrome version 59 or above
```

### Installing

```
yum install python

yum install pip
pip install selenium

cat /etc/yum.repos.d/chrome.repo
[google-chrome]
name=google-chrome
baseurl=http://dl.google.com/linux/chrome/rpm/stable/x86_64
enabled=1
gpgcheck=1
gpgkey=https://dl.google.com/linux/linux_signing_key.pub

yum install google-chrome-stable
```
Full example using centos 7 TO_DO




## Running the tests

For testing purpose edit function call in app.py script and run directly

```
python app.py
```

### Break down into end to end tests

Running app.py scripot will perform single web screenshot and save in provided directory. 

```
Example. TO_DO
```



## Deployment

Add additional notes about how to deploy this on a live system
TO_DO

## Built With

* Python
* Selenium
* Chrome Webdriver
* Firefox Webdriver
* NodeJS PhantomJS

## Known problems
* Unfortunatly Library GTK3 which is nessesery for Chrome/Firefox in suitable version is avaible for centos 7.0 and above.
* PhantomJS is not suported any more and screenshot some pages incorectly.
* Script still can't find out end of loading all dynamic content. For now wait til timeout.

## Authors
* **Tomasz Michalowski** https://github.com/tmichalowski
