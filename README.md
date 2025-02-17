# HexadeciPad

Welcome to the HexadeciPad! This README provides an overview of the project, including screenshots, a Bill of Materials (BOM), and additional resources to help you understand and contribute to the project.

## Overview

The HexadeciPad is a custom macropad designed as part of the Hackpad limited-time You Ship, We Ship (YSWS) event. I decided to make this Hackpad after realising that my keyboard media controls are kinda trash.

I spent ages trying to create the firmware after not knowing what I was doing. Finally after 20 hours of messing around i ahave finished my Hackpad. The HexadeciPad has 16 total inputs (2x encoder and 14x chery mx switches)

My next steps are probably to create a GUI and button editor app to make it easy to assign custom commands.

## 3D Model

![3D Model](https://viewscreen.githubusercontent.com/view/solid?url=https%3a%2f%2fraw.githubusercontent.com%2fskalnik%2fsecret-bear-clip%2fmaster%2fstl%2fclip.stl)

## Screenshots

### Overall Hackpad
![Overall Hackpad](images/overall_hackpad.png)

### Schematic
![Schematic](images/schematic.png)

### PCB
![PCB](images/pcb.png)


## Bill of Materials (BOM)

| Part Number                | Description                                      | Quantity |
|----------------------------|--------------------------------------------------|----------|
| SK6812MINI                 | Addressable RGB LED                              | 2        |
| R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal | Resistor, Axial, THT, Horizontal | 2        |
| RotaryEncoder_Alps_EC11E-Switch_Vertical_H20mm | Rotary Encoder with Switch | 2        |
| SW_Cherry_MX_1.00u_PCB     | Cherry MX keyswitch, 1.00u, PCB mount             | 14       |
| XIAO-RP2040-DIP            | Seeed Studio XIAO RP2040                         | 1        |
| MCP23017_SO                | I2C I/O Expander                                 | 1        |


## License

This project is licensed under the MIT License. See the [`LICENSE`](LICENSE ) file for details.