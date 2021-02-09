from typing import Tuple
import pygame
from ..props import *
pygame.init()


class BaseElement:
    """
    Empty element, other elements should inherit.
    """

    show: BoolProp

    def __init__(self):
        self.show = BoolProp(True)

    def render(self, res: Tuple[int], frame: int) -> pygame.Surface:...
