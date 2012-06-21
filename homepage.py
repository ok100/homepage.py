#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

### begin config ###

output = 'homepage.html'           # output html file
title = 'Speed Dial'               # title of the page
font = ['Monospace', '14px']       # font
separator = '>'                    # separator between group title and links
bgcolor = '#020202'                # background color
fgcolor = '#999999'                # foreground color
lnkcolor = '#999999'               # link color
hdrcolor = '#B3B3B3'               # group title color
sepcolor = '#4C4C4C'               # separator color

# add your links here
links = {
    'foo': [
        ['google', 'https://www.google.com/'],
        ['duckduckgo', 'http://duckduckgo.com/'],
        ['startpage', 'https://startpage.com/'],
    ],
    'bar': [
        ['wikipedia', 'http://en.wikipedia.org/wiki/Main_Page'],
        ['youtube', 'http://www.youtube.com/'],
    ],
    'blah': [
        ['wallbase', 'http://wallbase.cc/home'],
    ],
}

### end config ###

css_template = '''body {
  background-color: %s;
  color: %s;
  font-family: "%s";
  font-size: %s;
  font-weight: normal;
  margin-left: 7%%;
}
a:link,a:visited,a:active {
  text-decoration: none;
  color: %s;
  font-weight: normal;
}
a:hover {
  text-decoration: underline;
  color: %s;
  font-weight: normal;
}
table {
  border-spacing: 8px;
}
td:first-child {
  font-weight: bold;
  color: %s
}
td:nth-child(2) {
  font-weight: normal;
  color: %s;
}''' % (bgcolor, fgcolor, font[0], font[1],
        lnkcolor, lnkcolor, hdrcolor, sepcolor)

links_template = '<table valign="middle" border="0" \
                  width="100%" height="100%"><tr><td><table>'
for group in sorted(links):
    links_template += '<tr><td align="right">%s</td> \
                       <td>%s</td><td>' % (group, separator)
    for site in sorted(links[group]):
        links_template += '<a href="%s">%s</a> ' % (site[1], site[0])
    links_template += '</td></tr>'
links_template += '</table></td></tr></table>'

html_template = '''<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <title>%s</title>
  <link rel="stylesheet" type="text/css" href="style.css" />
</head>
<body>
  %s
</body>
</html>''' % (title, links_template)

f = open(output, 'w')
f.write(html_template)
f.close()

f = open('style.css', 'w')
f.write(css_template)
f.close()

os.system('tidy -utf8 -i -m -q -asxhtml %s' % output)
