import numpy as np
from PIL import Image
from kernel_data import valid_kernel
from image_choice import  image_choice
from check_grey import check_if_image_grey

if  valid_kernel :
   from kernel_data import kernels_parameters, kernel_type



if valid_kernel:

    #kernels argumments
    a1 , a2 , a3 , a4 , a5 , a6  ,a7 , a8 , a9 = kernels_parameters




    image_to_process_name = image_choice()
    is_image =1

    image = f"images\{image_to_process_name}"

    filter = np.array([[a1, a2, a3],
                       [a4, a5, a6],
                       [a7, a8, a9]])


    class Processing_image:

        def __init__(self, img_name):
            self.image_name = img_name
            self.image = Image.open(img_name)
            self.width = self.image.size[0]
            self.height = self.image.size[1]
            self.pix = self.image.load()
            self.new_pixels = []

        def greyify(self):
            for height_iter in range(self.height):
                for width_iter in range(self.width):
                    R ,G ,B = self.pix[width_iter  , height_iter]
                    grey_shade =(R + G + B)//3
                    self.pix[width_iter , height_iter] = (grey_shade , grey_shade , grey_shade)

            self.image.save(f"greyify\{image_to_process_name}")
            with open("greyify\is_grey.txt" ,"a") as grey_write_ptr:
                grey_write_ptr.write(image_to_process_name+"\n")


        def filtering(self):
            for height_iter in range(3,self.height,3):
                for width_iter in range(3,self.width,3):
                    square = np.array([[self.pix[width_iter-3 ,height_iter-3][0] ,self.pix[width_iter-2 ,height_iter-3][0] ,self.pix[width_iter-1 ,height_iter-3][0]],
                                       [self.pix[width_iter-3 ,height_iter-2][0] ,self.pix[width_iter-2 ,height_iter-2][0] ,self.pix[width_iter-1 ,height_iter-2][0]],
                                       [self.pix[width_iter-3 ,height_iter-1][0] ,self.pix[width_iter-2 ,height_iter-1][0] ,self.pix[width_iter-1 ,height_iter-1][0]]])
                    summation = np.sum((square * filter).flatten())
                    self.new_pixels.append(int(summation))

        def resizing(self):
            after_1st_line =0
            new_height , new_width= (0,0)
            for height_iter in range(3 ,self.height , 3):
                new_height+=1
                after_1st_line+=1
                for width_iter in range(3, self.width ,3):
                    if after_1st_line == 1:
                        new_width +=1

            self.width = new_width
            self.height = new_height
            self.image = self.image.resize((self.width, self.height), Image.NEAREST)

        def apply_filter(self  ,new_pixels_array):
            self.pix = self.image.load()
            new_pixels_array_iter = 0
            for height_iter in range(self.height):
                for width_iter in range(self.width):
                    self.pix[width_iter , height_iter] = (new_pixels_array[new_pixels_array_iter],
                                                          new_pixels_array[new_pixels_array_iter],
                                                          new_pixels_array[new_pixels_array_iter])
                    new_pixels_array_iter+=1


            self.image.save(f"output\{image_to_process_name[:-4] + '_' +kernel_type}.png")


    grey_image_array= []
    check_if_image_grey(grey_image_array)


    try:
        image_to_process = Processing_image(image)
    except:
        is_image =0
        print("this image is not available")

    if is_image :

        if not image_to_process_name in grey_image_array:
            image_to_process.greyify()
        image_to_process.filtering()



        image_to_filter_name = "greyify/%s" % (image_to_process_name)

        image_to_filter = Processing_image(image_to_filter_name)
        image_to_filter.resizing()
        image_to_filter.apply_filter(image_to_process.new_pixels)

else:
    print("the inserted kernel is not available")