import pytest
from q_2696_minimumStringLengthAfterRemovingSubstrings import Solution


@pytest.mark.parametrize("s, output", [("ABFCACDB", 2), ("ACBBD", 5)])
class TestSolution:
    def test_minLength(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.minLength(
                s,
            )
            == output
        )
