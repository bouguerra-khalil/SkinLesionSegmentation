def otsu_threshold(im):
    img = np.copy(im)
    res = 0
    ma=0
    histo = np.zeros(256)
    moy = np.zeros(256)
    num_pix = len(im)*len(im[0])
    for i in range(len(im)):
        for j in range(len(im[0])):
            histo[im[i][j]]+=1
    histo_cum = np.copy(histo)
    for i in range(1,256):
        histo_cum[i]+= histo_cum[i-1]
    for i in range(1,256):
        moy[i] =  i*histo[i] + moy[i-1]
    
    for t in range(0,256):
        n1 = histo_cum[t]
        n2 = num_pix - n1
        
        w1 = n1/(n1+n2)
        w2 = n2/(n1+n2)
        u1=0
        if histo_cum[i]!=0:
            u1 = moy[t]/histo_cum[t]
        u2 = 0
        if (histo_cum[255]-histo_cum[t])!=0:
            u2 = (moy[255]-moy[t])/(histo_cum[255]-histo_cum[t])
        Delta = w1*w2*(u1-u2)**2
        
        if Delta > ma:
            res = t
            ma = Delta
            
           
   
    img[img <= res] = 0
    img[img > res] = 1
    
    return (img*255).astype(np.uint8)