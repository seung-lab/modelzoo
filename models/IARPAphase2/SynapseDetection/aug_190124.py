#!/usr/bin/env python
__doc__ = """
Augmentor - No Box Occlusion
"""

from augmentor import *


def get_augmentation(is_train, **kwargs):
    # Mild misalignment
    m1 = Blend(
        [Misalign((0,10), margin=1), SlipMisalign((0,10), margin=1)],
        props=[0.7,0.3]
    )
    # Missing section
    missing = Compose([
        MixedMissingSection(maxsec=1, double=False, random=True, skip=0.2),
        MixedMissingSection(maxsec=3, double=False, random=True, skip=0.2)
    ])

    augs = list()

    augs.append(Blend([m1, missing]))

    # Grayscale
    augs.append(
        MixedGrayscale2D(
            contrast_factor=0.8,
            brightness_factor=0.5,
            prob=1, skip=0.5))

    # Warping
    if is_train:
        augs.append(Warp(skip=0.3))

    # Flip & rotate
    augs.append(FlipRotate())

    return Compose(augs)
