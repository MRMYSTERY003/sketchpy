# Welcome to sketchpy

<h2>Intro to the project and some quick information,followed by an image of the project.<h2>

<div align="center">
    <img src = 'https://user-images.githubusercontent.com/80098044/163577650-cd52c226-5cc2-464f-a5b2-a647a4924cc6.jpg'>
</div>

## Description

This is the beginning level python project to do some awesome drawing animation using the `turtle` module, hope it grows in the future
It is a Python module for animating drawings of images. The sketchpy module is created on top of the turtle module in Python.
To install sketchpy on your computer, you can go to your command prompt (command line) and run the following command.

### Usage

- Just install the package `pip install sketchpy`
- Import it to you project `import sketchpy` and use as you want😊

### Built with

- Turtle 
- Open-cv
- Pillow
- numpy
- Svgpathtools

## Getting started

### Lastes version of sketchpy: 0.1.7

- you can install the latest version with either
```
    pip install sketchpy==0.1.7
```
or
```
    pip install sketchpy --U
```

- the lates version of the package includes a class named `trace_from_image()`, which allowes you to get the same output as using a svg file without the need to convert it to a svg file. hecnce it reduces the run time and it is much effecient.
- To know more about this new class visit the blog post [here](https://codehub03.blogspot.com/2023/07/how-to-draw-ai-hoshino-with-just-3.html). 
- A sample output of the class

![sketch](https://github.com/MRMYSTERY003/sketchpy/assets/80098044/2c85a64f-be2e-49d6-bfbb-ca8e3a0857be)

- you can take a view about how the class working in [here](https://youtube.com/shorts/_F23GwUJcIU?feature=share)

- The new version also includes parameter `save`, which can be set to true to save the output as screenshot.png file once the sketching is done.



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


### Example

Open your code editor and write the example Python code snippets given below. Run your code and see the magic by yourself.


## Drawing Robert Downey Jr. Using Python

```
    from sketchpy import library as lib
    obj = lib.rdj()
    obj.draw()
```

### OUTPUT
<div align = "center">
   <img src = "https://user-images.githubusercontent.com/80098044/154792552-59c53805-35b9-46e0-be37-2c5dae0a87d1.gif">
</div>



## Drawing Tom Holland Using Python

```
    from sketchpy import library
    myObject = library.tom_holland()
    myObject.draw()
```


## OUTPUT
<div align = "center">
   <img src = "https://cdn-0.pythonistaplanet.com/wp-content/uploads/2022/05/image-5.png?ezimgfmt=ng:webp/ngcb19">
</div>
    
## More examples

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

## Drawing Iron Man ASCII Animation Using Python

```
    from sketchpy import library
    myObject = library.ironman_ascii()
    myObject.draw()
```

## OUTPUT

<div align = "center">
   <img src = "https://cdn-0.pythonistaplanet.com/wp-content/uploads/2022/05/image-8.png?ezimgfmt=ng:webp/ngcb19">
</div>



# Drawing from `SVG` file
    
Use the following code to draw a file from svg file, insted of tracing full image
    
#### NOTE: use this specific website to convert image to svg, sketchpy is specifically made to work with this [website](https://svgconvert.com/#/) only
    
```
    from sketchpy import canvas
    obj = canvas.sketch_from_svg('FILE PATH')
    obj.draw()
```
    
# `Saving` a loaded svg file

Insted of waiting for the svg file to load, you can save as .npy file and use that for future use
    
```
    from sketchpy import canvas
    obj = canvas.sketch_from_svg('FILE PATH')
    obj.load_svg(filename = 'data.npy')
```

## Drawing form `.npy` file

use the following code to draw your image from saved data file
    
```
    from sketchpy import canvas
    obj = canvas.sketch_from_svg('FILE PATH')
    obj.draw(filename = 'data.npy')
``` 
    
## Drawing from `raw image`
    
use the following code to draw any image, it need not to be an svg file
```
    from sketchpy import canvas
    obj = canvas.sketch_from_image('IMAGE PATH')
    obj.draw(threshold = 127)
```
#### NOTE: you can change the value of threshold to draw more detailed image, it's range is 0 - 255,use values between 90-190
to know more about it visit [here](https://codehub03.blogspot.com/2022/04/how-to-draw-image-with-python-using.html)

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
- upi id s`riramanand23@okicici`
- scan and encourage us to develop more features


![gpay qr code](https://user-images.githubusercontent.com/80098044/177810955-d9e1dae5-e84e-4839-a806-da76f93cb27e.jpg)


### License

This project is licensed under the [MIT License](https://github.com/MRMYSTERY003/sketchpy/blob/main/LICENSE).
