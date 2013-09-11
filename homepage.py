#!/usr/bin/env python

# Copyright (c) 2013 Ondrej Kipila <ok100 at lavabit dot com>
# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING file for more details.

import argparse
import os
import runpy
from collections import OrderedDict


config = {
    'output_dir': os.environ['HOME'],
    'title': 'Start Page',
    'font': ('Monospace', '12pt'),
    'separator': '>',
    'colors': ('#020202', '#999999', '#B3B3B3', '#4C4C4C'),
    'links': OrderedDict([
        ('search', [
            ['google', 'https://www.google.com/'],
            ['duckduckgo', 'http://duckduckgo.com/'],
            ['startpage', 'https://startpage.com/'],
        ]),
        ('media', [
            ['youtube', 'http://www.youtube.com/'],
        ]),
        ('foo', [
            ['wikipedia', 'http://en.wikipedia.org/wiki/Main_Page'],
            ['wallbase', 'http://wallbase.cc/home'],
        ])
    ])
}


def parse_args():
    parser = argparse.ArgumentParser(prog='homepage.py')
    parser.add_argument('-c', '--config-file', help='path to an alternate config file')
    parser.add_argument('-o', '--output-dir', help='output directory')
    return parser.parse_args()


def main():
    args = parse_args()

    config_file = args.config_file or '%s/.config/homepage/homepage.conf' % os.environ['HOME']
    if os.path.exists(config_file):
        config.update((k, v) for k, v in runpy.run_path(config_file).items() if k in config)

    css = '''html, body {
      background-color: %s;
      font-family: "%s";
      font-weight: normal;
      margin-left: 7%%;
      height: 100%%;
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
      font-size: %s;
      border-spacing: 8px;
    }
    td {
      vertical-align: middle;
    }
    td:first-child {
      font-weight: bold;
      color: %s
    }
    td:nth-child(2) {
      font-weight: normal;
      color: %s;
    }''' % (config['colors'][0], config['font'][0], config['colors'][1], config['colors'][1],
            config['font'][1], config['colors'][2], config['colors'][3])

    links_html = ''
    for group in config['links']:
        links_html += '<tr><td align="right">%s</td><td>%s</td><td>' % (group, config['separator'])
        for site in config['links'][group]:
            links_html += '<a href="%s">%s</a> ' % (site[1], site[0])
        links_html += '</td></tr>'

    html = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
    <html>
      <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>%s</title>
        <link rel="stylesheet" type="text/css" href="style.css" />
      </head>
      <body>
        <table summary="container" border="0" width="100%%" style="height: 100%%"><tr><td><table summary="container">
          %s
        </table></td></tr></table>
      </body>
    </html>''' % (config['title'], links_html)

    if not os.path.exists(config['output_dir']):
        os.makedirs(config['output_dir'])
    with open(config['output_dir'] + '/homepage.html', 'w') as file:
        file.write(html)
    with open(config['output_dir'] + '/style.css', 'w') as file:
        file.write(css)

    os.system('tidy -utf8 -i -m -q -asxhtml %s' % config['output_dir'] + '/homepage.html')


if __name__ == "__main__":
    main()
