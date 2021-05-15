import pygame
start = (20,320)
end = (160,160)

# set up pygame window
WIDTH = 500
HEIGHT = 600


# Define colours
WHITE = (255, 255, 255)
GREEN = (0, 255, 0,)
BLUE = (0, 0, 255)
YELLOW = (255 ,255 ,0)
BLACK = (0,0,0)
# initalise Pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((255,255,255))
pygame.display.set_caption("Python Maze Generator")
clock = pygame.time.Clock()

# setup maze variables
x = 0                    # x axis
y = 0                    # y axis
w = 20                   # width of cell


stack = []

lis = []
lis.append(start) # start poinnt

def build_grid(x, y, w):
    for i in range(16):
        x = 20                                                            # set x coordinate to start position
        y = y + 20                                                        # start a new row
        for j in range(16):
            pygame.draw.line(screen, BLACK, [x, y], [x + w, y])           # top of cell
            pygame.draw.line(screen, BLACK, [x + w, y], [x + w, y + w])   # right of cell
            pygame.draw.line(screen, BLACK, [x + w, y + w], [x, y + w])   # bottom of cellaa
            pygame.draw.line(screen, BLACK, [x, y + w], [x, y])           # left of cell
                                                                         # add cell to grid list
            x = x + 20                                                    # move cell to new position
       
            
build_grid(40, 0, 20)



pygame.draw.rect(screen, (255,0,0), (start[0]+7, start[1]+7, 5, 5), 0) # start

pygame.draw.rect(screen, (255,0,0), (end[0]+7, end[1]+7, 5, 5), 0) # END
pygame.display.update()

class maze:
    x = start[0]+1
    y = start[1]+1
    def right(self):
        self.x = self.x + 20
        pygame.draw.rect(screen, WHITE, (self.x-1, self.y, 20, 19), 0)
        pygame.display.update()
    def left(self):
        self.x = self.x - 20
        pygame.draw.rect(screen, WHITE, (self.x, self.y, 20, 19), 0)
        pygame.display.update()
    def bot(self):
        self.y = self.y + 20
        pygame.draw.rect(screen, WHITE, (self.x, self.y-1, 19, 20), 0)
        pygame.display.update()
    def top(self):
        self.y = self.y - 20
        pygame.draw.rect(screen, WHITE, (self.x, self.y+2, 19, 20), 0)
        pygame.display.update()




        
m = maze()
pos = []
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                m.left()
                pos.append([m.x,m.y,'left'])                      
            elif event.key == pygame.K_RIGHT:
                m.right()
                pos.append([m.x,m.y,'right'])
            elif event.key == pygame.K_UP:
                m.top()
                pos.append([m.x,m.y,'top'])
            elif event.key == pygame.K_DOWN:
                m.bot()
                pos.append([m.x,m.y,'bot'])
            if event.key == pygame.K_s:
                run = False
                break
            
      
            

        
fh = open("pos.txt",'w')
count = 0
for i in pos:
    fh.write(str(i[0])+" "+str(i[1])+" "+str(i[2])+'\n')
fh.close()
font = pygame.font.SysFont('Arial', 12)


fh = open('pos.txt')
for line in fh:
    line = line.split()
    x = int(line[0])
    y = int(line[1])
    lis.append((x-1,y-1))
    if line[2] == 'right1':
        pygame.draw.rect(screen, WHITE, (x-1, y, 20, 19), 0)
    elif line[2] =='left1':
        pygame.draw.rect(screen, WHITE, (x, y, 20, 19), 0)
    elif line[2] =='bot':
        pygame.draw.rect(screen, WHITE, (x, y-1, 19, 20), 0)
      
    elif line[2] == 'top':
        pygame.draw.rect(screen, WHITE, (x, y+2, 19, 20), 0)




##########################################################################Flood FIll ##############################################################



def flood_fill():
    stack = [end] # end 
    check = [end] # end
    
    while True:
        for m in stack:
            
            uni = []
            for l in m:
                if type(l)==int:
                    x ,y = m
                else:
                    x,y = l
                
                count = -1
                ind = -1

                for i in range(lis.count((x,y))):
                   ind = lis.index((x,y),ind+1)
                   try:

                       if (x+20,y) == lis[ind +1] or (x+20,y) == lis[ind -1] :
                           if(x+20,y)not in check :
                               uni.append((x+20,y))
                               check.append((x+20,y))
                   except:                     
                        if (x+20,y) == lis[ind -1] :
                            if(x+20,y)not in check :
                                uni.append((x+20,y))
                                check.append((x+20,y))
                        
                           
                   try:
                       if (x-20,y) == lis[ind +1] or (x-20,y) == lis[ind-1]:
                           if (x-20,y)not in check :
                               uni.append((x-20,y))
                               check.append((x-20,y))
                   except:
                      if (x-20,y) == lis[ind -1]:
                          if (x-20,y)not in check :
                              uni.append((x-20,y))
                              check.append((x-20,y))
                           

                           
                   try:         
                       if (x,y+20) == lis[ind +1] or (x,y+20) == lis[ind-1 ]:
                           if (x,y+20) not in check :
                               uni.append((x,y+20))
                               check.append((x,y+20))
                   except:
                       if (x,y+20) == lis[ind -1]:
                           if (x,y+20) not in check :
                               uni.append((x,y+20))
                               check.append((x,y+20))
                      
                           

                           
                   try:
                       
                       if (x,y-20) == lis[ind +1] or (x,y-20) == lis[ind-1 ]:
                           if (x,y-20) not in check :
                               uni.append((x,y-20))
                               check.append((x,y-20))
                   except:
                       if (x,y-20) == lis[ind -1] :
                           if (x,y-20) not in check :
                               uni.append((x,y-20))
                               check.append((x,y-20))

                          
    
                   uni = list(set(uni))
        if uni ==[]:
            break
        stack.append(uni)
    
    return stack  
########################################################SOLVIng################################################################################################
def numbring_maze(x):
    lis = x
    count = 0
    for i in lis:
        for j in i:
            if type(j) == int:
                x,y = i
            else:
                x,y = j
            screen.blit(font.render(str(count), True, (0,0,0)), (x+7, y+7))
        count = count +1 
    pygame.display.update()
#######################################################################################################
def sloving_path():
    start_point = start
    lis = flood_fill()
    start_index = 0
    path = [start_point]
    moves = []
    for i in lis:
        try:
           i.index((start_point))
           start_index = lis.index(i)
        except:
               continue
    j = start_index-1
    for i in path:
        x,y = i
        if (x+20,y) in lis[j] or(x+20,y) == lis[j] :
            path.append((x+20,y))
            moves.append('Right')
        if (x-20,y) in lis[j] or(x-20,y) == lis[j]:
            path.append((x-20,y))
            moves.append('left')
        if (x,y+20) in lis[j] or  (x,y+20) == lis[j]:
            path.append((x,y+20))
            moves.append('bot')
        if (x,y-20) in lis[j] or(x,y-20) == lis[j] :
            path.append((x,y-20))
            moves.append('top')

       
        j = j-1

    return path
    print(moves)   
###############################################################################
def solve():
    start_point = start
    path = [start_point]
    flood = flood_fill()
    move = []
    ch = []
    z = 0
    save = ''
    start_index = 0
    count = 0
    for i in flood:
            try:
                i.index((start_point))
                start_index = flood.index(i)
            except:
                    continue
    for j in range(start_index-1,-1,-1):
        x,y = path[count]
        ch = []
        for i in flood[j]:
            if type(i) == int:
                i = flood[j]
            if i == (x+20,y):
                ch.append((x+20,y))
            elif i == (x-20,y):
                ch.append((x-20,y))
            elif i == (x,y+20):
                ch.append((x,y+20))
            elif i == (x,y-20):
                ch.append((x,y-20))
        ch2= []
        ind = -1
        
        
        for i in range(lis.count((x,y))):
            ind = lis.index((x,y),ind+1)
            if lis[ind+1] == lis[ind-1]:
                ch2.append(lis[ind+1])
            else:
                ch2.append(lis[ind+1])
                ch2.append(lis[ind-1])

        path.append((list(set(ch).intersection(ch2))[0][0],
                        list(set(ch).intersection(ch2))[0][1]))
        
    
        if (list(set(ch).intersection(ch2))[0][0],list(set(ch).intersection(ch2))[0][1]) == (x+20,y):
            move.append('right1')
        elif (list(set(ch).intersection(ch2))[0][0],list(set(ch).intersection(ch2))[0][1]) == (x-20,y):
            move.append('left1')
        elif (list(set(ch).intersection(ch2))[0][0],list(set(ch).intersection(ch2))[0][1]) == (x,y+20):
            move.append('right')
        elif (list(set(ch).intersection(ch2))[0][0],list(set(ch).intersection(ch2))[0][1]) == (x,y-20):
            move.append('left')
        if move[z] == save:
             move[z] = 'forward'
        else:
            save = move[z]

        z = z+1
        count = count +1
    move[0] = 'forward'
    return path ,move
    
        



        




def solve_line():
    for i in solve()[0]:
        x,y = i
        pygame.draw.rect(screen, YELLOW, (x+7, y+7, 5, 5), 0)


      
solve_line()
pygame.draw.rect(screen, (255,0,0), (start[0]+7, start[1]+7, 5, 5), 0)
pygame.draw.rect(screen, (0,0,255), (end[0]+7, end[1]+7, 5, 5), 0)
pygame.display.update()


pygame.display.update()
