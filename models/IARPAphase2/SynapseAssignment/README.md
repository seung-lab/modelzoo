### Input specification
* 2 x 80 x 80 x 8 patches at 7.16 x 7.16 x 40 nm^3 resolution
* First 80 x 80 x 8 patch is the image context - with image intensity divided by 255 to normalize between [0,1] (originally uint8)
* Second patch is a 0/1 binary image of the cleft to assign (formatted as float32)
