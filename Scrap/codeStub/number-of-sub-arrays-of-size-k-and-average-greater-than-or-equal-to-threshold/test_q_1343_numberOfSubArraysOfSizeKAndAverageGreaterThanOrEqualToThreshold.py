import pytest
from q_1343_numberOfSubArraysOfSizeKAndAverageGreaterThanOrEqualToThreshold import (
    Solution,
)


@pytest.mark.parametrize(
    "arr, k, threshold, output",
    [
        ([2, 2, 2, 2, 5, 5, 5, 8], 3, 4, 3),
        ([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5, 6),
    ],
)
class TestSolution:
    def test_numOfSubarrays(self, arr: List[int], k: int, threshold: int, output: int):
        sc = Solution()
        assert (
            sc.numOfSubarrays(
                arr,
                k,
                threshold,
            )
            == output
        )
