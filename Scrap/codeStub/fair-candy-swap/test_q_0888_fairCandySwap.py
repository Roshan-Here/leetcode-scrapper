import pytest
from q_0888_fairCandySwap import Solution


@pytest.mark.parametrize(
    "aliceSizes, bobSizes, output",
    [([1, 1], [2, 2], [1, 2]), ([1, 2], [2, 3], [1, 2]), ([2], [1, 3], [2, 3])],
)
class TestSolution:
    def test_fairCandySwap(
        self, aliceSizes: List[int], bobSizes: List[int], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.fairCandySwap(
                aliceSizes,
                bobSizes,
            )
            == output
        )
