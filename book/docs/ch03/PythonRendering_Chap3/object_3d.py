import pygame as pg
from matrix_functions import *

class Object3D:
  def __init__(self, render):
    self.render = render # main.py의 SoftwareRender Object Reference
    self.vertexes = np.array([(0,0,0,1), (0,1,0,1), (1,1,0,1), (1,0,0,1),
                              (0,0,1,1), (0,1,1,1), (1,1,1,1), (1,0,1,1)])
    self.faces = np.array([(0,1,2,3), (4,5,6,7), (0,4,5,1), (2,3,7,6), (1,2,6,5), (0,3,7,4)])
    
    self.font = pg.font.SysFont('Arial', 30, bold=True)
    self.color_faces = [(pg.Color('orange'), face) for face in self.faces]
    self.movement_flag, self.draw_vertexes = False, True
    self.label = ''
    
    self.forward = np.array([0,0,1])
    self.up = np.array([0,1,0])
    self.right = np.array([1,0,0])
    
    # Object Movement
    self.moving_speed = 0.02
    self.rotation_speed = 0.01
    self.scale_speed = 1.01
  
  def control(self):
    key = pg.key.get_pressed()
    # Object Movement Control
    if key[pg.K_a]:
      self.translate(self.right * self.moving_speed *  -1)
    if key[pg.K_d]:
      self.translate(self.right * self.moving_speed * 1)
    if key[pg.K_w]:
      self.translate(self.forward * self.moving_speed * -1)
    if key[pg.K_s]:
      self.translate(self.forward * self.moving_speed * 1)
    if key[pg.K_q]:
      self.translate(self.up * self.moving_speed * 1)
    if key[pg.K_e]:
      self.translate(self.up * self.moving_speed * -1)
    
    # Camera Rotation Control
    if key[pg.K_LEFT]:
      self.rotate_x(self.rotation_speed * -1)
    if key[pg.K_RIGHT]:
      self.rotate_x(self.rotation_speed * 1)
    if key[pg.K_UP]:
      self.rotate_y(self.rotation_speed * -1)
    if key[pg.K_DOWN]:
      self.rotate_y(self.rotation_speed * 1)
    if key[pg.K_o]:
      self.rotate_z(self.rotation_speed * -1)
    if key[pg.K_p]:
      self.rotate_z(self.rotation_speed * 1)
    
    # Camera Scale Control
    if key[pg.K_LEFTBRACKET]:
      self.scale(self.scale_speed)
    if key[pg.K_RIGHTBRACKET]:
      self.scale(1 / self.scale_speed)
  
  def draw(self):
    self.screen_projection()
    self.movement()
  
  def movement(self):
    if self.movement_flag:
      self.rotate_y(pg.time.get_ticks() % 0.005)
  
  # screen_projection 함수는
  def screen_projection(self):
    vertexes = self.vertexes @ self.render.camera.camera_matrix()
    vertexes = vertexes @ self.render.projection.projection_matrix
    vertexes /= vertexes[:, -1].reshape(-1, 1)
    vertexes[(vertexes > 1) | (vertexes < -1)] = 0
    vertexes = vertexes @ self.render.projection.to_screen_matrix
    vertexes = vertexes[:, :2] # [x,y,z,w] -> [x,y]
    
    for index, color_face in enumerate(self.color_faces):
      color, face = color_face
      polygon = vertexes[face] # 이건 점들 좌표 2차원으로 박아버린거 좌표 다 얻어내는건데
      if not np.any((polygon == self.render.H_WIDTH) | (polygon == self.render.H_HEIGHT)):
        pg.draw.polygon(self.render.screen, color, polygon, 3)
        if self.label:
          text = self.font.render(self.label[index], True, pg.Color('white'))
          self.render.screen.blit(text, polygon[-1])
        
        if self.draw_vertexes:
          for vertex in vertexes:
            if not np.any((vertex == self.render.H_WIDTH) | (vertex == self.render.H_HEIGHT)):
              pg.draw.circle(self.render.screen, pg.Color('skyblue'), vertex, 5)
  
  # x` = M * x. x와 x`은 동차좌표계로 표현된 3D Point이고, M은 변환을 나타내는 행렬임
  # 동차좌표계로 표현되어 있어서, 
  # MVG 책과는 다르게 M과 x의 위치가 다른데, 그냥 Transpose한 결과로 보면 됨
  # 이거 코드 재구성할 때, 행렬 구성이랑 변환식 재구성 같이 하자.
  # @ 연산자는 행렬곱 연산자로 생각하면 될듯 하다 (데코레이터 아님)
  # translate, scale, rotate 함수는 factor가 들어가면 그 factor에 맞는 변환 행렬식 H를 반환해줌
  def translate(self, pos):
    self.vertexes = self.vertexes @ translate(pos)
  
  def scale(self, scale_to):
    self.vertexes = self.vertexes @ scale(scale_to)
  
  def rotate_x(self, angle):
    self.vertexes = self.vertexes @ rotate_x(angle)
  
  def rotate_y(self, angle):
    self.vertexes = self.vertexes @ rotate_y(angle)
  
  def rotate_z(self, angle):
    self.vertexes = self.vertexes @ rotate_z(angle)
    
class Axes(Object3D):
  def __init__(self, render):
    super().__init__(render)
    self.vertexes = np.array([(0,0,0,1), (1,0,0,1), (0,1,0,1), (0,0,1,1)])
    self.faces = np.array([(0,1), (0,2), (0,3)])
    self.colors = [pg.Color('red'), pg.Color('green'), pg.Color('blue')]
    self.color_faces = [(color, face) for color, face in zip(self.colors, self.faces)]
    self.draw_vertexes = False
    self.label = 'XYZ'