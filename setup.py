from setuptools import setup, find_packages

setup(
    name='gitgenius',
    version='0.1.0',
    description='GitGenius CLI - Understand Git errors in plain English',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Selva Neyas U',
    author_email='your-email@example.com',  # update with your email
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'GitPython==3.1.32',
        'gitdb==4.0.10',
        'rich==13.7.1'
    ],
    entry_points={
        'console_scripts': [
            'gitgenius = gitgenius.cli:main'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Environment :: Console',
        'Topic :: Software Development :: Version Control :: Git'
    ],
    python_requires='>=3.7',
)
