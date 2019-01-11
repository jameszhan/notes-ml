# -*- coding: utf-8 -*-
import os
import sys
import logging
import unittest

parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(parent_path)

from up_sampling import generate


logger = logging.getLogger("unittestLogger")


class TestUpSampling(unittest.TestCase):

    def test_less_equal(self):
        origin_text = "身高在150CM到160CM年龄不超过18周岁的同学"
        samples = generate(origin_text)
        # (150 ~ 160) * (1 ~ 18)
        self.assertEqual(198, len(samples))
        logger.info("{} => [\n{}\n]".format(origin_text, '\n'.join(samples)))


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(message)s')
    unittest.main()
