#!/usr/bin/env python

import argparse
import pandas as pd

def quantileRescale(src,dst):
    lower = 0.10
    upper = 0.90
    dstRange = dst.quantile([lower,upper])
    srcRange = src.quantile([lower,upper])
    scale = (srcRange.loc[upper] - srcRange.loc[lower]) / (dstRange.loc[upper] - dstRange.loc[lower])
    shift = (srcRange.loc[lower] / scale) - dstRange.loc[lower]
    scaleDF = src / scale - shift
    return scaleDF

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--src")
    parser.add_argument("--dst")
    parser.add_argument("--out")

    args = parser.parse_args()

    src = pd.read_csv(args.src, sep="\t", index_col=0)
    dst = pd.read_csv(args.dst, sep="\t", index_col=0)

    isect = src.columns.intersection(dst.columns)

    scaled = quantileRescale(src[ isect ], dst[ isect])

    scaled.to_csv(args.out, sep="\t")
