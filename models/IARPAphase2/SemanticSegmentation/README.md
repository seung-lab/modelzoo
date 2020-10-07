### Input specifications
* 256 x 256 x 20 patches @ 7.16 x 7.16 x 40 nm^3 resolution
* Scaled to [0,1] - division by 255

### Output specifications
* 5 separate volumes specifying (in order): soma, axon, dendrite, glia, blood vessel

### Inference parameters
* 20% overlap (i.e. stride 205 x 205 x 16)
* Classified each voxel by taking the argmax over volumes (after patch blending)

### Weights
https://storage.googleapis.com/microns-seunglab/minnie65/semanticweights/model479000.chkpt
