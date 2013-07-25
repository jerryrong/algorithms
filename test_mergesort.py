# coding: utf-8
# Author: Jerry Rong

import unittest
import mergesort

class TestMergeSort(unittest.TestCase):
    """
    Test case for merge sort
    """

    def test_merge_sort(self):
        """
        Test for merge_sort
        """
        list1 = [1]
        list2 = [2, 1]
        list3 = [4,5,9,8,7]
        list4 = [6,4,5,2,7,1]

        list1_expected = [1]
        list2_expected = [1,2]
        list3_expected = [4,5,7,8,9]
        list4_expected = [1,2,4,5,6,7]

        mergesort.merge_sort(list1)
        mergesort.merge_sort(list2)
        mergesort.merge_sort(list3)
        mergesort.merge_sort(list4)

        self.assertEqual(list1, list1_expected)
        self.assertEqual(list2, list2_expected)
        self.assertEqual(list3, list3_expected)
        self.assertEqual(list4, list4_expected)

    def test_merge_split(self):
        """
        Test for merge_split
        """
        a1     = [6, 7, 3, 1, 9, 0]
        left1  = [3, 6, 7]
        right1 = [0, 1, 9]

        a2 = [5,4,1,9,7]
        left2 = [4, 5]
        right2 = [1, 7, 9]
        
        a1_expected = [0, 1, 3, 6, 7, 9]
        a2_expected = [1, 4, 5, 7, 9]
        
        mergesort.merge_split(a1, left1, right1)
        mergesort.merge_split(a2, left2, right2)

        self.assertEqual(a1, a1_expected)
        self.assertEqual(a2, a2_expected)


if __name__ == "__main__":
    unittest.main(exit=False)
