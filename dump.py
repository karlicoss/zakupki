#!/usr/bin/env python2
"Dumps some recent pages for further processing"

__author__    = "Dmitry Gerasimov"
__date__      = "2012"
__email__     = "karlicoss@gmail.com"

import urllib
import sys

prefix = "http://zakupki.gov.ru/pgz/public/action/orders/info/common_info/show?notificationId={}"


if len(sys.argv) > 1:
	from_ = int(sys.argv[1])
else:
	from_ = 1

to = 4000000

for i in range(from_, to):
	page = urllib.urlopen(prefix.format(i)).read()
	open("{}.http".format(i), "w").write(page)
