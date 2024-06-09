import pytest
from q_1488_avoidFloodInTheCity import Solution


@pytest.mark.parametrize(
    "rains, output",
    [
        ([1, 2, 3, 4], [-1, -1, -1, -1]),
        ([1, 2, 0, 0, 2, 1], [-1, -1, 2, 1, -1, -1]),
        ([1, 2, 0, 1, 2], []),
    ],
)
class TestSolution:
    def test_avoidFlood(self, rains: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.avoidFlood(
                rains,
            )
            == output
        )
