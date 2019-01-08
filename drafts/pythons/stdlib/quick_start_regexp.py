# -*- coding: utf-8 -*-

import logging
import unittest
import re

logger = logging.getLogger("UnitTestLogger")


class TestRegExp(unittest.TestCase):

    def test_boundary(self):
        pattern = re.compile("\W", re.U)
        s = "abc def~ghi!jkl@500%3bbb中华，人民dafdasfasfa<1机织60%棉40%涤女童裙子>%共和：国(hello)&[123]"
        print(pattern.split(s))


if __name__ == '__main__':
    import sys
    logging.basicConfig(stream=sys.stderr, level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
    unittest.main()
