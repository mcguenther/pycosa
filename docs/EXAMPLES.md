# Code Examples

## Implementing a Sampling Startegy
```python
```
## Sampling with `pycosa`
```python
```
## Adding non-trivial Constraints
```python
from pycosa.features import FeatureModel

fm = FeatureModel('h2.dimacs')

features_to_enable = ['h2', 'PAGE_STORE', 'PAGE_STORE_TRIM']

# require that all features from a subset are enabled
fm.constrain_exact_enabled(features_to_enable, 3)

# require that at least one feature from a subset is enabled
fm.constrain_min_enabled(features_to_enable, 1)

# require that at most two feature from a subset is enabled
fm.constrain_max_enabled(features_to_enable, 2)
```
