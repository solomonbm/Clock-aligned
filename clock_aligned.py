import tkinter as tk
from tkinter import ttk
import math
import time

class ClockAlignmentFinder:
    def __init__(self, root):
        self.root = root
        self.root.title("Clock Alignment Finder")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')
        
        # Time tracking (in milliseconds)
        self.milliseconds = 0
        self.is_running = False
        self.speed = 100
        self.alignment_count = 0
        self.last_alignment = -1000  # Prevent duplicate detections
        self.tolerance = 5.0  # Degrees tolerance for alignment
        
        # Create UI
        self.create_widgets()
        
        # Initial draw
        self.draw_clock()
        self.update_time_display()
        
    def create_widgets(self):
        # Main container
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title = tk.Label(main_frame, text="⏰ Clock Hand Alignment Finder", 
                        font=('Arial', 18, 'bold'), bg='#f0f0f0', fg='#333')
        title.pack(pady=(0, 20))
        
        # Content frame
        content_frame = tk.Frame(main_frame, bg='#f0f0f0')
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Left side - Clock
        left_frame = tk.Frame(content_frame, bg='#f0f0f0')
        left_frame.pack(side=tk.LEFT, padx=20)
        
        self.canvas = tk.Canvas(left_frame, width=350, height=350, 
                               bg='#f8f9fa', highlightthickness=2, 
                               highlightbackground='#667eea')
        self.canvas.pack()
        
        self.time_label = tk.Label(left_frame, text="0:00:00.000", 
                                   font=('Courier', 20, 'bold'), 
                                   bg='#f0f0f0', fg='#667eea')
        self.time_label.pack(pady=10)
        
        # Right side - Controls
        right_frame = tk.Frame(content_frame, bg='#f0f0f0')
        right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20)
        
        # Buttons
        btn_frame = tk.Frame(right_frame, bg='#f0f0f0')
        btn_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.start_btn = tk.Button(btn_frame, text="▶ Start", command=self.start,
                                   bg='#10b981', fg='white', font=('Arial', 12, 'bold'),
                                   width=12, height=2, cursor='hand2')
        self.start_btn.pack(pady=5)
        
        self.stop_btn = tk.Button(btn_frame, text="⏸ Stop", command=self.stop,
                                  bg='#ef4444', fg='white', font=('Arial', 12, 'bold'),
                                  width=12, height=2, cursor='hand2')
        self.stop_btn.pack(pady=5)
        
        self.reset_btn = tk.Button(btn_frame, text="↻ Reset", command=self.reset,
                                   bg='#667eea', fg='white', font=('Arial', 12, 'bold'),
                                   width=12, height=2, cursor='hand2')
        self.reset_btn.pack(pady=5)
        
        self.clear_btn = tk.Button(btn_frame, text="🗑 Clear Log", command=self.clear_alignments,
                                   bg='#f59e0b', fg='white', font=('Arial', 12, 'bold'),
                                   width=12, height=2, cursor='hand2')
        self.clear_btn.pack(pady=5)
        
        # Speed control
        speed_frame = tk.Frame(right_frame, bg='#f0f0f0')
        speed_frame.pack(fill=tk.X, pady=10)
        
        speed_label = tk.Label(speed_frame, text="Speed:", 
                              font=('Arial', 10), bg='#f0f0f0')
        speed_label.pack(side=tk.LEFT)
        
        self.speed_var = tk.IntVar(value=1)
        self.speed_value_label = tk.Label(speed_frame, text="1x", 
                                         font=('Arial', 10, 'bold'), bg='#f0f0f0')
        self.speed_value_label.pack(side=tk.LEFT, padx=5)
        
        self.speed_scale = tk.Scale(speed_frame, from_=100, to=1000, 
                                   orient=tk.HORIZONTAL, variable=self.speed_var,
                                   command=self.update_speed, bg='#f0f0f0')
        self.speed_scale.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        # Tolerance control (NEW)
        tolerance_frame = tk.Frame(right_frame, bg='#f0f0f0')
        tolerance_frame.pack(fill=tk.X, pady=10)
        
        tolerance_label = tk.Label(tolerance_frame, text="Tolerance:", 
                                  font=('Arial', 10), bg='#f0f0f0')
        tolerance_label.pack(side=tk.LEFT)
        
        self.tolerance_var = tk.DoubleVar(value=5.0)
        self.tolerance_value_label = tk.Label(tolerance_frame, text="5.0°", 
                                             font=('Arial', 10, 'bold'), bg='#f0f0f0')
        self.tolerance_value_label.pack(side=tk.LEFT, padx=5)
        
        self.tolerance_scale = tk.Scale(tolerance_frame, from_=0.5, to=15.0, 
                                       orient=tk.HORIZONTAL, variable=self.tolerance_var,
                                       command=self.update_tolerance, bg='#f0f0f0',
                                       resolution=0.1)
        self.tolerance_scale.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        # Alignments log
        log_label = tk.Label(right_frame, text="Alignment Log:", 
                            font=('Arial', 12, 'bold'), bg='#f0f0f0')
        log_label.pack(anchor=tk.W, pady=(10, 5))
        
        log_frame = tk.Frame(right_frame, bg='white', relief=tk.SUNKEN, bd=2)
        log_frame.pack(fill=tk.BOTH, expand=True)
        
        scrollbar = tk.Scrollbar(log_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.log_text = tk.Text(log_frame, height=10, font=('Courier', 9),
                               yscrollcommand=scrollbar.set, wrap=tk.WORD)
        self.log_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.log_text.yview)
        
        self.log_text.insert('1.0', 'Alignments will appear here...')
        self.log_text.config(state=tk.DISABLED)
        
        # Info
        info = tk.Label(main_frame, 
                       text="Finding moments when all three hands align on a 180° line",
                       font=('Arial', 9), bg='#f0f0f0', fg='#666')
        info.pack(pady=(10, 0))
        
    def format_time(self, ms):
        """Format milliseconds as H:MM:SS.mmm"""
        total_seconds = ms // 1000
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        millis = ms % 1000
        
        return f"{hours}:{minutes:02d}:{seconds:02d}.{millis:03d}"
    
    def get_angles(self, ms):
        """Calculate angles for each hand in degrees (0 = 12 o'clock)"""
        total_seconds = ms / 1000.0
        
        # Second hand: 360° per 60 seconds = 6°/second
        second_angle = (total_seconds % 60) * 6
        
        # Minute hand: 360° per 3600 seconds = 0.1°/second
        minute_angle = (total_seconds % 3600) / 60 * 6
        
        # Hour hand: 360° per 43200 seconds = 0.00833...°/second
        hour_angle = (total_seconds % 43200) / 120
        
        return second_angle, minute_angle, hour_angle
    
    def normalize_angle(self, angle):
        """Normalize angle to 0-360 range"""
        return angle % 360
    
    def are_aligned(self, a1, a2, a3, tolerance=1.0):
        """Check if three angles form a straight line (aligned or 180° apart)"""
        # Normalize angles
        angles = [self.normalize_angle(a) for a in [a1, a2, a3]]
        angles.sort()
        
        # Check if all three are close together (within tolerance)
        if angles[2] - angles[0] <= tolerance:
            return True
        
        # Check if they form a line with one angle ~180° from the others
        # Pattern 1: angles[0] and angles[1] close, angles[2] ~180° away
        if (abs(angles[1] - angles[0]) <= tolerance and 
            abs(angles[2] - angles[0] - 180) <= tolerance):
            return True
        
        # Pattern 2: angles[1] and angles[2] close, angles[0] ~180° away
        if (abs(angles[2] - angles[1]) <= tolerance and 
            abs(angles[1] - angles[0] - 180) <= tolerance):
            return True
        
        # Pattern 3: angles[0] and angles[2] close (wrapping around 360)
        if (abs(angles[2] - angles[0]) >= 360 - tolerance and 
            abs(angles[1] - angles[0] - 180) <= tolerance):
            return True
        
        return False
    
    def check_alignment(self):
        """Check if hands are currently aligned"""
        # Debounce: don't check too frequently
        if self.milliseconds - self.last_alignment < 100:
            return
        
        sec_angle, min_angle, hour_angle = self.get_angles(self.milliseconds)
        
        if self.are_aligned(sec_angle, min_angle, hour_angle, self.tolerance):
            self.last_alignment = self.milliseconds
            self.alignment_count += 1
            
            log_entry = (f"#{self.alignment_count}: {self.format_time(self.milliseconds)} "
                        f"(S:{sec_angle:.1f}° M:{min_angle:.1f}° H:{hour_angle:.1f}°)\n")
            
            self.log_text.config(state=tk.NORMAL)
            if 'will appear here' in self.log_text.get('1.0', tk.END):
                self.log_text.delete('1.0', tk.END)
            self.log_text.insert('1.0', log_entry)
            self.log_text.config(state=tk.DISABLED)
    
    def draw_clock(self):
        """Draw the clock face and hands"""
        self.canvas.delete('all')
        
        center_x = 175
        center_y = 175
        radius = 140
        
        # Draw clock circle
        self.canvas.create_oval(center_x - radius, center_y - radius,
                               center_x + radius, center_y + radius,
                               outline='#667eea', width=5)
        
        # Draw tick marks
        for i in range(60):
            angle = math.radians(i * 6 - 90)
            
            if i % 15 == 0:
                tick_length = 25
                tick_width = 4
            elif i % 5 == 0:
                tick_length = 18
                tick_width = 3
            else:
                tick_length = 10
                tick_width = 2
            
            x1 = center_x + math.cos(angle) * radius
            y1 = center_y + math.sin(angle) * radius
            x2 = center_x + math.cos(angle) * (radius - tick_length)
            y2 = center_y + math.sin(angle) * (radius - tick_length)
            
            self.canvas.create_line(x1, y1, x2, y2, 
                                   fill='#667eea', width=tick_width)
        
        # Get current angles
        sec_angle, min_angle, hour_angle = self.get_angles(self.milliseconds)
        
        # Draw hour hand
        self.draw_hand(hour_angle, 70, 8, '#333')
        
        # Draw minute hand
        self.draw_hand(min_angle, 100, 6, '#555')
        
        # Draw second hand
        self.draw_hand(sec_angle, 120, 3, '#ef4444')
        
        # Draw center pin
        self.canvas.create_oval(center_x - 8, center_y - 8,
                               center_x + 8, center_y + 8,
                               fill='#667eea', outline='#333', width=2)
    
    def draw_hand(self, angle_degrees, length, width, color):
        """Draw a clock hand"""
        center_x = 175
        center_y = 175
        angle = math.radians(angle_degrees - 90)
        
        end_x = center_x + math.cos(angle) * length
        end_y = center_y + math.sin(angle) * length
        
        self.canvas.create_line(center_x, center_y, end_x, end_y,
                               fill=color, width=width, capstyle=tk.ROUND)
    
    def update_time_display(self):
        """Update the time display label"""
        self.time_label.config(text=self.format_time(self.milliseconds))
    
    def update_speed(self, value):
        """Update speed multiplier"""
        self.speed = int(value)
        self.speed_value_label.config(text=f"{self.speed}x")
    
    def update_tolerance(self, value):
        """Update tolerance value (NEW)"""
        self.tolerance = float(value)
        self.tolerance_value_label.config(text=f"{self.tolerance:.1f}°")
    
    def animate(self):
        """Animation loop"""
        if not self.is_running:
            return
        
        # Increment by 100ms * speed
        self.milliseconds += 100 * self.speed
        
        # Stop after 12 hours
        if self.milliseconds >= 12 * 60 * 60 * 1000:
            self.stop()
            return
        
        self.draw_clock()
        self.check_alignment()
        self.update_time_display()
        
        # Schedule next frame (roughly 60 FPS)
        self.root.after(16, self.animate)
    
    def start(self):
        """Start the clock"""
        if not self.is_running:
            self.is_running = True
            self.animate()
    
    def stop(self):
        """Stop the clock"""
        self.is_running = False
    
    def reset(self):
        """Reset the clock to 0"""
        self.stop()
        self.milliseconds = 0
        self.draw_clock()
        self.update_time_display()
    
    def clear_alignments(self):
        """Clear the alignment log"""
        self.log_text.config(state=tk.NORMAL)
        self.log_text.delete('1.0', tk.END)
        self.log_text.insert('1.0', 'Alignments will appear here...')
        self.log_text.config(state=tk.DISABLED)
        self.alignment_count = 0
        self.last_alignment = -1000

if __name__ == "__main__":
    root = tk.Tk()
    app = ClockAlignmentFinder(root)
    root.mainloop()
