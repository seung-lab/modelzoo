### Input specifications
* 160x160x16 patches at 7.16x7.16x40nm^3 resolution
* Image intensity scaled to [0,1] using division by 255 (originally uint8)

### Inference parameters
* 20% overlap (32, 32, 3) between patches
* Connected components threshold: 0.92
* Object size threshold: 300 voxels
