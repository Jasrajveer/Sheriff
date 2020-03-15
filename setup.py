import setuptools

setuptools.setup(
        name='incidents',
        version='1.0',
        author='Jasrajveer Malhi',
        description="Packages for using Jira platform api.",
        python_requires='>3.6.0',
        packages=setuptools.find_packages(),
        include_package_data=True,
        install_requires=['pyyaml', 'jira', 'argparse'],
        entry_points={
            'console_scripts': [
                'incidents = incidents.__main__:main'
                ]
            })

