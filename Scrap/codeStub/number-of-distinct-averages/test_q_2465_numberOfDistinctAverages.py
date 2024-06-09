import pytest
from q_2465_numberOfDistinctAverages import Solution


@pytest.mark.parametrize("nums, output", [([4, 1, 4, 0, 3, 5], 2), ([1, 100], 1)])
class TestSolution:
    def test_distinctAverages(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.distinctAverages(
                nums,
            )
            == output
        )
