import pygame
import math as m
import os, sys


class PyGame(object):
    os.environ["SDL_VIDEODRIVER"] = "dummy"

    #initialize pygame
    pygame.init()

    # window information
    displayW = 800
    displayH = 600
    size = (displayW,displayH)

    screen = pygame.display.set_mode(size, 0, 32)

    White = (255,255,255)
    Yellow = (255,255,0)
    Black = (0,0,0)

    def __init__(self):
        self.screen.fill(self.White)
        pygame.display.flip()

    def drawRectangle(self,starting_x,starting_y,length,breadth,width=1):
        pygame.draw.rect(self.screen,self.Black,[starting_x,starting_y,length,breadth],width)
        pygame.display.flip()

    def drawEllipse(self,starting_x,starting_y,major_axis,minor_axis,start_angle=0,stop_angle=m.pi,width=1):
        #pygame.draw.rect(screen,Yellow,[starting_x,starting_y,major_axis,minor_axis],1)
        pygame.draw.arc(self.screen,self.Black,[starting_x,starting_y,major_axis,minor_axis],start_angle,stop_angle,width)
        pygame.display.flip()

    def drawNozzle(self,starting_x,starting_y,length_nozzle,breadth_nozzle,nozzle_name,flip=False,width=1):

        overlappingValue = 1
        nozzleScreen_width = length_nozzle+20
        nozzleScreen_height = breadth_nozzle+10-overlappingValue+30

        nozzleScreen = pygame.surface.Surface((nozzleScreen_width,nozzleScreen_height), pygame.SRCALPHA,32)
        

        starting_xx = starting_x
        starting_yy = starting_y
        starting_x = 10
        starting_y = nozzleScreen_height-breadth_nozzle

        pygame.draw.rect(nozzleScreen,self.Black,[starting_x,starting_y,length_nozzle,breadth_nozzle],width)
        pygame.draw.polygon(nozzleScreen,self.Black,[
            [starting_x,starting_y],
            [starting_x-5,starting_y-5],
            [starting_x+length_nozzle+5,starting_y-5],
            [starting_x+length_nozzle,starting_y]
        ],width)
        pygame.draw.rect(nozzleScreen,self.Black,[starting_x-5-5,starting_y-5-5+overlappingValue,5+5+length_nozzle+5+5,5],width)

        # nozzle naming 
        pygame.draw.line(nozzleScreen,self.Black,(starting_x+length_nozzle/2,starting_y+breadth_nozzle/2),(starting_x+length_nozzle/2,starting_y-breadth_nozzle),width)
        pygame.draw.polygon(nozzleScreen,self.Black,[
            [starting_x+length_nozzle/2,starting_y-breadth_nozzle],
            [starting_x+length_nozzle/2-4,starting_y-breadth_nozzle],
            [starting_x+length_nozzle/2-4-4,starting_y-breadth_nozzle-4],
            [starting_x+length_nozzle/2-4,starting_y-breadth_nozzle-3-4],
            [starting_x+length_nozzle/2+4,starting_y-breadth_nozzle-3-4],
            [starting_x+length_nozzle/2+4+4,starting_y-breadth_nozzle-4],
            [starting_x+length_nozzle/2+4,starting_y-breadth_nozzle]
        ],width)
        
        

        if flip:
            nozzleScreen = pygame.transform.flip(nozzleScreen,False,True)
            self.screen.blit(nozzleScreen,(starting_xx-nozzleScreen_width,starting_yy))
            self.writeText(nozzle_name,starting_xx-starting_x-length_nozzle/2-3,starting_yy+starting_y+1,10)
        else :
            self.screen.blit(nozzleScreen,(starting_xx-nozzleScreen_width,starting_yy-nozzleScreen_height))
            self.writeText(nozzle_name,starting_xx-starting_x-length_nozzle/2-3,starting_yy-starting_y-7,10)

        pygame.display.flip()

    def writeText(self,words,starting_x,starting_y,text_size=5,rotate=False):
        font = pygame.font.SysFont('Calibri',text_size,True,False)
        text = font.render(words,True,self.Black)
        if rotate:
            text = pygame.transform.rotate(text,90)
            self.screen.blit(text,(starting_x,starting_y))
        else:
            self.screen.blit(text,(starting_x,starting_y))

            pygame.display.flip()

    def try_surface(self):
        myNewSurface = pygame.Surface((20,30))
        myNewSurface.fill(White)

        pygame.draw.circle(myNewSurface,self.Black,[10,15],10,0)

        self.screen.blit(myNewSurface,(20,20))
        pygame.display.flip()

    def do_task(self,location):
        starting_x = 100
        starting_y = 200
        ellipse_major = 200
        ellipse_minor = ellipse_major/2
        cylinder_length = 100
        position_nozzle1 = 50
        length_nozzle = 10
        breadth_nozzle = 20
        overlappingValue = 1

        self.drawEllipse(starting_x,starting_y,ellipse_minor,ellipse_major,m.pi/2,(3*m.pi/2)+0.1)
        
        self.drawRectangle((ellipse_minor/2) +starting_x,starting_y,cylinder_length,ellipse_major)

        self.drawRectangle(starting_x+(ellipse_minor/2)+cylinder_length-overlappingValue,starting_y,cylinder_length,ellipse_major)

        self.drawEllipse(starting_x+(ellipse_minor/2)+cylinder_length+cylinder_length-(ellipse_minor/2),starting_y,ellipse_minor,ellipse_major,(3*m.pi/2)-0.11,(m.pi/2)+0.1)

        self.drawNozzle(starting_x+ellipse_minor/2+position_nozzle1,starting_y+overlappingValue,length_nozzle,breadth_nozzle,"N1",False)

        self.drawNozzle(starting_x+ellipse_minor/2+cylinder_length+position_nozzle1,starting_y+overlappingValue,length_nozzle,breadth_nozzle,"N2",False)

        self.drawNozzle(starting_x+ellipse_minor/2+cylinder_length+position_nozzle1,starting_y+ellipse_major-overlappingValue,length_nozzle,breadth_nozzle,"N3",True)

        pygame.image.save(self.screen,location+"pygame.png")
        return location+"pygame.png"
        

# if __name__ == "__main__":

#     pygames = PyGame()
#     pygames.do_task()
#     #pygames.writeText()
    #pygames.try_surface()
    #pygames.drawNozzle()
    # pygames.drawRectangle(10,20,20,10)

        