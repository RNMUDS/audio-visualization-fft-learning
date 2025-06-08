# 音響可視化とFFT学習プロジェクト

初心者が楽しく学べる音響可視化、FFT（高速フーリエ変換）による周波数分解、そしてその可視化のための超シンプルなサンプルコード集です。

## 📁 プロジェクト構成

```
audio-visualization-fft-learning/
├── 01_basic_visualization/         # 基本的な音響可視化
│   ├── 01_simple_waveform.ipynb
│   ├── 02_amplitude_envelope.ipynb
│   ├── 03_stereo_visualization.ipynb
│   ├── 04_spectrogram_basics.ipynb
│   └── 05_3d_visualization.ipynb
├── 02_fft_analysis/               # FFTと周波数解析
│   ├── 01_fft_basics.ipynb
│   ├── 02_frequency_filtering.ipynb
│   ├── 03_harmonic_analysis.ipynb
│   ├── 04_pitch_detection.ipynb
│   └── 05_stft_analysis.ipynb
├── 03_interactive_audio/          # インタラクティブ音響処理
│   ├── 01_realtime_plotting.ipynb
│   ├── 02_audio_effects.ipynb
│   ├── 03_audio_synthesis.ipynb
│   ├── 04_music_analysis.ipynb
│   └── 05_voice_processing.ipynb
├── 04_advanced_visualization/     # 高度な可視化
│   ├── 01_plotly_interactive.ipynb
│   ├── 02_animations.ipynb
│   ├── 03_wavelets.ipynb
│   ├── 04_machine_learning.ipynb
│   └── 05_realtime_processing.ipynb
├── sample_audio/                  # サンプル音響ファイル
│   └── generate_samples.py
├── requirements.txt               # 必要なパッケージ
└── README.md                     # このファイル
```

## 🚀 セットアップ

### 1. 必要なパッケージのインストール

```bash
pip install -r requirements.txt
```

### 2. サンプル音響ファイルの生成

```bash
cd sample_audio
python generate_samples.py
```

### 3. Jupyter Notebookの起動

```bash
jupyter notebook
```

## 📚 学習カリキュラム

### レベル1: 基本的な音響可視化 (`01_basic_visualization/`)

音響信号の基本的な可視化方法を学びます。

- **01_simple_waveform.ipynb**: 基本的な波形表示とサンプリングの概念
- **02_amplitude_envelope.ipynb**: ADSR エンベロープと音の立ち上がり・減衰
- **03_stereo_visualization.ipynb**: ステレオ音響の可視化とパンニング効果
- **04_spectrogram_basics.ipynb**: スペクトログラムの基礎と時間-周波数解析
- **05_3d_visualization.ipynb**: 3次元での音響可視化技術

### レベル2: FFTと周波数解析 (`02_fft_analysis/`)

フーリエ変換を使った周波数領域での音響解析を学びます。

- **01_fft_basics.ipynb**: FFTの基礎概念と周波数スペクトラム
- **02_frequency_filtering.ipynb**: デジタルフィルタとノイズ除去
- **03_harmonic_analysis.ipynb**: 倍音解析と音色の分析
- **04_pitch_detection.ipynb**: ピッチ検出アルゴリズムの実装
- **05_stft_analysis.ipynb**: 短時間フーリエ変換と時間-周波数フィルタリング

### レベル3: インタラクティブ音響処理 (`03_interactive_audio/`)

リアルタイムでの音響処理とインタラクティブな可視化を学びます。

- **01_realtime_plotting.ipynb**: リアルタイム可視化のシミュレーション
- **02_audio_effects.ipynb**: エコー、リバーブ、ディストーション等の音響効果
- **03_audio_synthesis.ipynb**: シンセサイザーの実装と音響合成
- **04_music_analysis.ipynb**: ビート検出とテンポ解析
- **05_voice_processing.ipynb**: 音声解析とピッチトラッキング

### レベル4: 高度な可視化と応用 (`04_advanced_visualization/`)

最新の可視化技術と機械学習の応用を学びます。

- **01_plotly_interactive.ipynb**: Plotlyを使ったインタラクティブ可視化
- **02_animations.ipynb**: リアルタイムスペクトラム解析のアニメーション
- **03_wavelets.ipynb**: ウェーブレット変換による時間-周波数解析
- **04_machine_learning.ipynb**: 機械学習による音響分類と特徴抽出
- **05_realtime_processing.ipynb**: リアルタイム音響処理システムの構築

## 🛠️ 使用技術・ライブラリ

- **音響処理**: pydub, simpleaudio, scipy
- **数値計算**: numpy, scipy
- **可視化**: matplotlib, plotly, seaborn
- **機械学習**: scikit-learn
- **信号処理**: scipy.signal, PyWavelets
- **開発環境**: Jupyter Notebook

## 📖 学習のポイント

### 初心者向け
1. **01_basic_visualization**から順番に進めることをお勧めします
2. 各ノートブックは独立して実行できるように設計されています
3. 理論より実践を重視し、視覚的な理解を促進します

### 中級者向け
1. 興味のある分野から始めて、必要に応じて関連するノートブックを参照してください
2. パラメータを変更して異なる結果を確認しましょう
3. 自分の音響ファイルを使って実験してみましょう

### 上級者向け
1. コードを改良して新しい機能を追加してみましょう
2. リアルタイム処理をウェブアプリケーションとして実装してみましょう
3. 機械学習モデルを改善して、より高精度な音響分類を実現してみましょう

## 🔧 トラブルシューティング

### よくある問題

1. **パッケージのインポートエラー**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

2. **音響ファイルの読み込みエラー**
   - サンプル音響ファイルが生成されているか確認してください
   - ffmpegがインストールされているか確認してください

3. **Jupyter Notebookでのプロット表示問題**
   ```python
   %matplotlib inline
   # または
   %matplotlib widget  # インタラクティブプロット用
   ```

## 🎵 サンプル音響ファイル

`sample_audio/generate_samples.py`を実行すると、以下のファイルが生成されます：

- `sine_440hz.wav`: 純粋な正弦波（440Hz）
- `square_440hz.wav`: 方形波
- `sawtooth_440hz.wav`: のこぎり波
- `triangle_440hz.wav`: 三角波
- `c_major_chord.wav`: Cメジャーコード
- `c_major_scale.wav`: Cメジャースケール
- `frequency_sweep.wav`: 周波数スイープ（チャープ信号）
- `white_noise.wav`: ホワイトノイズ
- `beat_frequency.wav`: ビート周波数（うなり）

## 🤝 貢献

このプロジェクトへの貢献を歓迎します！

1. リポジトリをフォーク
2. 新しいブランチを作成 (`git checkout -b feature/amazing-feature`)
3. 変更をコミット (`git commit -m 'Add amazing feature'`)
4. ブランチにプッシュ (`git push origin feature/amazing-feature`)
5. プルリクエストを作成

## 📞 サポート

質問やバグ報告は、GitHubのIssueページでお願いします。

## 📄 ライセンス

このプロジェクトはMITライセンスの下で公開されています。

## 🙏 謝辞

このプロジェクトは、音響信号処理の学習を支援することを目的として作成されました。
音響信号処理の世界への第一歩として、ぜひご活用ください！

---

**Happy Learning! 🎶✨**