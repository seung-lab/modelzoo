#!/usr/bin/env python

import u
import torch, imp


def main(net_fname, chkpt_fname, *sample_fnames):

    net = read_network(net_fname, chkpt_fname)

    samples = read_samples(sample_fnames)

    for (i,sample) in enumerate(samples):
        output = infer_sample(net,sample)
        write_output(output, i)


def read_network(net_fname, chkpt_fname):

    model = imp.load_source("Model",net_fname).InstantiatedModel.cuda()
    model.load_state_dict(torch.load(chkpt_fname))
    return model


def read_samples(fnames):
    return [u.read_file(fname) for fname in fnames]


def infer_sample(net, sample):

    if len(sample.shape) == 3:
        sample = sample.reshape((1,1)+sample.shape)

    sample = sample.astype("float32") / 255.
    in_v = torch.autograd.Variable(torch.from_numpy(sample), volatile=True).cuda()

    output = net(in_v)

    output = torch.nn.functional.sigmoid(output[0]).data.cpu().numpy()
    return output


def write_output(output, num):
    u.write_file(output[0], "output_{num}.h5".format(num=num))
    #for (k,v) in output_dict.items():
    #    u.write_file(v, "{k}_{num}.h5".format(k=k,num=num))


if __name__ == "__main__":
    from sys import argv

    main(*argv[1:])
