# in this script any url can be used to create a basic qr code,
# using Segno library Seedocumentation -> https://segno.readthedocs.io/en/latest/ 
# Created by: Stephen Kerr - 20/09/25


# basic_qrcode.py

import segno

qrcode = segno.make_qr("https://segno.readthedocs.io/en/latest/")

qrcode_rotated = qrcode.to_pil().rotate(45)

qrcode_rotated.save(
    "rotated_qrcode.png",
    scale=5,
    border= 4,#
    light = "white",
    dark = "darkblue",
    quiet_zone = "black",
    data_dark = "pink",
    data_light = "green" 
    )

qrcode.save(
    "basic_qrcode.png",
    scale=5,
    border= 4,#
    light = "white",
    dark = "darkblue",
    quiet_zone = "black",
    data_dark = "pink",
    data_light = "green"
    )