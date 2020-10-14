def viewImage(image, name_of_window="a"):
    cv.namedWindow(name_of_window, cv.WINDOW_NORMAL)
    cv.imshow(name_of_window, image)
    cv.waitKey(0)
    cv.destroyAllWindows()
def contour(original,segmentation):
    contours = []
    dx = [0,0,1,-1,1,1,-1,-1]
    dy = [1,-1,0,0,1,-1,1,-1]
    result = np.copy(original)
    black = 0
    test = False
    for i in range(len(segmentation)):
        for j in range(len(segmentation[0])):
            if (segmentation[i][j] == 255 and test == True):
                result[i][j] = black
                for k in range(len(dx)):
                    result[i+dx[k]][j+dy[k]] = black
                
                test = False
                
            if (segmentation[i][j] == 0 and test == False):
                test = True
                result[i][j] = black
                for k in range(len(dx)):
                    result[i+dx[k]][j+dy[k]] = black
                
                
    
                
    for j in range(len(segmentation[0])):
        for i in range(len(segmentation)):
            if (segmentation[i][j] == 255 and test == True):
                result[i][j] = black
                for k in range(len(dx)):
                    result[i+dx[k]][j+dy[k]] = black
                
                test = False
                
            if (segmentation[i][j] == 0 and test == False):
                test = True
                result[i][j] = black
                for k in range(len(dx)):
                    result[i+dx[k]][j+dy[k]] = black
    

    return result
def contour(original,segmentation,out):
    contours = []
    dx = [0,0,1,-1,1,1,-1,-1]
    dy = [1,-1,0,0,1,-1,1,-1]
    result = np.copy(original)
    black = 0
    test = False
    for i in range(len(segmentation)):
        for j in range(len(segmentation[0])):
            if (segmentation[i][j] == 255 and test == True):
                result[i][j] = black
                for k in range(len(dx)):
                    if valid(result,i+dx[k],j+dy[k]):
                        result[i+dx[k]][j+dy[k]] = black
                
                test = False
                
            if (segmentation[i][j] == 0 and test == False):
                test = True
                result[i][j] = black
                for k in range(len(dx)):
                    if valid(result,i+dx[k],j+dy[k]):
                        result[i+dx[k]][j+dy[k]] = black
                
                
    
                
    for j in range(len(segmentation[0])):
        for i in range(len(segmentation)):
            if (segmentation[i][j] == 255 and test == True):
                result[i][j] = black
                for k in range(len(dx)):
                    if valid(result,i+dx[k],j+dy[k]):
                        result[i+dx[k]][j+dy[k]] = black
                
                test = False
                
            if (segmentation[i][j] == 0 and test == False):
                test = True
                result[i][j] = black
                for k in range(len(dx)):
                    if valid(result,i+dx[k],j+dy[k]):
                        result[i+dx[k]][j+dy[k]] = black
    
    cv.imwrite(out+".png",result)
    return result
def apply_contours(original,seg1,seg2,seg3,seg4,gt):
    contour(original,seg1)
    contour(original,seg2)
    contour(original,seg3)
    contour(original,seg4)
    contour(original,gt)

