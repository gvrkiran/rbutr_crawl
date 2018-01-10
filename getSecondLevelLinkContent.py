# script to get content from the rbuttr link to parse the (partial) url.

import sys,urllib2,time;
from bs4 import BeautifulSoup;

f = open("processed_links.txt");
#f = open("remaining.txt");
lines = f.readlines();

count = 1;
for line in lines:
    line = line.strip();
    line_split = line.split("\t");
    url = line_split[1];
    try:
        content = urllib2.urlopen(url).read();
        soup = BeautifulSoup(content);

        mydivs1 = soup.find_all("div",{ "class" : "contentRight" });
        link = mydivs1[0].find_all("a",{"class":"address"});
        print line_split[0] + "\t" + link[0].contents[0];
        print >> sys.stderr, count;
        count += 1;
    except:
        print >> sys.stderr, "err", url;
        pass;
    time.sleep(1);
