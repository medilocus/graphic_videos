import pygame
from ..options import get_font
import numpy as np

pygame.init()

class FrameText:
    def __init__(self):
        self.cursor_pos = 0
        self.text = ""
        self.editing = False
        self.frame = 0

        self.rpt_count = {}
        self.rpt_init = 400
        self.rpt_int = 35
        self.clock = pygame.time.Clock()

    def draw(self, window, events, width, height, text_size, font):
        self.frame += 1

        loc = [((width, height)[i] - text_size[i] - 2) for i in range(2)]

        text = font.render("Frame: " + self.text, 1, (255,)*3)
        window.blit(text, loc)

        if self.editing and (self.frame//30) % 2 == 0:
            cursor_x = loc[0] + font.size("Frame: " + self.text[:self.cursor_pos])[0]
            pygame.draw.line(window, (255,)*3, (cursor_x, loc[1]), (cursor_x, loc[1] + text_size[1]))

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.editing = self.hovered(loc, text_size)
            elif event.type == pygame.KEYDOWN and self.editing:
                if event.key in (pygame.K_ESCAPE, pygame.K_TAB):
                    self.editing = False
                elif event.key in (pygame.K_KP_ENTER, pygame.K_RETURN):
                    self.editing = False

                else:
                    if event.key not in self.rpt_count:
                        self.rpt_count[event.key] = [0, event.unicode]

                    if event.key == pygame.K_LEFT:
                        self.cursor_pos -= 1
                    elif event.key == pygame.K_RIGHT:
                        self.cursor_pos += 1
                    elif event.key in (pygame.K_HOME, pygame.K_PAGEDOWN):
                        self.cursor_pos = 0
                    elif event.key in (pygame.K_END, pygame.K_PAGEUP):
                        self.cursor_pos = len(self.text)

                    elif event.key == pygame.K_BACKSPACE:
                        if self.cursor_pos:
                            self.text = self.text[:self.cursor_pos-1] + self.text[self.cursor_pos:]
                            self.cursor_pos -= 1
                    elif event.key == pygame.K_DELETE:
                        self.text = self.text[:self.cursor_pos] + self.text[self.cursor_pos+1:]
                    else:
                        if event.unicode.isnumeric() and len(self.text) < 5:
                            self.text = self.text[:self.cursor_pos] + event.unicode + self.text[self.cursor_pos:]
                            self.cursor_pos += 1

                self.cursor_pos = min(max(self.cursor_pos, 0), len(self.text))

            elif event.type == pygame.KEYUP:
                if event.key in self.rpt_count:
                    del self.rpt_count[event.key]

        for key in self.rpt_count:
            self.rpt_count[key][0] += self.clock.get_time()

            if self.rpt_count[key][0] >= self.rpt_init:
                self.rpt_count[key][0] = self.rpt_init - self.rpt_int
                event_key, event_unicode = key, self.rpt_count[key][1]
                pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=event_key, unicode=event_unicode))

        self.clock.tick()

    def hovered(self, loc, size):
        mouse = pygame.mouse.get_pos()
        if loc[0] <= mouse[0] <= loc[0]+size[0] and loc[1] <= mouse[1] <= loc[1]+size[1]:
            return True
        return False


class Slider:
    colors = {
        "text": (255,) * 3,
        "slider": (50,) * 3,
        "cursor": (130,) * 3,
        "arrows": (255,) * 3,
        "boxes": (80,) * 3,
        "highlighted_boxes": (120,) * 3,
    }
    tri_padx = 8
    tri_pady = 5

    def __init__(self, init_val=80, val_range=(1, 100)):
        self.range = val_range
        self.value = init_val
        self.dragging = False

    def draw_arrows(self, window, y, w, h):
        left = pygame.Surface((h,)*2)
        right = pygame.Surface((h,)*2)
        mx, my = pygame.mouse.get_pos()
        colliding = 0 <= mx <= h and y <= my <= y + h
        color = self.colors["highlighted_boxes"] if colliding else self.colors["boxes"]
        left.fill(color)
        colliding = w - h <= mx <= w and y <= my <= y + h
        color = self.colors["highlighted_boxes"] if colliding else self.colors["boxes"]
        right.fill(color)
        l = self.tri_padx
        r = h - self.tri_padx
        t = self.tri_pady
        m = h/2
        b = h - self.tri_pady
        pygame.draw.polygon(left, self.colors["arrows"], ((r, t), (l, m), (r, b)))
        pygame.draw.polygon(right, self.colors["arrows"], ((l, t), (r, m), (l, b)))
        window.blit(left, (0, y))
        window.blit(right, (w - h, y))

    def update(self, window, events, width, height, w, h):
        y = height - h
        self.draw(window, y, w, h)
        mx, my = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if y <= my <= y + h:
                    self.dragging = h <= mx <= w - h
                    if 0 <= mx <= h:
                        self.value = max(self.value - 1, self.range[0])
                    elif w - h <= mx <= w:
                        self.value = min(self.value + 1, self.range[1])
            if event.type == pygame.MOUSEBUTTONUP:
                self.dragging = False

        if self.dragging:
            self.loc_to_value(w, h)

    def draw(self, window, y, w, h):
        pygame.draw.rect(window, self.colors["slider"], (0, y, w, h))
        pygame.draw.rect(window, self.colors["cursor"], (self.value_to_loc(w, h) - h/2, y, h, h))
        self.draw_arrows(window, y, w, h)

    def loc_to_value(self, w, h):
        return np.interp(pygame.mouse.get_pos()[0], (h*1.5, w - h*1.5), self.range)

    def value_to_loc(self, w, h):
        return np.interp(self.value, self.range, (h*1.5, w - h*1.5))
