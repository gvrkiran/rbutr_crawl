# script to process the raw html data from rbutr and get the opposing urls

import sys,glob;
from bs4 import BeautifulSoup;

for infile in glob.glob("html_data/page*"):
    print >> sys.stderr, infile;
    f = open(infile);
    line = f.read().strip();
    soup = BeautifulSoup(line);
    tables = soup.findChildren('table')[0];
    rows = tables.findChildren(['th', 'tr']);
    for row in rows:
        rows1 = row.findChildren('td');
        row1 = rows1[0];
        row2 = rows1[2];
        mydivs1 = row1.find_all("a",{ "class" : "hoverUrlImage" });
        mydivs2 = row2.find_all("a",{ "class" : "hoverUrlImage" });

        try:
            print str(mydivs1[0]['href']).encode('utf-8') + "\t" + str(mydivs2[0]['href']).encode('utf-8');
        except:
            print >> sys.stderr, "f";
