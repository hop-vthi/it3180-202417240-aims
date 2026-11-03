## [Unreleased]

## [1.1.0] - 2026-11-03

### Added
- Add DVD sorting by title (`sort_by_title`).
- Add DVD sorting by cost (`sort_by_cost`).
- Add DVD search by category (`search_by_category`).

## [1.0.0] - 2026-11-03

### Added
- Add DVD search by title.
- Add cart printing functionality.
- Add discount calculation functionality.
- Add validation for discount percentages.

### Changed
- Update the main program to use cart printing.
- Translate application messages into Vietnamese.

### Fixed
- Handle empty cart when printing.
- Correct cart printing behavior.
- Reject DVDs exceeding the maximum cart capacity of 20 (#6).