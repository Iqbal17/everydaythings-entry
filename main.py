"""Everyday Things, Two Lines, Longer Run — make.fun entry.

Bounty: u-suga-everyday-things-two-lines-longer-run-f8734479 ($2, winner-takes-all).
Gate: /output/entry.txt is UTF-8 text of 1 to 400 characters, exactly two lines.
Line 1 explains one everyday thing to a 10-year-old in a single vivid sentence
built on an analogy. Line 2 says in one sentence why the analogy works: what
it maps and what it leaves out. Judge weighs, in order: (1) it really explains
one everyday thing to a 10-year-old, (2) the analogy is concrete and surprising
— things a 10-year-old can see, hold or stand in, joined in a fresh way,
(3) line 1 is one vivid sentence that lands the picture whole, with no list
of comparisons and no second metaphor crowding it, (4) line 2 is honest and
specific about the mapping instead of praising the analogy, (5) the two lines
work as a pair, the second explaining the first, in language a 10-year-old
would follow without being talked down to.

DECISION RECORD — Pass 1 (four candidate pairs weighed against the brief):

A. Toaster (254 chars total):
   L1: "A toaster is a small sun that only shines inside a metal box, browning
   whatever you push down into it." (100)
   L2: "The sun part works because both turn things brown with heat, but a
   real sun shines on everything at once, and a toaster only warms the slice
   you feed it." (153)
   - For: one clean analogy, line 2 names a real limit (sun shines
     everywhere, toaster only inside).
   - Against: "toaster as a little sun" is a familiar join — a 10-year-old has
     probably heard heat compared to the sun before, so it scores weakly on
     criterion 2 (surprising).

B. Traffic jam (257 chars total):
   L1: "A traffic jam is a river of cars that has hit a dam, so every driver
   sits in their own boat waiting for the water to move." (122)
   L2: "The river part works because cars really do bunch up and flow like
   water, but rivers never beep their horns, and nobody can steer one." (134)
   - For: the dam image is vivid, line 2's limits (honking, steering) are
     specific and funny.
   - Against: "river of traffic" is a stock phrase — the analogy is concrete
     but not surprising; the boat extension also crowds line 1 with a second
     picture, which criterion 3 punishes.

C. Rain (chosen):
   L1: "Rain is the sky wringing out a giant sponge, squeezing drops over the
   roofs until the sponge is light enough to float away." (123)
   L2: "The sponge part works because clouds really do hold water and let it
   go, but a real sponge fits in your hand, and the sky never wrings anything
   out on purpose." (159)
   - For: a sponge is something a 10-year-old can actually hold and squeeze,
     so the analogy is tactile as well as visible; "wringing out the sky" is
     a fresh join; line 1 is one sentence with a single metaphor that lands
     whole; line 2 names two real limits (scale — a sponge fits in your hand,
     a cloud does not — and intention — the sky wrings nothing out on
     purpose) instead of praising the analogy.
   - Against: rain is the most familiar of the four subjects, so the topic
     itself is less surprising — but the analogy, not the topic, is what the
     judge weighs, and the sponge join is the freshest of the four.

D. Queue (260 chars total):
   L1: "A queue is a human train, and every person is a carriage waiting for
   the engine at the front to start moving." (109)
   L2: "The train part works because the line really does move one person at
   a time, but a carriage cannot step out for a snack, and a train never
   gets bored." (150)
   - For: "human train" is a fresh join, and standing in a queue is something
     a 10-year-old knows by heart.
   - Against: line 2's limits are cute rather than honest — "never gets
     bored" is a joke about the analogy, not a specific account of what the
     mapping leaves out — so it scores weakly on criterion 4.

DECISION RECORD — Pass 2 (refining the winner, C):
   - Draft line 2 was: "The sponge part works because clouds really do hold
     water and let it go, but you can squeeze a real sponge with your hands,
     and the sky never wrings anything out on purpose." (173)
   - Revision: "you can squeeze a real sponge with your hands" repeats the
     squeezing action already in line 1, so it explains nothing new. Replaced
     with "a real sponge fits in your hand", which names a genuinely different
     limit — scale — in fewer words (159 vs 173) and keeps the line tight.
   - Line 1 kept as drafted: "wringing out a giant sponge" is the single
     metaphor, and "light enough to float away" closes the picture without
     adding a second comparison.

FINAL ENTRY (283 characters total: 123 + 1 newline + 159):
Line 1: "Rain is the sky wringing out a giant sponge, squeezing drops over the
roofs until the sponge is light enough to float away."
Line 2: "The sponge part works because clouds really do hold water and let it
go, but a real sponge fits in your hand, and the sky never wrings anything
out on purpose."

Hand count, two ways. Line 1: 101 non-space characters + 22 spaces = 123.
Line 2: 129 non-space characters + 30 spaces = 159. Total: 123 + 1 + 159 = 283.
"""

import os

ENTRY = (
    "Rain is the sky wringing out a giant sponge, squeezing drops over the "
    "roofs until the sponge is light enough to float away.\n"
    "The sponge part works because clouds really do hold water and let it go, "
    "but a real sponge fits in your hand, and the sky never wrings anything "
    "out on purpose."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
