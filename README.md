# Clock Aligned ⏰

A simulation application that finds the exact moments when all three clock hands (hour, minute, and second) align on a straight 180° line.

## Overview

This simulation demonstrates a fascinating mathematical problem: determining when the hour, minute, and second hands of a clock are perfectly aligned (either pointing in the same direction or in opposite directions on a straight line). The application provides millisecond precision tracking to identify these rare alignment events.

## Features

- **Real-time Clock Simulation**: Visual analog clock with smooth hand movements
- **Millisecond Precision**: Time tracking accurate to 1 millisecond
- **Alignment Detection**: Automatically detects when all three hands align within 1° tolerance
- **Variable Speed Control**: Speed up the simulation from 1x to 1000x for faster analysis
- **Alignment Logging**: Records all alignment events with exact timestamps and hand angles
- **Two Versions**: HTML (web-based) and Python (desktop) implementations

## Quick Start

### HTML Version (Recommended - Fastest & Easiest)

1. Clone this repository:
```bash
git clone https://github.com/solomonbm/Clock-aligned.git
cd Clock-aligned
```

2. Open the HTML file in your browser:
```bash
# On macOS
open clock_alignment.html

# On Linux
xdg-open clock_alignment.html

# On Windows
start clock_alignment.html
```

Or simply double-click `clock_alignment.html` in your file explorer.

**No installation required!** Works in any modern web browser (Chrome, Firefox, Safari, Edge).

### Python Version (Desktop Application)

**Requirements:**
- Python 3.6 or higher
- tkinter (usually included with Python)

**Installation & Usage:**
```bash
git clone https://github.com/solomonbm/Clock-aligned.git
cd Clock-aligned
python clock_alignment.py
```

## Usage

1. **Start**: Click the "▶ Start" button to begin the simulation
2. **Adjust Speed**: Use the speed slider to run faster (100x-1000x recommended for quick results)
3. **Stop**: Click "⏸ Stop" to pause the simulation
4. **Reset**: Click "↻ Reset" to return the clock to 0:00:00.000
5. **Clear Log**: Click "🗑 Clear Log" to clear the alignment history

The simulation will automatically detect and log alignment events, showing:
- Sequential alignment number
- Exact timestamp (H:MM:SS.mmm)
- Precise angles of each hand at the moment of alignment

## How It Works

### Hand Movement

Each clock hand moves at a different angular velocity:
- **Second hand**: 6° per second (360° in 60 seconds)
- **Minute hand**: 0.1° per second (360° in 3600 seconds)
- **Hour hand**: 0.00833...° per second (360° in 43200 seconds)

### Alignment Detection

The algorithm checks if all three hands form a straight line by verifying that:
1. All three angles are within 1° of each other (pointing in the same direction), OR
2. Two hands are within 1° of each other and the third is within 1° of being 180° opposite

### Mathematical Background

In a 12-hour period, the hands of a clock align multiple times. This occurs when the relative positions of the hands satisfy specific angular relationships. The exact moments can be calculated using modular arithmetic and angular velocity ratios.

## Expected Results

When running the simulation, you should observe alignments at various intervals. The first non-trivial alignment typically occurs around **65-66 minutes** into the simulation.

Common alignment patterns occur approximately every **~65 minutes**, though the exact timing varies due to the complex relationship between the three hands' velocities.

**Pro Tip**: Run at 500x-1000x speed to quickly scan through the 12-hour period and find all alignment moments!

## Technical Details

### HTML Version
- **Language**: JavaScript (ES6+)
- **Graphics**: HTML5 Canvas API
- **Precision**: Millisecond-level time tracking
- **Performance**: Optimized with requestAnimationFrame (~60 FPS)
- **Compatibility**: All modern browsers

### Python Version
- **Language**: Python 3
- **GUI Framework**: Tkinter
- **Graphics**: Canvas API for 2D drawing
- **Precision**: Millisecond-level time tracking
- **Simulation Speed**: 16ms frame updates (~60 FPS)

## Comparison: HTML vs Python

| Feature | HTML Version | Python Version |
|---------|-------------|----------------|
| Speed | ⚡⚡⚡ Fastest | ⚡⚡ Fast |
| Installation | None required | Python + tkinter |
| Platform | Any browser | Windows/Mac/Linux |
| Portability | Share a single file | Requires Python |
| Performance | Excellent | Good |

**Recommendation**: Use the HTML version for the best performance and ease of use. The Python version is great if you prefer a native desktop application.

## Files in This Repository

- `clock_alignment.html` - Web-based version (recommended)
- `clock_alignment.py` - Python desktop version
- `README.md` - This file

## Future Enhancements

Potential improvements for future versions:
- Export alignment data to CSV
- Visualization of alignment frequency over time
- Mathematical prediction of alignment moments
- Support for different clock configurations (24-hour, custom hand ratios)
- Statistical analysis of alignment intervals

## License

MIT License - feel free to use and modify as needed.

## Author

Original SimpleGUI version created for educational purposes. Modernized with HTML5/JavaScript and Tkinter for improved accessibility and functionality.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

**Note**: Both simulations run for a maximum of 12 hours (43,200,000 milliseconds) before automatically stopping.
