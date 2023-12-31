import argparse
from . import jsondatafaker

def main():
    parser = argparse.ArgumentParser(description=get_description())
    parser.add_argument('--config', required=True, help='Config yaml file path')
    parser.add_argument('--target', required=False, help='Target folder/file')

    args = parser.parse_args()

    config_file_path = None
    target_file_path = None

    if args.config is not None:
        config_file_path = args.config
    else:
        print("Missing --config parameter. Use --help for more detail.")
        return

    if args.target is not None:
        target_file_path = args.target
    else:
        target_file_path = "."  


    if isinstance(config_file_path, str):
        jsondatafaker.to_json(config_file_path, target_file_path)
    else:
        print("Wrong paramater(s)")
        print(get_description())

def get_description():
    return "more detail: https://github.com/necatiarslan/json-datafaker/blob/main/README.md"

if __name__ == '__main__':
    main()



