from pathlib import Path


def generate_blank_files_lf(output_dir: str):
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    for i in range(1, 26):
        Path(f"{output_dir}/day_{i:02d}_test_01.txt").touch()
        Path(f"{output_dir}/day_{i:02d}_answer.txt").touch()

