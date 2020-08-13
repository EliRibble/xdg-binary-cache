"Setup the module."
import setuptools  # type: ignore

setuptools.setup(
	install_requires=[],
	extras_require={
		"develop": [
			"mypy",
			"nose2",
			"pylint",
			"twine",
			"wheel",
		]
	},
	package_data={},
)
