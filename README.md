# Clock Aligned ⏰

A Python application that simulates an analog clock and finds the exact moments when all three clock hands (hour, minute, and second) align on a straight 180° line.

## Overview

This simulation demonstrates a fascinating mathematical problem: determining when the hour, minute, and second hands of a clock are perfectly aligned (either pointing in the same direction or in opposite directions on a straight line). The application provides millisecond precision tracking to identify these rare alignment events.

## Features

- **Real-time Clock Simulation**: Visual analog clock with smooth hand movements
- **Millisecond Precision**: Time tracking accurate to 1 millisecond
- **Alignment Detection**: Automatically detects when all three hands align within 1° tolerance
- **Variable Speed Control**: Speed up the simulation from 1x to 100x for faster analysis
- **Alignment Logging**: Records all alignment events with exact timestamps and hand angles
- **Clean GUI**: Built with Tkinter for cross-platform compatibility

## Requirements

- Python 3.6 or higher
- tkinter (usually included with Python)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/clock-aligned.git
cd clock-aligned
```

2. Run the application:
```bash
python clock_alignment.py
```

## Usage

1. **Start**: Click the "▶ Start" button to begin the simulation
2. **Adjust Speed**: Use the speed slider to run faster (useful for finding alignments quickly)
3. **Stop**: Click "⏸ Stop" to pause the simulation
4. **Reset**: Click "↻ Reset" to return the clock to 0:00:00.000
5. **Clear Log**: Click "🗑 Clear Log" to clear the alignment history

The simulation will automatically detect and log alignment events in the right panel, showing:
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

When running the simulation for several hours, you should observe alignments at various intervals. The first non-trivial alignment typically occurs around **65-66 minutes** into the simulation.

Common alignment patterns occur approximately every **~65 minutes**, though the exact timing varies due to the complex relationship between the three hands' velocities.

## Technical Details

- **Language**: Python 3
- **GUI Framework**: Tkinter
- **Graphics**: Canvas API for 2D drawing
- **Precision**: Millisecond-level time tracking
- **Simulation Speed**: 16ms frame updates (~60 FPS)

## Future Enhancements

Potential improvements for future versions:
- Export alignment data to CSV
- Visualization of alignment frequency over time
- Mathematical prediction of alignment moments
- Support for different clock configurations (24-hour, custom hand ratios)

## License

MIT License - feel free to use and modify as needed.

## Author

Original SimpleGUI version created for educational purposes. Modernized with Tkinter for improved accessibility and functionality.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

**Note**: This simulation runs for a maximum of 12 hours (43,200,000 milliseconds) before automatically stopping.
