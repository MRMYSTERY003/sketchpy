# Welcome to sketchpy


<div align="center">
    <img src = 'https://user-images.githubusercontent.com/80098044/163577650-cd52c226-5cc2-464f-a5b2-a647a4924cc6.jpg'>
</div>

## Description

This is the Intermediate level python project to do some awesome drawing animation using the `turtle` module, hope it grows in the future.
It is a Python module for animating drawings of images. The sketchpy module is created on top of the turtle module in Python.
To install sketchpy on your computer, you can go to your command prompt (command line) and run the following command.

### Usage

- Just install the package `pip install sketchpy`
- Followed by `pip install --upgrade sketchpy` to update the package to the latest version.
- Import it to you project `import sketchpy` and use as you want😊

### Built with

- Turtle 
- Open-cv
- Pillow
- numpy
- Svgpathtools

## Getting started

### Lastes version of sketchpy: 0.1.8

- you can install the latest version with either
```
    pip install sketchpy==0.1.8
```
or
```
    pip install sketchpy --U
```

## Updates!!

- This version `0.1.8` uses multiprocessing for processing the single svg file in 4 different threads to reduce the time for loading the svg file
- Sample
    <div align = "center">
       <img src = "https://github.com/MRMYSTERY003/sketchpy/assets/80098044/5b09576e-3759-4501-bcf4-5134a9c1a133">
    </div>
- And I have included a new function named `get_svg()` from `utils` to convert your Image to svg, this function opens your default web browser to get you to the `best svg converting website`
- You can use the function as followes
  ```
      from sketchpy import utils
      uitls.get_svg()
  ```
- I have include a short url, to monitize this sketchpy package, Just 5 little steps then you can use your svg converter
     - `Step 1` Just click the `I am not robot` button on the top of the website
     - `Step 2` You will be redirected to the second site, where you need to scroll to tbe bottom and wait for about 10 seconds until you see `open-continue` button, click it.
     - `Step 3` A pop up with the same `open-continue` button will be visible, clicl it. Now you will be redirected to another wibsite scroll down and click `I am not a Robot` button.
     - `Step 4` Now you can see a loading circle, wait 100%, and click `Dual tap fast to get Link`, now click `go to link click open`
     - `Step 5` Now scroll down and wait for 5 seconds and click `Get link`, That's it you have reached the destinatied website.
-I know, It is kind of annyoing to use short url, But this is the only way that dosent require any skill from the uses. so both of us can get benifited!
 
      



### Prerequisites

- Python
- Basic text editor
- creativity😂

### Install

```
    pip install sketchpy
```
it should probably work, If not then try the following code
    
```
    pip install turtle open-cv wheel sketchpy
```


## Library Example

Open your code editor and write the example Python code snippets given below. Run your code and see the magic by yourself.


### Drawing Robert Downey Jr. Using Python

```
    from sketchpy import library as lib
    obj = lib.rdj()
    obj.draw()
```

### OUTPUT
<div align = "center">
   <img src = "https://user-images.githubusercontent.com/80098044/154792552-59c53805-35b9-46e0-be37-2c5dae0a87d1.gif">
</div>



### Drawing Tom Holland Using Python

```
    from sketchpy import library
    myObject = library.tom_holland()
    myObject.draw()
```


### OUTPUT
<div align = "center">
   <img src = "https://cdn-0.pythonistaplanet.com/wp-content/uploads/2022/05/image-5.png?ezimgfmt=ng:webp/ngcb19">
</div>
    
### More examples

```
    from sketchpy import library as lib
    
    obj = lib.bts()
    obj.draw()
```

```
    from sketchpy import library as lib

    obj = lib.vijay()
    obj.draw()
```
<div align = 'center' style = "display: flex; justify-content: space-between;"> 
<img src = "https://user-images.githubusercontent.com/80098044/154793329-e8ec9635-b49e-4898-8a3e-6462645d6c8c.gif" height = 180 width = 214>
<img src = "https://user-images.githubusercontent.com/80098044/154793382-6d012c24-adbf-4c5a-bd51-b5095a34e9fe.gif" height = 180 width = 214>
</div>

### Drawing Iron Man ASCII Animation Using Python

```
    from sketchpy import library
    myObject = library.ironman_ascii()
    myObject.draw()
```

### OUTPUT

<div align = "center">
   <img src = "https://cdn-0.pythonistaplanet.com/wp-content/uploads/2022/05/image-8.png?ezimgfmt=ng:webp/ngcb19">
</div>


## Trace from Image

The recent version of the package includes a class named `trace_from_image()`, which allowes you to get the same output as using a svg file without the need to convert it to a svg file. hecnce it reduces the run time and it is much effecient.

- To know more about this new class visit the blog post [here](https://codehub03.blogspot.com/2023/07/how-to-draw-ai-hoshino-with-just-3.html). 
- A sample output of the class  `trace_from_image()`.
- you can take a view about how the class working in [here](https://youtube.com/shorts/_F23GwUJcIU?feature=share)



<div align = 'center' style = "display: flex; justify-content: space-between;"> 
    <img src = "https://github.com/MRMYSTERY003/sketchpy/assets/80098044/2c85a64f-be2e-49d6-bfbb-ca8e3a0857be">
</div>


Sample Code:
```
    from sketchpy impor canvas
    obj = canvas.trace_from_image("Image Path")
    obj.draw()
```
### Parameters : 

    - Path: Path of the image
    - Scale:
          -scaling factor for the sketched image,
          - less than 1 => smaller than original image
          - equal to 1 => original size
          - greater than 1 => greater than original image
    
    - intensity -> intensity of details, keep the value between 0 and 255, optimal value lies between(200 - 255)
    - save -> take a screenshot when the program stops sketching, false by default


## Sketch from Image
used to trace the image line by line.

Example Code :

```
    from sketchpy impor canvas
    obj = canvas.sketch_from_image("Image Path")
    obj.draw(threshold = 127)
```

### Parameters 
    - path -> path of the image
    - save -> used to same the results

you can watch the example video from [here](https://www.youtube.com/watch?v=hCRppNooLYE) 
#### NOTE: you can change the value of threshold to draw more detailed image, it's range is 0 - 255,use values between 90-190
to know more about it visit [here](https://codehub03.blogspot.com/2022/04/how-to-draw-image-with-python-using.html)


## Drawing From `SVG` file 


You can sketch image uinsg the class `color_sketch_from_svg`, which takes the inpu in svg formate and then sketches it.
Example Code:
```
    from sketchpy impor canvas
    obj = canvas.sketch_from_image("Image Path")
    obj.draw()
```

Example output

<div align = 'center' style = "display: flex; justify-content: space-between;"> 
    <img src = "https://github.com/MRMYSTERY003/sketchpy/assets/80098044/b2d311a2-a981-4503-9955-58d3f13dc66b">
</div>

#### NOTE: `sketch_from_svg` class is remove from the package, since it can only draw with single color, `color_sketch_from_svg` class will be available.
### Parameters 
    - color_sketch_from_svg
        - path -> path of the svg file
        - scale -> zoom value
        - x_offset -> amount of movemnt in x direction
        - y_offset -> amount of movemnt in y direction
        - save -> (True by defaule)= take a screenshot and save it
    - load_svg
        - file_name -> name of the npy array, you can use this array data to sketch images directly
    - draw
        - retain -> retain the window after sketching (true by defaule)
        - file -> file path of the npy file for direct sketching
        - data -> raw data,  should be a list in [[[x1,y1], [x2,y2], ....], [255,255,255]], first nested list is the points and the second list the color
        - x_offset -> amount of movement in x direction while sketching
        - y_offset -> amount of movement in y direction while sketching
        - scale -> zoom value while sketching
        - speed -> speed of sketching





### Sketching form `.npy` file

Insted of waiting for the svg file to load, you can saved `.npy` file and use that for future use,
use the following code to draw your image from saved data file
    
```
    from sketchpy import canvas
    obj = canvas.color_sketch_from_svg(None)
    obj.draw(file = 'data.npy')
```


    

### Troubleshooting

- If you find any problem, you can pull request, or contact me on either [insta](https://www.instagram.com/mr.m_y_s_t_e_r_y/) or [discord](https://discord.gg/r2KFa73PM2)
- You can also find video on my [youtube channel](https://www.youtube.com/playlist?list=PLb1Kbw_2jl_mr3A_cl6pXA1N5lwtHCx_7)
- You can know more about sketchpy and get tutorial in this blog [page](https://codehub03.blogspot.com/)




### Acknowledgements

Thanks to all who helped inspire this project.❤

### See also

- [Youtube Videos](https://www.youtube.com/playlist?list=PLb1Kbw_2jl_mr3A_cl6pXA1N5lwtHCx_7)
- [Related Blogs](https://codehub0.blogspot.com/)
- [Contact me on Discord](https://discord.gg/r2KFa73PM2)
- [My insta ID](https://www.instagram.com/mr.m_y_s_t_e_r_y/)

# Consider supporting me
- we spend `hours` to implement these algorithms and making you to access these with just 3 lines
- consider `supporting` our work.
- even a single `rupee` conunts.
- upi id `sriramanand23@okicici`
- scan and encourage us to develop more features or use the `short url` to get the svg file


![gpay qr code](https://user-images.githubusercontent.com/80098044/177810955-d9e1dae5-e84e-4839-a806-da76f93cb27e.jpg)


### License

This project is licensed under the [MIT License](https://github.com/MRMYSTERY003/sketchpy/blob/main/LICENSE).
