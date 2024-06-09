import pytest
from q_2478_numberOfBeautifulPartitions import Solution


@pytest.mark.parametrize(
    "s, k, minLength, output",
    [("23542185131", 3, 2, 3), ("23542185131", 3, 3, 1), ("3312958", 3, 1, 1)],
)
class TestSolution:
    def test_beautifulPartitions(self, s: str, k: int, minLength: int, output: int):
        sc = Solution()
        assert (
            sc.beautifulPartitions(
                s,
                k,
                minLength,
            )
            == output
        )
