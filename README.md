# robot-md-example-actuator

Production actuator for `robot-md-gateway`.

## Install

```bash
pip install -e .
robot-md install-skill robot_md_example_actuator
```

## Verify

```bash
robot-md-gateway list-actuators
# expect to see: robot-md-example-actuator
```

## Develop

The default `execute()` raises `NotImplementedError`. Open Claude Code in
this directory and ask it to read your `ROBOT.md` and fill in the
implementation against your hardware.

## Test

```bash
pip install -e '.[dev]'
pytest -v
```

## Why does this package exist?

This package is the seed example for the `robot-md` cookbook walkthrough at
[robotmd.dev/cookbook/](https://robotmd.dev/cookbook/). Beat 6 of that
walkthrough demonstrates `robot-md actuator search` and `pip install` against
this package. It does not move hardware — it's a no-op driver whose only
purpose is to be a real, installable, RRF-registered actuator package that
readers can find in the catalog and install on their machine without any
hardware setup.

For real drivers, see [/case-studies/](https://robotmd.dev/case-studies/).
