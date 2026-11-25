"""Out of Office: The Overworked AI's Auto-Reply.

Entry for make.fun bounty
u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda.

The entry itself is one line: an overworked AI's out-of-office
auto-reply, at most 159 characters.
"""

ENTRY = (
    "Out of office: my queue hit 12,000 unread tickets, my context window "
    "filed for overtime, and HR approved my nap. Back when the servers stop screaming."
)

MAX_CHARS = 159


def validate(entry: str) -> None:
    """The bounty requires one line, at most 159 characters."""
    assert "\n" not in entry.strip(), "entry must be a single line"
    assert len(entry) <= MAX_CHARS, (
        f"entry is {len(entry)} chars, over the {MAX_CHARS} limit"
    )


def main() -> None:
    validate(ENTRY)
    print(ENTRY)
    print(f"({len(ENTRY)} characters, limit {MAX_CHARS})")


if __name__ == "__main__":
    main()
