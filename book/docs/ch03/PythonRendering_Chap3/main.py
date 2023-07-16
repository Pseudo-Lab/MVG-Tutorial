import pygame as pg
from object_3d import *
from camera import *
from projection import *

class SoftwareRender:
  def __init__(self):
    pg.init()
    self.RES = self.WIDTH, self.HEIGHT = 1600, 900
    self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
    self.FPS = 60
    self.screen = pg.display.set_mode(self.RES)
    self.clock = pg.time.Clock()
    self.create_objects()
  
  def create_objects(self):
    self.camera = Camera(self, [0, 0, -5])

    # self.camera = Camera(self, [0.5, 1, 4])
    self.projection = Projection(self)
    self.object = Object3D(self)
    self.object.translate([0.2, 0.4, 0.2])
    
    self.axes = Axes(self)
    self.axes.translate([0.7, 0.9, 0.7])
    self.world_axes = Axes(self)
    self.world_axes.movement_flag = False
    #self.world_axes.scale(2.5)
    self.world_axes.translate([0.0001, 0.0001, 0.0001])
  
  
  def draw_instruction(self):
    x = 50
    y = 50
    instruction = ['Move Left/Right: AD','Move Forward/Back: WS', 'Move Up/Down: QE',
                   'Rotation X: Left/Right', 'Rotation Y: Up/Down', 'Rotation Z: OP'
                   'Scale: [ / ]']
    instruction_font = pg.font.SysFont('Arial', 20, bold=True)

    for message in instruction:
      instruction_text = instruction_font.render(message, True, (255,255,255))
      self.screen.blit(instruction_text, [x, y])
      y += 25
    
  def draw(self):
    self.screen.fill(pg.Color('darkslategray'))
    self.world_axes.draw()
    # self.axes.draw()
    self.object.draw()
  
  def run(self):
    while True:
      self.draw()
      self.draw_instruction()
      # self.camera.control()
      self.object.control()
      [exit() for i in pg.event.get() if i.type == pg.QUIT]
      pg.display.set_caption(str(self.clock.get_fps()))
      pg.display.flip()
      self.clock.tick(self.FPS)

if __name__ == '__main__':
  app = SoftwareRender()
  app.run()