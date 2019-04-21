from unittest import TestCase

from model_spaces.core.covariance_grammar import CovarianceGrammar


class TestCovarianceGrammar(TestCase):

    def test_covariance_grammar_create(self):
        pass

    def test_covariance_grammar_expand_one_dimension(self):
        root = ['SE', 'RQ', 'LIN']
        dim = 1
        grammar = CovarianceGrammar(root, dim, None)

        # expanding around SE
        se = grammar.base_kernels[0]
        expected_covariances = ['(SE+SE)', '(SE*SE)', '(SE+RQ)', '(SE*RQ)', '(SE+LIN)', '(SE*LIN)']
        new_covariances = grammar.expand(se)

        for expected_cov, new_cov in zip(expected_covariances, new_covariances):
            self.assertEqual(expected_cov, new_cov.name)

        # expanding around(SE + RQ)
        se_plus_rq = new_covariances[2]
        expected_covariances = ['((SE+RQ)+SE)', '((SE+RQ)*SE)', '((SE+RQ)+RQ)', '((SE+RQ)*RQ)', '((SE+RQ)+LIN)',
                                '((SE+RQ)*LIN)']
        new_covariances = grammar.expand(se_plus_rq)

        for expected_cov, new_cov in zip(expected_covariances, new_covariances):
            self.assertEqual(expected_cov, new_cov.name)

    def test_covariance_grammar_mask_kernels(self):
        pass

    def test_covariance_grammar_expand_multi_dimensions(self):
        pass

    def test_full_expand(self):
        pass
