import random


class AbstractTestCase(object):
    def test_edge_case_empty(self):
        self.assertEqual(self.function([]), [])

    def test_edge_case_1_element(self):
        self.assertEqual(self.function([1]), [1])

    def test_domain_upper(self):
        unsorted = list(range(10**3))
        random.shuffle(unsorted)
        self.assertEqual(self.function(unsorted)[:10], list(range(10)))

    def test_2_elements(self):
        self.assertEqual(self.function([2, 1]), [1, 2])
        self.assertEqual(self.function([1, 2]), [1, 2])

    def test_4_elements(self):
        self.assertEqual(self.function([4, 3, 2, 1]), [1, 2, 3, 4])

    def test_unsorted_list(self):
        self.assertEqual(self.function([2, 1, 3]), [1, 2, 3])
        self.assertEqual(self.function([2, 3, 1]), [1, 2, 3])
        self.assertEqual(self.function([3, 2, 1]), [1, 2, 3])

    def test_sorted_list(self):
        self.assertEqual(self.function([1, 2, 3]), [1, 2, 3])
