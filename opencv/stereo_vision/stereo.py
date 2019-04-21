#!/usr/bin/env python3

from PIL import Image
import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
 
def find_min_by_shift(limg_arr, rimg_arr, row=650):
    """ Left image gets shifted left
    """
    assert(limg_arr.shape == rimg_arr.shape)

    # taking the right as base, shift the left img
    pos, val = 0, 0
    vals = []
    fig = plt.figure()
    #fig = plt.figure()
    imgs = []
    patch_rigth = rimg_arr[row:row+220,0,2]
    patch_left  = limg_arr[row:row+220,0,2]
    print(patch_rigth.shape)
    # Image.fromarray(np.vstack((patch_left, patch_rigth))).show()
    #Image.fromarray(patch_rigth).show()
    for shift in range(0,limg_arr.shape[1]):
        diff = np.correlate(patch_left, patch_rigth)
        vals.append(diff)
        if diff > val:
            val = diff
            pos = shift
        # patch_left = np.roll(patch_left, -1)
        patch_left  = limg_arr[row:row+220,shift,2]
        
        #print(diff.shape)
        #imgs.append([plt.imshow(np.vstack((patch_left, patch_rigth, diff)))])
    plt.plot(vals)
    plt.show()
    
    # anim = animation.ArtistAnimation(fig, imgs, interval=300, blit=True, repeat_delay=10000)
    # plt.show()
    #     vdiff = right_row - left_row
    #     print(sum(vdiff))
    #     diff_val = sum(right_row - left_row)
    #     vals.append(diff_val)
    #     #print("shift: {}, val: {}".format(shift, diff_val))
    #     # shift left to the left
    #     left_row = np.roll(left_row, -1)
    #     #left_row[-1] = 0
    #     if diff_val < val:
    #         val = diff_val
    #         pos = shift
    # #plt.plot(range(len(vals)), vals)
    # #plt.show()
    #     if shift % 10 == 0:
    #         left_row_3d = limg_arr[row-5:row+5,:,:]
    #         right_row_3d = rimg_arr[row-5:row+5,:,:]
    #         time.sleep(3)
    return pos


if __name__ == "__main__":
    limg = Image.open("opencv/stereo_vision/imgs/im2.jpg")
    rimg = Image.open("opencv/stereo_vision/imgs/im6.jpg")
    limg_arr = np.array(limg, dtype = np.int32)
    rimg_arr = np.array(rimg, dtype = np.int32)
    print("Image size {}".format(limg_arr.shape))
    sh=find_min_by_shift(limg_arr, rimg_arr)
    print("\n shift: {} \n\n".format(sh))
    limg_arr = np.array(limg)
    rimg_arr = np.array(rimg)
    limg_arr = np.roll(limg_arr, -sh)
    shifted_img = Image.fromarray(limg_arr)
    meld = Image.blend(rimg, shifted_img, 0.3)
    meld.show()