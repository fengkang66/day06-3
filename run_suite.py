import unittest

import scripts
from tools import HTMLTestReportCN
from tools.HTMLTestReportCN import HTMLTestRunner

suit = unittest.defaultTestLoader.discover("./scripts")
with open("./report/report.html","wb") as f:
    HTMLTestRunner(stream=f).run(suit)