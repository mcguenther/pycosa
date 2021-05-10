from unittest import TestCase
from pycosa.features import FeatureModel
import z3

class TestFeatureModel(TestCase):
    def test_shuffle(self):
        self.assertTrue(True)

'''
fm = FeatureModel('feature_models/h2.dimacs')
fm.constrain_min_enabled(['h2', 'MV_STORE', 'PAGE_STORE'], 2)
n_options = len(fm.feature_dict)
clauses = fm.clauses
target = fm.target

clauses = z3.And(clauses)

# for efficiency purposes, we use one solver instance
# for each possible distance from the origin
solvers = z3.Solver()
solvers.add(clauses)
solvers.add(fm.constraints)
if solvers.check() == z3.sat:
    print('satisfiable')
else:
    print('unsatisfiable')
#solvers[index].add(DistanceSampler.__hamming(origin, target, 1) == index)
'''