import math
import cairo

# WIDTH,HEIGHT,PIXEL = 1.41, 1, 3508

class DrawingClass:
    def __init__(self,fileName,drawing_scale_factor,type):
        WIDTH,HEIGHT,PIXEL = 1.41, 1, 3508
        if type == 'horizontal':
            WIDTH,HEIGHT,PIXEL = 1.41, 1, 3508
        elif type == 'vertical':
            WIDTH,HEIGHT,PIXEL = 1, 1.41, 3508
        self.fileName = fileName
        surface = self.create_surface(fileName+".svg",WIDTH,HEIGHT,PIXEL)
        self.surface = surface
        self.cr = self.create_context(surface,WIDTH,HEIGHT,PIXEL)
        self.drawingScaleFactor = drawing_scale_factor
        self.line_width = 10

    def create_surface(self,fileName,width,height,pixel):
        surface = cairo.SVGSurface(fileName, width*pixel, height*pixel)
#         surface.set_document_unit(4)
        return surface

    def create_context(self,surface,width,height,pixel):
        cr = cairo.Context(surface)
        cr.rectangle(0, 0, width*pixel, height*pixel)
        cr.set_source_rgb(1,1,1)
        cr.fill()
        return cr

    def draw_rectangle(self, startingX, startingY, length, breadth, line_width=2, colorRed=0, colorGreen=0, colorBlue=0, colorAlpha=1):
        self.cr.set_line_width(line_width)
        self.cr.set_source_rgba(colorRed, colorGreen, colorBlue, colorAlpha)
        self.cr.rectangle(startingX, startingY, length, breadth) # Rectangle(x0, y0, x1, y1)
        self.cr.stroke()

    def draw_ellipse(self, centerX, centerY, headScale1, headScale2, diameter, flip, orientation, line_width=2, colorRed=0, colorGreen=0, colorBlue=0, colorAlpha=1):
        self.cr.set_line_width(line_width)
        self.cr.set_source_rgba(colorRed, colorGreen, colorBlue, colorAlpha)
        
        if orientation:
            self.cr.scale(1,headScale1/headScale2)
            if flip:
                self.cr.arc_negative(centerX+diameter/2, 2*centerY, diameter/2, 0, math.pi)
            else :
                self.cr.arc(centerX+diameter/2, 2*centerY, diameter/2, 0, math.pi)
            self.cr.stroke()
            self.cr.scale(1,headScale2/headScale1)
        else:
            self.cr.scale(headScale1/headScale2,1)
            if flip:
                self.cr.arc_negative(2*centerX, centerY+diameter/2, diameter/2, math.pi/2, 3*math.pi/2)
            else :
                self.cr.arc(2*centerX, centerY+diameter/2, diameter/2, math.pi/2, 3*math.pi/2)
            self.cr.stroke()
            self.cr.scale(headScale2/headScale1,1)

    def draw_head_left(self, centerX, centerY, headScale1, headScale2, diameter, shellFlange, line_width=2, colorRed=0, colorGreen=0, colorBlue=0, colorAlpha=1):
        self.draw_rectangle(centerX-shellFlange, centerY, shellFlange, diameter, line_width, colorRed, colorGreen, colorBlue, colorAlpha)   
        self.draw_ellipse(centerX-shellFlange, centerY, headScale1, headScale2, diameter, False, False, line_width, colorRed, colorGreen, colorBlue, colorAlpha)

    def draw_head_right(self, centerX, centerY, headScale1, headScale2, diameter, shellFlange, line_width=2, colorRed=0, colorGreen=0, colorBlue=0, colorAlpha=1):
        self.draw_rectangle(centerX, centerY, shellFlange, diameter, line_width, colorRed, colorGreen, colorBlue, colorAlpha)
        self.draw_ellipse(centerX+shellFlange, centerY, headScale1, headScale2, diameter, True, False, line_width, colorRed, colorGreen, colorBlue, colorAlpha)
        
    def draw_head_top(self, centerX, centerY, headScale1, headScale2, diameter, shellFlange, line_width=2, colorRed=0, colorGreen=0, colorBlue=0, colorAlpha=1):
        self.draw_rectangle(centerX, centerY, diameter, shellFlange, line_width, colorRed, colorGreen, colorBlue, colorAlpha)
        self.draw_ellipse(centerX, centerY, headScale1, headScale2, diameter, True, True, line_width, colorRed, colorGreen, colorBlue, colorAlpha)
    
    def draw_head_bottom(self, centerX, centerY, headScale1, headScale2, diameter, shellFlange, line_width=2, colorRed=0, colorGreen=0, colorBlue=0, colorAlpha=1):
        self.draw_rectangle(centerX, centerY, diameter, shellFlange, line_width, colorRed, colorGreen, colorBlue, colorAlpha)
        self.draw_ellipse(centerX, centerY+shellFlange, headScale1, headScale2, diameter, False, True, line_width, colorRed, colorGreen, colorBlue, colorAlpha)

    def draw_nozzle_type_top(self, startingX, startingY, position, data, line_width=2, colorRed=0, colorGreen=0, colorBlue=0, colorAlpha=1):
        
        self.draw_rectangle(
            startingX+position,
            startingY-data.get('lengthOfPipe'),
            data.get('diameterOfPipe'),
            data.get('lengthOfPipe'),
            line_width,colorRed,colorGreen,colorBlue,colorAlpha)
        
        self.draw_rectangle(
            startingX+position+(data.get('diameterOfPipe')-data.get('diameterOfFlange'))/2,
            startingY-data.get('lengthOfPipe')-data.get('lengthOfFlange'),
            data.get('diameterOfFlange'),
            data.get('lengthOfFlange'),
            line_width,colorRed,colorGreen,colorBlue,colorAlpha)
        
        self.draw_rectangle(
            startingX+position+(data.get('diameterOfPipe')-data.get('diameterOfRaisedFace'))/2,
            startingY-data.get('lengthOfPipe')-data.get('lengthOfFlange')-4*data.get('lengthOfRaisedFace'),
            data.get('diameterOfRaisedFace'),
            data.get('lengthOfRaisedFace'),
            line_width,colorRed,colorGreen,colorBlue,colorAlpha)
        
    def draw_nozzle_type_bottom(self, startingX, startingY, position, data, line_width=2, colorRed=0, colorGreen=0, colorBlue=0, colorAlpha=1):
    
        self.draw_rectangle(
            startingX+position,
            startingY+data.get('diameterOfCylinder'),
            data.get('diameterOfPipe'),
            data.get('lengthOfPipe'),
            line_width,colorRed,colorGreen,colorBlue,colorAlpha)
        
        self.draw_rectangle(
            startingX+position+(data.get('diameterOfPipe')-data.get('diameterOfFlange'))/2,
            startingY+data.get('lengthOfPipe')+data.get('diameterOfCylinder'),
            data.get('diameterOfFlange'),
            data.get('lengthOfFlange'),
            line_width,colorRed,colorGreen,colorBlue,colorAlpha)
        
        self.draw_rectangle(
            startingX+position+(data.get('diameterOfPipe')-data.get('diameterOfRaisedFace'))/2,
            startingY+data.get('lengthOfPipe')+data.get('lengthOfFlange')+4*data.get('lengthOfRaisedFace')+data.get('diameterOfCylinder'),
            data.get('diameterOfRaisedFace'),
            data.get('lengthOfRaisedFace'),
            line_width,colorRed,colorGreen,colorBlue,colorAlpha)
        
    def draw_nozzle_type_left(self, startingX, startingY, position, data, line_width=2, colorRed=0, colorGreen=0, colorBlue=0, colorAlpha=1):
    
        self.draw_rectangle(
            startingX-data.get('lengthOfPipe'),
            startingY+position,
            data.get('lengthOfPipe'),
            data.get('diameterOfPipe'),
            line_width,colorRed,colorGreen,colorBlue,colorAlpha)
        
        self.draw_rectangle(
            startingX-data.get('lengthOfPipe')-data.get('lengthOfFlange'),
            startingY+position+(data.get('diameterOfPipe')-data.get('diameterOfFlange'))/2,
            data.get('lengthOfFlange'),
            data.get('diameterOfFlange'),
            line_width,colorRed,colorGreen,colorBlue,colorAlpha)
        
        self.draw_rectangle(
            startingX-data.get('lengthOfPipe')-data.get('lengthOfFlange')-4*data.get('lengthOfRaisedFace'),
            startingY+position+(data.get('diameterOfPipe')-data.get('diameterOfRaisedFace'))/2,
            data.get('lengthOfRaisedFace'),
            data.get('diameterOfRaisedFace'),
            line_width,colorRed,colorGreen,colorBlue,colorAlpha)
        
    def draw_nozzle_type_right(self, startingX, startingY, position, data, line_width=2, colorRed=0, colorGreen=0, colorBlue=0, colorAlpha=1):
    
        self.draw_rectangle(
            startingX+data.get('diameterOfCylinder'),
            startingY+position,
            data.get('lengthOfPipe'),
            data.get('diameterOfPipe'),
            line_width,colorRed,colorGreen,colorBlue,colorAlpha)
        
        self.draw_rectangle(
            startingX+data.get('lengthOfPipe')+data.get('diameterOfCylinder'),
            startingY+position+(data.get('diameterOfPipe')-data.get('diameterOfFlange'))/2,
            data.get('lengthOfFlange'),
            data.get('diameterOfFlange'),
            line_width,colorRed,colorGreen,colorBlue,colorAlpha)
        
        self.draw_rectangle(
            startingX+data.get('lengthOfPipe')+data.get('lengthOfFlange')+4*data.get('lengthOfRaisedFace')+data.get('diameterOfCylinder'),
            startingY+position+(data.get('diameterOfPipe')-data.get('diameterOfRaisedFace'))/2,
            data.get('lengthOfRaisedFace'),
            data.get('diameterOfRaisedFace'),
            line_width,colorRed,colorGreen,colorBlue,colorAlpha)
        
    def arrange_data (self,data):
        main_array = {
            "Cylinder": [],
            "Ellipsoidal Head":[],
            "Nozzle":[]
        }
        starting_x = 0
        starting_y = 0
        max_array = []
        total_length = 0
        for val in data.get('components'):
            if val.get('component') == 'Cylinder':
                main_array.get('Cylinder').append(val)
                total_length = total_length + float(val.get('length'))*12
            elif val.get('component') == 'Ellipsoidal Head':
                main_array.get('Ellipsoidal Head').append(val)
                total_length = total_length+((float(val.get('sd'))/2)/(float(val.get('hr').split(':')[0])))
                if float(val.get('position')) == 0:
                   starting_x = ((float(val.get('sd'))/2) /
                                    (float(val.get('hr').split(":")[0]))) * 40
            elif val.get('component') == 'Nozzle':
                main_array.get('Nozzle').append(val)
                if float(val.get('orientation')) >= 90 and float(val.get('orientation')) <=270:
                    max_array.append(float(val.get('externalNozzleProjection')))

        starting_y = max(max_array)*self.drawingScaleFactor
        return main_array,starting_x,total_length

        
    def draw_main_horizontal(self,data,starting_x,starting_y):
        leftx = float(starting_x)
        rightx = 0
        topy = float(starting_y)
        bottomy = 0
        if data.get('Cylinder'):
            for val in data.get('Cylinder'):
                self.draw_rectangle(
                    float(leftx + rightx),
                    float(topy),
                    float(val.get('length'))*self.drawingScaleFactor*12,
                    float(val.get('sd'))*self.drawingScaleFactor,
                    self.line_width
                )
                rightx = rightx + float(val.get('length'))*self.drawingScaleFactor*12

        if data.get('Ellipsoidal Head'):
            for val in data.get('Ellipsoidal Head'):
                if float(val.get('position')) == 0:
                    self.draw_head_left(
                        float(leftx),
                        float(topy),
                        float(val.get('hr').split(":")[1])*self.drawingScaleFactor,
                        float(val.get('hr').split(":")[0])*self.drawingScaleFactor,
                        float(val.get('sd'))*self.drawingScaleFactor,
                        float(val.get('srl'))*self.drawingScaleFactor,
                        self.line_width
                    )
                elif float(val.get('position')) == 1:
                    self.draw_head_right(
                        float(leftx+rightx),
                        float(topy),
                        float(val.get('hr').split(":")[1])*self.drawingScaleFactor,
                        float(val.get('hr').split(":")[0])*self.drawingScaleFactor,
                        float(val.get('sd'))*self.drawingScaleFactor,
                        float(val.get('srl'))*self.drawingScaleFactor,
                        self.line_width
                    )
        
        if data.get('Nozzle'):
            for val in data.get('Nozzle'):
                if float(val.get('orientation')) >= 0 and float(val.get('orientation')) <=180:
                    self.draw_nozzle_type_bottom(
                        float(leftx),
                        float(topy),
                        float(val.get('height'))*self.drawingScaleFactor*12,
                        {
                            "lengthOfPipe":float(val.get('externalNozzleProjection'))*self.drawingScaleFactor,
                            "diameterOfPipe":float(val.get('value').get('barrel_outer_diameter'))*self.drawingScaleFactor,
                            "lengthOfFlange":float(val.get('value').get('flange_thickness'))*self.drawingScaleFactor,
                            "diameterOfFlange":float(val.get('value').get('flange_outer_diameter'))*self.drawingScaleFactor,
                            "lengthOfRaisedFace":float(val.get('value').get('raised_face_thickness'))*self.drawingScaleFactor,
                            "diameterOfRaisedFace":float(val.get('value').get('raised_face_diameter'))*self.drawingScaleFactor,
                            "diameterOfCylinder":float(data.get('Cylinder')[0].get('sd'))*self.drawingScaleFactor
                        },
                        self.line_width
                    )
                else:
                    self.draw_nozzle_type_top(
                        float(leftx),
                        float(topy),
                        float(val.get('height'))*self.drawingScaleFactor*12,
                        {
                            "lengthOfPipe":float(val.get('externalNozzleProjection'))*self.drawingScaleFactor,
                            "diameterOfPipe":float(val.get('value').get('barrel_outer_diameter'))*self.drawingScaleFactor,
                            "lengthOfFlange":float(val.get('value').get('flange_thickness'))*self.drawingScaleFactor,
                            "diameterOfFlange":float(val.get('value').get('flange_outer_diameter'))*self.drawingScaleFactor,
                            "lengthOfRaisedFace":float(val.get('value').get('raised_face_thickness'))*self.drawingScaleFactor,
                            "diameterOfRaisedFace":float(val.get('value').get('raised_face_diameter'))*self.drawingScaleFactor,
                            "diameterOfCylinder":float(data.get('Cylinder')[0].get('sd'))*self.drawingScaleFactor
                        },
                        self.line_width
                    )

        self.surface.write_to_png(self.fileName+".png")  # Output to PNG
        self.surface.finish()
        
    def draw_main_vertical(self,data,starting_x,starting_y,total_length):
        leftx = 0
        rightx = float(starting_x)
        topy = float(starting_y)
        bottomy = float(total_length)
        if data.get('Cylinder'):
            cylinder_height = 0
            for val in data.get('Cylinder'):
                self.draw_rectangle(
                    float(rightx),
                    float(topy-cylinder_height),
                    float(val.get('sd'))*self.drawingScaleFactor,
                    float(val.get('length'))*self.drawingScaleFactor*12,
                    self.line_width
                )
                cylinder_height = cylinder_height - float(val.get('length'))*self.drawingScaleFactor*12

        if data.get('Ellipsoidal Head'):
            for val in data.get('Ellipsoidal Head'):
                if float(val.get('position')) == 0:
                    length_of_head = ((float(val.get('sd'))/2)/(float(val.get('hr').split(":")[0])))
                    self.draw_head_top(
                        float(rightx),
                        float(topy),
                        float(val.get('hr').split(":")[1])*self.drawingScaleFactor,
                        float(val.get('hr').split(":")[0])*self.drawingScaleFactor,
                        float(val.get('sd'))*self.drawingScaleFactor,
                        float(val.get('srl'))*self.drawingScaleFactor,
                        self.line_width
                    )
                elif float(val.get('position')) == 1:
                    self.draw_head_bottom(
                        float(rightx),
                        float(topy+(bottomy-2*length_of_head)*self.drawingScaleFactor),
                        float(val.get('hr').split(":")[1])*self.drawingScaleFactor,
                        float(val.get('hr').split(":")[0])*self.drawingScaleFactor,
                        float(val.get('sd'))*self.drawingScaleFactor,
                        float(val.get('srl'))*self.drawingScaleFactor,
                        self.line_width
                    )

        if data.get('Nozzle'):
            for val in data.get('Nozzle'):
                if float(val.get('orientation')) >= 0 and float(val.get('orientation')) <=180:
                    self.draw_nozzle_type_left(
                        float(rightx),
                        float(topy),
                        float(val.get('height'))*self.drawingScaleFactor*12,
                        {
                            "lengthOfPipe":float(val.get('externalNozzleProjection'))*self.drawingScaleFactor,
                            "diameterOfPipe":float(val.get('value').get('barrel_outer_diameter'))*self.drawingScaleFactor,
                            "lengthOfFlange":float(val.get('value').get('flange_thickness'))*self.drawingScaleFactor,
                            "diameterOfFlange":float(val.get('value').get('flange_outer_diameter'))*self.drawingScaleFactor,
                            "lengthOfRaisedFace":float(val.get('value').get('raised_face_thickness'))*self.drawingScaleFactor,
                            "diameterOfRaisedFace":float(val.get('value').get('raised_face_diameter'))*self.drawingScaleFactor,
                            "diameterOfCylinder":float(data.get('Cylinder')[0].get('sd'))*self.drawingScaleFactor
                        },
                        self.line_width
                    )
                else:
                    self.draw_nozzle_type_right(
                        float(rightx),
                        float(topy),
                        float(val.get('height'))*self.drawingScaleFactor*12,
                        {
                            "lengthOfPipe":float(val.get('externalNozzleProjection'))*self.drawingScaleFactor,
                            "diameterOfPipe":float(val.get('value').get('barrel_outer_diameter'))*self.drawingScaleFactor,
                            "lengthOfFlange":float(val.get('value').get('flange_thickness'))*self.drawingScaleFactor,
                            "diameterOfFlange":float(val.get('value').get('flange_outer_diameter'))*self.drawingScaleFactor,
                            "lengthOfRaisedFace":float(val.get('value').get('raised_face_thickness'))*self.drawingScaleFactor,
                            "diameterOfRaisedFace":float(val.get('value').get('raised_face_diameter'))*self.drawingScaleFactor,
                            "diameterOfCylinder":float(data.get('Cylinder')[0].get('sd'))*self.drawingScaleFactor
                        },
                        self.line_width
                    )

        self.surface.write_to_png(self.fileName+".png")  # Output to PNG
        self.surface.finish()
