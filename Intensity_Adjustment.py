def Histo(image):
    hist,bins = np.histogram(image.flatten(),256,[0,256])
    hist_cuml = hist.cumsum()
    hist_normalized = hist_cuml * hist.max()/ hist_cuml.max()
    return (hist_cuml,hist_normalized,hist)

def PlotHisto(image,hist_normalized):
    plt.plot(hist_normalized, color = 'b')
    plt.hist(image.flatten(),256,[0,256], color = 'r')
    plt.xlim([0,256])
    plt.legend(('histogram','cumulative histogram'), loc = 'upper left')
    plt.show()
    return 


def Intensity_Adjustment(image):
    hist=Histo(image)[1]
    hist_masked = np.ma.masked_equal(hist,0)
    normalize_ratio=255/(hist_masked.max()-hist_masked.min())
    hist_masked = (hist_masked - hist_masked.min())*normalize_ratio
    hist = np.ma.filled(hist_masked,0).astype('uint8')
    img2=hist[image]
    return img2


def Range(image,histo):
    begin=-1
    end=-1;
    for i in range(256):
        if(begin==-1 and histo[i]!=0):
            begin=i
        if(end==-1 and histo[-i-1]!=0):
            end=i   
    return (begin,end)
    
def imadjust(x,a,b,c,d,gamma=1):
    #how to use img_adjusted=imadjust(img,img.min(),img.max(),0,1) 
    #img 1D tab img = np.asarray(image)
    y = (((x - a) / (b - a)) ** gamma) * (d - c) + c
    return y
