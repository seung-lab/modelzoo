### Input specifications
* 160 x 160 x 18 patches at 7.16 x 7.16 x 40nm^3 resolution
* Image intensity scaled to [0,1] using division by 255 (originally uint8)

### Inference parameters
* 20% overlap (32, 32, 3) between patches
* Connected components threshold: 0.25
* Object size threshold: 50 voxels
