# Molecular dynamics of liquid n-alkanes — BSc research

**BSc thesis (2024), Bioinformatics — Jagiellonian University**

This repository contains research notes, simulation inputs, results and figures for a molecular-dynamics comparison of **n-octane, n-dodecane and n-pentadecane** using several classical force-field parameterizations.

## Research objective

Evaluate how force-field choice influences selected thermodynamic and kinetic properties of liquid n-alkanes, and compare simulation-derived values with available literature or experimental references.

**Systems:** n-octane, n-dodecane, n-pentadecane  
**Force fields:** OPLS/AA (1996, 2013, 2022 parameterizations) and CHARMM36  
**Simulation engine:** GROMACS 2022.4  
**Example production settings:** 298.15 K, 2 fs integration step, 100 ns production runs (consult individual simulation files for system-specific settings)

## Analysis

- Liquid density
- Enthalpy of vaporization
- Translational diffusion
- Force-field and reference-data comparison

**Example result:** for n-pentadecane, the [project summary](Podsumowanie.md) records a density of **768.962 kg/m³** under OPLS/AA 2022, against a reference value of **765 kg/m³**. This is one result, not a general claim that one force field performs best for every observable.

## Repository guide

| Location | Description |
| --- | --- |
| [`Podsumowanie.md`](Podsumowanie.md) | Simulation settings, selected numerical results and comparisons |
| [`Dziennik_Licencjacki.md`](Dziennik_Licencjacki.md) | Research log and historical development notes (in Polish) |
| [`Density_Results/`](Density_Results/) | Density analysis outputs |
| [`VaporizationEnthalpy_Results/`](VaporizationEnthalpy_Results/) | Enthalpy-of-vaporization outputs |
| [`Dyfuzja_Translacyjna_Wyniki/`](Dyfuzja_Translacyjna_Wyniki/) | Translational-diffusion outputs |
| [`Wykresy/`](Wykresy/) | Plots and visualization |
| [`data/`](data/) | Research data and simulation-related files |

## Reproducibility note

This is an **archived academic research repository**, not a one-command software package. Full reproduction requires GROMACS, compatible force-field and topology files, hardware/time for molecular dynamics, and review of system-specific inputs. Some original files and notes are retained in the form used during the thesis; the historical research log should not be interpreted as current instructions.

## Skills demonstrated

Molecular modeling · simulation design · GROMACS · numerical analysis · validation against reference data · scientific reporting

**Author:** Daniel Drabik
