<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

[<img src="images/languages/turkish-flag.png" height="28" alt="Logo" >][lang-tr-url]
[<img src="images/languages/british-flag.png" height="28" alt="Logo" >][lang-en-url]

<br />






<!-- About -->
<div align="center">

[<img src="images/logo.png" alt="Logo">][project-url]

<h3 align="center">Python ArgumentSignature</h3>

<p align="center">

Argument classes for callable objects in Python.

[Changelog][changelog-url] · [Report Bug][issues-url] · [Request Feature][issues-url]
 
</p>

</div>






<!-- TABLE OF CONTENTS -->

<details>

<summary>Table of Contents</summary>

<ol>

<li>

<a href="#about-the-project">About The Project</a>

<ul>

<li><a href="#built-with">Built With</a></li>

</ul>

</li>

<li>

<a href="#getting-started">Getting Started</a>

<ul>

<li><a href="#prerequisites">Prerequisites</a></li>

<li><a href="#installation">Installation</a></li>

</ul>

</li>

<li><a href="#usage">Usage</a></li>

<li><a href="#roadmap">Roadmap</a></li>

<li><a href="#contributing">Contributing</a></li>

<li><a href="#license">License</a></li>

<li><a href="#contact">Contact</a></li>

<li><a href="#acknowledgments">Acknowledgments</a></li>

</ol>

</details>






<!-- ABOUT THE PROJECT -->

##  About The Project

Provides easy-to-use argument features for Python 3.x.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

###  Built With

* [![python-shield][python-shield]][pypi-project-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>






<!-- GETTING STARTED -->

##  Getting Started

To get a local copy up and running follow these simple example steps.

###  Prerequisites

Does not require any prerequisites

###  Installation

1. Clone the repo
```sh
git clone https://github.com/TahsinCr/python-argumentsignature.git
```

2. Install PIP packages
```sh
pip install argumentsignature
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>






<!-- USAGE EXAMPLES -->

##  Usage

Can store the arguments and values of callable objects.
```python
from argumentsignature import Argument, ArgumentValue, ARG, ARGS, KWARGS

def item_to_string(key1:str, key2:str, *keys:str, **items:int):
    itmes = [f'{k}:{v}' for k, v in items]
    return ", ".join([key1, key2, *keys, itmes])

arg_items = item_to_string.__annotations__.items()
code = item_to_string.__code__
arg_defaults = item_to_string.__kwdefaults__ or {}
names = code.co_varnames
arg_keys = names[:code.co_argcount]
kwarg_keys = list(arg_defaults.keys())
is_args = True

arguments:list[Argument] = []
for arg_name, arg_type in arg_items:
    if arg_name in arg_keys:
        arguments.append(Argument(
            name = arg_name,
            type = arg_type,
            argtype = ARG
        ))
    elif arg_name in kwarg_keys:
        arguments.append(Argument(
            name = arg_name, 
            type = arg_type, 
            default = arg_defaults[arg_name],
            argtype = ARG
        ))
    elif arg_name == 'return':
        continue
    else:
        arguments.append(Argument(
            name = arg_name,
            type = arg_type,
            argtype = ARGS if is_args else KWARGS
        ))
        is_args = False

print("\n\n".join([str(x) for x in arguments]))

```
Output
```
Argument(name: key1, type: <class 'str'>, default: Ellipsis, argtype: ARG)

Argument(name: key2, type: <class 'str'>, default: Ellipsis, argtype: ARG)

Argument(name: keys, type: <class 'str'>, default: Ellipsis, argtype: ARGS)

Argument(name: items, type: <class 'int'>, default: Ellipsis, argtype: KWARGS)
```

_For more examples, please refer to the [Documentation][wiki-url]_

<p align="right">(<a href="#readme-top">back to top</a>)</p>






<!-- ROADMAP -->

##  Roadmap

- [ ] Add Documents

See the [open issues][issues-url] for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>






<!-- CONTRIBUTING -->

##  Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

Don't forget to give the project a star! Thanks again!

1. Fork the Project

2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)

3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)

4. Push to the Branch (`git push origin feature/AmazingFeature`)

5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>






<!-- LICENSE -->

##  License

Distributed under the MIT License. See [LICENSE.txt][license-url] for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>






<!-- CONTACT -->

##  Contact

Email: TahsinCr@outlook.com

X: [@TahsinCrs][x-url]

LinkedIn: [TahsinCr][linkedin-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>






<!-- ACKNOWLEDGMENTS -->

##  Acknowledgments

* [PyPI][pypi-project-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>






<!-- IMAGES URL -->

[python-shield]: https://img.shields.io/pypi/pyversions/argumentsignature?style=flat-square

[contributors-shield]: https://img.shields.io/github/contributors/TahsinCr/python-argumentsignature.svg?style=for-the-badge

[forks-shield]: https://img.shields.io/github/forks/TahsinCr/python-argumentsignature.svg?style=for-the-badge

[stars-shield]: https://img.shields.io/github/stars/TahsinCr/python-argumentsignature.svg?style=for-the-badge

[issues-shield]: https://img.shields.io/github/issues/TahsinCr/python-argumentsignature.svg?style=for-the-badge

[license-shield]: https://img.shields.io/github/license/TahsinCr/python-argumentsignature.svg?style=for-the-badge

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555



<!-- Github Project URL -->

[project-url]: https://github.com/TahsinCr/python-argumentsignature

[pypi-project-url]: https://pypi.org/project/argumentsignature

[contributors-url]: https://github.com/TahsinCr/python-argumentsignature/graphs/contributors

[stars-url]: https://github.com/TahsinCr/python-argumentsignature/stargazers

[forks-url]: https://github.com/TahsinCr/python-argumentsignature/network/members

[issues-url]: https://github.com/TahsinCr/python-argumentsignature/issues

[wiki-url]: https://github.com/TahsinCr/python-argumentsignature/wiki

[license-url]: https://github.com/TahsinCr/python-argumentsignature/blob/master/LICENSE

[changelog-url]:https://github.com/TahsinCr/python-argumentsignature/blob/master/CHANGELOG.md



<!-- Contacts URL -->

[linkedin-url]: https://linkedin.com/in/TahsinCr

[x-url]: https://twitter.com/TahsinCrs



<!-- File URL -->

[lang-tr-url]: https://github.com/TahsinCr/python-argumentsignature/blob/master/README_tr.md

[lang-en-url]: https://github.com/TahsinCr/python-argumentsignature/blob/master/README.md
