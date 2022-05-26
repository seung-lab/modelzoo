### Input specification
* 128 x 128 x 20 patches @ 16 x 16 x 40 nm^3 resolution
* Scaled to [0,1] - division by 255

### Inference parameters
* Model specification
  - [DeepEM](https://github.com/seung-lab/DeepEM)'s `rsunet_deprecated.py` [[link](https://github.com/seung-lab/DeepEM/blob/master/deepem/models/rsunet_deprecated.py)]
  - No output cropping
  - Use `updown_deprecated.py` [[link](https://github.com/seung-lab/DeepEM/blob/master/deepem/models/updown_deprecated.py)] instead for inference @ 8 x 8 x 40 nm^3 resolution, with modifying input/output patch size accordingly
* 50% overlap of input patches (i.e. stride = 64 x 64 x 10)
