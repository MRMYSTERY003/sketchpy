import turtle as tu
import cv2 


class trace:
    def __init__(self, img_path, zoom = 5,scale = .25):
        '''trace any image you want, with the help of this trace class\n
        img_path - path of the image to be traced\n
        zoom - zoom of the image\n
        scale - scale of the original image'''
        self.coordinates = []
        self.scale_x, self.scale_y = scale,scale
        self.zoom_scale_x, self.zoom_scale_y = zoom, zoom
        self.cx, self.cy = (self.zoom_scale_x*100)//2,(self.zoom_scale_y*100)//2
        print('----- USE RIGHT CLICK TO CREATE A TRACE POINT -----\n----- USE LEFT CLICK TO REMOVE A TRACE POINT -----\n----- ONCE FINISHED PRESS ANY BUTTON TO SAVE YOUR DATA -----')


        img = cv2.imread(img_path)
        self.img = cv2.resize(img,(0,0),None,self.scale_x, self.scale_y)
        self.color_li = []

    def click_event(self, event,x,y,flag,params):
        if event == cv2.EVENT_LBUTTONDOWN:
            print(x,' ',y)
            self.coordinates.append((x,y))
            print(self.img[x][y])
            self.color_li.append(tuple(self.img[x][y]))
            temp = cv2.circle(self.img, (x,y), radius=1, color=(0, 255, 255), thickness=-1)
        if event == cv2.EVENT_RBUTTONDOWN:
            print(f'poping {x} and {y}')
            print(f'coord : {self.coordinates[-1]}\n color : {tuple(self.color_li[-1])}')
            temp = cv2.circle(self.img, tuple(self.coordinates[-1]), radius=0, color=(int(self.color_li[-1][0]),int(self.color_li[-1][1]),int(self.color_li[-1][2])), thickness=-1)
            print(f"actual col {self.img[x][y]} : changed img {int(self.color_li[-1][0]),int(self.color_li[-1][1]),int(self.color_li[-1][2])}")
            #print('img:',img[y,x,:])

            self.coordinates.pop()
            self.color_li.pop()
        if event == cv2.EVENT_MBUTTONDOWN:
            print('mouse wheel pressed')
            print('creating break point')
            self.coordinates.append((-1,-1))
        try:
            zoom = cv2.resize(self.img[y-50:y+50,x-50:x+50,:],(0,0),None,self.zoom_scale_x,self.zoom_scale_y)
            zoom[self.cx-3:self.cx+3,self.cx-3:self.cx+3,:] = 175
            cv2.imshow('zoom',zoom)
        except:
            print('out of range!!')



    def trace(self):
        cv2.imshow('Main image',self.img)
        cv2.setMouseCallback('Main image',self.click_event)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print(self.coordinates)

        if len(self.coordinates) > 0:
            from os.path import exists
            file = input('enter the name the file: ')

            path_exists = exists(f"./{file}.txt")

            if path_exists:
                print(f'the file {file} already exists!!!')
                des = input('do you what to append the data: (y/n) ')
                if des == 'y' or des == 'Y':
                    data = open(f'{file}.txt','a')
                    print('creating a break point and appending....')
                    data.write(str((-1,-1))+'\n')
                    for i in self.coordinates:
                        #x,y = i
                        data.write(str(i)+'\n')
                    print(f'all the coordinates are save in {file}')
                    data.close()
                else:
                    print('deleting all the data and writing.....')
                    data = open(f'{file}.txt','w')
                    for i in self.coordinates:
                        x,y = i
                        data.write(str(i)+'\n')
                    print(f'all the coordinates are save in {file}')
                    data.close()

            else:
                data = open(f'{file}.txt','w')
                for i in self.coordinates:
                    x,y = i
                    data.write(str(i)+'\n')
                print(f'all the coordinates are save in {file}')
                data.close()
        
        else:
            print('no coordinates are detected to be saved...')




class sketch:

    def __init__(self,x_offset = 300, y_offset = 300):
        '''Draw the traced image with help of this sketch function\n
        x-offset - postion of the image in x axis\n
        y-offset - postion of the image in y axis\n
        call the draw_fn() to draw the traced image'''
        self.pen = tu.Turtle()
        self.pen.speed(0)
        self.x_offset = x_offset
        self.y_offset = y_offset


    def get_coord(self,data):                
        tu = []
        for i in data.readlines():
            i = (i.strip('\n')).strip('(').strip(')')
            tu.append(tuple(map(int,i.split(','))))

        return tu


    def go(self, x, y):
        self.pen.penup()
        self.pen.goto(x-self.x_offset,(y*-1)+self.y_offset)
        self.pen.pendown()  


    def paint(self,coord,co=(0,0,0)):
        self.pen.color(co)
        t_x,t_y = coord[0]
        self.go(t_x,t_y)
        self.pen.fillcolor(co)
        self.pen.begin_fill()
        t = 0
        for i in coord[1:]:
            print(i)
            x,y = i
            if t:
                self.go(x,y)
                t = 0
                self.pen.begin_fill()
                continue
            if x == -1 and y == -1:
                t = 1
                self.pen.end_fill()
                continue
            else:
                self.pen.goto(x-self.x_offset,(y*-1)+self.y_offset) 
        self.pen.end_fill()


    def draw_fn(self,file,mode = 1,co = (0,0,0),thickness = 1,retain = False):

        '''file - path of the file which contains the coordinates\n
        mode - mode of drawing (1 - sketch with line, 0 - fill with color)\n
        co - color of the line or fill\n
        thickness - thickness of the line\n
        retain - retain the image drawn after executing'''

        co = (co[0]/255,co[1]/255,co[2]/255)

        self.pen.color(co)
        data = open(f'{file}.txt','r')
        coord = self.get_coord(data)

        if mode:
            self.pen.width(thickness)
            t_x,t_y = coord[0]
            self.go(t_x,t_y)
            t = 0
            for i in coord[1:]:
                print(i)
                x,y = i
                if t:
                    self.go(x,y)
                    t = 0
                    continue
                if x == -1 and y == -1:
                    t = 1
                    continue
                else:
                    self.pen.goto(x-self.x_offset,(y*-1)+self.y_offset)
        else:
            self.paint(coord=coord,co = co)
        
        if retain:
            tu.done()

    





