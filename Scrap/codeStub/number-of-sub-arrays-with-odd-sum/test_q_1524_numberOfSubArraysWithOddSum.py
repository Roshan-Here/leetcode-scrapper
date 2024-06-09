import pytest
from q_1524_numberOfSubArraysWithOddSum import Solution


@pytest.mark.parametrize(
    "arr, output", [([1, 3, 5], 4), ([2, 4, 6], 0), ([1, 2, 3, 4, 5, 6, 7], 16)]
)
class TestSolution:
    def test_numOfSubarrays(self, arr: List[int], output: int):
        sc = Solution()
        assert (
            sc.numOfSubarrays(
                arr,
            )
            == output
        )
