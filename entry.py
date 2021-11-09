import cv2
from application.examples import floyd_steiberg_dithering_2
from application.controllers.error_diffusion_func import one_way, from_bell_lab_way, floyd_steinberg_way

ui_content = {
    "mode": {
        "input": "Choose the mode that you want (in number): ", 
    },
    "file_dir": {
        "input": "Copy the directory of your image here: ", 
    },
    "result_image_name": {
        "input": "Copy the directory of your image here: ",
    }, 
    "f": {
        "input": "Choose your f: "
    },
    "not_valid": "Please provide valid info!", 
    "result": "Done! Get your result at results file. Have fun!"
}
def print_menu(): 
    print("Error Diffusion Tools")
    print(" ---------------- MENU ----------------")
    print(" 1. One-way error diffusion.")
    print(" 2. Floyd-Steiberg error diffusion.")
    print(" 3. From Bell Lab error diffusion.")
    print(" 4. Menu")
    print(" ---Press Q to exit---")

def check_valid(key=None, value=None):
    while (value is None) or (value == ""): 
        print(ui_content["not_valid"])
        value = input(ui_content[key]["input"])
    return value


def manager(): 
    print_menu()
    while 1: 
        mode = input(ui_content["mode"]["input"])
        
        # Endpoint
        if mode == "q" or mode == "Q":
            print("Good bye!")
            break
        

        mode = check_valid("mode", mode)
        # while mode == "": 
        #     print("Please provide valid info!")
        #     mode = input("Choose the mode that you want (in number): ")

        file_dir = input(ui_content["file_dir"]["input"]) 
        file_dir = check_valid("file_dir", file_dir)

        result_image_name = input(ui_content["result_image_name"]["input"])
        result_image_name = check_valid("result_image_name", result_image_name)
        
        f = input(ui_content["f"]["input"])
        f = check_valid("f", f)

        diffusedImage = None
        if mode == "1": 
            diffusedImage = one_way(file_dir, int(f))
            #TODO add choose type of file
        elif mode == "2": 
            diffusedImage = floyd_steinberg_way(file_dir, int(f))
        elif mode == "3": 
            diffusedImage = from_bell_lab_way(file_dir, int(f))    
        elif mode == "4": 
            continue
        else: 
            print(f"{mode} is not an option!")
        
        cv2.imwrite(f"./results/{result_image_name}.png", diffusedImage)
        print(ui_content["result"])

if __name__ == '__main__':
    manager()
