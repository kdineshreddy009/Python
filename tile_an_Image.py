from PIL import Image
import sys
import traceback

def saveTiledImage(input_file,number_of_tiles,save_to_path):
    im = Image.open(input_file)

    # im_resized: a tile image
    tile_size = im.size[0]/number_of_tiles, im.size[1]/number_of_tiles
    im_resized = im.resize(tile_size)

    # creating an empty image with horizontal tiled size
    h_size = im.size[0], im.size[1]/number_of_tiles
    horizontal_tiled = Image.new('RGB', h_size)

    xvar = 0
    yvar = 0
    #form a horizontal tiled image
    for x in range(0, number_of_tiles, 1):
        horizontal_tiled.paste(im_resized, (xvar, yvar))
        xvar += im_resized.size[0]

    #make use of a horizontal tiled image to fill vertical way
    full_sized_img = Image.new('RGB', im.size)
    yvar = 0
    while yvar < im.size[1]:
        full_sized_img.paste(horizontal_tiled,(0,yvar))
        yvar += im_resized.size[1]
    full_sized_img.show()
    full_sized_img.save(str(save_to_path)+"/newTiledImage.jpg", format="JPEG")


if __name__ == "__main__":
    try:
        saveTiledImage(sys.argv[1],int(sys.argv[2]),sys.argv[3])
    except IndexError:
        print("\n*********Please check if your input is correct as per below format*********\npython tile_image.py <input_image_filepath>/filename.jpg number_of_tiles <output_image_filepath>\n")
    except Exception:
        traceback.print_exc()
