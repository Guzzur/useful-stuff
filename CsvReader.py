import os
import csv
import errno
import shutil


class CsvReader:

    def __init__(self):
        self.reader = None
        self.fn = None

    def read_csv_to_list(self, path_in, fn):
        self.fn = path_in + "\\" + fn

        buff = []

        with open(self.fn, 'rb') as f:
            self.reader = csv.reader(f)
            for row in self.reader:
                print "\t" + str(row)
                buff.append(row)

        return buff

    def create_pattern(self, buff):
        # add pattern creation logic
        return buff

    def write_csv_from_list(self, path_out, fn, buff):
        self.fn = path_out + "\\" + fn

        with open(self.fn, 'wb') as f:
            writer = csv.writer(f)
            writer.writerows(buff)


if __name__ == '__main__':
    print "Enter full path to csv input files dir: "

    path_in = r"C:\PythonProjects\CsvReader\in"
    print path_in
    # path_in = raw_input()

    print "Enter full path to output: "

    path_out = r"C:\PythonProjects\CsvReader\out"
    print path_out
    # path_out = raw_input()

    # Change path to the input directory
    if os.path.exists(path_in):
        os.chdir(path_in)
    else:
        print "Input path " + path_in + " does not exists. Exiting..."
        exit(1)

    # Create output directory
    try:
        os.makedirs(path_out)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path_out):
            for the_file in os.listdir(path_out):
                file_path = os.path.join(path_out, the_file)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print(e)
        else:
            print "Cannot create output dir " + path_out + ". Exiting..."
            exit(1)

    csvReader = CsvReader()

    included_extensions = ['csv']
    file_names = [fn for fn in os.listdir(".") if any(fn.endswith(ext) for ext in included_extensions)]

    for fn in file_names:
        print "Processing " + path_in + "\\" + fn + " into " + path_out + "\\" + fn
        buff = csvReader.read_csv_to_list(path_in, fn)
        buff = csvReader.create_pattern(buff)
        csvReader.write_csv_from_list(path_out, fn, buff)
