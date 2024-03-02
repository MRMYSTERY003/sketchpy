import multiprocessing as mp
from tqdm import tqdm
import numpy as np
import turtle as tu
import os
import cv2
import sys
import subprocess
from svgpathtools import svg2paths2
from svg.path import parse_path
from PIL import ImageGrab
import pkg_resources



def get_svg():
    '''Usage: \n
    from sketchpy import canvas
    canvas.get_svg()
    
    opens a local window from converting image files to svg files\n
    requires internet connection!!!'''
    exe_path = pkg_resources.resource_filename('sketchpy', 'files/converter.exe')
    try:
        subprocess.run(exe_path, shell=True)
    except Exception as e:
        print("An error occurred:", e)



class trace:
    def __init__(self, img_path, zoom=5, scale=0.25):
        """trace any image you want, with the help of this trace class\n
        USE RIGHT CLICK TO CREATE A TRACE POINT \n
        USE LEFT CLICK TO REMOVE A TRACE POINT\n
        ONCE FINISHED PRESS ANY BUTTON TO SAVE YOUR DATA\n \n
        img_path - path of the image to be traced\n
        zoom - zoom of the image\n
        scale - scale of the original image"""
        self.coordinates = []
        self.scale_x, self.scale_y = scale, scale
        self.zoom_scale_x, self.zoom_scale_y = zoom, zoom
        self.cx, self.cy = (self.zoom_scale_x * 100) // 2, (
            self.zoom_scale_y * 100
        ) // 2
        print(
            "----- USE RIGHT CLICK TO CREATE A TRACE POINT -----\n----- USE LEFT CLICK TO REMOVE A TRACE POINT -----\n----- ONCE FINISHED PRESS ANY BUTTON TO SAVE YOUR DATA -----"
        )

        img = cv2.imread(img_path)
        self.img = cv2.resize(img, (0, 0), None, self.scale_x, self.scale_y)
        self.color_li = []

    def click_event(self, event, x, y, flag, params):
        if event == cv2.EVENT_LBUTTONDOWN:
            print(x, " ", y)
            self.coordinates.append((x, y))
            print(self.img[x][y])
            self.color_li.append(tuple(self.img[x][y]))
            temp = cv2.circle(
                self.img, (x, y), radius=1, color=(0, 255, 255), thickness=-1
            )
        if event == cv2.EVENT_RBUTTONDOWN:
            print(f"poping {x} and {y}")
            print(
                f"coord : {self.coordinates[-1]}\n color : {tuple(self.color_li[-1])}"
            )
            temp = cv2.circle(
                self.img,
                tuple(self.coordinates[-1]),
                radius=0,
                color=(
                    int(self.color_li[-1][0]),
                    int(self.color_li[-1][1]),
                    int(self.color_li[-1][2]),
                ),
                thickness=-1,
            )
            print(
                f"actual col {self.img[x][y]} : changed img {int(self.color_li[-1][0]),int(self.color_li[-1][1]),int(self.color_li[-1][2])}"
            )
            # print('img:',img[y,x,:])

            self.coordinates.pop()
            self.color_li.pop()
        if event == cv2.EVENT_MBUTTONDOWN:
            print("mouse wheel pressed")
            print("creating break point")
            self.coordinates.append((-1, -1))
        try:
            zoom = cv2.resize(
                self.img[y - 50 : y + 50, x - 50 : x + 50, :],
                (0, 0),
                None,
                self.zoom_scale_x,
                self.zoom_scale_y,
            )
            zoom[self.cx - 3 : self.cx + 3, self.cx - 3 : self.cx + 3, :] = 175
            cv2.imshow("zoom", zoom)
        except:
            print("out of range!!")

    def trace(self):
        cv2.imshow("Main image", self.img)
        cv2.setMouseCallback("Main image", self.click_event)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print(self.coordinates)

        if len(self.coordinates) > 0:
            from os.path import exists

            file = input("enter the name the file: ")

            path_exists = exists(f"./{file}.txt")

            if path_exists:
                print(f"the file {file} already exists!!!")
                des = input("do you what to append the data: (y/n) ")
                if des == "y" or des == "Y":
                    data = open(f"{file}.txt", "a")
                    print("creating a break point and appending....")
                    data.write(str((-1, -1)) + "\n")
                    for i in self.coordinates:
                        # x,y = i
                        data.write(str(i) + "\n")
                    print(f"all the coordinates are save in {file}")
                    data.close()
                else:
                    print("deleting all the data and writing.....")
                    data = open(f"{file}.txt", "w")
                    for i in self.coordinates:
                        x, y = i
                        data.write(str(i) + "\n")
                    print(f"all the coordinates are save in {file}")
                    data.close()

            else:
                data = open(f"{file}.txt", "w")
                for i in self.coordinates:
                    x, y = i
                    data.write(str(i) + "\n")
                print(f"all the coordinates are save in {file}")
                data.close()

        else:
            print("no coordinates are detected to be saved...")



class sketch:

    def __init__(self, x_offset=300, y_offset=300, save=False):
        """Draw the traced image with help of this sketch function\n
        x-offset - postion of the image in x axis\n
        y-offset - postion of the image in y axis\n
        call the draw_fn() to draw the traced image"""
        self.pen = tu.Turtle()
        self.pen.speed(0)
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.save = save

    def get_coord(self, data):
        tu = []
        for i in data.readlines():
            i = (i.strip("\n")).strip("(").strip(")")
            tu.append(tuple(map(int, i.split(","))))

        return tu

    def go(self, x, y):
        self.pen.penup()
        self.pen.goto(x - self.x_offset, (y * -1) + self.y_offset)
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
                self.pen.goto(x - self.x_offset, (y * -1) + self.y_offset)
        self.pen.end_fill()

    def draw_fn(self, file, mode=1, co=(0, 0, 0), thickness=1, retain=False):
        """file - path of the file which contains the coordinates\n
        mode - mode of drawing (1 - sketch with line, 0 - fill with color)\n
        co - color of the line or fill\n
        thickness - thickness of the line\n
        retain - retain the image drawn after executing"""

        co = (co[0] / 255, co[1] / 255, co[2] / 255)

        self.pen.color(co)
        data = open(f"{file}.txt", "r")
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
                    self.pen.goto(x - self.x_offset, (y * -1) + self.y_offset)
        else:
            self.paint(coord=coord, co=co)

        if self.save:
            image = ImageGrab.grab()
            image.save("sketch.png")
            print("your sketch is saved as sketch.png!!")


        if retain:
            tu.done()



class ascii_art:
    def __init__(
        self,
        x_len=5,
        y_len=7,
        chars=["*", "S", "#", "&", "@", "$", "%", "*", "!", ":", "."],
        color_set={
            "*": "white",
            "S": "green",
            "#": "green",
            "&": "white",
            "@": "black",
            "$": "white",
            "%": "white",
            "!": "blue",
            ":": "darkgreen",
            ".": "grey",
        },
        save=True,
    ):
        """example usage:
        from sketchpy import canvas
        obj = cavnas.ascii_art()
        res = obj.load_data(img_path="image.png")
        obj.draw()

        paramerter:
        x_len = pixel movement in x direction
        y_lenn = pixel movement in y direction
        chars = list of characters to be used from convertion of image to ASCII art
        color_set = dictionary map for specific character to a specific color
        save = takes a screen shot of the entire screen and saves it

        """
        self.x_len = x_len
        self.y_len = y_len
        self.chars = chars
        self.colo_set = color_set
        self.save = save

    def convert_to_acsii(self, img_path, file_name=None) -> str:
        """Converts the given image to ascii art and save it to output_file, returns string
        img_path = path of the image
        file_name = name of the output text file"""

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
        img = img.convert("L")

        pixels = img.getdata()

        # replace each pixel with a character from array
        chars = self.chars
        new_pixels = [chars[pixel // 25] for pixel in pixels]
        new_pixels = "".join(new_pixels)

        # split string of chars into multiple strings of length equal to the new width and create a list
        new_pixels_count = len(new_pixels)
        ascii_image = [
            new_pixels[index : index + new_width]
            for index in range(0, new_pixels_count, new_width)
        ]
        n_chars = len(ascii_image[0])

        self.half_width = n_chars * self.x_len * -1

        ascii_image = "\n".join(ascii_image)

        # write to a text file.
        if file_name != None:
            with open(f"{file_name}.txt", "w") as f:
                f.write(ascii_image)
        print(ascii_image)
        return ascii_image

    def load_data(self, file_path=None, img_path=None, raw_data=None):
        """used to load a previously processed image,
        file_path = path of the ascii art txt file
        img_path = path of the image
        raw_data = sting containing the ascii art"""

        if img_path != None:
            self.data = self.convert_to_acsii(img_path)
        elif file_path != None:
            re = open(file_path, "r")
            self.data = re.readlines()
        elif raw_data != None:
            self.data = raw_data
            print("sepcify the correct data")
            return
        return self.data

    def draw(self, data=None):
        # setting the x and y coordinates
        s_x = self.half_width
        s_y = 250

        if data != None:
            self.data = data

        p = tu.Pen()
        p.speed(0)
        tu.bgcolor("black")
        p.up()
        p.width(2)
        p.goto(s_x, s_y)
        p.down()

        # function to select the color
        def set_col(c):
            chars = self.colo_set
            col = chars[c]
            p.pencolor(col)
            return col

        for i in self.data:

            if i == "\n":
                p.up()
                p.goto(self.half_width, s_y - self.y_len)
                s_y -= self.y_len
                s_x = self.half_width
                p.down()
                continue
            else:
                col = set_col(i)
                if col == "black":
                    s_x += 2 * self.x_len
                    p.up()
                    p.goto(s_x, s_y)
                    continue
                else:
                    p.down()
                    s_x += self.x_len
                    p.goto(s_x, s_y)

                    s_x += self.x_len
                    p.up()
                    p.goto(s_x, s_y)
                    p.down()
        if self.save:
            image = ImageGrab.grab()
            image.save("sketch.png")
            print("your sketch is saved as sketch.png!!")
        tu.done()

    def print_to_terminal(self):
        for i in self.data:
            print(i, end="")



class color_sketch_from_svg:

    def __init__(
        self,
        path=None,
        no_of_processes = 4,
        scale=500,
        x_offset=0,
        y_offset=0,
        save=False,
    ):
        """
        path -> path of the svg file\n
        no_of_processes -> on of simultanious threads to process the SVG file faster(set it to the no of cores in the system, default value: 4)\n
        scale -> zoom value\n
        x_offset -> amount of movemnt in x direction\n
        y_offset -> amount of movemnt in y direction\n
        save -> True = take a screenshot and save it\n

        used to sketch an colored image from a svg file,  reffer my youtube channel to know more about it
        """
        self.path = path
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.scale = scale
        self.save = save
        self.no_of_processes =  no_of_processes


    def hex_to_rgb(self, string):
        strlen = len(string)
        # print(string)
        if string.startswith("#"):
            if strlen == 7:
                r = string[1:3]
                g = string[3:5]
                b = string[5:7]
            elif strlen == 4:
                r = string[1:2] * 2
                g = string[2:3] * 2
                b = string[3:4] * 2
        elif strlen == 3:
            r = string[0:1] * 2
            g = string[1:2] * 2
            b = string[2:3] * 2
        else:
            r = string[0:2]
            g = string[2:4]
            b = string[4:6]

        return int(r, 16) / 255, int(g, 16) / 255, int(b, 16) / 255

    def process(self,data, id, queue):
        try:
            for i in tqdm(data):
                path = parse_path(i["d"])
                co = i["style"].replace("fill: ", "").replace(";", "")
                col = self.hex_to_rgb(co)
                transform = i["transform"].replace("translate(", "").replace(")", "")
                transform = list(map(float, transform.split(",")))
                transform = list(map(int, transform))
                n = str(path).split(" ")
                n = len(n) // 5 - 10
                if n <= 20:
                    n = 20
                pts = [
                    (
                        (int(((p.real + transform[0]) / self.width) * self.scale))
                        - self.x_offset,
                        (int(((p.imag + transform[1]) / self.height) * self.scale))
                        - self.y_offset,
                    )
                    for p in (path.point(i / n) for i in range(1, n + 1))
                ]

                queue.put((pts, col))
        except Exception as e:
            print(f"Error : {e}")  

    def load_svg(self, file_name=os.path.abspath(sys.argv[0])):
        """file_name -> name of the npy array, you can use this array data to sketch images directly"""
        if self.path != None:
            paths, attributes, svg_att = svg2paths2(self.path)
            self.attr = attributes
        print("loding svg data...")
        try:
            try:
                h = svg_att["height"]
                w = svg_att["width"]
            except:
                temp = list(map(int, svg_att["viewBox"].split()))
                h = temp[2]
                w = temp[3]

            try:
                h = h.replace("px", "")
                w = w.replace("px", "")
                self.height = int(h[: h.find(".")])
                self.width = int(w[: w.find(".")])
            except:
                self.height = int(h)
                self.width = int(w)

            if self.x_offset == 0:
                self.x_offset = (self.height) // 2

            if self.y_offset == 0:
                self.y_offset = (self.width) // 2

            self.res = []
            try:
                self.res.append([self.height, self.width, self.scale])
                def divide_list(lst, n):
                    division = len(lst) / n
                    return [lst[int(round(division * i)): int(round(division * (i + 1)))] for i in range(n)]


                div_list = divide_list(attributes, self.no_of_processes)
                processes = []
                queue = mp.Queue()
                for num, i in enumerate(div_list):
                    p = mp.Process(target= self.process, args= ( i, num, queue ))
                    p.start()

                    processes.append(p)

                while True:
                    if not any(p.is_alive() for p in processes) and queue.empty():
                        break  # If all processes finished and queue is empty, break the loop
                    while not queue.empty():
                        data_received = queue.get() 
                        self.res.append(data_received)

                    
                for p in processes:
                    p.join()

                # temp = [self.res]

                # for num in range(self.no_of_processes):
                #     temp.append(np.load(f"{num}.npy", allow_pickle=True))
                # self.res = np.concatenate(temp, axis=0)
                return self.res

            except Exception as e:
                print(e)
                print(f"Error : {e}")
                print("youtube : https://www.youtube.com/c/CODEHUB03")
                return None
        except Exception as e:
            print("error found!!!")
            print(f"ERROR: {e}")
            print(
                """you can contact me on my youtube channel: https://www.youtube.com/c/codehub03 \\n discord : https://discord.gg/r2KFa73PM2 \\n instagram : https://www.instagram.com/mr.m_y_s_t_e_r_y/"""
            )

    def move_to(self, x, y):
        self.pen.up()
        self.pen.goto(x, y)
        self.pen.down()

    def draw(
        self,
        retain=True,
        file=None,
        data=None,
        x_offset=0,
        y_offset=0,
        scale=None,
        speed=1,
    ):
        """
        retain -> retain the window after sketching\n
        file -> file path of the npy file for direct sketching\n
        data -> raw data,  should be a list in [[[x1,y1], [x2,y2], ....], [255,255,255]], first nested list is the points and the second list the color\n
        x_offset -> amount of movement in x direction while sketching\n
        y_offset -> amount of movement in y direction while sketching\n
        scale -> zoom value while sketching\n
        speed -> speed of sketching"""
        if file != None:
            coordinates = np.load(file, allow_pickle=True)
            print(f"datas are loaded from {file}")
        elif data != None:
            coordinates = data
        else:
            coordinates = self.load_svg()
            if coordinates == None:
                return 0
        wn = tu.Screen()
        wn.tracer(0)
        self.pen = tu.Turtle()
        self.pen.speed(0)
        self.screen = tu.Screen()
        dimension = coordinates[0]
        height = dimension[0]
        width = dimension[1]

        if scale == None:
            try:
                scale = dimension[2]

            except:
                scale = self.scale

        else:
            print(f"scaling the image by the factor of :{scale}")

        print("sketching...")

        for n_path, path_col in enumerate(tqdm(coordinates[1:])):
            f = 1
            self.pen.color("black")
            path = path_col[0]
            col = path_col[1]
            self.pen.color(col)
            self.pen.begin_fill()

            for num, coord in enumerate(path):
                x, y = coord
                x, y = (int((x * scale) / height)) - x_offset, (
                    int((y * scale) / width)
                ) - y_offset
                y *= -1
                if f:
                    self.pen.end_fill()
                    self.move_to(x, y)
                    self.pen.begin_fill()

                    f = 0

                elif coord in path[num + 1 :]:
                    self.pen.end_fill()
                    self.move_to(x, y)
                    self.pen.begin_fill()

                else:
                    self.pen.goto(x, y)
            self.pen.end_fill()
            if n_path % speed == 0:
                wn.update()

        if self.save:
            image = ImageGrab.grab()
            image.save("sketch.png")
            print("your sketch is saved as sketch.png!!")

        if retain == True:
            print("done sketching")
            tu.done()



class trace_from_image:
    def __init__(self, path, scale=0.75, intensity=170, save=False, details=5, blur=51):
        """path -> path of the image to be sketched

        scale - > scaling factor for the sketched image,

            less than 1 => smaller than original image,
            equal to 1 => original size

            greater than 1 => greater than original image,

        intensity -> intensity of details, keep the value between 0 and 255, optimal value lies between(200 - 255)

        save -> take a screenshot when the program stops sketching, false by default
        """
        self.path = path
        self.scale = scale
        self.pen = tu.Turtle()
        self.img = cv2.imread(path, 0)
        self.x_off = int(-1 * (self.img.shape[1] // 2) * self.scale)
        self.y_off = int((self.img.shape[0] // 2) * self.scale)
        self.intensity = intensity
        self.save = save
        self.window = tu.Screen()
        self.details = details
        self.blur = blur

    def move_to(self, x, y):
        self.pen.up()
        self.pen.goto(x, y)
        self.pen.down()

    def processimage(self):
        try:
            _, binary_image = cv2.threshold(
                self.img, self.intensity, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
            )
            kernel = np.ones((1, 1), np.uint8)
            binary_image = cv2.morphologyEx(
                binary_image, cv2.MORPH_OPEN, kernel, iterations=3
            )
            binary_image = cv2.morphologyEx(
                binary_image, cv2.MORPH_CLOSE, kernel, iterations=3
            )
            num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(
                binary_image
            )
            output_image = np.zeros(
                (self.img.shape[0], self.img.shape[1], 3), dtype=np.uint8
            )
            min_region_size = self.details

            for label in range(1, num_labels):
                region_size = stats[label, cv2.CC_STAT_AREA]
                if region_size > min_region_size:
                    region = np.where(labels == label, 255, 0).astype(np.uint8)
                    output_image[np.where(labels == label)] = (255, 255, 255)

            invert = cv2.bitwise_not(output_image)
            blur = cv2.GaussianBlur(invert, (self.blur, self.blur), 0)
            invertedblur = cv2.bitwise_not(blur)
            sketch = cv2.divide(output_image, invertedblur, scale=256.0)

            cv2.imwrite("ttmp.jpg", sketch)
            self.img = cv2.imread("ttmp.jpg")

            grey_img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
            invert = cv2.bitwise_not(grey_img)
            blur = cv2.GaussianBlur(invert, (self.blur, self.blur), 0)
            invertedblur = cv2.bitwise_not(blur)
            sketch = cv2.divide(grey_img, invertedblur, scale=256.0)
            ret, thresh = cv2.threshold(sketch, self.intensity, 255, 0)
            ctu, hire = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

            return ctu
        except Exception as e:
            print("error found!!!")
            print(f"ERROR: {e}")
            print(
                """you can contact me on my youtube channel: https://www.youtube.com/c/codehub03 \\n discord : https://discord.gg/r2KFa73PM2 \\n instagram : https://www.instagram.com/mr.m_y_s_t_e_r_y/"""
            )

    def draw(self):
        ctu = self.processimage()
        for n, pos in enumerate(ctu):
            if len(pos) <= self.details:
                continue
            mask = np.zeros(self.img.shape[:2], dtype=np.uint8)
            cv2.drawContours(mask, ctu, n, (255), thickness=cv2.FILLED)
            average_color = cv2.mean(self.img, mask=mask)
            rgb = (
                1 - average_color[0] / 255,
                1 - average_color[1] / 255,
                1 - average_color[2] / 255,
            )
            te = pos.flatten()
            print(len(te))
            x, y = (
                int((te[0] * self.scale)) + self.x_off,
                int(((te[1] * -1) * self.scale)) + self.y_off,
            )
            self.move_to(x, y)
            self.pen.color(rgb)
            self.pen.speed(0)
            temp = (-999, -999)
            self.pen.begin_fill()
            for i in pos[1:]:
                te = i.flatten()
                x, y = (
                    int((te[0] * self.scale)) + self.x_off,
                    int(((te[1] * -1) * self.scale)) + self.y_off,
                )
                if temp != (x, y):
                    self.pen.goto(x, y)
                    temp = x, y
            self.pen.end_fill()

        print("done")
        if self.save:
            image = ImageGrab.grab()
            image.save("sketch.png")
            print("your sketch is saved as sketch.png!!")
        tu.done()




class sketch_from_image:
    def __init__(self, path, save=True) -> None:
        """used to trace the image line by line,
        path -> path of the image
        save -> used to same the results
        reffer my youtube channel to know more about it,"""
        self.path = path
        self.save = save
        self.window = tu.Screen()

    def draw(self, threshold=127):

        img = cv2.imread(self.path, 2)
        ret, bw_img = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
        width = int(img.shape[1])
        height = int(img.shape[0])
        print(f"image loaded from {self.path}")
        my_screen = tu.Screen()
        my_screen.screensize(width, height)
        my_pen = tu.Turtle()
        my_screen.tracer(0)

        for i in tqdm(range(int(height / 2), int(height / -2), -1)):
            my_pen.penup()
            my_pen.goto(-(width / 2), i)

            for l in range(-int(width / 2), int(width / 2), 1):
                pix_width = int(l + (width / 2))
                pix_height = int(height / 2 - i)
                # print(f'height = {pix_height} ,width = {pix_width}, val = {bw_img[pix_height,pix_height]}')
                if bw_img[pix_height, pix_width] == 0:
                    my_pen.pendown()
                    my_pen.forward(1)
                else:
                    my_pen.penup()
                    my_pen.forward(1)
            my_screen.update()
        if self.save:
            image = ImageGrab.grab()
            image.save("sketch.png")
            print("your sketch is saved as sketch.png!!")

        my_pen.hideturtle()
        print("done!")
        tu.done()




