import sys
import shutil
from pathlib import Path
from normalize import normalize

path = None

try:
    path = Path(sys.argv[1])
    print('You enter valid path')
except IndexError:
    print("Please enter valid path")

extensions = {
    "images": ['.jpeg', '.png', '.jpg', '.svg'],
    "video": ['.avi', '.mp4', '.mov', '.mkv'],
    "documents": ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'],
    "music": ['.mp3', '.ogg', '.wav', '.amr'],
    "archives": ['.zip', '.gz', '.tar'],
    "unknown": [""]
}

def create_folders(path: Path):
    for name in extensions.keys():
        if not path.joinpath(name).exists():
            path.joinpath(name).mkdir()


def sort_files(path: Path):
    
    known_extensions = []
    unknow_extensions = []

    for file in path.glob("**/*"):
        new_name = file.with_name(normalize(file.stem)).with_suffix(file.suffix)
        if file.is_file():
                if file.suffix in extensions["images"]:
                    file.rename(new_name)
                    new_name.replace(path / "images" / new_name.name)
                    known_extensions.append(file.suffix)

                elif file.suffix in extensions["video"]:
                    file.rename(new_name)
                    new_name.replace(path / "video" / new_name.name)
                    known_extensions.append(file.suffix)
                    

                elif file.suffix in extensions["documents"]:
                    file.rename(new_name)
                    new_name.replace(path / "documents" / new_name.name)
                    known_extensions.append(file.suffix)

                elif file.suffix in extensions["music"]:
                    file.rename(new_name)
                    new_name.replace(path / "music" / new_name.name)
                    known_extensions.append(file.suffix)

                elif file.suffix in extensions["archives"]:
                    file.rename(new_name)
                    new_name.replace(path / "archives" / new_name.name)
                    known_extensions.append(file.suffix)

                else:
                    file.rename(new_name)
                    new_name.replace(path / "unknown" / new_name.name)
                    unknow_extensions.append(file.suffix)

    return known_extensions, unknow_extensions


def delete_folders(path: Path):
    for f in list(path.glob("*/**"))[::-1]:
        if f.is_dir:
            try:
                f.rmdir()
            except OSError:
                pass


def unpack_archives(path: Path):
    path_folder = path / "archives"
    for f in path_folder.iterdir():
        shutil.unpack_archive(f.name)
        
def main():
    create_folders(path)
    sort_files(path)
    delete_folders(path)

if __name__ == "__main__":
    main()