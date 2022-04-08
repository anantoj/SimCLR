import glob
import PIL.Image as Image


class ModifiedDataset:
    def __init__(self, folder_path, transforms):
        self.images = glob.glob(folder_path + "/*")
        self.transforms = transforms

    def __getitem__(self, idx):
        image_path = self.images[idx]
        img = Image.open(image_path)
        data = self.transforms(img)
        return data

    def __len__(self):
        return len(self.images)
