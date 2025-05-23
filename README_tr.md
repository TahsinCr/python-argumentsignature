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

Python'da çağılarbilir nesneler için argüman sınıfları.

[Changelog][changelog-url] · [Report Bug][issues-url] · [Request Feature][issues-url]
 
</p>

</div>






<!-- TABLE OF CONTENTS -->

<details>

<summary>İçindekiler</summary>

<ol>

<li>

<a href="#about-the-project">Proje hakkında</a>

<ul>

<li><a href="#built-with">İle İnşa Edildi</a></li>

</ul>

</li>

<li>

<a href="#getting-started">Başlarken</a>

<ul>

<li><a href="#prerequisites">Önkoşullar</a></li>

<li><a href="#installation">Kurulum</a></li>

</ul>

</li>

<li><a href="#usage">Kullanım</a></li>

<li><a href="#roadmap">Yol haritası</a></li>

<li><a href="#contributing">Katkı</a></li>

<li><a href="#license">Lisans</a></li>

<li><a href="#contact">İletişim</a></li>

<li><a href="#acknowledgments">Teşekkürler</a></li>

</ol>

</details>






<!-- ABOUT THE PROJECT -->

##  Proje hakkında

Python 3.x'e kullanımı kolay argüman özellikleri sağlar.

<p align="right">(<a href="#readme-top">başa geri dön</a>)</p>

###  İle İnşa Edildi

* [![python-shield][python-shield]][pypi-project-url]

<p align="right">(<a href="#readme-top">başa geri dön</a>)</p>






<!-- GETTING STARTED -->

##  Başlarken

Yerel bir kopyayı çalışır duruma getirmek için bu basit örnek adımları izleyin.

###  Önkoşullar

Herhangi bir ön koşul gerektirmez.

###  Kurulum

1. Depoyu klonla
```sh
git clone https://github.com/TahsinCr/python-argumentsignature.git
```

2. PIP paketlerini kurun
```sh
pip install argumentsignature
```

<p align="right">(<a href="#readme-top">başa geri dön</a>)</p>






<!-- USAGE EXAMPLES -->

##  Kullanım

Çağrlabilir nesnelerin argümanlarını ve değerlerini tutabilir.
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
Çıktı
```
Argument(name: key1, type: <class 'str'>, default: Ellipsis, argtype: ARG)

Argument(name: key2, type: <class 'str'>, default: Ellipsis, argtype: ARG)

Argument(name: keys, type: <class 'str'>, default: Ellipsis, argtype: ARGS)

Argument(name: items, type: <class 'int'>, default: Ellipsis, argtype: KWARGS)
```

<br>

_Daha fazla örnek için lütfen [belgelere][wiki-url] bakın_

Önerilen özelliklerin (ve bilinen sorunların) tam listesi için [açık sorunlara][issues-url] bakın.

<p align="right">(<a href="#readme-top">başa geri dön</a>)</p>






<!-- ROADMAP -->

##  Yol haritası

- [ ] Dökümantasyon ekle.

Önerilen özelliklerin (ve bilinen sorunların) tam listesi için [açık sorunlara][issues-url] bakın.

<p align="right">(<a href="#readme-top">başa geri dön</a>)</p>






<!-- CONTRIBUTING -->

##  Katıkı

Katkılar, açık kaynak topluluğunu öğrenmek, ilham vermek ve yaratmak için harika bir yer yapan şeydir. Yaptığınız tüm katkılar **çok makbule geçer**.

Bunu daha iyi hale getirecek bir öneriniz varsa, lütfen repoyu çatallayın ve bir çekme isteği oluşturun. Ayrıca "geliştirme" etiketiyle bir sorun açabilirsiniz.

Projeye yıldız vermeyi unutmayın! Tekrar teşekkürler!

1. Projeyi çatallayın

2. Özellik Dalınızı oluşturun (`git checkout -b feature/AmazingFeature`)

3. Değişikliklerinizi taahhüt edin (`git commit -m 'Add some AmazingFeature'`)

4. Şubeye Gönderin (`git push origin feature/AmazingFeature`)

5. Bir Çekme İsteği Açın

<p align="right">(<a href="#readme-top">başa geri dön</a>)</p>






<!-- LICENSE -->

##  Lisans

MIT Lisansı altında dağıtılmaktadır. Daha fazla bilgi için [LICENSE][license-url] konusuna bakın.

<p align="right">(<a href="#readme-top">başa geri dön</a>)</p>






<!-- CONTACT -->

##  İletişim

Email: TahsinCr@outlook.com

X: [@TahsinCrs][x-url]

LinkedIn: [TahsinCr][linkedin-url]

<p align="right">(<a href="#readme-top">başa geri dön</a>)</p>






<!-- ACKNOWLEDGMENTS -->

##  Teşekkürler

* [PyPI][pypi-project-url]

<p align="right">(<a href="#readme-top">başa geri dön</a>)</p>






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
