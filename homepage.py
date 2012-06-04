#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os

### begin config ###

output = 'homepage.html'           # output html file
title = 'OK100'                    # title of the page
font = ['Monospace', '14px']       # font
bgcolor = '#020202'                # background color
fgcolor = '#999999'                # foreground color
lnkcolor = '#999999'               # link color
hdrcolor = '#B3B3B3'               # group title color
sepcolor = '#4C4C4C'               # separator color

# add your links here
links = {
    'admin': [
        ['cups', 'http://localhost:631/'],
        ['dd-wrt', 'http://192.168.1.1/'],
        ['diskstation', 'http://192.168.1.147/'],
        ['transmission', 'http://127.0.0.1:9091/transmission/web/'],
        ['dropbox', 'https://www.dropbox.com/home'],
    ],
    'arch': [
        ['wiki', 'https://wiki.archlinux.org/index.php/Main_Page'],
        ['forums', 'https://bbs.archlinux.org/index.php'],
    ],
    'art': [
        ['deviantart', 'http://www.deviantart.com/'],
        ['simpledesktops', 'http://simpledesktops.com/'],
        ['wallbase', 'http://wallbase.cc/home'],
        ['omploader', 'http://ompldr.org/'],
    ],
    'dev': [
        ['github', 'https://github.com/ok100'],
    ],
    'media': [
        ['last.fm', 'http://www.last.fm/home'],
        ['youtube', 'http://www.youtube.com/'],
    ],
    'misc': [
        ['shmú', 'http://www.shmu.sk/sk/?page=1'],
    ],
    'linux': [
        ['abclinuxu', 'http://www.abclinuxu.cz/'],
        ['root', 'http://www.root.cz/'],
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
    links_template += '<tr><td align="right">%s</td><td>></td><td>' % group
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
