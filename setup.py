from setuptools import setup

setup(
    name='agentocr',
    packages=['agentocr', 'agentocr.imaug', 'agentocr.infer', 'agentocr.postprocess'],
    include_package_data=True,
    entry_points={"console_scripts": ["agentocr = agentocr:command"]},
    version='1.0.0',
    install_requires=['shapely', 'pyclipper', 'numpy', 'opencv-python', 'pillow', 'wget'],
    license='Apache License 2.0',
)