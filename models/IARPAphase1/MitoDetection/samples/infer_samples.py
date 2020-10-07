#!/usr/bin/env python

import synaptor as s
import torch, imp


def main(net_fname, chkpt_fname, *sample_fnames):

    net = read_network(net_fname, chkpt_fname)

    samples = read_samples(sample_fnames)

    for (i,sample) in enumerate(samples):
        #output, intermed = infer_sample(net,sample)
        output = infer_sample(net, sample)
        write_output(output, i, "output")
        #write_output(intermed, i, "intermed")


def read_network(net_fname, chkpt_fname):

    model = imp.load_source("Model",net_fname).InstantiatedModel.cuda()
    model.load_state_dict(torch.load(chkpt_fname))
    return model


def read_samples(fnames):
    return [s.io.read_h5(fname) for fname in fnames]


def infer_sample(net, sample):

    if len(sample.shape) == 3:
        sample = sample.reshape((1,1)+sample.shape)

    sample = sample.astype("float32") / 255.
    in_v = torch.from_numpy(sample).cuda()

    output = net(in_v)

    output = torch.nn.functional.sigmoid(output[0]).data.cpu().numpy()
    #intermed = intermed.data.cpu().numpy()[0,...]

    return output#, intermed


def write_output(output, num, tag):
    s.io.write_h5(output, f"{tag}_{num}.h5")


if __name__ == "__main__":
    from sys import argv

    main(*argv[1:])
