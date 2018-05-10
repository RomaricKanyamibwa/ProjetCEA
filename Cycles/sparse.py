#!/usr/bin/env python3

from __future__ import division, print_function, absolute_import

import numpy as np
import pprint
from numpy.testing import assert_equal
from scipy.sparse.csgraph import *
from scipy.sparse import diags, csc_matrix, csr_matrix, coo_matrix

def test_graph_reverse_cuthill_mckee(A):
    graph = csr_matrix(A)
    perm = reverse_cuthill_mckee(graph)
    correct_perm = np.array([6, 3, 7, 5, 1, 2, 4, 0])
    assert_equal(perm, correct_perm)
    # Test int64 indices input
    graph.indices = graph.indices.astype('int64')
    graph.indptr = graph.indptr.astype('int64')
    perm = reverse_cuthill_mckee(graph, True)
    assert_equal(perm, correct_perm)
    return perm,graph

A = np.array([[1, 0, 0, 0, 1, 0, 0, 0],
                [0, 1, 1, 0, 0, 1, 0, 1],
                [0, 1, 1, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 1, 0],
                [1, 0, 1, 0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 1, 0, 1],
                [0, 0, 0, 1, 0, 0, 1, 0],
                [0, 1, 0, 0, 0, 1, 0, 1]], dtype=int)

B = test_graph_reverse_cuthill_mckee(A)

print(B[0])

print(B[1])

