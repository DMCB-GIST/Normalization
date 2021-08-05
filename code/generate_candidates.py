#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import argparse
import time
import numpy as np
import gensim


def calculate_ranking_test (MEDIC_path, input_file, output_file, topn):
    model = gensim.models.KeyedVectors.load_word2vec_format(MEDIC_path, binary=False)

    with open(input_file, 'r') as reader, \
         open(output_file, 'w') as writer:
        for line in reader:
            mention_info = line.strip().split("\t")[0]
            conceptIDs = mention_info.split("_")[0]
            mention = " ".join(mention_info.split("_")[1:])

            vector = np.array(line.strip().split("\t")[-1].split(" "), dtype='f')
            writer.write("{}\t{}\n".format(mention, conceptIDs))

           
            i = 1
            ID_set = set()
            label = ""
            for similar_word, score in model.similar_by_vector(vector, topn=500):            
                sim_IDs = similar_word.split("_")[0]
                if "+" in sim_IDs:
                    continue

                if sim_IDs in ID_set:
                    continue;
                else:
                    ID_set.add(sim_IDs)

                for sim_ID in sim_IDs.split("|"):
                    if sim_ID in conceptIDs.split("|"):
                        label = "*"
                        break
                    else:
                        label = ""

                writer.write("\t%s\t%d\t%s\t%.6f\n" % (label, i, similar_word, score))
                i += 1

                if len(ID_set) == topn:
                    break

            writer.write("\n")



def calculate_ranking_train (MEDIC_path, input_file, output_file, topn):
    model = gensim.models.KeyedVectors.load_word2vec_format(MEDIC_path, binary=False)

    with open(input_file, 'r') as reader, \
         open(output_file, 'w') as writer:
        for line in reader:
            mention_info = line.strip().split("\t")[0]
            conceptIDs = mention_info.split("_")[0]
            mention = " ".join(mention_info.split("_")[1:])

            vector = np.array(line.strip().split("\t")[-1].split(" "), dtype='f')
            writer.write("{}\t{}\n".format(mention, conceptIDs))

            i = 1
            for similar_word, score in model.similar_by_vector(vector, topn):            
                sim_IDs = similar_word.split("_")[0]
                if "+" in sim_IDs:
                    continue

                for sim_ID in sim_IDs.split("|"):
                    if sim_ID in conceptIDs.split("|"):
                        label = "*"
                        break
                    else:
                        label = ""

                writer.write("\t%s\t%d\t%s\t%.6f\n" % (label, i, similar_word, score))
                i += 1

            writer.write("\n")


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--input_file', default='input.txt', type=str, required=True, help='input_file')
    parser.add_argument('--dict_file', default='dict.txt', type=str, required=True, help='dictionary_file')
    parser.add_argument('--output_file', default='output.txt', type=str, required=True, help='output_file')
    parser.add_argument('--topn', default=10 , type=int, required=False, help='the number of rankings')
    parser.add_argument('--type', default='test', type=str, required=False, help='train/test')
    args = parser.parse_args()
    print('\nargs:\n' + args.__repr__())

    start_time = time.time()
    if args.type == 'test':
    	calculate_ranking_test (args.dict_file, args.input_file, args.output_file, args.topn)
    else:
        calculate_ranking_train (args.dict_file, args.input_file, args.output_file, args.topn)    
    end_time = time.time()

    print ("*******************************")
    print (time.strftime("     %Y-%m-%d %H:%M:%S", time.localtime(start_time)))
    print (time.strftime("     %Y-%m-%d %H:%M:%S", time.localtime(end_time)))
    print ("     --- {} seconds---".format(end_time-start_time))
    print ("*******************************")



if __name__ == '__main__':
    main()