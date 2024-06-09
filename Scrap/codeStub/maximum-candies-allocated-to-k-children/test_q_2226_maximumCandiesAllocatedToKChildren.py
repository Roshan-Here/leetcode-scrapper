import pytest
from q_2226_maximumCandiesAllocatedToKChildren import Solution


@pytest.mark.parametrize("candies, k, output", [([5, 8, 6], 3, 5), ([2, 5], 11, 0)])
class TestSolution:
    def test_maximumCandies(self, candies: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.maximumCandies(
                candies,
                k,
            )
            == output
        )
