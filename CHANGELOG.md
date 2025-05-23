# **Change Log**
All notable changes to this project will be documented in this file.

## **[1.0.1] - 23.05.2025**
Added `EMPTY`, `is_default_argument` and fixed `ArgumentValue` generic structure.
### Added
 * A variable named `EMPTY` holding the value `Ellipsis` has been added.
 * A function named `is_default_argument` has been added to check whether an argument has a default value and is of type `ARG`.

### Fixed
 * The generic structure of the `Argument` class, which the `ArgumentValue` class inherits from, has been fixed.

<br>

## **[1.0] - 22.05.2025**
New ArgumentSignature module created.
### Added
 * `ArgumentType`, `Argument`, and `ArgumentValue` classes have been added.
 * Created instances of `ARG`, `ARGS`, `KWARGS`, and `RETURN` from the `ArgumentType` class.

<br>
