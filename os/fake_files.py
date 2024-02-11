from time import time


MIN_FILES = 1
MAX_FILES = 100

MIN_SIZE_MB = 1
MAX_SIZE_MB = 10240


totalSizeMB = -1

while True:
    try:
        totalSizeMB = float(input('- File size (megabytes): '))
    except ValueError:
        print(f'x Enter a megabyte value between {MIN_SIZE_MB}mb and {MAX_SIZE_MB}mb!\n')
        continue

    if not (MIN_SIZE_MB <= totalSizeMB <= MAX_SIZE_MB):
        print(f'x Enter a megabyte value between {MIN_SIZE_MB}mb and {MAX_SIZE_MB}mb!\n')
        continue

    print(f'> All files together will occupy {totalSizeMB}mb\n')
    break


filesCount = -1

while True:
    try:
        filesCount = int(input('- Amount of files: '))
    except ValueError:
        print(f'x Enter a number of files between {MIN_FILES} and {MAX_FILES} (only integers)!\n')
        continue

    if not (MIN_FILES <= filesCount <= MAX_FILES):
        print(f'x Enter a number of files between {MIN_FILES} and {MAX_FILES} (only integers)!\n')
        continue

    print(f'> {filesCount} files will be created and each file will occupy {totalSizeMB / filesCount}mb\n')
    break


destinyPath = input('- Destiny path: ')

character = 'A'
characterBytes = 1

bytesPerFile = ((totalSizeMB * 1024 * 1024) / characterBytes)
charactersPerFile = round(bytesPerFile / filesCount)

print('> Creating files...')

for i in range(1, filesCount + 1):
    begin = time()

    with open(f'{destinyPath}/fake_file_{time()}_{i}', 'a+') as file:
        file.write(character * charactersPerFile)

    print(f'File {i} created ({round(time() - begin, 2)}s).')
