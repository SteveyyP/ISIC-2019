#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 15:24:23 2020

@author: steveyyp
"""

import os
import cv2
import pandas as pd
import numpy as np
import argparse
from pathlib import Path


def image_preprocessing(file_loc: str, img_size: int) -> np.array:
    '''
    Preprocess Image

    Input
    file_loc: str - file location of a .jpg image
    img_size: int - size of resized image

    Output
    img: np.array - processed image file
    '''

    img = cv2.imread(file_loc)                              # Read Image
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)              # Correct Color Space
    img = cv2.resize(img, (img_size, img_size))             # Resize Image
    img = cv2.bilateralFilter(img, 2, 100, 100)             # Reduce Noise + Keep Edges

    return img


def file_rename(file_path: str, search_term: str) -> None:
    '''
    Standardize naming in folder

    Input
    file_path: str - folder directory of files
    search_term: str - term to remove from file name

    Output
    None
    '''

    for file in os.listdir(file_path):
        if search_term in file:
            start_loc = file.find(search_term)
            new_name = file[:start_loc] + file[start_loc+len(search_term):]
            print(file)
            print(new_name)


def resize_img(file_path_read: str, file_path_write: str, img_size: int) -> None:
    '''
    Resize Raw Images and Write to .npy File

    Input
    file_path_read: str - folder location of images
    file_path_write: str - folder location to save .npy files
    img_size: int - size of resized images

    Output
    None
    '''
    counter = 0

    for file in os.listdir(file_path_read):
        if file.endswith('.jpg'):

            # Preprocess Image
            img = image_preprocessing(file_path_read + file, img_size)

            # Save Image as .npy Array
            file = file[:-4]
            np.save(file_path_write + file + '.npy', img)

        counter += 1

        if counter % 300 == 0:
            print('Completed Iteration ', counter)

    print('Image Resize Complete')


def gt_file_writer(file_path_read: str, file_path_write: str, columns: list) -> None:
    '''
    Write Data From Pandas to .npy File

    Input
    file_path_read: str - file path to .csv file
    file_path_write: str - folder location to save .npy files
    columns: list - list of columns to save

    Output
    None
    '''

    df = pd.read_csv(file_path_read)

    for i in range(len(df)):
        arr = np.asarray(df[columns].loc[i])
        file_name = df['image'].iloc[i]

        np.save(file_path_write + str(file_name) + '.npy', arr)

        if i % 300 == 0:
            print('Completed Iteration ', i)

    print('File Writer Complete')


def merge_numpy_array(file_path: str, file_list: str) -> np.array:
    '''
    Helper function: Merge .npy arrays together

    Input
    file_path: str - folder location of files
    file_list: list - list of files in folder

    Output
    out: np array - merged np arrays
    '''
    output = []

    for i in range(len(file_list)):
        tmp = np.load(file_path + file_list[i])
        output.append(tmp)

    out = np.array(output)

    return out


def merge_arrays(file_path: str) -> np.array:
    '''
    Merge .npy arrays together

    Input
    file_path: str - folder location of files

    Output
    np_file: np array - merged np array
    '''

    # Get File List
    flist = [x for x in os.listdir(file_path) if x.endswith('.npy')]

    # Sort File List
    flist.sort()

    # Merge Numpy Arrays
    np_file = merge_numpy_array(file_path=file_path, file_list=flist)

    # Return Merged Array
    return np_file


def directory_check(dir_path: str) -> None:
    '''
    Check if Directory Exists, if not, create directory

    Inputs
    dir_path: str - Directory Location

    Output
    None
    '''
    if os.path.isdir(dir_path) == False:
        try:
            Path(dir_path).mkdir(parents=True, exist_ok=True)
        except OSError:
            print("Creation of the directory %s failed" % dir_path)
        else:
            print("Successfully created the directory %s " % dir_path)
    else:
        print('Directory Exists Already')


if __name__ == '__main__':

    # Main Directory
    main_dir = os.path.dirname(os.path.realpath(__file__))                                                                  # Main Directory
    size = 'medium_size'                                                                                                    # Sub Directory

    # Image Type List
    myList = ['MEL', 'NV', 'BCC', 'AK', 'BKL', 'DF', 'VASC', 'SCC', 'UNK']

    # Argument Parser
    parser = argparse.ArgumentParser()

    # Input Arguments
    parser.add_argument('--img_size', help='Size of rescaled image, default=224', type=int, default=224)                     # img_size
    parser.add_argument('--training_folder', help='Folder location of training data', required=True)                         # train_img_read
    parser.add_argument('--test_folder', help='Folder location of test data', required=True)                                 # test_img_read
    parser.add_argument('--train_gt', help='.csv file location of gt data', required=True)                                   # train_img_gt
    parser.add_argument('--train_img_img', help='Folder location of Individual img numpy arrays', default='train/Images/')   # train_img_write_img
    parser.add_argument('--train_img_gt', help='Folder location of Individual gt numpy arrays', default='train/gt/')         # train_img_write_gt
    parser.add_argument('--test_img_img', help='Folder location of Individual img numpy arrays', default='test/Images/')     # test_img_write_img

    # Define Arguments
    args = parser.parse_args()
    img_size = args.img_size

    # Training Data
    train_img_read = os.path.join(main_dir, args.training_folder)
    test_img_read = os.path.join(main_dir, args.test_folder)

    # Read & Write Directories
    merged = os.path.join(main_dir, 'datasets', size)
    train_img_gt = os.path.join(main_dir, args.train_gt)

    train_img_write_img = os.path.join(merged, args.train_img_img)
    train_img_write_gt = os.path.join(merged, args.train_img_gt)
    test_img_write_img = os.path.join(merged, args.test_img_img)

    # Directory Check
    directory_check(train_img_write_img)
    directory_check(train_img_write_gt)
    directory_check(test_img_write_img)

    # Image Processing
    resize_img(train_img_read, train_img_write_img, img_size)
    resize_img(test_img_read, test_img_write_img, img_size)
    gt_file_writer(train_img_gt, train_img_write_gt, myList)

    # Array Generation
    print('Generating Numpy Array')
    train_img_arr = merge_arrays(train_img_write_img)
    train_gt_arr = merge_arrays(train_img_write_gt)
    test_img_arr = merge_arrays(test_img_write_img)
    print('Saving Arrays...')
    np.save(os.path.join(merged, 'train_img.npy'), train_img_arr)
    np.save(os.path.join(merged, 'train_gt.npy'), train_gt_arr)
    np.save(os.path.join(merged, 'test_img.npy'), test_img_arr)
    print('Arrays Saved!')
