# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [2.0.1] - 2019-12-01
### Changed

- `get_context_data` now calls the `super()` method to keep context data intact from other superclasses and mix-ins

## [2.0.1] - 2018-01-27
### Changed
- `get` and `forms_invalid` have been updated to call `render_to_response` instead of `render`
  allowing a developer to customize the response_class on a view
- updated dependecies and CircleCI

## [2.0.0] - 2017-09-14
### Added
- `get_form_kwargs` now follows the same format `get_initial` and returns an object whos keys are
  the form names allowing support for custom kwargs for each included form

## [1.1.0] - 2017-09-13
### Added
- Support for Python 3

## 1.0.0 - 2016-11-06
### Added
- MultiFormView
- MultiModelFormView
