
image_kernels =("blur",
                "emboss",
                "top_sobel",
                "bottom_sobel",
                "identity",
                "left_sobel",
                "outline",
                "sharpen",
                "right_sobel"
                )

print("insert kernel  name : \n ")
kernel_type = (input())

valid_kernel =1
if kernel_type in image_kernels:

    kernel_dir = f'kernels\{kernel_type}.txt'



    kernel_fptr = open(kernel_dir , "r")


    kernels_parameters =[]

    data = kernel_fptr.readlines()

    for item in data:
        processed_data =item.split()
        kernels_parameters.extend([float(processed_data[0]) , float(processed_data[1]) ,float(processed_data[2])])

else:
    valid_kernel =0