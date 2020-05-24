import os

for i, filename in enumerate(os.listdir("cGoodResized/")): 
        dst ="good_" + str(i) + ".png"
        src ='cGoodResized/'+ filename 
        dst ='cGoodResized/'+ dst 
 
        os.rename(src, dst) 