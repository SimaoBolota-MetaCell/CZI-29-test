setup(
    use_scm_version={"local_scheme": local_scheme},
    
    entry_points={
        'napari.plugin': [
            'naparij = napari_j',
        ],
	'napari.manifest': [
	    'naparij = napari.yaml',
        ], 
    },
    
    classifiers=[
	'Development Status :: 4 - Beta',
	'Intended Audience :: Science/Research',
	'Topic :: Scientific/Engineering',
	'License :: OSI Approved :: MIT License',

	'Operating System :: OS Independent',

	'Programming Language :: Python :: 3.7',
	'Programming Language :: Python :: 3.8',
	'Programming Language :: Python :: 3.9',

	'Framework :: napari',
    ],
    
    setup_requires=['setuptools_scm'],
    
     install_requires=[
        'JPype1>=1.2.1',
        'matplotlib',
	'imageio_ffmpeg',
    ],
)
