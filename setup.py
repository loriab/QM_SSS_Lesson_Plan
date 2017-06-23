import setuptools

if __name__ == "__main__":
    setuptools.setup(
        name='quantum_python',
        version="0.2.1",
        description='A small ',
        author='Daniel Smith',
        author_email='dgasmith@vt.edu',
        url="https://github.com/MolSSI/python_template",
        license='BSD-3C',
        packages=setuptools.find_packages(),
        install_requires=[
            'numpy>=1.7',
            'pytest>=3.0',
            'pytest-cov',
        ],
        extras_require={
            'docs': [
                'sphinx==1.2.3',  # autodoc was broken in 1.3.1
                'sphinxcontrib-napoleon',
                'sphinx_rtd_theme',
                'numpydoc',
            ],
        },

        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Science/Research',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
        ],
        zip_safe=True,
    )
