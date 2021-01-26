from typing import Sequence
import logging
import z3
import numpy as np
import random 
from bitarray.util import int2ba
from numpy import dtype

class FeatureModel(object):
    '''
    
    '''

    def __init__(self, src: str, shuffle_seed: int = 0):

        self.clauses_raw, feature_dict = FeatureModel.__parse_dimacs(src)
                
        self.clauses, self.target = FeatureModel.__convert_dimacs_to_bitvec(self.clauses_raw, len(feature_dict))
        self.feature_dict = feature_dict
        
    def shuffle(self, random_seed: int = 0):
        """
        Re-shuffles the composition of the feature model CNF
        """
        # shuffle feature model clauses (used for div. promotion)
        random.seed(random_seed)
        clauses_ = []
        for clause in self.clauses_raw:
            clause_ = random.sample(clause, len(clause))
            clauses_.append(clause_)
        clauses = random.sample(clauses_, len(clauses_))
            
        self.clauses, self.target = FeatureModel.__convert_dimacs_to_bitvec(clauses, len(self.feature_dict))
        
    @staticmethod
    def __parse_dimacs(path: str) -> (Sequence[Sequence[int]], dict):
        '''
        :param path:
        :return:
        '''
    
        dimacs = list()
        dimacs.append(list())
        with open(path) as mfile:
            lines = list(mfile)
    
            # parse names of features from DIMACS comments (lines starting with c)
            feature_lines = list(filter(lambda s: s.startswith("c"), lines))
    
            # remove comments
    
        dimacs = list()
        dimacs.append(list())
        with open(path) as mfile:
            lines = list(mfile)
    
            # parse names of features from DIMACS comments (lines starting with c)
            feature_lines = list(filter(lambda s: s.startswith("c"), lines))
            feature_names = dict(map(lambda l: (int(l.split(" ")[1]), l.split(" ")[2].replace("\n", "")), feature_lines))
    
            # remove comments
            lines = list(filter(lambda s: not s.startswith("c"), lines))

            for line in lines:
                tokens = line.split()
                if len(tokens) != 0 and tokens[0] not in ("p", "c"):
                    for tok in tokens:
                        lit = int(tok)
                        if lit == 0:
                            dimacs.append(list())
                        else:
                            dimacs[-1].append(lit)
            assert len(dimacs[-1]) == 0
            dimacs.pop()
        
        return dimacs, feature_names
    
    @staticmethod
    def __convert_dimacs_to_bitvec(dimacs: Sequence[Sequence[int]], n_options: int) -> (Sequence[z3.Or], z3.BitVec):
        
        clauses = []
        target = z3.BitVec('target', n_options)

        # add clauses of variability model
        for clause in dimacs:
            c = []
            for opt in clause:
                opt_sign = 1 if opt >= 0 else 0
                optid = n_options - abs(opt)
                c.append(z3.Extract(optid, optid, target) == opt_sign)
    
            clauses.append(z3.Or(c))
    
        return clauses, target
    
    @staticmethod
    def config_to_int(config: np.ndarray) -> int:
        '''
        :param config:
        :return:
        '''
        pass
    
    @staticmethod
    def int_to_config(i: int, n_options: int) -> np.ndarray:
        '''
        :param i:
        :param n_options:
        :return:
        '''

        without_offset = np.array([int(x) for x in np.binary_repr(i)])
        offset = n_options - len(without_offset)
        binary = np.append(np.zeros(dtype=int, shape=offset), without_offset)
        
        return binary
