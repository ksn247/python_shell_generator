import os
import glob


def shell_script_generator(file):
    sftp_script_file = os.path.join("shell_script", file.split('.')[0] + ".ksh")

    with open(sftp_script_file, 'w') as fout:
        with open(r'template\sftp.txt', 'r') as fin:
            for line in fin:
                if line.startswith("source_file"):
                    line = "source_file=/opt/test/" + file + "\n"
                if line.startswith("dest_file"):
                   line = "dest_file=" + "new_" + file + "\n"

                fout.writelines(line)

        fin.close()
    fout.close()


def main():
    file_path = r"sftp_files"
    for fl in glob.glob(os.path.join(file_path, "*.txt")):
        file = fl.split('\\')[-1]
        print(file)
        shell_script_generator(file)


if __name__ == '__main__':
    main()
