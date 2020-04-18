"""Declare test cases here."""
successful_parsing_cases = [
    '{"x": 123, "y": 456}',
    '{"abc": ["yolo","swag", "wololo"], "def": {"123": "foo", "466":"bar"}}',
    '[223, "iolo", "qfq"]',
    '"qwerty"',
]
successful_parsing_validation = [
    """{
  "x": 123,
  "y": 456
}""",
    """{
  "abc": [
    "yolo",
    "swag",
    "wololo"
  ],
  "def": {
    "123": "foo",
    "466": "bar"
  }
}""",
    """[
  223,
  "iolo",
  "qfq"
]""",
    '"qwerty"',
]
error_cases = [
    "abc",
    '{123: "abc", 44: "def"}',
    "[abc,def,gji]",
    '[("abc", 123), ("xyz", 5567)]',
    "",
]
