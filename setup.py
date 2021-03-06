import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setup_args = dict(
	name="pycosa", 
	version="0.1",
	author="smba",
	author_email="",
	description="configuration sampling in python",	
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/smba/pycosa",
	packages=setuptools.find_packages(),
	classifiers=[
        	"Programming Language :: Python :: 3",
        	"License :: OSI Approved :: Creative Commons Zero v1.0 Universal",
        	"Operating System :: OS Independent",
    	],
	python_requires='>=3.5',
)

install_requires = [
	"numpy",
	"pandas",
	"z3-solver",
	"xmltodict",
	"pyeda",
	"networkx",
	"pyDOE2"
]

if __name__ == "__main__":
	setuptools.setup(**setup_args, install_requires=install_requires)
