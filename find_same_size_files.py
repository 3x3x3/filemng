import os


def main(path: str):
    file_nms = os.listdir(path)
    file_infos: dict = {}

    for file_nm in file_nms:
        file_size = os.path.getsize(os.path.join(path, file_nm))

        if file_size not in file_infos:
            file_infos[file_size] = list()

        file_infos[file_size].append(file_nm)

    idx = 0

    for file_size, file_nms in file_infos.items():
        if 1 < len(file_nms):
            print(f'idx: {idx}, size: {round(file_size/1024)}, nms: {file_nms}')
            idx = idx + 1


if '__main__' == __name__:
    path_dir = '[FolderPath]'

    main(path_dir)
