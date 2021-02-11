import graphics

scene = graphics.Scene(0, 60)

rect = graphics.elements.simple.Rect((0, 0), (200, 150), (255, 255, 255))
rect.loc.keyframe((0, 0), 0)
rect.loc.keyframe((500, 300), 30)
rect.loc.keyframe((100, 500), 60)

scene.add_element(rect)

graphics.export.export_sc((1280, 720), 30, [scene], "out.mp4")
