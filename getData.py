from selenium import webdriver;
import time,random;

driver = webdriver.Chrome();

for i in range(1,500):
        url = "http://rbutr.com/rbutr/WebsiteServlet?requestType=browse";
    	driver.get(url);
        html_source = driver.page_source.encode('utf-8');
        out = open("data/page" + str(i), "w");
        out.write(html_source);
        out.close();
        link = driver.find_element_by_link_text('Next Page >>');
        link.click();
        random_num = random.randint(5,15);
        time.sleep(random_num);
