from unittest import TestCase
from . import THIS_DIR
import logging

from pycosa.features import FeatureModel
from pycosa.sampling import CoverageSampler, NaiveRandomSampler, DiversityPromotionSampler

'''
each sampling strategy is tested for
- should result in unique set of configurations with N samples
- should be deterministic via seed (two repetitions yield same sample)
- should perform consistently on randomized data sets (feature models)

'''


class TestCoverageSampler(TestCase):

    def setUp(self):
        self.fm_h2 = FeatureModel(THIS_DIR + '/feature_models/h2.dimacs')

    def test_sample(self):
        sampler = CoverageSampler(self.fm_h2)

        for t in range(1, 3):
            logging.warning('Sampling {}-wise'.format(t))
            s = sampler.sample(t, negwise=False)
            logging.warning('found {} configurations'.format(len(s)))
            logging.warning('Sampling negative {}-wise'.format(t))
            s = sampler.sample(t, negwise=True)
            logging.warning('found {} configurations'.format(len(s)))


class TestNaiveRandomSampler(TestCase):

    def setUp(self):
        self.fm_h2 = FeatureModel(THIS_DIR + '/feature_models/h2.dimacs')

    def test_sample(self):
        sampler = NaiveRandomSampler(self.fm_h2)

        sample = sampler.sample(1000)
        length = sample.shape[0]
        sample = sample.drop_duplicates()
        self.assertTrue(length == sample.shape[0])


class TestDiversityPromotionSampler(TestCase):

    def setUp(self):
        self.fm_h2 = FeatureModel(THIS_DIR + '/feature_models/h2.dimacs')

    def test_sample(self):
        sampler = DiversityPromotionSampler(self.fm_h2)

        sample = sampler.sample(100)
        length = sample.shape[0]
        sample = sample.drop_duplicates()
        self.assertTrue(length == sample.shape[0])
