from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox();
driver.get('http://192.168.234.1');
elem = driver.find_element_by_id("LonginUsername");
elem.clear();
elem.send_keys("admin");
elem = driver.find_element_by_id("LonginPassword");
elem.clear();
elem.send_keys("admin");
elem = driver.find_element_by_name("Login");
elem.clear();
elem.send_keys(Keys.RETURN);
