
def check_if_image_grey(grey_images_list):
    grey_read_ptr = open("greyify\is_grey.txt", "r")
    grey_images = grey_read_ptr.readlines()

    for image in grey_images:
        grey_images_list.append(image[:-1])


