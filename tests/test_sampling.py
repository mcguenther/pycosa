from unittest import TestCase
from . import THIS_DIR
import logging

from pycosa.features import FeatureModel
from pycosa.sampling import CoverageSampler

class TestCoverageSampler(TestCase):

    def setUp(self):
        self.fm_h2 = FeatureModel(THIS_DIR+'/feature_models/h2.dimacs')

    def test_sample(self):
        sampler = CoverageSampler(self.fm_h2)

        for t in range(1,4):
            logging.warning('Sampling {}-wise'.format(t))
            s = sampler.sample(t, negwise=False)
            logging.warning('found {} configurations'.format(len(s)))
            logging.warning('Sampling negative {}-wise'.format(t))
            s = sampler.sample(t, negwise=True)
            logging.warning('found {} configurations'.format(len(s)))
