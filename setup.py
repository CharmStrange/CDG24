from setuptools import setup, find_packages

setup(
    name='CDG24',
    version='0.0.1', # 추후 업데이트 시 중요
    description='Content Data Generator 2024',
    author='CharmStrange',
    author_email='sacredcrawler@gmail.com',
    url='',
    install_requires=['random', 'time', 'os', 'string'],
    packages=find_packages(exclude=[]),
    keywords=[],
    python_requires='>=3.11',
    package_data={},
    zip_safe=False, # False 가 안전 기본 
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)