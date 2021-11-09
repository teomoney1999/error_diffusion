import cv2
from application.algo.error_diffusion import ErrorDiffusion

result_dir = "../../results"

def get_img_info(file_dir=None, f=None): 
    if file_dir is None: 
        return None
    
    Image = cv2.imread(file_dir)

    GrayImage = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)

    Height = GrayImage.shape[0]
    Width = GrayImage.shape[1]

    diffuser = ErrorDiffusion(GrayImage, f, Height, Width)

    return diffuser

def one_way(file_dir=None, f=None): 
    if file_dir is None or f is None: 
        return None

    diffuser = get_img_info(file_dir, f)

    diffusedImage = diffuser.one_way()

    return diffusedImage


def floyd_steinberg_way(file_dir=None, f=None): 
    if file_dir is None or f is None: 
        return None

    diffuser = get_img_info(file_dir, f)

    diffusedImage = diffuser.floyd_steinberg_way()

    return diffusedImage

def from_bell_lab_way(file_dir=None, f=None): 
    if file_dir is None or f is None: 
        return None

    diffuser = get_img_info(file_dir, f)

    diffusedImage = diffuser.from_bell_lab_way()

    return diffusedImage
