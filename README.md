# VIBRATON ANALYSIS USING ADXL345

## About Project

<p align="justify">All rotating machines produce vibrations that are a function of the machine dynamics, such as
the alignment and balance of the rotating parts. Measuring the amplitude of vibration at certain
frequencies can provide valuable information about the accuracy of shaft alignment and balance,
the condition of bearings or gears, and the effect on the machine due to resonance from
the housings, piping and other structures. Vibration measurement is an effective, non-intrusive
method to monitor machine condition during start-ups, shutdowns and normal operation. Vibration
analysis is used primarily on rotating equipment such as steam and gas turbines, pumps,
motors, compressors, paper machines, rolling mills, machine tools and gearboxes. A major
advantage is that vibration analysis can identify developing problems before they become too
serious and cause unscheduled downtime. This can be achieved by conducting regular monitoring
of machine vibrations either on continuous basis or at scheduled intervals. Regular
vibration monitoring can detect deteriorating or defective bearings, mechanical looseness and
worn or broken gears. Vibration analysis can also detect misalignment and unbalance before
these conditions result in bearing or shaft deterioration. Trending vibration levels can identify
poor maintenance practices, such as improper bearing installation and replacement, inaccurate
shaft alignment or imprecise rotor balancing.</p>

## Components Required
1. Raspberry Pi 3 Model B
2. Accelerometer ADXL345
3. 5v-2A power supply for Raspberry Pi


## Block Diagram

<p align="center">
  <img src="https://user-images.githubusercontent.com/30443054/42444876-ed620f2c-838e-11e8-8b3e-44d269cf327a.png"/></p>
  
  
## Connections

|Raspberry Pi|ADXL345|
|---|---|
|Pin 1 - 3v3|Vcc|
|Pin 3 - SDA1 I2C|SDA|
|Pin 5 - SCL1 I2C|SCL|
|Pin 9 - Ground|GND|


