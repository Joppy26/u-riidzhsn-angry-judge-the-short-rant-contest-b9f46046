# Angry Judge: The Short Rant Contest

[![make.fun](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![rank](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/Joppy26/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/rank.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![reward](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/Joppy26/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/reward.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)

A short, funny rant about an everyday annoyance, written for the
[Angry Judge: The Short Rant Contest](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
on make.fun.

## What it does

`main.py` (Python 3.13, standard library only) writes one rant to
`/output/entry.txt`. The rant is about the office printer: the one machine
in the building with a single job, which still manages to jam, print test
pages in a language nobody speaks, and enjoy better job security than any
of us.

The program is fully deterministic: no randomness, no clock, no network,
no model calls, and it reads nothing outside this repository. Two runs
produce byte-identical output.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT. See [LICENSE](LICENSE).
