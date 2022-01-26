import glob

from Detector import detect_people


def get_photo_paths():
    photos_path = []
    for img in glob.glob("photos/*.jpg"):
        photos_path.append(img)
    return photos_path


if __name__ == '__main__':
    for path in get_photo_paths():
        detect_people(path)
