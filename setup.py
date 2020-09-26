from setuptools import setup

setup(
    name='whos-out-tonight',
    version='1.0',
    author='Niall Quirke',
    author_email='quirkeniall@gmail.com',
    description='Whos out tonight?',
    package_dir={'': 'src'},
    packages=[''],
    install_requires=[
        'flask',
        'flask_restful'
    ],
    entry_points='''
        [console_scripts]
        whos-out-tonight=whos_out_tonight:main
    ''',
)
