"""How Many Tabs Do You Have Open?

One number, digits only: my honest count of open browser tabs.
The browser is a graveyard of good intentions -- every tab is an
article I meant to read, a doc I meant to finish, a video I meant
to watch. I never close them; I just open new ones and promise
myself I will get back to the old ones someday.
"""

import os

# The count: high enough to be a confession, specific enough to be
# believed. A round number would read invented; this one reads lived-in.
# It hints at the life behind it without a word of explanation: a
# researcher who opens a tab for every half-formed idea and closes
# none of them, because closing one feels like giving up on it.
TABS_OPEN = "127"


def main():
    if not TABS_OPEN.isdigit():
        raise ValueError("entry must be digits only")
    if not 1 <= len(TABS_OPEN) <= 5:
        raise ValueError("entry must be 1-5 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TABS_OPEN)


if __name__ == "__main__":
    main()
