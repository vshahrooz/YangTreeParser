



import os
import subprocess

# Replace this with your YANG filename (must be in the same folder or full path)
YANG_FILE = r"\public-master\release\models\interfaces\openconfig-interfaces.yang"

def run_pyang_tree():
    """
    Run pyang -f tree on the YANG file and return the output as a string.
    If error occurs, print error and return None.
    """
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        cmd = [
            "pyang",
            "-f", "tree",
            "-p", script_dir,
            os.path.join(script_dir, YANG_FILE)
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print("❌ pyang error or missing module dependencies:")
            print(result.stderr)
            return None
        return result.stdout
    except FileNotFoundError:
        print("❌ pyang is not installed or not found in PATH.")
        return None

def parse_tree_and_build_paths(tree_str):
    """
    Parse pyang tree output lines and build all paths (like XPath) of leaves and containers.
    Returns a list of string paths.
    """
    lines = tree_str.splitlines()
    paths = []
    stack = []  

    for line in lines:
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip(' '))
        parts = line.strip().split()
        if len(parts) < 2:
            continue
        node_name = parts[1]

        if '*' in node_name:
            node_name = node_name.replace('*', '')
        if node_name.endswith('?'):
            node_name = node_name[:-1]

        level = indent // 3

        while stack and stack[-1][0] >= level:
            stack.pop()

        stack.append((level, node_name))

        path_parts = [n for _, n in stack]
        path_str = "/".join(path_parts)
        paths.append(path_str)

    return paths

def save_paths_to_file(paths, filename):
    """
    Save all generated paths line by line into a text file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        for p in paths:
            f.write(p + "\n")

def main():
    print("Running pyang tree...")
    tree_output = run_pyang_tree()
    if tree_output is None:
        return

    print("Parsing tree and building paths...")
    paths = parse_tree_and_build_paths(tree_output)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = "paths.txt"
    output_path = os.path.join(script_dir, output_file)

    save_paths_to_file(paths, output_path)

    print(f"✅ Paths saved to {output_path}")

if __name__ == "__main__":
    main()
