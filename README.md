# AtCoder

[AtCoder](https://atcoder.jp/) solutions.

| Contest | URL |
| ------- | --- |
| [practice contest](./practice) | https://atcoder.jp/contests/practice |
| [AtCoder Beginners Selection](./abs) | https://atcoder.jp/contests/abs |
| [競プロ典型90問](./typical90) | https://atcoder.jp/contests/typical90 |

## Run tasks

```bash
contest=<contest_name>
cd ${contest}

poetry install

task=<task_name>
poetry run python -m ${contest}.${task}
```

## Run tests

```bash
contest=<contest_name>
cd ${contest}

poetry install

poetry run pytest tests/
```
