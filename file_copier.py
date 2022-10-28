import os
import shutil


def main(from_dir: str, to_dir: str):
    chk_strs = []

    with open('copy_list.txt') as f:
        for row in f:
            s = row.replace('\r', '')
            s = s.replace('\n', '')
            s = s.lower()

            chk_strs.append('[' + s + ']')
            chk_strs.append('[' + s + ',')
            chk_strs.append(', ' + s + ',')
            chk_strs.append(', ' + s + ']')

    file_nms = os.listdir(from_dir)

    for file_nm in file_nms:
        lcase_f_nm = file_nm.lower()
        from_full_path = os.path.join(from_dir, file_nm)

        if not os.path.isfile(from_full_path):
            continue

        to_full_path = os.path.join(to_dir, file_nm)
        need_to_copy = False

        for chk_str in chk_strs:
            if 0 <= lcase_f_nm.find(chk_str):
                need_to_copy = True
                break

        if not need_to_copy:
            continue

        if (not os.path.exists(to_full_path)) or (os.path.getsize(to_full_path) < os.path.getsize(from_full_path)):
            shutil.copy2(from_full_path, to_full_path)
            print('{0} is copied'.format(file_nm))


if '__main__' == __name__:
    FROM_PATH = '[FolderPath]'
    TO_PATH = '[FolderPath]'

    print('START !!')
    main(FROM_PATH, TO_PATH)
    print('DONE !!')

