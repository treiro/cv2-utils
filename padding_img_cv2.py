import cv2

def square_padding_img(image, desired_size, color=(0,0,0)):
    old_size = image.shape[:2] # old_size is in (height, width) format
    ratio = float(desired_size)/max(old_size)
    new_size = tuple([int(x*ratio) for x in old_size])
    # new_size should be in (width, height) format
    image = cv2.resize(image, (new_size[1], new_size[0]))
    delta_w = desired_size - new_size[1]
    delta_h = desired_size - new_size[0]
    top, bottom = delta_h//2, delta_h-(delta_h//2)
    left, right = delta_w//2, delta_w-(delta_w//2)
    new_image = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT,
        value=color)
    return new_image


desired_size = 512
img_pth = "1.jpg"
img = cv2.imread(img_pth)
new_img = square_padding_img(img, desired_size=desired_size, color=(255,255,255))
cv2.imshow("image", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()