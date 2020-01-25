###################################
#
# Controls:
#
#  Space       - start/stop
#  R           - reset
#  Left click  - create new red point
#  Up/Down     - increase/decrease interval ratio (0.5 by default -> each new point
#                is added 50% of the way between a random red point and its previous pos)
#                or modify it here:
ratio = 50/100
#
# change window dimensions:
WINDOW = (1000, 700)
###################################

import math, pygame, random

BLACK = (0, 0, 0)
BLUE = (0, 255, 255)
RED = (255, 0, 0)
X = 0
Y = 1
MARGIN = 50

# position of starting points
# triangle
points = [(WINDOW[X] // 2, MARGIN), (WINDOW[X] // 6, WINDOW[Y] - MARGIN), (5 * WINDOW[X] // 6, WINDOW[Y] - MARGIN)]

# square
# points = [(MARGIN, MARGIN), (MARGIN, WINDOW[Y] - MARGIN), (WINDOW[X] - MARGIN, MARGIN), (WINDOW[X] - MARGIN, WINDOW[Y] - MARGIN)]

# default values
nb_points = len(points);
new_point = [WINDOW[X] // 2, WINDOW[Y] // 2];
old_point = [];
i = 0;
loop = False

# setup pygame
pygame.init()
window = pygame.display.set_mode(WINDOW)
window.fill(BLUE)
pygame.display.set_caption("Ratio: "+str(round(ratio, 2)))
pixels = pygame.PixelArray(window)
pygame.display.flip()

# stats
time = 0
time_now = pygame.time.get_ticks()
time_prev = 0

def display_stats(i, time):
   print("Iterations: %d" % (i))

   if time > 0:
      print("Iterations per second: %.3f" % (1000 * i / time))

def event_handler():
   global loop, points, nb_points, i, ratio, time
   for evenement in pygame.event.get():
      if evenement.type == pygame.QUIT:
         display_stats(i, time)
         pygame.display.quit()
         exit()
      elif evenement.type == pygame.KEYDOWN:
         if evenement.key == pygame.K_SPACE:
            nb_points = len(points)
            if (nb_points > 0):
               loop = not loop
               if not loop:
                  display_stats(i, time)
         elif evenement.key == pygame.K_r:
            loop = False
            points = []
            window.fill(BLUE)
            pygame.display.flip()
         elif evenement.key == pygame.K_DOWN and not loop:
            ratio -= 1/100
            pygame.display.set_caption("Ratio: "+str(round(ratio, 2)))
         elif evenement.key == pygame.K_UP and not loop:
            ratio += 1/100
            pygame.display.set_caption("Ratio: "+str(round(ratio, 2)))
      elif evenement.type == pygame.MOUSEBUTTONDOWN and not loop:
         if evenement.button == 1 :
            points.append(evenement.pos)
            i = 0
            time = 0
            display_point(evenement.pos)

def display_point(pos):
   pygame.draw.circle(window, RED, pos, 2)
   pygame.display.flip()

def update_pixel(pos):
   global pixels
   x = round(pos[X])
   y = round(pos[Y])

   if x < 0 or x >= WINDOW[X]:
      return
   if y < 0 or y >= WINDOW[Y]:
      return

   pixels[x][y] = BLACK
   pygame.display.update(((x, y), (1, 1)))


for p in points:
   display_point(p)

while True:
   event_handler()

   time_prev = time_now
   time_now = pygame.time.get_ticks()

   if loop:
      time += (time_now - time_prev)

      r = random.randrange(0, nb_points)
      old_point = new_point
      new_point[X] = (old_point[X] + (points[r][X] - old_point[X]) * ratio)
      new_point[Y] = (old_point[Y] + (points[r][Y] - old_point[Y]) * ratio)

      update_pixel(new_point)

      i += 1
   else:
      pygame.time.Clock().tick(5)
