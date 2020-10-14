def hair_removal(img):
    kernel = np.ones((10,10),np.uint8)
    closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel,iterations = 1)
    median = cv.medianBlur(closing, 5)
    return median
