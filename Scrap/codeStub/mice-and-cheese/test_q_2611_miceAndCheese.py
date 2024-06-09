import pytest
from q_2611_miceAndCheese import Solution


@pytest.mark.parametrize(
    "reward1, reward2, k, output",
    [([1, 1, 3, 4], [4, 4, 1, 1], 2, 15), ([1, 1], [1, 1], 2, 2)],
)
class TestSolution:
    def test_miceAndCheese(
        self, reward1: List[int], reward2: List[int], k: int, output: int
    ):
        sc = Solution()
        assert (
            sc.miceAndCheese(
                reward1,
                reward2,
                k,
            )
            == output
        )
