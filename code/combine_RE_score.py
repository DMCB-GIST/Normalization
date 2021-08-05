#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import argparse
import time
import numpy as np
import re


def create_test_data(input_file, prob_file, output_file):
    f = open(prob_file, 'r')
    prob_lines = f.readlines()
    f.close()

    i = 0
    with open(output_file, 'w') as writer, \
         open(input_file, 'r') as reader:
            for line in reader:
                if not line.strip():
                    mention = ""
                    writer.write("\n")
                else:
                    tmp = line.split("\t")
                    if len(tmp) == 2:
                        writer.write(line.strip() + "\n")
                    else:
                        prob = prob_lines[i].strip().split("\t")[-1]
                        if "*" in line:
                            writer.write("\t{}\t{}\n".format(line.strip(), prob))
                        else:
                            writer.write("\t\t{}\t{}\n".format(line.strip(), prob))
                        i += 1
                  


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--input_file', default='input.txt', type=str, required=True, help='input_file')
    parser.add_argument('--prob_file', default='prob.txt', type=str, required=True, help='prob_file')
    parser.add_argument('--output_file', default='output.txt', type=str, required=True, help='output_file')
    args = parser.parse_args()
    print('\nargs:\n' + args.__repr__())

    start_time = time.time()
    create_test_data(args.input_file, args.prob_file, args.output_file)
    end_time = time.time()

    print ("*******************************")
    print (time.strftime("     %Y-%m-%d %H:%M:%S", time.localtime(start_time)))
    print (time.strftime("     %Y-%m-%d %H:%M:%S", time.localtime(end_time)))
    print ("     --- {} seconds---".format(end_time-start_time))
    print ("*******************************")



if __name__ == '__main__':
    main()

