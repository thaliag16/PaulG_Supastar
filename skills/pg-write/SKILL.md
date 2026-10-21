---
name: pg-write
description: pgstack writing review using Paul Graham's essays on writing (Write Simply, Write Like You Talk, How to Write Usefully, Putting Ideas into Words, Good Writing) plus his advice on pitching (How to Convince Investors, How to Present to Investors, What I've Learned from Users). Reviews a YC application, pitch, deck text, memo, landing page, cold email, or essay. Use for "review my YC application", "make this clearer", "PG edit", "is my pitch clear".
---

# /pg-write — make it plain, true, and strong

Writing is thinking. If the writing is muddled, the idea usually is too *(words, writes,
goodwriting)*. This skill edits for clarity **and** uses the editing to find the gaps in
the thinking.

## 0. Load

Read `~/.claude/skills/pgstack/knowledge/voice.md`. Get the text: ask the user to paste it
or give a file path, and Read it. Ask who the reader is (a YC partner, an investor, a user,
a general audience) if it isn't obvious.

## 1. The five passes

Run each pass and collect **specific** findings with quoted fragments from *their* text.

1. **One sentence.** Can you state what they're doing in one plain sentence after reading
   it? Write that sentence. If you can't, that's the top finding *(investors, convince)*.
2. **Plain words** *(simply, talk)*. Flag every word or phrase they wouldn't say out loud to
   a friend: jargon, buzzwords, "leverage," "revolutionize," "seamless," "AI-powered
   platform." Suggest the spoken version.
3. **Concrete and true** *(useful, convince)*. Flag claims that are vague, unfalsifiable, or
   hype ("huge market," "everyone needs this"). Ask for the number, the name, or the observed
   behavior. Hedges that hide a weak claim should be cut, or the claim made strong *and* true.
4. **Users** *(users, ace)*. Does it say what they've **learned from users**? For YC
   applications, the essays single this out as the best advice per word. If it's missing,
   it's the #1 addition.
5. **Sound** *(goodwriting)*. Read it as if aloud. Flag sentences that sound bad. Fixing them
   usually sharpens the idea underneath.

## 2. Thinking gaps

List the questions a smart reader would still have after reading, such as "Why hasn't X done
this?", "Who exactly pays?", or "What's the growth rate?" Each one is something to answer in
the text, or something the founder needs to go find out *(words: writing reveals what you
don't know)*.

## 3. Output

```
One-sentence version: <your plain restatement>

Top 3 fixes (most important first):
1. <finding> — "<their fragment>" → "<suggested rewrite>"  (essay)
2. ...
3. ...

Plain-word swaps: <list of "X" → "Y">
Questions a reader will still have: <bullets>
```

Then offer to produce a **full rewrite**. If they accept, keep their voice and facts, cut
length by at least 20%, and never invent facts, metrics, or user stories. Leave
`[NEED: ...]` placeholders where the evidence is missing.

## YC application specifics

- Lead with what the product does, in plain words.
- Show what you've learned from users, specifically *(users)*.
- Show the founders are builders: what you've already made *(prepare, ace)*.
- State growth as a rate *(growth)*.
- Don't perform. Being earnest beats being polished *(earnest)*.
