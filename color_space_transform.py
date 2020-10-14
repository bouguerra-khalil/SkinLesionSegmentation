def color_space_trans(image,par):
    epselon = 0.00001
    img = np.copy(image)
    img = np.float32(img)/255

    R = img[:,:,0]
    G = img[:,:,1]
    B = img[:,:,2]
   
    if par=='R':
        result= R
                
    if par=='G':
        
        result= G
        
    if par=='B':
        
        result= B

    if par=='X':
        
        result= 0.4125*R + 0.3576*G + 0.1804*B
        
    if par=='Y':
        
        y = 0.2127*R + 0.7152 * G + 0.0722*B
        result= y;
                
    if par=='Z':
        
        z = 0.0193*R + 0.1192*G + 0.9502*B
        result= z;
                         
    if par=='I':
        
        inte = R + G + B
        inte = inte / 3
        result= inte;
        
    if par=='S':
        ss = R + G + B+epselon
        s = 1-(3* np.minimum(np.minimum(R , G) , B)/ss)
        result= s;
                
    if par=='H':
        result = B
        for i in range(0,len(img)):
            for j in range(0,len(img[0])):
                up = (R[i][j]-((G[i][j]/2+B[i][j]/2)))

                
                down = math.sqrt((R[i][j]-G[i][j])**2 +(R[i][j]-B[i][j])*(G[i][j]-B[i][j]))
                
                W = math.acos(up / math.sqrt(down))
                h = W
                if G[i][j]<B[i][j]:
                    h = 2*math.pi - W
                result[i][j]= h;
            
    return (result*255).astype(np.uint8)
