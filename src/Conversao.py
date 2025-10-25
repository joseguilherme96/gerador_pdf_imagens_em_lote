class Conversao:

    def convert_mm_to_pixel(mm):

        return int((mm * 96) / 25.4)
    
    def convert_pixel_to_mm(pixel):

        return int((pixel / 96) * 25.4)