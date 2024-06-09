import pytest
from q_0786_kThSmallestPrimeFraction import Solution


@pytest.mark.parametrize(
    "arr, k, output", [([1, 2, 3, 5], 3, [2, 5]), ([1, 7], 1, [1, 7])]
)
class TestSolution:
    def test_kthSmallestPrimeFraction(self, arr: List[int], k: int, output: List[int]):
        sc = Solution()
        assert (
            sc.kthSmallestPrimeFraction(
                arr,
                k,
            )
            == output
        )
