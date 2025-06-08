#!/usr/bin/env python3
"""
サンプル音響ファイル生成スクリプト

このスクリプトは、学習用のサンプル音響ファイルを生成します。
"""

import numpy as np
from pydub import AudioSegment
from pydub.generators import Sine, Square, Sawtooth, Triangle
import os

def create_sample_files():
    """サンプル音響ファイルを生成"""
    
    # ディレクトリが存在しない場合は作成
    os.makedirs('.', exist_ok=True)
    
    # 1. 純粋な正弦波（440Hz - A4音）
    sine_wave = Sine(440).to_audio_segment(duration=3000)  # 3秒
    sine_wave.export("sine_440hz.wav", format="wav")
    print("Created: sine_440hz.wav")
    
    # 2. 方形波
    square_wave = Square(440).to_audio_segment(duration=3000)
    square_wave.export("square_440hz.wav", format="wav")
    print("Created: square_440hz.wav")
    
    # 3. のこぎり波
    sawtooth_wave = Sawtooth(440).to_audio_segment(duration=3000)
    sawtooth_wave.export("sawtooth_440hz.wav", format="wav")
    print("Created: sawtooth_440hz.wav")
    
    # 4. 三角波
    triangle_wave = Triangle(440).to_audio_segment(duration=3000)
    triangle_wave.export("triangle_440hz.wav", format="wav")
    print("Created: triangle_440hz.wav")
    
    # 5. 和音（C Major - C, E, G）
    c_note = Sine(261.63).to_audio_segment(duration=4000)  # C4
    e_note = Sine(329.63).to_audio_segment(duration=4000)  # E4
    g_note = Sine(392.00).to_audio_segment(duration=4000)  # G4
    
    chord = c_note.overlay(e_note).overlay(g_note)
    chord = chord.fade_in(100).fade_out(500)
    chord.export("c_major_chord.wav", format="wav")
    print("Created: c_major_chord.wav")
    
    # 6. スケール（C Major Scale）
    notes = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88, 523.25]
    scale = AudioSegment.silent(duration=100)
    
    for freq in notes:
        note = Sine(freq).to_audio_segment(duration=500)
        note = note.fade_in(50).fade_out(100)
        scale += note + AudioSegment.silent(duration=100)
    
    scale.export("c_major_scale.wav", format="wav")
    print("Created: c_major_scale.wav")
    
    # 7. チャープ信号（周波数スイープ）
    # 手動でチャープ信号を生成
    sample_rate = 44100
    duration = 3.0
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    
    # 200Hzから2000Hzまでの線形チャープ
    f0, f1 = 200, 2000
    chirp_signal = np.sin(2 * np.pi * (f0 * t + (f1 - f0) * t**2 / (2 * duration)))
    
    # AudioSegmentに変換
    chirp_signal = (chirp_signal * 32767).astype(np.int16)
    chirp_audio = AudioSegment(
        chirp_signal.tobytes(),
        frame_rate=sample_rate,
        sample_width=chirp_signal.dtype.itemsize,
        channels=1
    )
    chirp_audio.export("frequency_sweep.wav", format="wav")
    print("Created: frequency_sweep.wav")
    
    # 8. ホワイトノイズ
    noise_samples = np.random.randn(44100 * 2)  # 2秒
    noise_samples = (noise_samples * 32767 * 0.1).astype(np.int16)  # 音量調整
    
    noise_audio = AudioSegment(
        noise_samples.tobytes(),
        frame_rate=44100,
        sample_width=noise_samples.dtype.itemsize,
        channels=1
    )
    noise_audio.export("white_noise.wav", format="wav")
    print("Created: white_noise.wav")
    
    # 9. ビート周波数（うなり）
    beat_freq1 = Sine(440).to_audio_segment(duration=5000)
    beat_freq2 = Sine(445).to_audio_segment(duration=5000)  # 5Hz差
    
    beat_sound = beat_freq1.overlay(beat_freq2)
    beat_sound.export("beat_frequency.wav", format="wav")
    print("Created: beat_frequency.wav")
    
    print("\nAll sample audio files have been generated successfully!")
    print("These files can be used with the Jupyter notebooks for learning audio analysis.")

if __name__ == "__main__":
    create_sample_files()