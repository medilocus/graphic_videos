import pygame

pygame.init()

class FrameText:
    def __init__(self, font, label=""):
        self.font = font
        self.label = label

        self.cursor_pos = 0
        self.text = ""
        self.editing = False
        self.frame = 0

        self.rpt_count = {}
        self.rpt_init = 400
        self.rpt_int = 35
        self.clock = pygame.time.Clock()

    def draw(self, window, events, width, height):
        self.frame += 1

        text_size = self.font.size("Frame: " + self.text)
        loc = [((width, height)[i] - text_size[i] - 2) for i in range(2)]

        text = self.font.render("Frame: " + self.text, 1, (255,)*3)
        window.blit(text, loc)

        if self.editing and (self.frame//30) % 2 == 0:
            cursor_x = loc[0] + self.font.size("Frame: " + self.text[:self.cursor_pos])[0]
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
                        if event.unicode.isnumeric() and len(self.text) <= 5:
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
