from setuptools import setup, find_packages
import os

setup(
    name='IMS-Toucan',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'torch_complex~=0.4.3',
        'tqdm~=4.64.1',
        'scipy~=1.9.3',
        'librosa~=0.9.2',
        'scikit-learn~=1.1.3',
        'praat-parselmouth~=0.4.2',
        'torch~=2.0.0',
        'numpy~=1.23.4',
        'torchaudio~=2.0.0',
        'soundfile~=0.12.1',
        'urllib3~=1.26.12',
        'pypinyin~=0.47.1',
        'pyloudnorm~=0.1.0',
        'numba~=0.56.4',
        'cvxopt~=1.3.0',
        'sounddevice~=0.4.5',
        'matplotlib~=3.6.2',
        'phonemizer~=3.2.1',
        'gradio~=3.19.1',
        'wandb~=0.13.5',
        'speechbrain~=0.5.13',
        'dragonmapper~=0.2.6',
        'auraloss~=0.2.2',
        'alias_free_torch~=0.0.6',
    ],
)
