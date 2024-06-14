import os
import shutil
import imaging_classifying_rules


def filter_eidon_files(file, outputfolder):

    filename = file.split("/")[-1]
    rule = imaging_classifying_rules.find_rule(file)
    b = imaging_classifying_rules.extract_dicom_entry(file)
    laterality = b.laterality
    uid = b.sopinstanceuid
    patientid = b.patientid
    rows = b.rows
    columns = b.columns
    seriesuid = b.seriesuid
    error = b.error
    name = b.name

    original_path = file
    output_path = f"{outputfolder}/{rule}/{rule}_{filename}"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    shutil.copyfile(original_path, output_path)

    dic = {
        "Rule": rule,
        "PatientID": patientid,
        "PatientName": name,
        "Laterality": laterality,
        "Rows": rows,
        "Columns": columns,
        "SOPInstanceuid": uid,
        "SeriesInstanceuid": seriesuid,
        "Filename": filename,
        "Path": file,
        "Error": error,
    }
    print(dic)
    return dic
