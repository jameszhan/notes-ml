# -*- coding: utf-8 -*-

import logging
import unittest

logger = logging.getLogger("unittestLogger")

class TestPythonTrick(unittest.TestCase):

    def test_counter(self):
        from collections import Counter
        a = [3, 6, 3, 6, 3, 2, 2, 5, 5, 5, 5, 5, 1, 1, 3, 2, 3, 5, 2]

        counter = Counter(a)
        logger.info("counter is {0}".format(counter))
        self.assertEqual(5, len(counter.items()))
        self.assertEqual([(5, 6)], counter.most_common(1))
        self.assertEqual([(5, 6), (3, 5)], counter.most_common(2))


if __name__ == '__main__':
    import sys
    logging.basicConfig(stream=sys.stderr, level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
    unittest.main()


