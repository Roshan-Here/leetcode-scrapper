import pytest
from q_3123_findEdgesInShortestPaths import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_findAnswer(self, n: int, edges: List[List[int]], output: List[bool]):
        sc = Solution()
        assert sc.findAnswer() == output
