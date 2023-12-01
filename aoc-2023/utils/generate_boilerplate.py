from pathlib import Path


def generate_blank_files_lf(output_dir: str):
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    for i in range(1, 26):
        Path(f"{output_dir}/day_{i:02d}").mkdir(parents=True, exist_ok=True)
        Path(f"{output_dir}/day_{i:02d}/day_{i:02d}_test_01.txt").touch()
        Path(f"{output_dir}/day_{i:02d}/day_{i:02d}_test_02.txt").touch()
        Path(f"{output_dir}/day_{i:02d}/day_{i:02d}_challenge.txt").touch()


def generate_python_src(output_dir: str):
    for i in range(2, 26):
        Path(f"{output_dir}/day_{i:02d}.py").touch()
        with open(f"{output_dir}/day_{i:02d}.py", "w", encoding="utf-8") as f:
            f.write(f"""\"""Day {i:02d} AoC 2023\"\"\"\n\n\n\
count = 0

def get_answer(challenge: str) -> int:
    return count\n""")

