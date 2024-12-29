import os
from converter import ImageConverter

def main():
   
    input_folder = os.path.join("images")  
    output_folder = os.path.join("output")  


    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".heic"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.jpeg")

            print(f"Converting: {input_path} -> {output_path}")
            converter = ImageConverter(input_path, output_path, quality=100)  
            converter.convert()

if __name__ == "__main__":
    main()
