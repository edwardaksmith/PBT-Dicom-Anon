#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 11:37:18 2019

@author: edwardsmith
"""

import os as os
import pydicom as pyd
import copy as copy


def anon_ct(dataset, pat_name, pat_id):
    """ Quick Summary:  This function anonymises DICOM CT files produced at the
                        PBT Department of Christie Hospital.
    """

    date = '19010101'
    time = '000000'
    patsex = '0'
    name = 'name'
    description = 'description'

    dataset.InstanceCreationDate = date
    dataset.InstanceCreationTime = time

    dataset.StudyDate = date
    dataset.SeriesDate = date
    dataset.ContentDate = date

    dataset.StudyTime = time
    dataset.SeriesTime = time
    dataset.ContentTime = time

    dataset.InstitutionName = name
    dataset.ReferringPhysicianName = name
    dataset.StationName = name
    dataset.StudyDescription = description
    dataset.SeriesDescription = description
    dataset.PhysiciansOfRecord = name

    dataset.PatientName = pat_name
    dataset.PatientID = pat_id
    dataset.PatientBirthDate = date
    dataset.PatientBirthTime = time
    dataset.PatientSex = patsex
    dataset.OtherPatientIDs = pat_id

    return dataset


def anon_rd(dataset, pat_name, pat_id):
    """Quick Summary:   This function anonymises DICOM RD files produced at the
                        PBT Department of Christie Hospital.
    """

    date = '19010101'
    time = '000000'
    patsex = '0'
    name = 'name'
    description = 'description'

    dataset.InstanceCreationDate = date
    dataset.InstanceCreationTime = time

    dataset.StudyDate = date
    dataset.SeriesDate = date
    dataset.ContentDate = date

    dataset.StudyTime = time
    dataset.SeriesTime = time
    dataset.ContentTime = time

    dataset.InstitutionName = name
    dataset.ReferringPhysicianName = name
    dataset.StationName = name
    dataset.StudyDescription = description
    dataset.SeriesDescription = description
    dataset.PhysiciansOfRecord = name

    dataset.PatientName = pat_name
    dataset.PatientID = pat_id
    dataset.PatientBirthDate = date
    dataset.PatientBirthTime = time
    dataset.PatientSex = patsex
    dataset.OtherPatientIDs = pat_id

    return dataset


def anon_rn(dataset, pat_name, pat_id):
    """Quick Summary:   This function anonymises DICOM RN (Plan) files produced at the
                        PBT Department of Christie Hospital.
    """

    date = '19010101'
    time = '000000'
    patsex = '0'
    name = 'name'
    description = 'description'

    dataset.InstanceCreationDate = date
    dataset.InstanceCreationTime = time

    dataset.StudyDate = date
    dataset.StudyTime = time

    dataset.ReferringPhysicianName = name
    dataset.StationName = name
    dataset.StudyDescription = description
    dataset.SeriesDescription = description
    dataset.PhysiciansOfRecord = name
    dataset.OperatorName = name

    dataset.PatientName = pat_name
    dataset.PatientID = pat_id
    dataset.PatientBirthDate = date
    dataset.PatientBirthTime = time
    dataset.PatientSex = patsex
    dataset.OtherPatientIDs = pat_id

    dataset.RTPlanLabel = description
    dataset.RTPlanName = name
    dataset.RTPlanDate = date
    dataset.RTPlanTime = time

    dataset.ReviewDate = date
    dataset.ReviewTime = time
    dataset.ReviewerName = name

    return dataset


def anon_rs(dataset, pat_name, pat_id):
    """Quick Summary:   This function anonymises DICOM RS (Structure) files produced at the
                        PBT Department of Christie Hospital.
    """

    date = '19010101'
    time = '000000'
    patsex = '0'
    name = 'name'
    description = 'description'

    dataset.InstanceCreationDate = date
    dataset.InstanceCreationTime = time

    dataset.StudyDate = date
    dataset.StudyTime = time

    dataset.ReferringPhysicianName = name
    dataset.StationName = name
    dataset.StudyDescription = description
    dataset.SeriesDescription = description
    dataset.PhysiciansOfRecord = name

    dataset.PatientName = pat_name
    dataset.PatientID = pat_id
    dataset.PatientBirthDate = date
    dataset.PatientBirthTime = time
    dataset.PatientSex = patsex
    dataset.OtherPatientIDs = pat_id

    dataset.StructureSetDate = date
    dataset.StructureSetTime = time

    dataset.ReviewDate = date
    dataset.ReviewTime = time
    dataset.ReviewerName = name

    return dataset


def anon_data_folder(anon_dir, pat_id):
    try:
        os.stat(anon_dir + pat_id)
    except:
        os.mkdir('/Users/edwardsmith/Documents/spyder/dicom_anon/' + pat_id)


def anon_dcm_write(anon_dir, pat_id, fn, data):

    save_location = anon_dir + pat_id,
    pyd.filewriter.dcmwrite(sp + fn, data, write_like_original=True)


def anon_dicom_folder(file_dir, anon_dir, pat_name, pat_id):
    anon_data_folder(pat_name)

    save_place = anon_dir + pat_name + '_anon_data/'

    file_list = os.listdir(file_dir)

    for file in file_list:

        d_data = pyd.dcmread(file_dir + file, force=True)

        if file[0:2] == 'CT':

            anon_d_data = anon_ct(d_data, pat_name, pat_id)
            new_filename = copy.deepcopy(file)
            new_filename = new_filename[:3] + pat_id + new_filename[12:]

            anon_dcm_write(anon_dir, pat_id, new_filename, anon_d_data)

        elif file[0:2] == 'RD':

            anon_d_data = anon_rd(d_data, pat_name, pat_id)
            new_filename = copy.deepcopy(file)
            new_filename = new_filename[:3] + pat_id + new_filename[12:]

            anon_dcm_write(anon_dir, pat_id, new_filename, anon_d_data)

        elif file[0:2] == 'RS':

            anon_d_data = anon_rs(d_data, pat_name, pat_id)
            new_filename = copy.deepcopy(file)
            new_filename = new_filename[:3] + pat_id + new_filename[12:]

            anon_dcm_write(anon_dir, pat_id, new_filename, anon_d_data)

        elif file[0:2] == 'RN':

            anon_d_data = anon_rn(d_data, pat_name, pat_id)

            new_filename = copy.deepcopy(file)
            new_filename = new_filename[:3] + pat_id + new_filename[12:]

            anon_dcm_write(anon_dir, pat_id, new_filename, anon_d_data)

        else:
            print(file, ' is not a recognised dicom file type and has not been anonymised')
