import cv2
import matplotlib.pyplot as plt

def show_rgb_image(image, title=None, conversion=cv2.COLOR_BGR2RGB):
    # Converts from one colour space to the other. this is needed as RGB
    # is not the default colour space for OpenCV
    image = cv2.cvtColor(image, conversion)

    # Show the image
    plt.imshow(image)

    # remove the axis / ticks for a clean looking image
    plt.xticks([])
    plt.yticks([])

    # if a title is provided, show it
    if title is not None:
        plt.title(title)

    plt.show()

def show_images(images, size):
    conversion=cv2.COLOR_BGR2RGB
    items_count = len(images.keys())
    
    fig = plt.figure(figsize=(size, size))
    
    for index, (title, image) in enumerate(images.items()):       
        #w, h = image.shape[:2]
        
        plt.subplot(1, items_count, index + 1)
        
        image = cv2.cvtColor(image, conversion)
        plt.imshow(image)
        plt.xticks([])
        plt.yticks([])
        if title is not None:
            plt.title(title, fontdict = {'fontsize': size})
            
    plt.show()
