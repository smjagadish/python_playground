import re
import importlib.resources


def calc():
    with importlib.resources.open_text("org", "data.txt") as f:
        """
                alternative way of opening considering open_text is deprecated
                p = importlib.resources.files('package').joinpath('file').open('r') as f
                another option
                with importlib.resources.as_file(
    importlib.resources.files(package_name).joinpath(resource_name)
) as temp_file_path:
    with open(temp_file_path, 'r', newline='') as f:
        for line in csv.DictReader(f):
            print(line)
                """
        print(f.read())
        content = f.read()
        int_list = list()
        count = 0
        match = re.findall(r"[0-9]+", content, re.DOTALL)
        ss = sum([int(w) for w in match])
        print(ss)
        if match:
            for word in match:
                count = count + int(word)
        print(f"sum is:{count}")


if __name__ == "__main__":
    calc()
