from . import panda
from .panda import WalkingPanda

import argparse


def cli():

    parser = argparse.ArgumentParser(prog="walking_panda")
    parser.add_argument("--no-rotate",help="Suppress Rotation",
                        action="store_true")
    parser.add_argument("--scale", help="Size down the panda",
                        action="store_true")
    parser.add_argument("--change_color", help="Change Panda's color",
                        action="store_true")
    parser.add_argument("--disappear_panda", help="Make panda disappear",
                        action="store_true")
    parser.add_argument("--change_scenery", help="Change Panda's background scenery",
                        action="store_true")

    args = parser.parse_args()

    walking = panda.WalkingPanda(**vars(args))
    walking.run()
