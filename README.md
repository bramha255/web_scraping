# Web Scraping

- Error:
1. Check this when you have time \
--
Link: https://instrack.app/instagram/jennaortega/stats \
--
Error: ```<noscript>
    <strong>We're sorry but InsTrack doesn't work properly without JavaScript enabled. Please enable it to continue.</strong>
  </noscript>``` \
  -- Solution: that means the browser is javascript driver(a complex webpage)
  and work only with selenium 

2. Error: AttributeError: 'WebDriver' object has no attribute 'find_elements_by_class_name' \
Check the solution in- Due to new version upgrade in selenium: https://stackoverflow.com/questions/72773206/selenium-python-attributeerror-webdriver-object-has-no-attribute-find-el

3. Error: webdriver.Chrome('\chromedriver.exe') doesnt work anymore \
Selenium.webdriver - upgrade 4.0+ i believe 
https://stackoverflow.com/questions/64717302/deprecationwarning-executable-path-has-been-deprecated-selenium-python/71628814#71628814



  Note:
  
  1. XPath - is a Selenium technique to navigate through a page's HTML structure
  2. To keep the browser up brought by selenium run with shift+enter rather than entire file since it will close the broser after the code ends
  

