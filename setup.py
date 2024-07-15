from setuptools import find_packages, setup

# with open("readme.md", "r") as f:
#     long_description = f.read()
    
setup(
    name="tae_celery_pac",
    version="0.0.1",
    description="simple celery package test",
    # package_dir ={"": "tae_celery_pac"},
    packages=find_packages(),
    # long_description=long_description,
    long_description_content_type="text/markdown",
    url="me@home.com",
    author="taenaive",
    author_email="tyoon2000@hotmail.com",
    license="MIT",
    classifiers=["License :: OIS Approved :: MIT License",
                 "Programming Language :: Python :: 3.10",
                 "Operating System :: OS Independent",
                 ],
    install_requires=[ "celery >=5.4.0",
                       "redis >=5.0.7",
                       "six >=1.16.0",
                        "tornado >=6.4.1",
                        "vine >= 5.1.0",
                        ],
    python_requires=">=3.11",
    entry_points={
        'console_scripts': [
            'tae-celery-run = tae_celery_pac.tae_server:main'
        ]
    }
)