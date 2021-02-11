from typing import Tuple
import pygame
from ..props import *
pygame.init()


class BaseElement:
    """
    Empty element, other elements should inherit.
    """

    show: BoolProp

    def __init__(self) -> None:
        """
        BaseElement init. Other elements should have their own init
        and call super().__init__()
        """
        self.show = BoolProp(True)

    def render(self, res: Tuple[int], frame: int) -> pygame.Surface:
        """
        Renders element as pygame surface.
        :param res: Resolution to render.
        :param frame: Frame to render.
        """
