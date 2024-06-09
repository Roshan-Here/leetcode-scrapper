import pytest
from q_2193_minimumNumberOfMovesToMakePalindrome import Solution


@pytest.mark.parametrize("s, output", [("aabb", 2), ("letelt", 2)])
class TestSolution:
    def test_minMovesToMakePalindrome(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.minMovesToMakePalindrome(
                s,
            )
            == output
        )
