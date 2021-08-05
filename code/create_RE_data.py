#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import tensorflow as tf
import os
import argparse
import time
import numpy as np
import re


def create_RE_test_data(input_file, output_file):
    
    with open(output_file, 'w') as writer, \
         open(input_file, 'r') as reader:
            for line in reader:
                label = 0
                if not line.strip():
                    mention = ""
                    #writer.write("\n")
                else:
                    tmp = line.split("\t")

                    if len(tmp) == 2:
                        mention = tmp[0]
                    else:
                        candidate = " ".join(tmp[3].split("_")[1:])
                        if "*" in line:
                            label = 1

                        writer.write("{}\t{}\t{}\n".format(mention, candidate.strip(), label))


def create_RE_train_data(input_file, output_file):
    
    with open(output_file, 'w') as writer, \
         open(input_file, 'r') as reader:
            for line in reader:
                label = 0
                if not line.strip():
                    mention = ""
                    #writer.write("\n")
                else:
                    tmp = line.split("\t")

                    if len(tmp) == 2:
                        mention = tmp[0]
                    else:
                        candidate = " ".join(tmp[3].split("_")[1:])
                        if "*" in line:
                            label = 1

                        if mention != candidate:
                            writer.write("{}\t{}\t{}\n".format(mention, candidate, label))
                                    


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--input_file', default='input.txt', type=str, required=True, help='input_file')
    parser.add_argument('--input_type', default='test', type=str, required=True, help='train/test')
    parser.add_argument('--output_file', default='output.txt', type=str, required=True, help='output_file')
    args = parser.parse_args()
    print('\nargs:\n' + args.__repr__())

    start_time = time.time()
    if args.input_type == 'train':
        create_RE_train_data(args.input_file, args.output_file)
    elif args.input_type == 'test':
        create_RE_test_data(args.input_file, args.output_file)
    else:
        print("ERROR! You should choose a data type (train/test).")
    end_time = time.time()

    print ("*******************************")
    print (time.strftime("     %Y-%m-%d %H:%M:%S", time.localtime(start_time)))
    print (time.strftime("     %Y-%m-%d %H:%M:%S", time.localtime(end_time)))
    print ("     --- {} seconds---".format(end_time-start_time))
    print ("*******************************")



if __name__ == '__main__':
    main()


#python _7_create_fine_tuning_data.py  --input_file=test.txt  --output_file=output_test.txt 
#python _7_create_fine_tuning_data.py  --input_file=output_nonreplicated_train_dev_with_abbr_feature_extraction_result_from_BioBERT_ver2.txt  --output_file=NCBI_fine_tuning_classification_data.txt
#python _7_1_create_fine_tuning_data.py  --input_file=output_nonreplicated_train_dev_with_abbr_feature_extraction_result_from_BioBERT_ver2.txt  --output_file=NCBI_fine_tuning_classification_data_with_MEDIC_info.txt


