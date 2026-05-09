---
name: using-robot-md-example-actuator
description: Minimal example actuator that demonstrates the robot-md actuator package layout. Anchors the cookbook beat 6 demo. Does not move physical hardware.
hardware_tags: ["example", "tutorial"]
manifest_signals: []
---

# robot-md-example-actuator

## Purpose

This is a no-op example actuator. It exists to anchor the
[robotmd.dev cookbook](https://robotmd.dev/cookbook/) beat 6 demo
(discover/install) without requiring readers to have specific hardware.

## Capabilities exposed

None. This actuator does not move hardware.

## Safety boundaries

Cannot drive any physical device. Calls into this actuator return immediately
with a stub response. For real drivers, see [/case-studies/](https://robotmd.dev/case-studies/).

## Prompts that should call this actuator

None — this is a tutorial fixture, not a runtime actuator.
