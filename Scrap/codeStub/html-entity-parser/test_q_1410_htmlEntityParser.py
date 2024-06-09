import pytest
from q_1410_htmlEntityParser import Solution


@pytest.mark.parametrize(
    "text, output",
    [
        (
            "&amp; is an HTML entity but &ambassador; is not.",
            "& is an HTML entity but &ambassador; is not.",
        ),
        ("and I quote: &quot;...&quot;", 'and I quote: "..."'),
    ],
)
class TestSolution:
    def test_entityParser(self, text: str, output: str):
        sc = Solution()
        assert (
            sc.entityParser(
                text,
            )
            == output
        )
