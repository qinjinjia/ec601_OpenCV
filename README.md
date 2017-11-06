# EC601_OpenCV Exercise
## Brief Introduction :sunglasses:
  Hello Everyone! :trollface::trollface::trollface::trollface:
  
  This is the page for **EC601(Fall 2017) A1 OpenCV Exercise** 
  [@github/qinjinjia/ec601_OpenCV](https://github.com/qinjinjia/ec601_OpenCV)
  

  The Author: :boy: **Qinjin Jia** qjia@bu.edu   :point_right:[@github/qinjinjia](https://github.com/qinjinjia)

## Exercise 1
**Q1. How does a program read the cvMat object, in particular, what is the
order of the pixel structure?**

```
[[[125 137 226]
  [125 137 226]
  [133 137 223]
  ..., 
  [122 148 230]
  [110 130 221]
  [ 90  99 200]]

  ......,
  
 [[ 57  22  82]
  [ 57  22  82]
  [ 62  32  96]
  ..., 
  [ 79  70 179]
  [ 81  71 181]
  [ 81  74 185]]]
```

</br>

## Exercise 2
**Q1. ColorImage.cpp is a program that takes a look at colorspace conversions in OpenCV. Run the code in ColorImage.cpp and comment on the outputs. Implement the same thing in Python and save each image.**

#### Comment on the output of ColorImage:


#### Implement ColorImage.cpp in Python:  

:sun_with_face: Please check the **ColorImage.py code** here :link: **[ColorImage.py](https://github.com/qinjinjia/ec601_OpenCV/blob/master/ColorImage.py)**

:full_moon_with_face: Please check the **Saved Images** from ColorImage.py here :link: **[exercise2_py_results](https://github.com/qinjinjia/ec601_OpenCV/tree/master/exercise2_py_results)**

:new_moon_with_face: The **Saved Images** can also be found below, :point_down:     

:bangbang: N.B. The images are shown in **1-channel greyscale** format

|Row\Col |Colorspace |Left |Mid |Right |     
|---|---|---|---|---    
|1 |RBG |Blue |Green |Red |
|2 |YCbCr |Y |Cb |Cr |
|3 |HSV |Hue |Saturation |Value | 

    
<img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise2_py_results/Blue.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise2_py_results/Green.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise2_py_results/Red.png" width="200" height="200">

<img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise2_py_results/Y.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise2_py_results/Cb.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise2_py_results/Cr.png" width="200" height="200">

<img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise2_py_results/Hue.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise2_py_results/Saturation.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise2_py_results/Value.png" width="200" height="200">

</br>

**Q2. Print out the values of the pixel at (20,25) in the RGB, YCbCr and HSV versions of the image. What are the ranges of pixel values in each channel of each of the above mentioned colorspaces?**

|Colorspace |Pixel |Value |Range|
|---|---|---|---
|RGB |R(20,25) |225 | 0~255|
||G(20,25) |122 | 0~255|
||B(20,25) |106 | 0~255|
|YCbCr|Y(20,25) |151 | 0~255|
||Cb(20,25) |181 | 0~255|
||Cr(20,25) |103 | 0~255|
|HSV |Hue(20,25) |4 | 0~179|
||Saturation(20,25) |135 | 0~255|
||Value(20,25) |225 | 0~255|

</br>

:heavy_exclamation_mark: The range of each channel of each colorspace is based on **CV_8U image in OpenCV**.


|Colorspace |Channel |Range |
|---|---|---
|LAB |Lightness |0~100 |
||A |-127~127 |
||B |-127~127 |
|RGB |R |0~255 |
||G |0~255 |
||B |0~255 |
|YCbCr|Y |0~255 | 
||Cb |0~255 |
||Cr |0~255 |
|HSV |Hue |0~179 |
||Saturation |0~255 |
||Value |0~255 |
|CMYK |Cyan |0~100 |
||Magenta |0~100 |
||Yellow |0~100 |
||Key |0~100 |

**Ref:** [OpenCV Documentation - Miscellaneous Image Transformations](https://docs.opencv.org/2.4/modules/imgproc/doc/miscellaneous_transformations.html#cvtcolor) (accessed on Nov. 5, 2017)

</br>

## Exercise 3
**Q1. Look at the code in Noise.cpp and implement the code in Python. Also, print the results for different noise values in the Gaussian case, mean = 0, 5, 10, 20 and sigma = 0, 20, 50, 100 and for the salt-and-pepper case, pa = 0.01, 0.03, 0.05, 0.4 and pb = 0.01, 0.03, 0.05, 0.4.**

#### Implement Noise.cpp in Python:
:waxing_crescent_moon: Please check the **Noise.py code** here :link: **[Noise.py](https://github.com/qinjinjia/ec601_OpenCV/blob/master/Noise.py)**

</br>

#### Print the results for different noise values in the Gaussian Noise case:

|Row\Col |Gaussian Noise |Box Filter |Gaussian Filter |Median |     
|---|---|---|---|---    
|1 |mean=0, sigma=0 | |Best | |
|2 |mean=5, sigma=20 | | | |
|3 |mean=10, sigma=50 | | | |
|4 |mean=20, sigma=100 | | | |

:new_moon_with_face: **Gaussian Noise (mean=0, sigma=0):**

<img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_mean%3D0_sigma%3D0/Gaussian%20Noise.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_mean%3D0_sigma%3D0/Gaussian%20Noise%20-%20Box%20filter.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_mean%3D0_sigma%3D0/Gaussian%20Noise%20-%20Gaussian%20filter.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_mean%3D0_sigma%3D0/Gaussian%20Noise%20-%20Median%20filter.png" width="200" height="200">

:first_quarter_moon: **Gaussian Noise (mean=5, sigma=20):**

<img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_mean%3D5_sigma%3D20/Gaussian%20Noise.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_mean%3D5_sigma%3D20/Gaussian%20Noise%20-%20Box%20filter.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_mean%3D5_sigma%3D20/Gaussian%20Noise%20-%20Gaussian%20filter.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_mean%3D5_sigma%3D20/Gaussian%20Noise%20-%20Median%20filter.png" width="200" height="200">


:waxing_gibbous_moon: **Gaussian Noise (mean=10, sigma=50):**

<img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_mean%3D10_sigma%3D50/Gaussian%20Noise.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_mean%3D10_sigma%3D50/Gaussian%20Noise%20-%20Box%20filter.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_mean%3D10_sigma%3D50/Gaussian%20Noise%20-%20Gaussian%20filter.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_mean%3D10_sigma%3D50/Gaussian%20Noise%20-%20Median%20filter.png" width="200" height="200">


:full_moon: **Gaussian Noise (mean=20, sigma=100):**

<img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_mean%3D20_sigma%3D100/Gaussian%20Noise.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_mean%3D20_sigma%3D100/Gaussian%20Noise%20-%20Box%20filter.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_mean%3D20_sigma%3D100/Gaussian%20Noise%20-%20Gaussian%20filter.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_mean%3D20_sigma%3D100/Gaussian%20Noise%20-%20Median%20filter.png" width="200" height="200">


</br>

#### Print the results for different noise values in the Salt-and-Pepper Noise case:

|Row\Col |Salt-and-Pepper Noise |Box Filter |Gaussian Filter |Median |     
|---|---|---|---|---    
|1 |pa=0.01, pb=0.01 | | |Best |
|2 |pa=0.03, pb=0.03 | | | |
|3 |pa=0.05, pb=0.05 | | | |
|4 |pa=0.4, pb=0.4 | | | |

:new_moon_with_face: **Salt-and-Pepper Noise Noise (pa=0.01, pb=0.01):**

<img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_pa%3D0.01_pb%3D0.01/Salt%20and%20Pepper%20Noise.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_pa%3D0.01_pb%3D0.01/Salt%20and%20Pepper%20Noise%20-%20Box%20filter.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_pa%3D0.01_pb%3D0.01/Salt%20and%20Pepper%20Noise%20-%20Gaussian%20filter.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_pa%3D0.01_pb%3D0.01/Salt%20and%20Pepper%20Noise%20-%20Median%20filter.png" width="200" height="200">

:first_quarter_moon: **Salt-and-Pepper Noise Noise (pa=0.03, pb=0.03):**

<img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_pa%3D0.03_pb%3D0.03/Salt%20and%20Pepper%20Noise.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_pa%3D0.03_pb%3D0.03/Salt%20and%20Pepper%20Noise%20-%20Box%20filter.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_pa%3D0.03_pb%3D0.03/Salt%20and%20Pepper%20Noise%20-%20Gaussian%20filter.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_pa%3D0.03_pb%3D0.03/Salt%20and%20Pepper%20Noise%20-%20Median%20filter.png" width="200" height="200">

:waxing_gibbous_moon: **Salt-and-Pepper Noise Noise (pa=0.05, pb=0.05):**

<img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_pa%3D0.05_pb%3D0.05/Salt%20and%20Pepper%20Noise.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_pa%3D0.05_pb%3D0.05/Salt%20and%20Pepper%20Noise%20-%20Box%20filter.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_pa%3D0.05_pb%3D0.05/Salt%20and%20Pepper%20Noise%20-%20Gaussian%20filter.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_pa%3D0.05_pb%3D0.05/Salt%20and%20Pepper%20Noise%20-%20Median%20filter.png" width="200" height="200">

:full_moon: **Salt-and-Pepper Noise Noise (pa=0.4, pb=0.4):**

<img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_pa%3D0.4_pb%3D0.4/Salt%20and%20Pepper%20Noise.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_pa%3D0.4_pb%3D0.4/Salt%20and%20Pepper%20Noise%20-%20Box%20filter.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_pa%3D0.4_pb%3D0.4/Salt%20and%20Pepper%20Noise%20-%20Gaussian%20filter.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_pa%3D0.4_pb%3D0.4/Salt%20and%20Pepper%20Noise%20-%20Median%20filter.png" width="200" height="200">

</br>

**Q2. Change the kernel sizes for all the filters with all different values for noises and print the results for 3x3, 5x5 and 7x7 kernels. Comment on the results. Which filter seems to work ”better” for images with salt-and-pepper noise and gaussian noise?**


#### Gaussian Noise (mean=10, sigma=50):

:sun_with_face: The images for **differnt Kernel Size** and **different Filter** can be found below, :point_down:    

|Row\Col |Gaussian Noise |Box Filter |Gaussian Filter |Median |     
|---|---|---|---|---    
|Kernel 3*3 | | |**Best** | |
|Kernel 5*5 | | |Well | |
|Kernel 7*7 | | |Good | |

<img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_kernel%3D3*3_mean%3D10_sigma%3D50/Gaussian%20Noise.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_kernel%3D3*3_mean%3D10_sigma%3D50/Gaussian%20Noise%20-%20Box%20filter.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_kernel%3D3*3_mean%3D10_sigma%3D50/Gaussian%20Noise%20-%20Gaussian%20filter.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_kernel%3D3*3_mean%3D10_sigma%3D50/Gaussian%20Noise%20-%20Median%20filter.png" width="200" height="200">

<img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_kernel%3D5*5_mean%3D10_sigma%3D50/Gaussian%20Noise.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_kernel%3D5*5_mean%3D10_sigma%3D50/Gaussian%20Noise%20-%20Box%20filter.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_kernel%3D5*5_mean%3D10_sigma%3D50/Gaussian%20Noise%20-%20Gaussian%20filter.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_kernel%3D5*5_mean%3D10_sigma%3D50/Gaussian%20Noise%20-%20Median%20filter.png" width="200" height="200">

<img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_kernel%3D7*7_mean%3D10_sigma%3D50/Gaussian%20Noise.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_kernel%3D7*7_mean%3D10_sigma%3D50/Gaussian%20Noise%20-%20Box%20filter.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_kernel%3D7*7_mean%3D10_sigma%3D50/Gaussian%20Noise%20-%20Gaussian%20filter.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_kernel%3D7*7_mean%3D10_sigma%3D50/Gaussian%20Noise%20-%20Median%20filter.png" width="200" height="200">

</br>

#### Salt-and-Pepper Noise (pa=0.05, pb=0.05):

:full_moon_with_face: The images for **differnt Kernel Size** and **different Filter** can be found below, :point_down: 

|Row\Col |Salt-and-Pepper Noise |Box Filter |Gaussian Filter |Median |     
|---|---|---|---|---    
|Kernel 3*3 | | | |**Best** |
|Kernel 5*5 | | | |Well |
|Kernel 7*7 | | | |Good |

<img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_kernel%3D3*3_pa%3D0.05_pb%3D0.05/Salt%20and%20Pepper%20Noise.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_kernel%3D3*3_pa%3D0.05_pb%3D0.05/Salt%20and%20Pepper%20Noise%20-%20Box%20filter.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_kernel%3D3*3_pa%3D0.05_pb%3D0.05/Salt%20and%20Pepper%20Noise%20-%20Gaussian%20filter.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_kernel%3D3*3_pa%3D0.05_pb%3D0.05/Salt%20and%20Pepper%20Noise%20-%20Median%20filter.png" width="200" height="200">

<img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_kernel%3D3*3_pa%3D0.05_pb%3D0.05/Salt%20and%20Pepper%20Noise.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_kernel%3D5*5_pa%3D0.05_pb%3D0.05/Salt%20and%20Pepper%20Noise%20-%20Box%20filter.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_kernel%3D5*5_pa%3D0.05_pb%3D0.05/Salt%20and%20Pepper%20Noise%20-%20Gaussian%20filter.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_kernel%3D5*5_pa%3D0.05_pb%3D0.05/Salt%20and%20Pepper%20Noise%20-%20Median%20filter.png" width="200" height="200">

<img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_kernel%3D7*7_pa%3D0.05_pb%3D0.05/Salt%20and%20Pepper%20Noise.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_kernel%3D7*7_pa%3D0.05_pb%3D0.05/Salt%20and%20Pepper%20Noise%20-%20Box%20filter.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_kernel%3D7*7_pa%3D0.05_pb%3D0.05/Salt%20and%20Pepper%20Noise%20-%20Gaussian%20filter.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise3_py_kernel%3D7*7_pa%3D0.05_pb%3D0.05/Salt%20and%20Pepper%20Noise%20-%20Median%20filter.png" width="200" height="200">

</br>

:sun_with_face: **In summary:**

Effect of **Kernel size**: 

**Smaller** Kernel size, **better** result.

|Kernel |Result |
|---|--- 
|Kernel 3*3 |Best |
|Kernel 5*5 |Well |
|Kernel 7*7 |Good |

</br>

**'Best' filter** for different types of noise:

**Gaussian Filter** is good at **Gaussian Noise**, **Median Filter** does well in **Salt-and-Pepper Noise**.

|Noise Type |Best Filter|
|---|--- 
|Gaussian Noise |Gaussian Filter |
|Salt-and-Pepper Noise |Median Filter |

</br>

## Exercise 4
**Q1. Look at Threshold.cpp and implement the code in Python, and observe the results for different threshold values. Comment on the results.**

#### Implement Threshold.cpp in Python:
:waxing_crescent_moon: Please check the **Threshold.py code** here :link: **[Threshold.py](https://github.com/qinjinjia/ec601_OpenCV/blob/master/Threshold.py)**

:first_quarter_moon: Please check the **Saved Images** from Threshold.py here :link: **[exercise4_py_results](https://github.com/qinjinjia/ec601_OpenCV/tree/master/exercise4_py_results)**

:waxing_gibbous_moon: The **Saved Images** can also be found below, :point_down:  

|Row\Col |1 |2 |3 |4 |     
|---|---|---|---|---    
|1 |Input Image|Thresholded Image |Binary threshold |Band Thresholding |
|2 |Semi Thresholding |Adaptive Thresholding| | |

<img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise4_py_results/Input%20Image.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise4_py_results/Thresholded%20Image.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise4_py_results/Binary%20threshold.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise4_py_results/Band%20Thresholding.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise4_py_results/Semi%20Thresholding.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise4_py_results/Adaptive%20Thresholding.png" width="200" height="200">

#### Comment on the results for different threshold values:

|Row/Col |Th before |Th after |Comment |   
|---|---|---|--- 
|Input Image|N/A |N/A |N/A |
|Thresholded Image|threshold_value = 128 |threshold_value = 200|Less pixels are truncated |
|Binary threshold|current_threshold = 128|current_threshold = 200 |More pixels are forced to 255|
|Band Thresholding|threshold1, threshold2 = 27, 125 |threshold1, threshold2 = 75, 100 |More pixels are forced to 255|
|Semi Thresholding|current_threshold = 128 |current_threshold = 200  |N/A |
|Adaptive Thresholding|101, 10 |71, 30|Brighter |

<img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise4_py_results/Input%20Image.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise4_py_results_difTh/Input%20Image.png" width="200" height="200">

<img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise4_py_results/Thresholded%20Image.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise4_py_results_difTh/Thresholded%20Image.png" width="200" height="200">

<img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise4_py_results/Binary%20threshold.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise4_py_results_difTh/Binary%20threshold.png" width="200" height="200"> 

<img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise4_py_results/Band%20Thresholding.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise4_py_results_difTh/Band%20Thresholding.png" width="200" height="200"> 

<img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise4_py_results/Semi%20Thresholding.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise4_py_results_difTh/Semi%20Thresholding.png" width="200" height="200">

<img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise4_py_results/Adaptive%20Thresholding.png" width="200" height="200"> <img src="https://github.com/qinjinjia/ec601_OpenCV/blob/master/exercise4_py_results_difTh/Adaptive%20Thresholding.png" width="200" height="200">

</br>

**Q2. What are the disadvantages of binary threshold?**

The main :-1: **disadvantages** of **binary threshold** is that it will force each pixel to **two extremes (i.e. 0 or 255)**, this results in many information lost. 

Also, the **binary threshold** magnifies the effect of the :high_brightness: **lighting conditions**.

<img src="https://docs.opencv.org/3.3.0/threshold.jpg" width="400" height="300">

</br>

**Q3. When is Adaptive Threshold useful?**

Using a **global value** as threshold value is **not** good in all the conditions where image has different :high_brightness: lighting conditions in different areas. However, the algorithm of **adaptive thresholding** calculates the threshold for a small regions of the image (i.e. different thresholds for different regions of the same image).  Therefore, **adaptive thresholding** would be useful for images with **varying illumination**.

Below piece of code compares global thresholding and adaptive thresholding for an image with varying illumination **[[Ref]](https://docs.opencv.org/trunk/d7/d4d/tutorial_py_thresholding.html)**:

```
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('sudoku.png', 0)
img = cv2.medianBlur(img, 5)
ret,th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
titles = ['Original Image', 'Global Thresholding (v = 127)', 
          'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]
for i in xrange(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
```
Result:

<img src="https://docs.opencv.org/trunk/ada_threshold.jpg" width="500" height="500">


**Ref:** [OpenCV Documentation - Image Thresholding](https://docs.opencv.org/trunk/d7/d4d/tutorial_py_thresholding.html) (accessed on Nov. 5, 2017)
