import pathlib

from ttkbootstrap import PhotoImage


def icon_loader(path_to_folder, pattern="*.png"):
    loaded_images = []

    for image_path in pathlib.Path(path_to_folder).glob(pattern):
        image = PhotoImage(name=image_path.stem, file=str(image_path))
        loaded_images.append(image)

    return loaded_images
