from setuptools import setup

setup(
    name='vocal_remover',
    version='0.1.1',
    packages=["vocal_remover"],
    install_requires=[
        'tqdm>=4.30',
        'librosa>=0.9',
        'opencv_python>=4.2.0',
        'resampy>=0.4.2',
    ],
    # entry_points={
    #     'console_scripts': [
    #         'your_command = your_package_name.module:main_function',
    #     ],
    # },
    author='fengxxc',
    description='Vocal Remover using Deep Neural Networks',
    license='MIT',
)
