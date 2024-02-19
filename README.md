# Automatic aspect extraction from scientific texts
This repo cintains dataset and code for the paper [Automatic aspect extraction from scientific texts](https://arxiv.org/abs/2310.04074).  
This project is part of the [TERMinator](https://github.com/iis-research-team/terminator): a tool for information extraction from Russian scientific texts (repo might be closed due to paper review).


## Examples

You can get aspect annotation in different formats.


<img alt = "Example of automatic annotation" src="https://github.com/anna-marshalova/automatic-aspect-extraction-from-scientific-texts/assets/78635473/5df954f4-00a4-4e74-b150-119bd63cf982" width="500">

or 

```
ЗАДАЧА
1. Восстановление коэффициентов системы линейных разностных уравнений
ВКЛАД
1. Восстановление коэффициентов системы линейных разностных
2. Доказана сходимость и установлены оценки скорости сходимости метода
МЕТОД
1. Модификация метода обратной итерации
```

## How to use

1. Clone the repository: `git clone https://github.com/iis-research-team/Terminator.git `
2. Download weights file from [here](https://disk.yandex.ru/d/31i9D65Z25cj6Q) and put it to `aspect_extractor/weights`.
3. Use the tool for aspect extraction.

```python
from aspect_extractor.aspect_extractor import AspectExtractor

extractor = AspectExtractor()
text = "Определена модель для визуализации связей между объектами и их атрибутами в различных процессах. "
       "На основании модели разработан универсальный абстрактный компонент графического пользовательского интерфейса и приведены примеры его программной реализации. "
       "Также проведена апробация компонента для решения прикладной задачи по извлечению информации из документов."
print(extractor.stringify_extracted_aspects(text = text))
```
