# Networked Measurement Instruments and Python

This repository contains a Python script that demonstrates remote control and data acquisition from networked laboratory instruments using the **VXI-11 protocol**.  
It enables communication with a signal generator and an oscilloscope over Ethernet, automated waveform retrieval, and graphical analysis.

---

## 1. Overview

The project illustrates a laboratory automation workflow where instruments are accessed and controlled remotely via TCP/IP.  
The script provides the following functionality:

- Establishes communication with VXI-11–compatible instruments.
- Reads configuration parameters from a signal generator.
- Acquires waveform data from an oscilloscope.
- Automatically plots and saves the captured waveforms in PDF format.
- Allows remote configuration of generator parameters.

This setup can be adapted for laboratory experiments, automated testing, or research data collection.

---

## 2. Repository Structure

```
networked-instruments-python-labs/
├── src/
│   └── instruments.py        # Main Python script
└── media/
    └── demo.mp4              # Optional demonstration video
```

---

## 3. Requirements and Dependencies

The code is compatible with **Python 3.x** and requires the following packages:

```
python-vxi11
numpy
matplotlib
si-prefix
```

To install all dependencies:

```bash
pip install -r requirements.txt
```

If a `requirements.txt` file is not yet present, the packages above can be installed individually.

---

## 4. Configuration

Update the IP addresses of your instruments in the script before execution:

```python
g = vxi11.Instrument('172.17.51.102')  # Signal generator
o = vxi11.Instrument('172.17.51.103')  # Oscilloscope
```

Ensure both devices are reachable from the host computer and support the VXI-11 protocol.  
It is recommended to verify communication using the `*IDN?` SCPI command prior to running automated measurements.

---

## 5. Usage

1. Clone this repository:

```bash
git clone https://github.com/YOUR_USERNAME/networked-instruments-python-labs.git
cd networked-instruments-python-labs
```

2. (Optional) Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

3. Install required packages:

```bash
pip install -r requirements.txt
```

4. Run the main script:

```bash
python src/instruments.py
```

The script will connect to the instruments, acquire waveform data, and save the generated plot in PDF format.

---

## 6. Demonstration Video

A short demonstration of the measurement and plotting process is available in the repository:

[View demonstration video](media/waveform-oscilloscope-20251010-143906.pdf)

---

## 7. Output

Each measurement produces a waveform plot saved as a timestamped PDF file, for example:

```
waveform-oscilloscope-20251020-153245.pdf
```

The plot includes both oscilloscope channels with voltage and time scaling extracted directly from instrument parameters.

---

## 8. Acknowledgements

This project was developed for Electronics education and remote instrument control and automated data acquisition using Python.

---

## 9. License

This project uses a dual-license model:

- **Source code** is licensed under the [MIT License](LICENSE).
- **Documentation, images, and other non-code content** are licensed under the [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).
