import pytest
from q_1576_replaceAllSToAvoidConsecutiveRepeatingCharacters import Solution


@pytest.mark.parametrize("s, output", [("?zs", "azs"), ("ubv?w", "ubvaw")])
class TestSolution:
    def test_modifyString(self, s: str, output: str):
        sc = Solution()
        assert (
            sc.modifyString(
                s,
            )
            == output
        )
