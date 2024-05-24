from setuptools import setup, find_packages,  Extension
import codecs
import os




VERSION = '0.3.2'
DESCRIPTION = 'sketchpy3'
LONG_DESCRIPTION = """
# Welcome to sketchpy


<div align="center">
    <img src = 'https://user-images.githubusercontent.com/80098044/163577650-cd52c226-5cc2-464f-a5b2-a647a4924cc6.jpg'>
</div>

## Description

This is the Intermediate level python project to do some awesome drawing animation using the `turtle` module, hope it grows in the future.
It is a Python module for animating drawings of images. The sketchpy module is created on top of the turtle module in Python.
To install sketchpy on your computer, you can go to your command prompt (command line) and run the following command.

### Usage

- Just install the package `pip install sketchpy3`
- Followed by `pip install --upgrade sketchpy3` to update the package to the latest version.
- Import it to you project `import sketchpy3` and use as you want😊

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
    pip install sketchpy3==0.3.1
```
or
```
    pip install sketchpy3 --U
```

## Updates!!

- Now uses `AI` to generate different styles of images for sketching using the class `canvas.ai_sketch_from_image`
- You can use the function as followes
  ```
      from sketchpy3 import canvas
      if __name__ == "__main__":
          obj = canvas.ai_sketch_from_image(IMG_PATH,3)
          obj.draw()
  ```

- Sample
 <div align = 'center' style = "display: flex; justify-content: space-between; flex-direction: column;"> 
        <img src = "https://github.com/MRMYSTERY003/sketchpy/assets/80098044/d7bfc559-267a-464c-861e-0f2f6714490a">
        <img src = "https://github.com/MRMYSTERY003/sketchpy/assets/80098044/ee981888-4fec-4e25-b76c-174f33a05e34">
        <img src = "https://github.com/MRMYSTERY003/sketchpy/assets/80098044/b79df331-69c7-4547-b5c9-e8936a1d3a9c">
        <img src = "https://github.com/MRMYSTERY003/sketchpy/assets/80098044/65a2578f-1293-4ba8-823f-66c7663a75ee">
        <img src = "https://github.com/MRMYSTERY003/sketchpy/assets/80098044/61b1d15f-e43f-41bd-867c-16d3ce45174b" height=400px width=auto>
        <img src = "https://github.com/MRMYSTERY003/sketchpy/assets/80098044/98bb8e9a-18a2-4044-bac1-f7890a1c6c75" height=400px width=auto>

</div>

- The first image is the `source image`, and the following corresponds to different styles from `[0-3]`
- This version `0.3.1` uses multiprocessing for processing the single svg file in 4 different threads to reduce the time for loading the svg file
- Sample
    <div align = "center">
       <img src = "https://github.com/MRMYSTERY003/sketchpy/assets/80098044/5b09576e-3759-4501-bcf4-5134a9c1a133">
    </div>
- And I have included a new function named `get_svg()` from `canvas` to convert your Image to svg,
- You can use the function as followes
  ```
      from sketchpy import canvas
      canvas.get_svg(img_path)
  ```
- The `get_svg()` function opens a short url only `once` a day. Just enter the 4 digit number from the landing page from the short url in the cmd to access the svg converter. And you need to complete the short url only once a day, So it's no big deal.      



### Prerequisites

- Python
- Basic text editor
- creativity😂

### Install

```
    pip install sketchpy3
```
it should probably work, If not then try the following code
    
```
    pip install turtle open-cv wheel sketchpy3
```


# Trace from Image

The recent version of the package includes a class named `trace_from_image()`, which allowes you to get the same output as using a svg file without the need to convert it to a svg file. hecnce it reduces the run time and it is much effecient.

- To know more about this new class visit the blog post [here](https://codehub03.blogspot.com/2023/07/how-to-draw-ai-hoshino-with-just-3.html). 
- A sample output of the class  `trace_from_image()`.
- you can take a view about how the class working in [here](https://youtube.com/shorts/_F23GwUJcIU?feature=share)



<div align = 'center' style = "display: flex; justify-content: space-between;"> 
    <img src = "https://github.com/MRMYSTERY003/sketchpy/assets/80098044/a7cb5f01-d4b3-4d45-8b62-b39cc57784c0">
    <img src = "https://github.com/MRMYSTERY003/sketchpy/assets/80098044/da374957-38b5-4228-b058-b587fab2d4b9">
</div>


Sample Code:
```
    from sketchpy3 impor canvas
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
    - details -> use to skip the small details from the image to increase the speed. details=0 -> inculde all minor details, details=50 -> include all details which are greater than 50
    - blur -> always provide a odd number, the lower the value the more distortion, higher the value the more smooth, optimal value 51
    - skip_frequency -> used to speed the sketchpy the process by skipping some values


# Sketch from Image
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


# Drawing From `SVG` file 


You can sketch image uinsg the class `color_sketch_from_svg`, which takes the inpu in svg formate and then sketches it.
Example Code:
```
    from sketchpy3 impor canvas
    if __name__ == "__main__":
        obj = canvas.color_sketch_from_svg("Image Path")
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
        - no_of_processes -> no of individual branches the process the svg file
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

<br>


# Sketching form `.npy` file

Insted of waiting for the svg file to load, you can saved `.npy` file and use that for future use,
use the following code to draw your image from saved data file
    
```
    from sketchpy3 import canvas
    obj = canvas.color_sketch_from_svg(None)
    obj.draw(file = 'data.npy')
```

<br>

# Converting `Image` to `SVG` formate

Sketchpy3 requires specific type of `SVG` file formate to work properly, hence this version includes a standalone svg converter function with it
use the follow code to convert you images to svg files

```
    from sketchpy3 import canvas
    canvas.get_svg(IMG_PATH)
```

 - It takes the image from the `IMG_PATH` and converts it into an svg file
 - But to access this SVG converter you have to complete a shorturl, don't worry you need to do this only once a day
 - Use brave browser to complete it with ih 20 sec.
   
<br>

# Converting `Image` to `AI ART`

 - This new version sketchpy3 includes a class named `ai_sketch_from_image`
 - This class converts the given imag to different styles of image using `generative art` from bryandlee/animegan2
 - You can use it as follows

   ```
   from sketchpy3 import canvas

    if __name__ == "__main__":
        obj = canvas.ai_sketch_from_image(IMG_PATH, STYLE_INDEX)
        obj.draw()
   ```
### Use the following code to get the AI ART as image

    ```
    from sketchpy3 import canvas
    obj = canvas.ai_sketch_from_image(IMG_PATH, STYLE_INDEX)
    obj.convert_image()
    ```
- You can find your output image as `source.jpg` file

### Example

<div align = 'center' style = "display: flex; justify-content: space-between;"> 
     <img src = "https://github.com/MRMYSTERY003/sketchpy/assets/80098044/615e59db-2701-4cda-989e-7f98ecb506f9">
     <img src = "https://github.com/MRMYSTERY003/sketchpy/assets/80098044/86b89fec-8055-48ea-ac8a-7944c04f2eb9">
     <img src = "https://github.com/MRMYSTERY003/sketchpy/assets/80098044/d8440209-cf9d-4e60-98f3-deb54e24ad34">
     <img src = "https://github.com/MRMYSTERY003/sketchpy/assets/80098044/a52ae3c3-3d9c-4a94-9ad8-a3ee9a8cf5c6">
     <img src = "https://github.com/MRMYSTERY003/sketchpy/assets/80098044/d194573a-59d8-4461-8703-caa5366566c4">



</div>


### Parameters 
    - ai_sketch_from_image
        - path -> path of the svg file
        - style_index -> [0-3] each number produces different styles of image
        - no_of_processes -> no of individual branches the process the svg file
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

# Library Example

Open your code editor and write the example Python code snippets given below. Run your code and see the magic by yourself.


### Drawing Robert Downey Jr. Using Python

```
    from sketchpy3 import library as lib
    obj = lib.rdj()
    obj.draw()
```

### OUTPUT
<div align = "center">
   <img src = "https://user-images.githubusercontent.com/80098044/154792552-59c53805-35b9-46e0-be37-2c5dae0a87d1.gif">
</div>



### Drawing Tom Holland Using Python

```
    from sketchpy3 import library
    myObject = library.tom_holland()
    myObject.draw()
```


### OUTPUT
<div align = "center">
   <img src = "https://cdn-0.pythonistaplanet.com/wp-content/uploads/2022/05/image-5.png?ezimgfmt=ng:webp/ngcb19">
</div>
    
### More examples

```
    from sketchpy3 import library as lib
    
    obj = lib.bts()
    obj.draw()
```

```
    from sketchpy3 import library as lib

    obj = lib.vijay()
    obj.draw()
```
<div align = 'center' style = "display: flex; justify-content: space-between;"> 
<img src = "https://user-images.githubusercontent.com/80098044/154793329-e8ec9635-b49e-4898-8a3e-6462645d6c8c.gif" height = 180 width = 214>
<img src = "https://user-images.githubusercontent.com/80098044/154793382-6d012c24-adbf-4c5a-bd51-b5095a34e9fe.gif" height = 180 width = 214>
</div>

### Drawing Iron Man ASCII Animation Using Python

```
    from sketchpy3 import library
    myObject = library.ironman_ascii()
    myObject.draw()
```

### OUTPUT

<div align = "center">
   <img src = "https://cdn-0.pythonistaplanet.com/wp-content/uploads/2022/05/image-8.png?ezimgfmt=ng:webp/ngcb19">
</div>



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

"""
# Setting up
setup(
    name="sketchpy3",
    version=VERSION,
    author="Mr Mystery",
    author_email="sriramanand23@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,

    packages=find_packages(),
    package_data={'': ['files/*']},
    include_package_data=True,
    install_requires=['opencv-python', 'turtle==0.0.1',
                      'wheel', 'Pillow', 'svg.path', 'svgpathtools', 'tqdm', 'requests', 'geocoder', 'geopy','torch'],
    keywords=['python', 'sketch', 'drawing', 'animation',
              'code hub', 'pencil sketch', 'painting', 'sketchpy', 'draw', 'sketching'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)