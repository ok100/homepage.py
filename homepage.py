#!/usr/bin/env python
# -*- coding: utf-8 -*-

########## begin config ##########

output = 'homepage.html'      # output file
title = 'Speed Dial'          # page title
font = ('Monospace', '14px')  # font
separator = '>'               # separator between group title and links
colors = (
    '#020202',  # background
    '#999999',  # links
    '#B3B3B3',  # group title
    '#4C4C4C',  # separator
)

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

########## end config ##########

import os

css = '''body {
  background-color: %s;
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
}''' % (colors[0], font[0], font[1], colors[1], colors[1], colors[2], colors[3])

links_html = ''
for group in sorted(links):
    links_html += '<tr><td align="right">%s</td><td>%s</td><td>' % (group, separator)
    for site in sorted(links[group]):
        links_html += '<a href="%s">%s</a> ' % (site[1], site[0])
    links_html += '</td></tr>'

html = '''<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <title>%s</title>
  <link rel="stylesheet" type="text/css" href="style.css" />
</head>
<body>
  <table valign="middle" border="0" width="100%%" height="100%%"><tr><td><table>
    %s
  </table></td></tr></table>
</body>
</html>''' % (title, links_html)

with open(output, 'w') as file:
    file.write(html)
with open('style.css', 'w') as file:
    file.write(css)

os.system('tidy -utf8 -i -m -q -asxhtml %s' % output)
