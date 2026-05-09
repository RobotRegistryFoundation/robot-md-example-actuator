"""Protocol-conformance tests for robot-md-example-actuator."""

from __future__ import annotations

from robot_md_gateway.actuator import Actuator

from robot_md_example_actuator.actuator import RobotMdExampleActuatorActuator


def test_implements_actuator_protocol():
    instance = RobotMdExampleActuatorActuator()
    assert isinstance(instance, Actuator)


def test_metadata():
    instance = RobotMdExampleActuatorActuator()
    assert instance.name == "robot-md-example-actuator"
    assert instance.description
    assert isinstance(instance.config_schema, dict)
