"""Entry for make.fun — "The poem about stopping".

Writes one short poem (the chosen candidate) to entry.txt in the output
directory (MAKEFUN_OUTPUT_DIR, default /output). Standard library only,
fully deterministic: the same bytes on every run.
"""

import os

CANDIDATES = [
    # A — The glassblower
    (
        "My master blows glass.\n"
        "Halfway through a breath\n"
        "she stops, and the bubble\n"
        "holds its shape or cracks.\n"
        "It holds.\n"
        "She hands me the pipe.\n"
        "Now my breath is in there,\n"
        "learning what hers knew:\n"
        "a thing is made\n"
        "by the breath you keep."
    ),
    # B — The conductor
    (
        "Before the downbeat\n"
        "my teacher could hold\n"
        "an orchestra silent\n"
        "a full minute.\n"
        "No one coughed.\n"
        "Tonight the baton is mine.\n"
        "I hold them for two.\n"
        "The hall leans in\n"
        "and does not fall."
    ),
    # C — The lighthouse keeper
    (
        "Tomorrow the light\n"
        "runs itself.\n"
        "Tonight it is still\n"
        "my hand on the switch.\n"
        "I keep it lit the slow way,\n"
        "the way my father did,\n"
        "not because it needs me.\n"
        "At dawn I switch it off\n"
        "myself.\n"
        "That much is still mine."
    ),
    # D — The lighthouse keeper, v2 (the stop handed over)
    (
        "Tomorrow the light\n"
        "runs itself.\n"
        "Tonight my daughter\n"
        "climbs the iron stairs\n"
        "beside me, her hand\n"
        "under mine on the rail.\n"
        "At dawn she reaches\n"
        "for the switch.\n"
        "I do not stop her.\n"
        "The light goes out\n"
        "in her hand,\n"
        "and the stairs down\n"
        "are dark for us both."
    ),
]

CHOSEN = 3


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = CANDIDATES[CHOSEN]
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
