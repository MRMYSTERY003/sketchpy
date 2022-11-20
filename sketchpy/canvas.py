from traceback import print_tb
from tqdm import tqdm
import turtle
import numpy as np
import turtle as tu
import os
import cv2
import sys
from svgpathtools import svg2paths2
from svg.path import parse_path


class trace:
    def __init__(self, img_path, zoom=5, scale=.25):
        '''trace any image you want, with the help of this trace class\n
        img_path - path of the image to be traced\n
        zoom - zoom of the image\n
        scale - scale of the original image'''
        self.coordinates = []
        self.scale_x, self.scale_y = scale, scale
        self.zoom_scale_x, self.zoom_scale_y = zoom, zoom
        self.cx, self.cy = (self.zoom_scale_x *
                            100)//2, (self.zoom_scale_y*100)//2
        print('----- USE RIGHT CLICK TO CREATE A TRACE POINT -----\n----- USE LEFT CLICK TO REMOVE A TRACE POINT -----\n----- ONCE FINISHED PRESS ANY BUTTON TO SAVE YOUR DATA -----')

        img = cv2.imread(img_path)
        self.img = cv2.resize(img, (0, 0), None, self.scale_x, self.scale_y)
        self.color_li = []

    def click_event(self, event, x, y, flag, params):
        if event == cv2.EVENT_LBUTTONDOWN:
            print(x, ' ', y)
            self.coordinates.append((x, y))
            print(self.img[x][y])
            self.color_li.append(tuple(self.img[x][y]))
            temp = cv2.circle(self.img, (x, y), radius=1,
                              color=(0, 255, 255), thickness=-1)
        if event == cv2.EVENT_RBUTTONDOWN:
            print(f'poping {x} and {y}')
            print(
                f'coord : {self.coordinates[-1]}\n color : {tuple(self.color_li[-1])}')
            temp = cv2.circle(self.img, tuple(self.coordinates[-1]), radius=0, color=(int(
                self.color_li[-1][0]), int(self.color_li[-1][1]), int(self.color_li[-1][2])), thickness=-1)
            print(
                f"actual col {self.img[x][y]} : changed img {int(self.color_li[-1][0]),int(self.color_li[-1][1]),int(self.color_li[-1][2])}")
            # print('img:',img[y,x,:])

            self.coordinates.pop()
            self.color_li.pop()
        if event == cv2.EVENT_MBUTTONDOWN:
            print('mouse wheel pressed')
            print('creating break point')
            self.coordinates.append((-1, -1))
        try:
            zoom = cv2.resize(self.img[y-50:y+50, x-50:x+50, :],
                              (0, 0), None, self.zoom_scale_x, self.zoom_scale_y)
            zoom[self.cx-3:self.cx+3, self.cx-3:self.cx+3, :] = 175
            cv2.imshow('zoom', zoom)
        except:
            print('out of range!!')

    def trace(self):
        cv2.imshow('Main image', self.img)
        cv2.setMouseCallback('Main image', self.click_event)
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
                    data = open(f'{file}.txt', 'a')
                    print('creating a break point and appending....')
                    data.write(str((-1, -1))+'\n')
                    for i in self.coordinates:
                        #x,y = i
                        data.write(str(i)+'\n')
                    print(f'all the coordinates are save in {file}')
                    data.close()
                else:
                    print('deleting all the data and writing.....')
                    data = open(f'{file}.txt', 'w')
                    for i in self.coordinates:
                        x, y = i
                        data.write(str(i)+'\n')
                    print(f'all the coordinates are save in {file}')
                    data.close()

            else:
                data = open(f'{file}.txt', 'w')
                for i in self.coordinates:
                    x, y = i
                    data.write(str(i)+'\n')
                print(f'all the coordinates are save in {file}')
                data.close()

        else:
            print('no coordinates are detected to be saved...')


class sketch:

    def __init__(self, x_offset=300, y_offset=300):
        '''Draw the traced image with help of this sketch function\n
        x-offset - postion of the image in x axis\n
        y-offset - postion of the image in y axis\n
        call the draw_fn() to draw the traced image'''
        self.pen = tu.Turtle()
        self.pen.speed(0)
        self.x_offset = x_offset
        self.y_offset = y_offset

    def get_coord(self, data):
        tu = []
        for i in data.readlines():
            i = (i.strip('\n')).strip('(').strip(')')
            tu.append(tuple(map(int, i.split(','))))

        return tu

    def go(self, x, y):
        self.pen.penup()
        self.pen.goto(x-self.x_offset, (y*-1)+self.y_offset)
        self.pen.pendown()

    def paint(self, coord, co=(0, 0, 0)):
        self.pen.color(co)
        t_x, t_y = coord[0]
        self.go(t_x, t_y)
        self.pen.fillcolor(co)
        self.pen.begin_fill()
        t = 0
        for i in coord[1:]:
            print(i)
            x, y = i
            if t:
                self.go(x, y)
                t = 0
                self.pen.begin_fill()
                continue
            if x == -1 and y == -1:
                t = 1
                self.pen.end_fill()
                continue
            else:
                self.pen.goto(x-self.x_offset, (y*-1)+self.y_offset)
        self.pen.end_fill()

    def draw_fn(self, file, mode=1, co=(0, 0, 0), thickness=1, retain=False):
        '''file - path of the file which contains the coordinates\n
        mode - mode of drawing (1 - sketch with line, 0 - fill with color)\n
        co - color of the line or fill\n
        thickness - thickness of the line\n
        retain - retain the image drawn after executing'''

        co = (co[0]/255, co[1]/255, co[2]/255)

        self.pen.color(co)
        data = open(f'{file}.txt', 'r')
        coord = self.get_coord(data)

        self.pen.width(thickness)
        if mode:
            t_x, t_y = coord[0]
            self.go(t_x, t_y)
            t = 0
            for i in coord[1:]:
                print(i)
                x, y = i
                if t:
                    self.go(x, y)
                    t = 0
                    continue
                if x == -1 and y == -1:
                    t = 1
                    continue
                else:
                    self.pen.goto(x-self.x_offset, (y*-1)+self.y_offset)
        else:
            self.paint(coord=coord, co=co)

        if retain:
            tu.done()


class ascii_art:
    def __init__(self):
        pass

    def convert_to_acsii(self, img_path, file_name=None) -> str:
        """Converts the given image to ascii art and save it to output_file"""

        from PIL import Image
        # pass the image as command line argument
        img = Image.open(img_path)

        # resize the image
        width, height = img.size
        aspect_ratio = height / width
        new_width = 80
        new_height = aspect_ratio * new_width * 0.55
        img = img.resize((new_width, int(new_height)))
        # new size of image
        # print(img.size)

        # convert image to greyscale format
        img = img.convert('L')

        pixels = img.getdata()

        # replace each pixel with a character from array
        chars = ["*", "S", "#", "&", "@", "$", "%", "*", "!", ":", "."]
        new_pixels = [chars[pixel // 25] for pixel in pixels]
        new_pixels = ''.join(new_pixels)

        # split string of chars into multiple strings of length equal to the new width and create a list
        new_pixels_count = len(new_pixels)
        ascii_image = [new_pixels[index:index + new_width]
                       for index in range(0, new_pixels_count, new_width)]
        ascii_image = "\n".join(ascii_image)

        # write to a text file.
        if file_name != None:
            with open(f"{file_name}.txt", "w") as f:
                f.write(ascii_image)
        return ascii_image

    def load_data(self, file_path=None, img_path=None, raw_data=None):

        if img_path != None:
            self.data = self.convert_to_acsii(img_path)
        elif file_path != None:
            re = open(file_path, 'r')
            self.data = re.readlines()
        elif raw_data != None:
            self.data = raw_data
            print('sepcify the correct data')
            return
        return self.data

    def draw(self, data):
        # setting the x and y coordinates
        s_x = -320
        s_y = 250

        p = tu.Pen()
        p.speed(0)
        tu.bgcolor('black')
        p.up()
        p.width(2)
        f_m = 0
        d_m = 4

        # function to select the color
        def set_col(c):
            chars = {"*": 'white', "S": 'green', "#": 'green', "&": 'white', "@": 'black',
                     "$": 'white', "%": 'white', "!": 'blue', ":": 'darkgreen', ".": 'grey'}
            col = chars[c]
            p.pencolor(col)

        def d(m, s_char):
            p.up()
            if s_char != '\n':
                set_col(s_char)

            p.goto(s_x - m, s_y)
            p.down()
            p.forward(1)

        for i in self.data:
            for j in i:
                d(f_m, j)
                f_m -= 4
            s_y -= 9
            s_x = -320
            f_m = 0
            d_m = 4

        tu.done()

    def print_to_terminal(self):
        for i in self.data:
            print(i, end='')
    
    def save(image, fName): # image will be img object pre-defined in user's code.
        image.save(fName + ".jpg")


class sketch_from_svg:

    def __init__(self, path, scale=500, x_offset=300, y_offset=300):

        self.path = path
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.scale = scale
  
    def save(image, fName): # image will be img object pre-defined in user's code.
        image.save(fName + ".jpg")
  

    def hex_to_rgb(self, string):
        strlen = len(string)
        if string.startswith('#'):
            if strlen == 7:
                r = string[1:3]
                g = string[3:5]
                b = string[5:7]
            elif strlen == 4:
                r = string[1:2]*2
                g = string[2:3]*2
                b = string[3:4]*2
        elif strlen == 3:
            r = string[0:1]*2
            g = string[1:2]*2
            b = string[2:3]*2
        else:
            r = string[0:2]
            g = string[2:4]
            b = string[4:6]

        return int(r, 16)/255, int(g, 16)/255, int(b, 16)/255

    def load_svg(self, file=None):
        print('loading data')
        paths, attributes, svg_att = svg2paths2(self.path)
        h = svg_att["height"]
        w = svg_att['width']
        try:
            self.height = int(h[:h.find('.')])
            self.width = int(w[:w.find('.')])
        except:
            self.height = int(h)
            self.width = int(w)
        self.x_offset = self.x_offset
        self.y_offset = self.y_offset

        res = []
        res.append([self.height, self.width, self.scale])
        for i in tqdm(attributes):
            path = parse_path(i['d'])
            co = i['fill']
            # print(co)
            col = self.hex_to_rgb(co)
            # print(col)
            n = len(list(path))+2
            pts = [((int((p.real/self.width)*self.scale))-self.x_offset, (int((p.imag/self.height)
                    * self.scale))-self.y_offset) for p in (path.point(i/n) for i in range(0, n+1))]
            res.append((pts, col))
            # res.append(pts)
        print('svg data loaded')
        if file != None:
            temp = np.array(res)
            np.save(file, res, allow_pickle=True)
            print(f'file is saved to {res}....')
        return res

    def move_to(self, x, y):
        self.pen.up()
        self.pen.goto(x, y)
        self.pen.down()

    def draw(self, retain=True, file=None, data=None, x_offset=0, y_offset=0, scale=None):
        if file != None:
            coordinates = np.load(file, allow_pickle=True)
            print(f'datas are loaded from {file}')
        elif data != None:
            coordinates = data
        else:
            coordinates = self.load_svg()
        self.pen = tu.Turtle()
        self.pen.speed(0)
        self.screen = tu.Screen()
        dimension = coordinates[0]
        height = dimension[0]
        width = dimension[1]
        if scale == None:
            try:
                self.scale = dimension[2]
            except:
                self.scale = self.scale
            # print(height*self.scale,width*self.scale)
            # self.screen.setup(width*self.scale,height*self.scale)
        else:
            self.scale = scale
            # self.screen.setup(width*self.scale,height*self.scale)
            # print(height*self.scale,width*self.scale)

        for path_col in coordinates[1:]:
            f = 1
            self.pen.color('black')
            # print(path_col)
            path = path_col[0]
            # print(path_col)
            col = path_col[1]
            # print(col)
            self.pen.color(col)
            self.pen.begin_fill()
            next = 0
            for coord in path:
                # for coord in path_col:
                x, y = coord
                x, y = (int((x/height)*self.scale)) - \
                    x_offset, (int((y/width)*self.scale))-y_offset
                y *= -1
                # print(x,y)
                if f:
                    self.move_to(x, y)
                    f = 0
                else:
                    self.pen.goto(x, y)
            self.pen.end_fill()
       
  
        if retain == True:
            tu.done()


class sketch_from_image:
    def __init__(self, path) -> None:
        self.path = path

    def save(image, fName): # image will be img object pre-defined in user's code.
        image.save(fName + ".jpg")

    def draw(self, threshold=127):

        img = cv2.imread(self.path, 2)
        ret, bw_img = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
        width = int(img.shape[1])
        height = int(img.shape[0])
        print(f'image loaded from {self.path}')
        my_screen = turtle.Screen()
        my_screen.screensize(width, height)
        my_pen = turtle.Turtle()
        my_screen.tracer(0)

        for i in tqdm(range(int(height/2), int(height/-2),  -1)):
            my_pen.penup()
            my_pen.goto(-(width / 2), i)

            for l in range(-int(width/2), int(width/2), 1):
                pix_width = int(l + (width/2))
                pix_height = int(height/2 - i)
                #print(f'height = {pix_height} ,width = {pix_width}, val = {bw_img[pix_height,pix_height]}')
                if bw_img[pix_height, pix_width] == 0:
                    my_pen.pendown()
                    my_pen.forward(1)
                else:
                    my_pen.penup()
                    my_pen.forward(1)
            my_screen.update()

        my_pen.hideturtle()
        print('done!')
        turtle.done()


class color_sketch_from_svg:

    def __init__(self, path=None, scale=50, x_offset=300, y_offset=300):

        self.path = path
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.scale = scale
    
    def save(image, fName): # image will be img object pre-defined in user's code.
        image.save(fName + ".jpg")

    def hex_to_rgb(self, string):
        strlen = len(string)
        # print(string)
        if string.startswith('#'):
            if strlen == 7:
                r = string[1:3]
                g = string[3:5]
                b = string[5:7]
            elif strlen == 4:
                r = string[1:2]*2
                g = string[2:3]*2
                b = string[3:4]*2
        elif strlen == 3:
            r = string[0:1]*2
            g = string[1:2]*2
            b = string[2:3]*2
        else:
            r = string[0:2]
            g = string[2:4]
            b = string[4:6]

        return int(r, 16)/255, int(g, 16)/255, int(b, 16)/255

    def load_svg(self, file=os.path.abspath(sys.argv[0])):
        print('loading data')
        if self.path != None:
            paths, attributes, svg_att = svg2paths2(self.path)
        h = svg_att["height"]
        w = svg_att['width']
        try:
            h = h.replace("px", "")
            w = w.replace("px", "")
            self.height = int(h[:h.find('.')])
            self.width = int(w[:w.find('.')])
        except:
            self.height = int(h)
            self.width = int(w)
        self.x_offset = self.x_offset
        self.y_offset = self.y_offset

        res = []
        res.append([self.height, self.width, self.scale])
        for i in tqdm(attributes):
            path = parse_path(i['d'])
            co = i['fill']
            # co = co.replace("fill: ", "")
            # # print(co)
            # co = co.replace(";", "")
            # # print(co)
            col = self.hex_to_rgb(co)
            # print(col)
            n = len(list(path))
            n = n-(n//4)
            pts = [((int((p.real/self.width)*self.scale))-self.x_offset, (int((p.imag/self.height)
                    * self.scale))-self.y_offset) for p in (path.point(i/n) for i in range(1, n+1))]
            res.append((pts, col))
            # res.append(pts)
        print('svg data loaded')

        temp = np.array(res)
        np.save(file, res, allow_pickle=True)
        print(f'file is saved to {file}....')
        return res

    def move_to(self, x, y):
        self.pen.up()
        self.pen.goto(x, y)
        self.pen.down()

    def draw(self, retain=True, file=None, data=None, x_offset=0, y_offset=0, scale=None):
        if file != None:
            coordinates = np.load(file, allow_pickle=True)
            print(f'datas are loaded from {file}')
        elif data != None:
            coordinates = data
        else:
            coordinates = self.load_svg()
        self.pen = tu.Turtle()
        self.pen.speed(0)
        self.screen = tu.Screen()
        dimension = coordinates[0]
        height = dimension[0]
        width = dimension[1]
        if scale == None:
            try:
                self.scale = dimension[2]
            except:
                self.scale = self.scale
            # print(height*self.scale,width*self.scale)
            # self.screen.setup(width*self.scale,height*self.scale)
        else:
            self.scale = scale
            # self.screen.setup(width*self.scale,height*self.scale)
            # print(height*self.scale,width*self.scale)

        for path_col in coordinates[1:]:
            f = 1
            self.pen.color('black')
            # print(path_col)
            path = path_col[0]
            # print(path_col)
            col = path_col[1]
            # print(col)
            self.pen.color(col)
            self.pen.begin_fill()
            le = len(path)

            for num, coord in enumerate(path):
                # for coord in path_col:
                x, y = coord
                x, y = (int((x/height)*self.scale)) - \
                    x_offset, (int((y/width)*self.scale))-y_offset
                y *= -1
                # print(x,y)
                if f:
                    self.pen.end_fill()
                    self.move_to(x, y)
                    self.pen.begin_fill()

                    f = 0
                # elif num == le-2:
                #     self.pen.end_fill()
                #     self.move_to(x, y)
                #     self.pen.begin_fill()
                #     print("in le-2")
                #     input()

                elif coord in path[num+1:]:
                    self.pen.end_fill()
                    self.move_to(x, y)
                    self.pen.begin_fill()
                    print("in coord")
                    input()

                else:
                    self.pen.goto(x, y)
            self.pen.end_fill()
            # input("enter")

        if retain == True:
            print("done sketching")
            tu.done()
