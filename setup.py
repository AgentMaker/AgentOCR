from setuptools import setup


def readme():
    with open('docs/package_usage.md', 'r', encoding="UTF-8") as f:
        README = f.read()
    return README


def requirements():
    with open('requirements.txt', 'r', encoding='UTF-8') as f:
        REQUIREMENTS = f.read().split('\n')
    return REQUIREMENTS


setup(name='agentocr',
      packages=[
          'agentocr', 'agentocr.preprocess', 'agentocr.infer',
          'agentocr.postprocess'
      ],
      include_package_data=True,
      entry_points={"console_scripts": ["agentocr = agentocr:command"]},
      version='1.3.0',
      install_requires=requirements(),
      license='Apache License 2.0',
      description='An easy-to-use OCR package with multilingual support.',
      url='https://github.com/AgentMaker/AgentOCR',
      author='jm12138',
      long_description=readme(),
      long_description_content_type='text/markdown')
