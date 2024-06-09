import pytest
from q_0978_longestTurbulentSubarray import Solution


@pytest.mark.parametrize(
    "arr, output", [([9, 4, 2, 10, 7, 8, 8, 1, 9], 5), ([4, 8, 12, 16], 2), ([100], 1)]
)
class TestSolution:
    def test_maxTurbulenceSize(self, arr: List[int], output: int):
        sc = Solution()
        assert (
            sc.maxTurbulenceSize(
                arr,
            )
            == output
        )
