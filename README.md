scripts to crawl rbutr.com

The crawling involves multiple stages because of the weird way in which the site is set up (including redirects, proxy links, etc)

getData.py uses simple browser scraping to get the html content of the pages

You can process this html using processHTMLData.py, which outputs two links, tab separated. The original link and its rebuttal.

The rebuttal links is still an rbutr.com redirect link, so you have to do a second round of crawling.

This is done using getSecondLevelLinkContent.py

If you have questions, contact Kiran Garimella
