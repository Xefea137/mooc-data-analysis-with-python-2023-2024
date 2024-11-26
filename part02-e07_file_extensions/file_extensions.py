#!/usr/bin/env python3
def file_extensions(filename):
    filename_list = []
    filename_dict = {}
    with open(filename) as f:
        for line in f:
            if '.' not in line.strip():
                filename_list.append(line.strip())
            else:
                parts = line.strip().split('.')
                if parts[-1] in filename_dict:
                    filename_dict[parts[-1]].append(line.strip())
                else:
                    filename_dict[parts[-1]] = [line.strip()]
    
    return (filename_list, filename_dict)

def main():
    result = file_extensions('src\\filenames.txt')
    print(f"{len(result[0])} files with no extension")
    for key, value in result[1].items():
        print(key, len(value))

if __name__ == "__main__":
    main()