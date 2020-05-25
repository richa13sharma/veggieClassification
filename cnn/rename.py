import os

for i, filename in enumerate(os.listdir("cGoodCarrots/")): 
        dst ="good_" + str(i) + ".png"
        src ='cGoodCarrots/'+ filename 
        dst ='cGoodCarrots/'+ dst 
        os.rename(src, dst) 