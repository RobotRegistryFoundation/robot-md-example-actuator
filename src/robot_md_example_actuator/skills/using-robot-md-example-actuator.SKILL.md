---
name: using-robot-md-example-actuator
description: When operating <hardware-class> via robot-md-gateway, this skill teaches Claude how to use the robot-md-example-actuator actuator. Triggers on actuating <hardware-class>.
hardware_tags: ["{{ hardware_tag_1 }}", "{{ hardware_tag_2 }}"]
manifest_signals: ["{{ signal_1 }}"]
---

# robot-md-example-actuator

## Purpose
Minimal example actuator that demonstrates the robot-md actuator package layout. Does not move physical hardware. See https://robotmd.dev/cookbook/ for usage.

## Capabilities exposed
{% for capability in capabilities %}
- `{{ capability.tool_name }}` — {{ capability.description }}
{% endfor %}

## Safety boundaries
{{ safety_notes }}

## Prompts that should call this actuator
{% for prompt in prompts %}
- "{{ prompt }}"
{% endfor %}
