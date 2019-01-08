# -*- coding: utf-8 -*-

import logging
import unittest

logger = logging.getLogger("unittestLogger")


class TestPythonTrick(unittest.TestCase):

    def test_warning(self):
        import warnings

        def check_month(m, category=UserWarning):
            if 0 < m <= 12:
                logger.info("Current month is {0}".format(m))
            else:
                warnings.warn("month ({0}) is not between 1 and 12".format(m), category)

        check_month(0)
        check_month(12)
        warnings.filterwarnings(action='ignore', category=UserWarning)
        check_month(13)

    def test_counter(self):
        from collections import Counter
        a = [3, 6, 3, 6, 3, 2, 2, 5, 5, 5, 5, 5, 1, 1, 3, 2, 3, 5, 2]

        counter = Counter(a)
        logger.info("a is {0}".format(counter))
        self.assertEqual(5, len(counter.items()))
        self.assertEqual([(5, 6)], counter.most_common(1))
        self.assertEqual([(5, 6), (3, 5)], counter.most_common(2))


if __name__ == '__main__':
    import sys
    logging.basicConfig(stream=sys.stderr, level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

    unittest.main()
