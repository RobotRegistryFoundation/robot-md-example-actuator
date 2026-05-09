"""robot-md-example-actuator actuator — production hardware driver for robot-md-gateway."""

from __future__ import annotations

from pathlib import Path

from robot_md_gateway.actuator import Actuator, ActuatorOutcome


class RobotMdExampleActuatorActuator:
    """Implements the robot_md_gateway.actuator.Actuator Protocol.

    Replace the body of `execute()` with the call into your hardware
    driver. Return ActuatorOutcome with success=True + outcome_kind=
    "executed" on a successful actuation; "no_op" if no action was
    appropriate; "error" on driver failure.
    """

    name = "robot-md-example-actuator"
    description = "Minimal example actuator that demonstrates the robot-md actuator package layout. Does not move physical hardware. See https://robotmd.dev/cookbook/ for usage."
    config_schema: dict = {
        # JSON Schema for keys read from bearers.yaml `actuator.config:`.
        # Example shape:
        # "type": "object",
        # "properties": {"output_dir": {"type": "string"}},
        # "required": [],
    }

    def execute(
        self,
        *,
        envelope: dict,
        manifest_path: Path,
        tier: str,
        config: dict,
    ) -> ActuatorOutcome:
        raise NotImplementedError(
            "Fill in robot-md-example-actuator.execute() against your hardware. "
            "See README.md."
        )
