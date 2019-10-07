class: center, middle

# Multiply your Testing Effectiveness with Parameterized Testing

Brian Okken

@brianokken

---
# Brian Okken

![](images/logos.png)

---

# Outline

* Value of Tests
* Parametrize vs Parameterize
* Tests without Parametrization
* Function Parametrization
* Fixture Parametrization
* Parametrizing with `pytest_generate_tests()`
* Choosing a Technique
* Combining Techniques
* For futher study
* Advanced (if time)
    * ids
    * indirect parametrization
---

# Introduction
---
# Triangles

Right Triangle ![](images/right_triangle.png)
one angle is 90 degrees

--

Obtuse Triangle ![](images/obtuse_triangle.png)
one angle is greater than 90 degrees

--

Acute Triangle ![](images/acute_triangle.png)
all angles are less than 90 degrees
