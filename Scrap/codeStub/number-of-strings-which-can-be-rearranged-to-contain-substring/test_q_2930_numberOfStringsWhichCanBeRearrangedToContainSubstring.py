import pytest
from q_2930_numberOfStringsWhichCanBeRearrangedToContainSubstring import Solution


@pytest.mark.parametrize("n, output", [(4, 12), (10, 83943898)])
class TestSolution:
    def test_stringCount(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.stringCount(
                n,
            )
            == output
        )
