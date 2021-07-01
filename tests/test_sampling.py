from unittest import TestCase
from . import THIS_DIR
import logging

import matplotlib.pyplot as plt

import pandas as pd
from pycosa.features import FeatureModel
from pycosa.sampling import CoverageSampler, NaiveRandomSampler, DiversityPromotionSampler, DistanceSampler

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


class TestSampler(TestCase):

    def setUp(self):
        self.fm = FeatureModel(THIS_DIR + '/feature_models/h2.dimacs')

    def test_exclude_configurations(self):
        n = 50
        sampler1 = NaiveRandomSampler(self.fm)
        sample1 = sampler1.sample(n)

        sampler_without_exclusion = NaiveRandomSampler(self.fm)
        sample_without_exclusion = sampler_without_exclusion.sample(n)

        sampler_with_exclusion = NaiveRandomSampler(self.fm)
        sampler_with_exclusion.exclude_configurations(sample1)
        sample_with_exclusion = sampler_with_exclusion.sample(n)

        sample1_hash = pd.util.hash_pandas_object(sample1)
        sw = pd.util.hash_pandas_object(sample_with_exclusion)
        swo = pd.util.hash_pandas_object(sample_without_exclusion)

        for i in range(n):
            self.assertTrue(sample1_hash.iloc[i] == swo.iloc[i])
            self.assertFalse(sample1_hash.iloc[i] == sw.iloc[i])


class TestSampler(TestCase):

    def setUp(self):
        self.fm = FeatureModel(THIS_DIR + '/feature_models/h2.dimacs')

    def test_set_partial_configurations(self):
        sampler = DistanceSampler(self.fm)
        sampler.set_partial_configurations(['MV_STORE'], ['PAGE_STORE'])
        sample = sampler.sample(100)
        print(sample)

