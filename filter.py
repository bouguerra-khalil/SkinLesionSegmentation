def generate_kernal(r):
    kernal=np.zeros((2*r+1,2*r+1))
    c=(r,r)
    for i in range(c[0]-r,c[0]+r+1):
        for j in range(c[1]-r, c[1]+r+1):
            if((c[0] - i) ** 2 + (c[1] - j) ** 2 <= r**2):
                kernal[i,j]=1
    return kernal/kernal.sum()


def apply_filter(im,mask):
    fft2=np.fft.fft2
    ifft2=np.fft.ifft2
    (y,x)=im.shape
    (ym,xm)=mask.shape
    mm=np.zeros((y,x))
    mm[:ym,:xm]=mask
    fout=(fft2(im)*fft2(mm))
    mm[:ym,:xm]=0
    y2=int(np.round(ym/2-0.5))
    x2=int(np.round(xm/2-0.5))
    mm[y2,x2]=1
    out=np.real(ifft2(fout*np.conj(fft2(mm))))
    return 