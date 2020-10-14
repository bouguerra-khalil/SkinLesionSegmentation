def compare_2_segmentation(seg,gt_seg):
    tp=0
    tn=0
    fp=0
    fn=0
    img_size=seg.shape[0]*seg.shape[1]
    for i in range(seg.shape[0]):
        for j in range(seg.shape[1]): 
            if(seg[i][j]==gt_seg[i][j] and seg[i][j]==255):
                tp+=1
            if(seg[i][j]==gt_seg[i][j] and seg[i][j]==0):
                tn+=1
            if(seg[i][j]!=gt_seg[i][j] and seg[i][j]==255):
                fp+=1
            if(seg[i][j]!=gt_seg[i][j] and seg[i][j]==0):
                fn+=1
    return(tp,tn,fp,fn)
def get_metrics(seg,gt_seg):
    (TP,TN,FP,FN)=compare_2_segmentation(seg,gt_seg)
    print (TP,TN,FP,FN)
    Sensitivity = TP/(TP + FN)
    Specificity = TN/(TN + FP)
    Accuracy =(TP + TN)/(TP + FP + FN + TN)
    Similarity=(2*TP)/(2*TP + FN + FP)
    return(Sensitivity*100,Specificity*100,Accuracy*100,Similarity*100)
def get_best_channel(data,header): 
    Sensitivity=[-1]*3
    Specificity=[-1]*3
    Accuracy=[-1]*3
    Similarity=[-1]*3
    mean_data=data.mean(axis=0)
    for index,channel in enumerate(mean_data): 
        if(channel[0]>Sensitivity[1]):
            Sensitivity[2]=index
            Sensitivity[1]=channel[0]
            Sensitivity[0]=header[index]
        if(channel[1]>Specificity[1]):
            Specificity[2]=index
            Specificity[1]=channel[1]
            Specificity[0]=header[index]
        if(channel[2]>Accuracy[1]):
            Accuracy[2]=index
            Accuracy[1]=channel[2]
            Accuracy[0]=header[index]
        if(channel[3]>Similarity[1]):
            Similarity[2]=index
            Similarity[1]=channel[3]
            Similarity[0]=header[index]
    return(np.asarray([Sensitivity,Specificity,Accuracy,Similarity]))

def get_graphs_channel(data,best_channel):
    import time 
    color=["yellow","blue","green","red"]
    channels=[channel for channel in best_channel[:,0]]
    Sensitivity=[data[:,int(i),0] for i in best_channel[:,2]]
    Specificity=[data[:,int(i),1] for i in best_channel[:,2]]
    Accuracy=[data[:,int(i),2] for i in best_channel[:,2]]
    Similarity=[data[:,int(i),3] for i in best_channel[:,2]]
    metrics=[Sensitivity,Specificity,Accuracy,Similarity]
    metrics_name=["Sensitivity","Specificity","Accuracy","Similarity"]
    for i in range(4):
        plt.axis([0,32,0,100])
        plt.title(metrics_name[i])
        plt.ylabel(metrics_name[i])
        plt.xlabel("Number of image")
        for j in range(4):
            plt.plot(list(range(len(metrics[i][j]))),metrics[i][j], marker = 'o',label=channels[j],color=color[j])
        plt.legend()
        plt.savefig(metrics_name[i]+'.png')
        plt.figure()
