import pygame
import random
import time
import numpy as np
from pygame import gfxdraw

# Inisialisasi Pygame
pygame.init()

# Konstanta layar
WIDTH, HEIGHT = 1024, 768
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Symphony of Logic: Musical Sorting Visualization")

# Warna dengan palet yang lebih elegan
BACKGROUND = (15, 15, 35)
GRADIENT_TOP = (142, 68, 173)    # Ungu elegan
GRADIENT_BOTTOM = (41, 128, 185)  # Biru tenang
WHITE = (255, 255, 255)
HIGHLIGHT = (255, 236, 179)      # Highlight kuning lembut

# Piano notes (frekuensi untuk tangga nada mayor C)
PIANO_NOTES = [
    261.63,  # C4
    293.66,  # D4
    329.63,  # E4
    349.23,  # F4
    392.00,  # G4
    440.00,  # A4
    493.88,  # B4
    523.25   # C5
]

# Inisialisasi mixer audio dengan kualitas tinggi
pygame.mixer.init(44100, -16, 2, 512)

# Data untuk sorting
N = 60
data = [random.randint(50, HEIGHT - 100) for _ in range(N)]

def create_piano_sound(frequency, duration=0.1):
    """Membuat suara piano dengan envelope ADSR."""
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    
    # Gelombang dasar (sine wave + square wave untuk karakter piano)
    wave = 0.7 * np.sin(2 * np.pi * frequency * t) + 0.3 * np.sign(np.sin(2 * np.pi * frequency * t))
    
    # Envelope ADSR (Attack, Decay, Sustain, Release)
    attack = 0.01
    decay = 0.05
    sustain_level = 0.7
    release = 0.05
    
    # Membuat envelope
    envelope = np.ones_like(t)
    attack_samples = int(attack * sample_rate)
    decay_samples = int(decay * sample_rate)
    release_samples = int(release * sample_rate)
    
    envelope[:attack_samples] = np.linspace(0, 1, attack_samples)
    envelope[attack_samples:attack_samples + decay_samples] = np.linspace(1, sustain_level, decay_samples)
    envelope[-release_samples:] = np.linspace(sustain_level, 0, release_samples)
    
    # Aplikasikan envelope
    wave = wave * envelope
    
    # Normalisasi dan konversi ke 16-bit integer
    wave = np.int16(wave * 32767)
    stereo_wave = np.column_stack((wave, wave))
    
    return pygame.sndarray.make_sound(stereo_wave)

def get_gradient_color(height, max_height):
    """Membuat gradien warna berdasarkan tinggi bar."""
    factor = height / max_height
    r = int(GRADIENT_BOTTOM[0] + (GRADIENT_TOP[0] - GRADIENT_BOTTOM[0]) * factor)
    g = int(GRADIENT_BOTTOM[1] + (GRADIENT_TOP[1] - GRADIENT_BOTTOM[1]) * factor)
    b = int(GRADIENT_BOTTOM[2] + (GRADIENT_TOP[2] - GRADIENT_BOTTOM[2]) * factor)
    return (r, g, b)

def draw_bar(surface, x, y, width, height, color):
    """Menggambar bar dengan efek gradien dan pencahayaan."""
    # Gambar bar utama dengan gradien
    for h in range(height):
        current_color = get_gradient_color(h, height)
        gfxdraw.hline(surface, x, x + width - 1, y - h, current_color)
    
    # Tambah efek highlight di sisi kiri
    gfxdraw.vline(surface, x, y - height, y, (*color, 200))

def draw_data(data, highlight_indices=None):
    """Menggambar data dengan efek visual yang ditingkatkan."""
    SCREEN.fill(BACKGROUND)
    
    bar_width = (WIDTH - 100) // len(data)
    margin = 50  # Margin dari tepi layar
    
    for i, val in enumerate(data):
        x = margin + i * bar_width
        y = HEIGHT - margin
        color = HIGHLIGHT if highlight_indices and i in highlight_indices else WHITE
        draw_bar(SCREEN, x, y, bar_width - 2, val, color)
    
    pygame.display.flip()

def musical_bubble_sort(data):
    """Bubble sort dengan efek musik piano."""
    n = len(data)
    for i in range(n):
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                # Tukar elemen
                data[j], data[j + 1] = data[j + 1], data[j]
                
                # Mainkan nada piano
                note_index = int((data[j] / HEIGHT) * len(PIANO_NOTES))
                note_index = min(note_index, len(PIANO_NOTES) - 1)
                sound = create_piano_sound(PIANO_NOTES[note_index])
                sound.play()
                
                # Visualisasi
                draw_data(data, {j, j + 1})
                time.sleep(0.05)
    
    # Mainkan arpeggio saat selesai
    for note in PIANO_NOTES:
        sound = create_piano_sound(note, 0.15)
        sound.play()
        time.sleep(0.1)

def main():
    running = True
    sorting = False
    clock = pygame.time.Clock()
    
    while running:
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not sorting:
                    sorting = True
                    musical_bubble_sort(data.copy())
                    sorting = False
                elif event.key == pygame.K_r:
                    # Reset data
                    data[:] = [random.randint(50, HEIGHT - 100) for _ in range(N)]
        
        draw_data(data)
    
    pygame.quit()

if __name__ == "__main__":
    main()
