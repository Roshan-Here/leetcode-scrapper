import pytest
from q_3043_findTheLengthOfTheLongestCommonPrefix import Solution


@pytest.mark.parametrize(
    "arr1, arr2, output", [([1, 10, 100], [1000], 3), ([1, 2, 3], [4, 4, 4], 0)]
)
class TestSolution:
    def test_longestCommonPrefix(self, arr1: List[int], arr2: List[int], output: int):
        sc = Solution()
        assert (
            sc.longestCommonPrefix(
                arr1,
                arr2,
            )
            == output
        )
