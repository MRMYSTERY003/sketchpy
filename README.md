# Welcome to sketchpy

<h2>Intro to the project and some quick information,followed by an image of the project.<h2>

<div align="center">
    <img src = 'https://user-images.githubusercontent.com/80098044/163577650-cd52c226-5cc2-464f-a5b2-a647a4924cc6.jpg'>
</div>

## Description

This is the beginning level python project to do some awesome drawing animation using the `turtle` module, hope it grows in the future

### Usage

- Just install the package `pip install sketchpy`
- Import it to you project `import sketchpy` and use as you want😊

### Built with

- Turtle 
- Open-cv
- Pillow
- Svgpathtools

## Getting started

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

```
    from sketchpy import library as lib
    

    obj = lib.rdj()
    obj.draw()
```

### OUTPUT
<div align = "center">
   <img src = "https://user-images.githubusercontent.com/80098044/154792552-59c53805-35b9-46e0-be37-2c5dae0a87d1.gif">
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
    
# Drawing from `SVG` file
    
Use the following code to draw a file from svg file, insted of tracing full image
    
#### NOTE: use this specific website to convert image to svg, sketchpy is specifically made to work with this [website](https://svgconvert.com/#/) only
    
```
    from sketchpy import canvas
    obj = canvas.draw_from_svg('FILE PATH')
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
    obj = draw(threshold = 127)
```
#### NOTE: you can change the value of threshold to draw more detailed image, it's range is 0 - 255,use values between 90-190

### Troubleshooting

- If you find any problem, you can pull request, or contact me on either [insta](https://www.instagram.com/mr.m_y_s_t_e_r_y/) or [discord](https://discord.gg/r2KFa73PM2)
- You can also find video on my [youtube channel](https://www.youtube.com/playlist?list=PLb1Kbw_2jl_mr3A_cl6pXA1N5lwtHCx_7)




### Acknowledgements

Thanks to all who helped inspire this project.❤

### See also

- [Youtube Videos](https://www.youtube.com/playlist?list=PLb1Kbw_2jl_mr3A_cl6pXA1N5lwtHCx_7)
- [Related Blogs](https://codehub0.blogspot.com/)
- [Contact me on Discord](https://discord.gg/r2KFa73PM2)
- [My insta ID](https://www.instagram.com/mr.m_y_s_t_e_r_y/)

### Consider supporting me

- upi id sriramanand23@okicici
- scan and encourage us to develop more features
- even one rupee make a huge difference

![gpay qr code](https://user-images.githubusercontent.com/80098044/177810955-d9e1dae5-e84e-4839-a806-da76f93cb27e.jpg)


### License

This project is licensed under the [MIT License](https://github.com/MRMYSTERY003/sketchpy/blob/main/LICENSE).
