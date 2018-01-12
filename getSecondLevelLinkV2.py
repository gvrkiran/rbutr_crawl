from selenium import webdriver
import time;
driver = webdriver.Chrome("/usr/local/bin/chromedriver");

f = open("processed_links.txt");
lines = f.readlines();


for line in lines:
	line = line.strip();
	line_split = line.split("\t")
	url = line_split[1]
#        print url;

    	driver.get(url)
    	driver.find_element_by_class_name("address").click();
    	driver.switch_to.window(driver.window_handles[1])
    	time.sleep(5)
    	resolved_url = driver.current_url
        print line_split[0] + "\t" + resolved_url;

    # This is the link we want
    	driver.close()
    	driver.switch_to.window(driver.window_handles[0])
